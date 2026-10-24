"""
============================================================
PLANT DISEASE DETECTION WEB APPLICATION
============================================================

Model:
    EfficientNetB0

Classes:
    62

Test Accuracy:
    92.88%

Database:
    62/62 classes verified

IMPORTANT:
    Prediction confidence is NOT model accuracy.
============================================================
"""

import uuid
from pathlib import Path

import numpy as np
import tensorflow as tf

from PIL import Image

from flask import (
    Flask,
    render_template,
    request,
    redirect,
    url_for,
    flash,
    jsonify
)

from werkzeug.utils import secure_filename

# ============================================================
# DATABASE
# ============================================================

# IMPORTANT:
# Only import DISEASE_DATABASE.
# The helper functions are defined below in this file.
from disease_database import DISEASE_DATABASE


# ============================================================
# FLASK APPLICATION
# ============================================================

app = Flask(__name__)

app.secret_key = "plant-disease-detection-secret-key"


# ============================================================
# CORS HEADERS (FOR FLUTTER APP & CROSS-ORIGIN REQUESTS)
# ============================================================

@app.after_request
def add_cors_headers(response):
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Methods"] = "GET, POST, OPTIONS"
    response.headers["Access-Control-Allow-Headers"] = "Content-Type, Authorization"
    return response


# ============================================================
# PROJECT PATHS
# ============================================================

WEB_APP_DIR = Path(__file__).resolve().parent

PROJECT_DIR = WEB_APP_DIR.parent

MODEL_PATH = (
    
    PROJECT_DIR
    / "models"
    / "final_model.keras"
)

LABELS_PATH = (
    PROJECT_DIR
    / "models"
    / "labels.txt"
)

UPLOAD_DIR = (
    WEB_APP_DIR
    / "static"
    / "uploads"
)

UPLOAD_DIR.mkdir(
    parents=True,
    exist_ok=True
)


# ============================================================
# SETTINGS
# ============================================================

IMAGE_SIZE = (224, 224)

EXPECTED_CLASSES = 62

ALLOWED_EXTENSIONS = {
    "jpg",
    "jpeg",
    "png",
    "webp",
    "bmp"
}


# ============================================================
# PLANT / LEAF GATEKEEPER (REJECTS HUMANS, DRESSES, CHARGERS)
# ============================================================

