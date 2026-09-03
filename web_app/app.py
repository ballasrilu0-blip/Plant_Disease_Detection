"""
============================================================
PLANT DISEASE DETECTION WEB APPLICATION
============================================================

Model:
    EfficientNetB0

Classes:
    62

Test Accuracy:
    90.88%

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
    flash
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
# PROJECT PATHS
# ============================================================

WEB_APP_DIR = Path(__file__).resolve().parent

PROJECT_DIR = WEB_APP_DIR.parent

MODEL_PATH = (
    PROJECT_DIR
    / "models"
    / "best_model.keras"
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
    "Test Acc.  : 90.88%"
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

def predict_image(image_path):

    image = preprocess_image(
        image_path
    )

    predictions = MODEL.predict(
        image,
        verbose=0
    )[0]


    # --------------------------------------------------------
    # TOP 3 PREDICTIONS
    # --------------------------------------------------------

    top_indices = np.argsort(
        predictions
    )[-3:][::-1]


    top_predictions = []


    for index in top_indices:

        index = int(index)

        model_class = CLASS_NAMES[
            index
        ]

        confidence = float(
            predictions[index] * 100
        )


        info = get_disease_info(
            model_class
        )


        if info:

            disease = info.get(
                "disease",
                "Unknown"
            )

            plant = info.get(
                "plant",
                "Unknown"
            )

        else:

            disease = "Unknown"

            plant = "Unknown"


        top_predictions.append({

            "model_class":
                model_class,

            "disease":
                disease,

            "plant":
                plant,

            "confidence":
                confidence
        })


    # --------------------------------------------------------
    # MAIN PREDICTION
    # --------------------------------------------------------

    predicted_index = int(
        np.argmax(predictions)
    )

    predicted_class = CLASS_NAMES[
        predicted_index
    ]

    confidence = float(
        predictions[
            predicted_index
        ] * 100
    )


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
        "Test Acc.   : 90.88%"
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
        host="127.0.0.1",
        port=5000,
        debug=False
    )