# ============================================================
# PLANT DISEASE DETECTION SYSTEM
# EfficientNetB0
# Complete Prediction Code
# ============================================================

import os
import sys
import pickle
import numpy as np
import tensorflow as tf

from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image


# ============================================================
# CONFIGURATION
# ============================================================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

MODEL_DIR = os.path.join(BASE_DIR, "models")

MODEL_PATH = os.path.join(
    MODEL_DIR,
    "final_model.keras"
)

LABELS_PATH = os.path.join(
    MODEL_DIR,
    "labels.txt"
)

CLASS_INDICES_PATH = os.path.join(
    MODEL_DIR,
    "class_indices.pkl"
)

IMAGE_SIZE = (224, 224)

TOP_K = 5


# ============================================================
# HEADER
# ============================================================

print()
print("=" * 75)
print("              PLANT DISEASE DETECTION SYSTEM")
print("=" * 75)
print("                         EfficientNetB0")
print("=" * 75)
print()


# ============================================================
# CHECK MODEL
# ============================================================

print("Loading trained model...")
print()


if not os.path.exists(MODEL_PATH):

    print("=" * 75)
    print("ERROR: MODEL NOT FOUND")
    print("=" * 75)

    print()
    print("Expected model:")
    print(MODEL_PATH)

    sys.exit(1)


# ============================================================
# LOAD MODEL
# ============================================================

try:

    model = load_model(
        MODEL_PATH,
        compile=False
    )

    print("Model loaded successfully.")
    print("Model path :", MODEL_PATH)

except Exception as e:

    print()
    print("=" * 75)
    print("ERROR LOADING MODEL")
    print("=" * 75)

    print()
    print(e)

    sys.exit(1)


# ============================================================
# LOAD CLASS INFORMATION
# ============================================================

class_names = []


# ============================================================
# LOAD labels.txt
# ============================================================

if os.path.exists(LABELS_PATH):

    print()
    print("Loading class labels...")
    print("Labels path :", LABELS_PATH)

    try:

        with open(
            LABELS_PATH,
            "r",
            encoding="utf-8"
        ) as f:

            lines = f.readlines()


        for line in lines:

            line = line.strip()

            if not line:
                continue

            # Supports:
            #
            # 0 : anthracnose
            #
            # and:
            #
            # anthracnose

            if ":" in line:

                parts = line.split(
                    ":",
                    1
                )

                class_name = parts[1].strip()

            else:

                class_name = line


            if class_name:

                class_names.append(
                    class_name
                )


        print(
            "Labels loaded successfully."
        )

        print(
            "Number of labels :",
            len(class_names)
        )


    except Exception as e:

        print()
        print(
            "Error reading labels.txt:"
        )

        print(e)

        class_names = []


else:

    print()
    print(
        "labels.txt not found."
    )


# ============================================================
# LOAD class_indices.pkl
# ============================================================

if os.path.exists(
    CLASS_INDICES_PATH
):

    print()
    print(
        "Class index file found."
    )

    print(
        "Class index path :",
        CLASS_INDICES_PATH
    )

    try:

        with open(
            CLASS_INDICES_PATH,
            "rb"
        ) as f:

            class_indices = pickle.load(
                f
            )


        # ----------------------------------------------------
        # Only use pickle if labels.txt was not loaded
        # ----------------------------------------------------

        if len(class_names) == 0:

            if isinstance(
                class_indices,
                dict
            ):

                sorted_classes = sorted(

                    class_indices.items(),

                    key=lambda x: x[1]

                )


                class_names = [

                    name

                    for name, index
                    in sorted_classes

                ]


        print(
            "Class index information loaded."
        )


    except Exception as e:

        print()
        print(
            "Error reading class_indices.pkl:"
        )

        print(e)


else:

    print()
    print(
        "class_indices.pkl not found."
    )


# ============================================================
# FALLBACK
# ============================================================

if len(class_names) == 0:

    print()
    print("=" * 75)
    print(
        "WARNING: CLASS INFORMATION NOT FOUND"
    )
    print("=" * 75)

    print()
    print(
        "Using generic class names."
    )


    class_names = [

        f"Class_{i}"

        for i in range(62)

    ]


# ============================================================
# NUMBER OF CLASSES
# ============================================================

NUM_CLASSES = len(
    class_names
)


print()
print("=" * 75)
print("CLASS INFORMATION")
print("=" * 75)

print()
print(
    "Number of classes :",
    NUM_CLASSES
)


# ============================================================
# DISPLAY CLASSES
# ============================================================

print()
print("-" * 75)
print("CLASS LIST")
print("-" * 75)


for i, class_name in enumerate(
    class_names
):

    print(
        f"{i:3d} : {class_name}"
    )


# ============================================================
# IMAGE PREPROCESSING
# ============================================================

def prepare_image(
    image_path
):

    try:

        img = image.load_img(

            image_path,

            target_size=IMAGE_SIZE

        )


        img_array = image.img_to_array(
            img
        )


        img_array = img_array.astype(
            np.float32
        )


        # ----------------------------------------------------
        # EfficientNet preprocessing
        # ----------------------------------------------------
        #
        # Keras EfficientNet models normally contain their
        # preprocessing internally.
        #
        # Therefore we do not divide by 255 here.
        # ----------------------------------------------------


        img_array = np.expand_dims(

            img_array,

            axis=0

        )


        return img_array


    except Exception as e:

        print()
        print(
            "ERROR PROCESSING IMAGE"
        )

        print(e)

        return None


# ============================================================
# PREDICTION FUNCTION
# ============================================================