def is_plant_image(image_path):
    """
    Gatekeeper: Validates whether the uploaded image is a genuine plant leaf.
    Filters out:
    - Humans (faces, skin, ears, selfies, hands, arms)
    - Bottles / Household items / Desks / Furniture
    - Clothing / Dresses (synthetic fabrics, shirts, textiles)
    - Electronics / Chargers / Cables (household objects, neutral plastics/metals)

    Returns (is_valid: bool, rejection_message: str)
    """
    try:
        img = Image.open(image_path).convert("RGB").resize((160, 160))
        arr = np.asarray(img, dtype=np.float32) / 255.0
        r, g, b = arr[:, :, 0], arr[:, :, 1], arr[:, :, 2]

        cmax = np.maximum(np.maximum(r, g), b)
        cmin = np.minimum(np.minimum(r, g), b)
        delta = cmax - cmin
        sat = np.where(cmax > 0, delta / (cmax + 1e-7), 0.0)
        bright = (r + g + b) / 3.0

        # Compute Hue [0, 360]
        hue = np.zeros_like(r)
        mask_r = (cmax == r) & (delta > 0)
        mask_g = (cmax == g) & (delta > 0)
        mask_b = (cmax == b) & (delta > 0)
        hue[mask_r] = 60.0 * (((g[mask_r] - b[mask_r]) / (delta[mask_r] + 1e-7)) % 6)
        hue[mask_g] = 60.0 * (((b[mask_g] - r[mask_g]) / (delta[mask_g] + 1e-7)) + 2)
        hue[mask_b] = 60.0 * (((r[mask_b] - g[mask_b]) / (delta[mask_b] + 1e-7)) + 4)
        hue = np.clip(hue, 0, 360)
        total = float(hue.size)

        # 1. Genuine green leaf foliage (hue 48 to 165 deg, sat >= 0.12)
        green_mask = (hue >= 48) & (hue <= 165) & (sat >= 0.12)
        green_pct = float(np.sum(green_mask)) / total

        # 2. Excess Green vegetation index (2G - R - B)
        exg = 2.0 * g - r - b
        exg_pos = float(np.mean(exg > 0.04))

        # 3. Human skin detection (covers fair, medium, olive, and dark skin in natural & indoor light)
        skin_mask = (
            (hue >= 0) & (hue <= 45) &
            (sat >= 0.10) & (sat <= 0.65) &
            (bright >= 0.12) & (bright <= 0.90) &
            (r > g) & (g > b) &
            ((r - g) > 0.015) &
            ((g - b) > 0.010)
        )
        skin_pct = float(np.sum(skin_mask)) / total

        # 4. Synthetic fabric / dress colors (blues, purples, cyans, magentas, pinks)
        fabric_mask = (sat >= 0.14) & (hue >= 175) & (hue <= 345)
        fabric_pct = float(np.sum(fabric_mask)) / total

        # 5. Bright artificial red/pink fabrics
        bright_red_mask = (sat >= 0.50) & ((hue >= 345) | (hue <= 10)) & (bright >= 0.22)
        bright_red_pct = float(np.sum(bright_red_mask)) / total

        # 6. Neutral / Monochromatic objects (chargers, black cables, white chargers, metallic laptops)
        neutral_mask = (sat < 0.12)
        neutral_pct = float(np.sum(neutral_mask)) / total

        # ----------------------------------------------------
        # 7. FOREGROUND FOCUS (CENTER ROI) ANALYSIS
        # Legitimate plant photos focus on the leaf/crop in the center.
        # Animals (dogs, cats, pets) or objects sitting on outdoor lawn/grass
        # have green grass only on the perimeter, while the center is animal fur/object.
        # ----------------------------------------------------
        H, W = r.shape
        y1, y2 = int(H * 0.22), int(H * 0.78)
        x1, x2 = int(W * 0.22), int(W * 0.78)

        c_r, c_g, c_b = r[y1:y2, x1:x2], g[y1:y2, x1:x2], b[y1:y2, x1:x2]
        c_hue, c_sat, c_bright = hue[y1:y2, x1:x2], sat[y1:y2, x1:x2], bright[y1:y2, x1:x2]
        c_total = float(c_hue.size)

        c_green_pct = float(np.sum((c_hue >= 45) & (c_hue <= 165) & (c_sat >= 0.10))) / c_total
        c_white_fur = float(np.mean((c_sat < 0.20) & (c_bright > 0.55)))
        c_warm_fur = float(np.mean(
            (c_hue >= 10) & (c_hue <= 42) &
            (c_sat >= 0.12) & (c_sat <= 0.70) &
            (c_r > c_g) & (c_g > c_b)
        ))
        c_dark_fur = float(np.mean((c_bright < 0.20) & (c_sat < 0.25)))
        c_neutral_pct = float(np.mean(c_sat < 0.15))

        print(
            f"[Gatekeeper] green={green_pct:.1%} exg={exg_pos:.1%} skin={skin_pct:.1%} "
            f"fabric={fabric_pct:.1%} red={bright_red_pct:.1%} neutral={neutral_pct:.1%} | "
            f"c_green={c_green_pct:.1%} white_fur={c_white_fur:.1%} warm_fur={c_warm_fur:.1%} dark_fur={c_dark_fur:.1%}"
        )

        # === GATEKEEPER RULES ===

        # Rule 1: Human rejection (face, ear, neck, arm, selfie)
        if (skin_pct > 0.18 and green_pct < 0.12) or (skin_pct > 0.30 and green_pct < 0.20) or (skin_pct > 0.40):
            return False, "Human detected (face, skin, or selfie). Please point the camera only at a plant leaf."

        # Rule 2: Animal / Pet rejection (dogs, cats, puppies, mammal fur on grass or indoors)
        if c_white_fur > 0.35 and c_green_pct < 0.18:
            return False, "Animal or pet detected (dog/cat/white fur). Please point the camera only at a plant leaf."

        if c_warm_fur > 0.40 and c_green_pct < 0.15:
            return False, "Animal or pet detected (dog/cat/mammal fur). Please point the camera only at a plant leaf."

        if c_dark_fur > 0.40 and c_green_pct < 0.15:
            return False, "Animal or pet detected (dark fur/dog/cat). Please point the camera only at a plant leaf."

        if c_neutral_pct > 0.55 and c_green_pct < 0.15:
            return False, "Non-plant subject detected (animal, pet, or household object). Please focus closely on an infected plant leaf."

        # Rule 3: Clothing / Dress rejection
        if (fabric_pct > 0.20 and green_pct < 0.10) or (fabric_pct > 0.50):
            return False, "Clothing or fabric detected (dress/shirt/cloth). Please capture a photo of a plant leaf."

        if (bright_red_pct > 0.20 and green_pct < 0.10) or (bright_red_pct > 0.45):
            return False, "Clothing or non-plant object detected (red fabric). Please capture a photo of a plant leaf."

        # Rule 4: Electronics / Chargers / Household objects / Bottles on desks
        if neutral_pct > 0.65 and green_pct < 0.10:
            return False, "Household object or device detected (bottle/charger/cable). Please focus closely on a plant leaf."

        # Rule 5: Mandatory green foliage requirement for plant disease diagnosis
        if green_pct < 0.08 and exg_pos < 0.15:
            return False, "No plant or leaf detected in the image. Please focus closely on a plant leaf."

        if c_green_pct < 0.05 and exg_pos < 0.20:
            return False, "No plant or leaf detected in the center of the image. Please focus closely on the affected leaf."

        return True, "OK"

    except Exception as e:
        print(f"[Gatekeeper Error] {e}")
        return False, "Could not validate the image. Please upload a clear plant photo."





# ============================================================
# DATABASE HELPER FUNCTIONS
# ============================================================

def get_disease_info(model_class):
    """
    Get disease information for a model class.
    """

    return DISEASE_DATABASE.get(
        model_class
    )


def is_supported_class(model_class):
    """
    Check whether the model class exists
    in the disease database.
    """

    return model_class in DISEASE_DATABASE


def is_healthy_class(model_class):
    """
    Determine whether the predicted class
    represents a healthy plant.
    """

    if model_class not in DISEASE_DATABASE:
        return False

    info = DISEASE_DATABASE[
        model_class
    ]

    disease_type = str(
        info.get(
            "disease_type",
            ""
        )
    ).lower()

    disease_name = str(
        info.get(
            "disease",
            ""
        )
    ).lower()

    model_name = str(
        model_class
    ).lower()

    return (
        "healthy" in model_name
        or disease_type == "healthy"
        or disease_name in {
            "healthy",
            "no disease",
            "no disease detected"
        }
    )


# ============================================================
# LOAD LABELS
# ============================================================

def load_labels():

    if not LABELS_PATH.exists():

        raise FileNotFoundError(
            f"""
labels.txt was not found.

Expected location:
{LABELS_PATH}
"""
        )

    with open(
        LABELS_PATH,
        "r",
        encoding="utf-8"
    ) as file:

        labels = [
            line.strip()
            for line in file
            if line.strip()
        ]

    if len(labels) != EXPECTED_CLASSES:

        raise ValueError(
            f"""
Expected {EXPECTED_CLASSES} classes.

Found:
{len(labels)}

Please check:
models/labels.txt
"""
        )

    return labels


CLASS_NAMES = load_labels()


# ============================================================
# LOAD MODEL
# ============================================================

print()

print("=" * 70)
print("LOADING PLANT DISEASE MODEL")
print("=" * 70)


if not MODEL_PATH.exists():

    raise FileNotFoundError(
        f"""
Model file was not found.

Expected:
{MODEL_PATH}
"""
    )


MODEL = tf.keras.models.load_model(
    MODEL_PATH,
    compile=False
)


print(
    "Model loaded successfully."
)

print(
    "Model      :",
    MODEL_PATH
)