def predict_image(
    image_path
):

    # --------------------------------------------------------
    # Check file
    # --------------------------------------------------------

    if not os.path.isfile(
        image_path
    ):

        print()
        print("=" * 75)
        print("ERROR: IMAGE NOT FOUND")
        print("=" * 75)

        print()
        print(
            "Image path:"
        )

        print(
            image_path
        )

        return


    # --------------------------------------------------------
    # Prepare image
    # --------------------------------------------------------

    img_array = prepare_image(
        image_path
    )


    if img_array is None:

        return


    # ========================================================
    # PREDICTION
    # ========================================================

    print()
    print("=" * 75)
    print("ANALYZING IMAGE")
    print("=" * 75)

    print()
    print(
        "Image :",
        image_path
    )

    print()
    print(
        "Running prediction..."
    )


    try:

        predictions = model.predict(

            img_array,

            verbose=0

        )


    except Exception as e:

        print()
        print("=" * 75)
        print("PREDICTION ERROR")
        print("=" * 75)

        print()
        print(e)

        return


    # ========================================================
    # PROCESS OUTPUT
    # ========================================================

    predictions = np.asarray(
        predictions
    )


    predictions = np.squeeze(
        predictions
    )


    # --------------------------------------------------------
    # Check output shape
    # --------------------------------------------------------

    if predictions.ndim != 1:

        print()
        print(
            "Unexpected prediction shape:"
        )

        print(
            predictions.shape
        )

        return


    # ========================================================
    # SOFTMAX
    # ========================================================

    prediction_sum = np.sum(
        predictions
    )


    if (

        np.min(predictions) < 0

        or

        np.max(predictions) > 1

        or

        not np.isclose(
            prediction_sum,
            1.0,
            atol=0.05
        )

    ):

        predictions = tf.nn.softmax(

            predictions

        ).numpy()


    # ========================================================
    # BEST CLASS
    # ========================================================

    predicted_index = int(
        np.argmax(predictions)
    )


    confidence = (

        float(
            predictions[
                predicted_index
            ]
        )

        * 100

    )


    # ========================================================
    # CLASS NAME
    # ========================================================

    if (

        predicted_index
        <
        len(class_names)

    ):

        predicted_class = (

            class_names[
                predicted_index
            ]

        )

    else:

        predicted_class = (

            f"Class_{predicted_index}"

        )


    # ========================================================
    # DISPLAY MAIN RESULT
    # ========================================================

    print()
    print("=" * 75)
    print("PREDICTION RESULT")
    print("=" * 75)

    print()

    print(
        "Predicted Class / Disease:"
    )

    print()

    print(
        "   ",
        predicted_class
    )

    print()

    print(
        f"Confidence : {confidence:.2f}%"
    )


    # ========================================================
    # HEALTHY / DISEASE STATUS
    # ========================================================

    class_lower = (
        predicted_class.lower()
    )


    healthy_keywords = [

        "healthy",
        "health",
        "normal"

    ]


    is_healthy = any(

        keyword in class_lower

        for keyword
        in healthy_keywords

    )


    print()


    if is_healthy:

        print(
            "Plant Status : HEALTHY"
        )

    else:

        print(
            "Plant Status : DISEASE DETECTED"
        )


    # ========================================================
    # TOP 5 PREDICTIONS
    # ========================================================

    print()
    print("-" * 75)
    print(
        f"TOP {TOP_K} PREDICTIONS"
    )
    print("-" * 75)


    top_k = min(

        TOP_K,

        len(predictions)

    )


    top_indices = np.argsort(

        predictions

    )[::-1][:top_k]


    for rank, index in enumerate(

        top_indices,

        start=1

    ):

        index = int(
            index
        )


        probability = (

            float(
                predictions[index]
            )

            * 100

        )


        if index < len(class_names):

            name = class_names[index]

        else:

            name = f"Class_{index}"


        print(

            f"{rank}. "
            f"{name:<35} "
            f"{probability:6.2f}%"

        )


    # ========================================================
    # CONFIDENCE LEVEL
    # ========================================================

    print()
    print("-" * 75)
    print("CONFIDENCE LEVEL")
    print("-" * 75)


    if confidence >= 90:

        print(
            "Very High Confidence"
        )

    elif confidence >= 75:

        print(
            "High Confidence"
        )

    elif confidence >= 60:

        print(
            "Moderate Confidence"
        )

    elif confidence >= 40:

        print(
            "Low Confidence"
        )

    else:

        print(
            "Very Low Confidence"
        )


    # ========================================================
    # COMPLETED
    # ========================================================

    print()
    print("=" * 75)
    print(
        "Prediction completed successfully."
    )
    print("=" * 75)


# ============================================================
# READY
# ============================================================

print()
print("=" * 75)
print("READY FOR PREDICTION")
print("=" * 75)

print()
print(
    "Enter plant leaf image path."
)

print()
print(
    "Type 'exit' to close the program."
)


# ============================================================
# PREDICTION LOOP
# ============================================================

while True:

    try:

        image_path = input(
            "\nEnter image path: "
        ).strip()


    except KeyboardInterrupt:

        print()
        print()
        print(
            "Program stopped."
        )

        break


    except EOFError:

        print()
        print()
        print(
            "Program stopped."
        )

        break


    # --------------------------------------------------------
    # Remove quotation marks
    # --------------------------------------------------------

    image_path = image_path.strip(
        '"'
    )

    image_path = image_path.strip(
        "'"
    )


    # ========================================================
    # EXIT
    # ========================================================

    if image_path.lower() in [

        "exit",
        "quit",
        "q"

    ]:

        print()
        print("=" * 75)
        print(
            "Thank you for using Plant Disease Detection System."
        )
        print("=" * 75)

        break


    # ========================================================
    # EMPTY INPUT
    # ========================================================

    if not image_path:

        print()

        print(
            "Please enter an image path."
        )

        continue


    # ========================================================
    # PREDICT
    # ========================================================

    predict_image(
        image_path
    )