print(
    "Classes    :",
    len(CLASS_NAMES)
)

print(
    "Image size :",
    IMAGE_SIZE
)

print(
    "Test Acc.  : 92.88%"
)

print(
    "Database   :",
    len(DISEASE_DATABASE),
    "entries"
)

print("=" * 70)


# ============================================================
# FILE VALIDATION
# ============================================================

def allowed_file(filename):

    if not filename:
        return False

    if "." not in filename:
        return False

    extension = (
        filename
        .rsplit(".", 1)[1]
        .lower()
    )

    return extension in ALLOWED_EXTENSIONS


# ============================================================
# IMAGE PREPROCESSING
# ============================================================

def preprocess_image(image_path):

    image = Image.open(
        image_path
    ).convert("RGB")

    image = image.resize(
        IMAGE_SIZE,
        Image.Resampling.LANCZOS
    )

    image_array = np.asarray(
        image,
        dtype=np.float32
    )

    image_array = np.expand_dims(
        image_array,
        axis=0
    )

    return image_array


# ============================================================
# MODEL PREDICTION
# ============================================================

SUPPORTED_CROPS = [
    "Apple",
    "Banana",
    "Bell Pepper",
    "Citrus",
    "Corn",
    "Grape",
    "Guava",
    "Mango",
    "Papaya",
    "Potato",
    "Tomato"
]


def is_leaf_foliage(image_path):
    """
    Checks if the uploaded image represents foliage/leaf rather than a fruit.
    Leaf images have substantial green foliage pixels or positive Excess Green index.
    """
    try:
        img = Image.open(image_path).convert("RGB")
        img_small = img.resize((128, 128))
        arr = np.asarray(img_small, dtype=np.float32) / 255.0
        r, g, b = arr[:, :, 0], arr[:, :, 1], arr[:, :, 2]
        cmax = np.maximum(np.maximum(r, g), b)
        cmin = np.minimum(np.minimum(r, g), b)
        delta = cmax - cmin
        sat = np.where(cmax > 0, delta / (cmax + 1e-7), 0.0)
        hue = np.zeros_like(r)
        mask_r = (cmax == r) & (delta > 0)
        mask_g = (cmax == g) & (delta > 0)
        mask_b = (cmax == b) & (delta > 0)
        hue[mask_r] = 60.0 * (((g[mask_r] - b[mask_r]) / (delta[mask_r] + 1e-7)) % 6)
        hue[mask_g] = 60.0 * (((b[mask_g] - r[mask_g]) / (delta[mask_g] + 1e-7)) + 2)
        hue[mask_b] = 60.0 * (((r[mask_b] - g[mask_b]) / (delta[mask_b] + 1e-7)) + 4)
        hue = np.clip(hue, 0, 360)
        green_foliage = (hue >= 45) & (hue <= 165) & (sat >= 0.10)
        exg = 2.0 * g - r - b
        green_ratio = float(np.mean(green_foliage))
        exg_ratio = float(np.mean(exg > 0.03))
        return (green_ratio > 0.08) or (exg_ratio > 0.12)
    except Exception:
        return True


def predict_image(image_path, crop=None):
    image = preprocess_image(image_path)
    predictions = MODEL.predict(image, verbose=0)[0].copy()

    # Biological Organ Filtering:
    # If the image is a leaf, suppress fruit-only classes so a leaf is never diagnosed as a fruit disease
    if is_leaf_foliage(image_path):
        fruit_suppressed = False
        for i, c in enumerate(CLASS_NAMES):
            info = get_disease_info(c)
            if info and info.get("affected_part") == "Fruit":
                predictions[i] *= 0.01
                fruit_suppressed = True
        if fruit_suppressed:
            total_prob = float(np.sum(predictions))
            if total_prob > 0:
                predictions = predictions / total_prob

    # Crop filter (if user specified a target crop)
    if crop and crop.lower() not in ["auto", "all", ""]:
        crop_clean = crop.strip().lower()
        crop_indices = []
        for i, c in enumerate(CLASS_NAMES):
            info = get_disease_info(c)
            if info:
                plant_name = str(info.get("plant", "")).lower()
                if crop_clean in plant_name or plant_name in crop_clean:
                    crop_indices.append(i)

        if crop_indices:
            mask = np.zeros_like(predictions)
            mask[crop_indices] = predictions[crop_indices]
            total_crop_prob = float(np.sum(mask))
            if total_crop_prob > 0:
                predictions = mask / total_crop_prob

    # --------------------------------------------------------
    # TOP 3 PREDICTIONS
    # --------------------------------------------------------
    top_indices = np.argsort(predictions)[-3:][::-1]
    top_predictions = []

    for index in top_indices:
        index = int(index)
        model_class = CLASS_NAMES[index]
        confidence = float(predictions[index] * 100)
        info = get_disease_info(model_class)

        if info:
            disease = info.get("disease", "Unknown")
            plant = info.get("plant", "Unknown")
        else:
            disease = "Unknown"
            plant = "Unknown"

        top_predictions.append({
            "model_class": model_class,
            "disease": disease,
            "plant": plant,
            "confidence": confidence
        })

    # --------------------------------------------------------
    # MAIN PREDICTION
    # --------------------------------------------------------
    predicted_index = int(np.argmax(predictions))
    predicted_class = CLASS_NAMES[predicted_index]
    confidence = float(predictions[predicted_index] * 100)

    return (
        predicted_class,
        confidence,
        top_predictions
    )


# ============================================================
# BUILD RESULT
# ============================================================

def build_result(
    predicted_class,
    confidence,
    top_predictions
):

    info = get_disease_info(
        predicted_class
    )


    # --------------------------------------------------------
    # DATABASE ENTRY NOT FOUND
    # --------------------------------------------------------

    if not info:

        return {

            "model_class":
                predicted_class,

            "disease":
                "Unknown",

            "plant":
                "Unknown",

            "affected_part":
                "Unknown",

            "disease_type":
                "Unknown",

            "confidence":
                confidence,

            "healthy":
                False,

            "knowledge_available":
                False,

            "cause":
                "",

            "pathogen":
                "",

            "symptoms":
                [],

            "why_it_happens":
                [],

            "favorable_conditions":
                [],

            "prevention":
                [],

            "immediate_action":
                [],

            "cultural_control":
                [],

            "biological_control":
                [],

            "chemical_control":
                "",

            "safety_warning":
                "",

            "top_predictions":
                top_predictions
        }


    # --------------------------------------------------------
    # HEALTHY
    # --------------------------------------------------------

    healthy = is_healthy_class(
        predicted_class
    )


    # --------------------------------------------------------
    # GET DATABASE FIELDS
    # --------------------------------------------------------

    cause = info.get(
        "cause",
        ""
    )

    pathogen = info.get(
        "pathogen",
        ""
    )

    symptoms = info.get(
        "symptoms",
        []
    )

    why_it_happens = info.get(
        "why_it_happens",
        []
    )

    favorable_conditions = info.get(
        "favorable_conditions",
        []
    )

    prevention = info.get(
        "prevention",
        []
    )

    immediate_action = info.get(
        "immediate_action",
        []
    )

    cultural_control = info.get(
        "cultural_control",
        []
    )

    biological_control = info.get(
        "biological_control",
        []
    )

    chemical_control = info.get(
        "chemical_control",
        ""
    )

    safety_warning = info.get(
        "safety_warning",
        ""
    )


    # --------------------------------------------------------
    # KNOWLEDGE AVAILABLE
    # --------------------------------------------------------

    knowledge_available = bool(
        cause
        or pathogen
        or symptoms
        or why_it_happens
        or favorable_conditions
        or prevention
        or immediate_action
        or cultural_control
        or biological_control
        or chemical_control
    )


    # --------------------------------------------------------
    # FINAL RESULT
    # --------------------------------------------------------

    return {

        "model_class":
            predicted_class,

        "disease": (

            "No Disease"

            if healthy

            else info.get(
                "disease",
                "Unknown"
            )
        ),

        "plant":
            info.get(
                "plant",
                "Unknown"
            ),

        "affected_part":
            info.get(
                "affected_part",
                "Unknown"
            ),

        "disease_type":
            info.get(
                "disease_type",
                "Unknown"
            ),

        "confidence":
            confidence,

        "healthy":
            healthy,

        "knowledge_available":
            knowledge_available,

        "cause":
            cause,

        "pathogen":
            pathogen,

        "symptoms":
            symptoms,

        "why_it_happens":
            why_it_happens,

        "favorable_conditions":
            favorable_conditions,

        "prevention":
            prevention,

        "immediate_action":
            immediate_action,

        "cultural_control":
            cultural_control,

        "biological_control":
            biological_control,

        "chemical_control":
            chemical_control,

        "safety_warning":
            safety_warning,

        "top_predictions":
            top_predictions
    }


# ============================================================
# HOME PAGE
# ============================================================

@app.route(
    "/",
    methods=["GET"]
)
def index():

    return render_template(
        "index.html",
        result=None,
        image_url=None
    )


# ============================================================
# PREDICT ROUTE
# ============================================================

@app.route(
    "/predict",
    methods=["POST"]
)
def predict():

    # --------------------------------------------------------
    # CHECK FILE
    # --------------------------------------------------------

    if "image" not in request.files:

        flash(
            "Please select an image.",
            "error"
        )

        return redirect(
            url_for("index")
        )


    file = request.files[
        "image"
    ]


    # --------------------------------------------------------
    # EMPTY FILE
    # --------------------------------------------------------

    if file.filename == "":

        flash(
            "Please select an image.",
            "error"
        )

        return redirect(
            url_for("index")
        )


    # --------------------------------------------------------
    # FILE TYPE
    # --------------------------------------------------------

    if not allowed_file(
        file.filename
    ):

        flash(
            "Invalid image format. "
            "Use JPG, JPEG, PNG, WEBP or BMP.",
            "error"
        )

        return redirect(
            url_for("index")
        )


    try:

        # ----------------------------------------------------
        # SECURE FILE NAME
        # ----------------------------------------------------

        original_name = secure_filename(
            file.filename
        )


        extension = (
            original_name
            .rsplit(".", 1)[1]
            .lower()
        )


        unique_name = (
            uuid.uuid4().hex
            + "."
            + extension
        )


        image_path = (
            UPLOAD_DIR
            / unique_name
        )


        file.save(
            image_path
        )


        # ----------------------------------------------------
        # GATEKEEPER: Check if image is a genuine plant leaf
        # ----------------------------------------------------

        is_valid, rejection_reason = is_plant_image(image_path)

        if not is_valid:
            try:
                image_path.unlink(missing_ok=True)
            except Exception:
                pass
            flash(rejection_reason, "error")
            return redirect(url_for("index"))


        # ----------------------------------------------------
        # PREDICT
        # ----------------------------------------------------

        (
            predicted_class,
            confidence,
            top_predictions
        ) = predict_image(
            image_path
        )


        print()
        print("=" * 70)
        print("PREDICTION")
        print("=" * 70)

        print(
            "Class      :",
            predicted_class
        )

        print(
            "Confidence :",
            f"{confidence:.2f}%"
        )

        print("=" * 70)

        # Post-inference confidence gate: reject ambiguous non-plant predictions
        if confidence < 20.0:
            try:
                image_path.unlink(missing_ok=True)
            except Exception:
                pass
            flash("Low confidence prediction. The image does not clearly match any plant disease in our database. Please upload a clear photo of an infected leaf.", "error")
            return redirect(url_for("index"))


        # ----------------------------------------------------
        # DATABASE
        # ----------------------------------------------------

        result = build_result(
            predicted_class,
            confidence,
            top_predictions
        )


        # ----------------------------------------------------
        # IMAGE URL
        # ----------------------------------------------------

        image_url = url_for(
            "static",
            filename=(
                "uploads/"
                + unique_name
            )
        )


        # ----------------------------------------------------
        # DISPLAY RESULT
        # ----------------------------------------------------

        return render_template(
            "index.html",
            result=result,
            image_url=image_url
        )


    except Exception as error:

        print()
        print("=" * 70)
        print("PREDICTION ERROR")
        print("=" * 70)

        print(
            type(error).__name__
        )

        print(
            str(error)
        )

        print("=" * 70)


        flash(
            "Unable to analyze the image. "
            "Please try another image.",
            "error"
        )

        return redirect(
            url_for("index")
        )


# ============================================================
# REST API ENDPOINTS (FOR FLUTTER & EXTERNAL CLIENTS)
# ============================================================

@app.route("/api/health", methods=["GET"])
def api_health():
    """
    Health check endpoint to verify backend status.
    """
    return jsonify({
        "status": "online",
        "model": "EfficientNetB0",
        "classes_count": len(CLASS_NAMES),
        "database_entries": len(DISEASE_DATABASE),
        "test_accuracy": "92.88%",
        "supported_crops": SUPPORTED_CROPS
    }), 200


@app.route("/api/predict", methods=["POST"])
def api_predict():
    """
    REST API endpoint for plant disease diagnosis.
    Accepts multipart form-data image upload (key: 'image' or 'file').
    Optional form field: 'crop' (e.g. 'Potato', 'Tomato', 'Apple', etc.)
    Returns structured JSON with predictions and treatment guidelines.
    """
    try:
        # Check if file part exists
        file = None
        if "image" in request.files:
            file = request.files["image"]
        elif "file" in request.files:
            file = request.files["file"]

        if not file or file.filename == "":
            return jsonify({
                "status": "error",
                "message": "No image provided. Please send an image using key 'image' or 'file'."
            }), 400

        if not allowed_file(file.filename):
            return jsonify({
                "status": "error",
                "message": f"Invalid file format. Allowed extensions: {', '.join(sorted(ALLOWED_EXTENSIONS))}"
            }), 400

        # Save uploaded image safely
        extension = file.filename.rsplit(".", 1)[1].lower()
        unique_name = uuid.uuid4().hex + "." + extension
        image_path = UPLOAD_DIR / unique_name
        file.save(image_path)

        # ----------------------------------------------------
        # GATEKEEPER: Validate leaf image (reject humans, clothes, electronics)
        # ----------------------------------------------------
        is_valid, rejection_reason = is_plant_image(image_path)

        if not is_valid:
            try:
                image_path.unlink(missing_ok=True)
            except Exception:
                pass
            return jsonify({
                "status": "not_a_plant",
                "message": rejection_reason
            }), 422

        # Optional crop filter from client
        crop = request.form.get("crop") or request.args.get("crop")

        # Run prediction
        predicted_class, confidence, top_predictions = predict_image(image_path, crop=crop)

        # Post-inference confidence gate: reject ambiguous non-plant predictions
        if confidence < 15.0:
            try:
                image_path.unlink(missing_ok=True)
            except Exception:
                pass
            return jsonify({
                "status": "not_a_plant",
                "message": "Low confidence prediction. The image does not clearly match any plant disease in our database. Please upload a clear photo of an infected leaf."
            }), 422

        diagnosis = build_result(predicted_class, confidence, top_predictions)

        return jsonify({
            "status": "success",
            "prediction": diagnosis,
            "image_filename": unique_name
        }), 200

    except Exception as error:
        print("\nAPI PREDICTION ERROR:", str(error))
        return jsonify({
            "status": "error",
            "message": f"Prediction failed: {str(error)}"
        }), 500


# ============================================================
# RUN APPLICATION
# ============================================================

if __name__ == "__main__":

    print()
    print("=" * 70)
    print("PLANT DISEASE DETECTION WEB APPLICATION")
    print("=" * 70)

    print(
        "Model       : EfficientNetB0"
    )

    print(
        "Classes     : 62"
    )

    print(
        "Test Acc.   : 92.88%"
    )

    print(
        "Database    :",
        len(DISEASE_DATABASE),
        "entries"
    )

    print()

    print(
        "Open:"
    )

    print(
        "http://127.0.0.1:5000"
    )

    print("=" * 70)


    app.run(
        host="0.0.0.0",
        port=5000,
        debug=False
    )
