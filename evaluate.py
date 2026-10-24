import tensorflow as tf
import numpy as np
import os
import csv


# ============================================================
# CONFIGURATION
# ============================================================

MODEL_PATH = "models/final_model.keras"
TEST_DIR = "dataset/test"

IMG_SIZE = (224, 224)
BATCH_SIZE = 32


# ============================================================
# HEADER
# ============================================================

print("=" * 75)
print("PLANT DISEASE MODEL EVALUATION")
print("=" * 75)


# ============================================================
# CHECK MODEL
# ============================================================

if not os.path.exists(MODEL_PATH):

    print()
    print("ERROR: Model not found:")
    print(MODEL_PATH)

    raise SystemExit


# ============================================================
# CHECK DATASET
# ============================================================

if not os.path.exists(TEST_DIR):

    print()
    print("ERROR: Test dataset not found:")
    print(TEST_DIR)

    raise SystemExit


# ============================================================
# LOAD MODEL
# ============================================================

print()
print("Loading model...")
print("Model:", MODEL_PATH)

model = tf.keras.models.load_model(
    MODEL_PATH
)

print("Model loaded successfully.")


# ============================================================
# LOAD TEST DATASET
# ============================================================

print()
print("Loading test dataset...")

test_data = tf.keras.utils.image_dataset_from_directory(
    TEST_DIR,
    image_size=IMG_SIZE,
    batch_size=BATCH_SIZE,
    shuffle=False
)


class_names = test_data.class_names
num_classes = len(class_names)


print()
print("Number of classes:", num_classes)

print()
print("Classes:")

for i, name in enumerate(class_names):
    print(f"{i:3d} : {name}")


# ============================================================
# MODEL EVALUATION
# ============================================================

print()
print("=" * 75)
print("OVERALL EVALUATION")
print("=" * 75)

results = model.evaluate(
    test_data,
    verbose=1
)

print()

print("Raw evaluation results:", results)

# First value is loss.
loss = float(results[0])

# Accuracy is normally the second value.
accuracy = float(results[1])


print()
print("=" * 75)
print("FINAL RESULT")
print("=" * 75)

print(f"Test Loss     : {loss:.4f}")
print(f"Test Accuracy : {accuracy * 100:.2f}%")

if len(results) >= 3:
    print(f"Top-3 Accuracy: {float(results[2]) * 100:.2f}%")

print("=" * 75)


# ============================================================
# GET TRUE LABELS
# ============================================================

print()
print("Collecting test labels...")

true_labels = []

for images, labels in test_data:

    true_labels.extend(
        labels.numpy().tolist()
    )

true_labels = np.array(true_labels)


print(
    "Number of test images:",
    len(true_labels)
)


# ============================================================
# GET PREDICTIONS
# ============================================================

print()
print("Generating predictions...")
print("This may take some time on CPU.")

predictions = model.predict(
    test_data,
    verbose=1
)


predicted_labels = np.argmax(
    predictions,
    axis=1
)


# ============================================================
# CONFUSION MATRIX
# ============================================================

print()
print("Building confusion matrix...")

confusion_matrix = tf.math.confusion_matrix(
    true_labels,
    predicted_labels,
    num_classes=num_classes
).numpy()


# ============================================================
# PER-CLASS ACCURACY
# ============================================================

print()
print("=" * 75)
print("PER-CLASS ACCURACY")
print("=" * 75)

class_results = []

for i, class_name in enumerate(class_names):

    total = int(
        np.sum(confusion_matrix[i])
    )

    correct = int(
        confusion_matrix[i, i]
    )

    if total > 0:
        class_accuracy = (
            correct / total
        ) * 100
    else:
        class_accuracy = 0.0

    class_results.append(
        (
            class_accuracy,
            class_name,
            correct,
            total
        )
    )


# Sort from worst to best
class_results_sorted = sorted(
    class_results,
    key=lambda x: x[0]
)


print()
print(
    f"{'Class':<40}"
    f"{'Correct':>10}"
    f"{'Total':>10}"
    f"{'Accuracy':>12}"
)

print("-" * 75)


for accuracy_value, name, correct, total in class_results_sorted:

    print(
        f"{name:<40}"
        f"{correct:>10}"
        f"{total:>10}"
        f"{accuracy_value:>11.2f}%"
    )


# ============================================================
# WORST CLASSES
# ============================================================

print()
print("=" * 75)
print("10 LOWEST-PERFORMING CLASSES")
print("=" * 75)

for rank, item in enumerate(
    class_results_sorted[:10],
    start=1
):

    accuracy_value, name, correct, total = item

    print(
        f"{rank:2d}. "
        f"{name:<40} "
        f"{accuracy_value:6.2f}% "
        f"({correct}/{total})"
    )


# ============================================================
# MISCLASSIFICATIONS
# ============================================================

print()
print("=" * 75)
print("MOST COMMON MISCLASSIFICATIONS")
print("=" * 75)


misclassifications = []


for true_index in range(num_classes):

    for predicted_index in range(num_classes):

        if true_index == predicted_index:
            continue

        count = int(
            confusion_matrix[
                true_index,
                predicted_index
            ]
        )

        if count > 0:

            misclassifications.append(
                (
                    count,
                    class_names[true_index],
                    class_names[predicted_index]
                )
            )


misclassifications.sort(
    reverse=True
)


print()

for rank, (count, actual, predicted) in enumerate(
    misclassifications[:20],
    start=1
):

    print(
        f"{rank:2d}. "
        f"{actual}"
        f" -> "
        f"{predicted}"
        f" : {count}"
    )


# ============================================================
# APPLE / CITRUS ANALYSIS
# ============================================================

print()
print("=" * 75)
print("APPLE / CITRUS CONFUSION ANALYSIS")
print("=" * 75)


apple_or_citrus_indices = []


for i, class_name in enumerate(class_names):

    name_lower = class_name.lower()

    if (
        "apple" in name_lower
        or
        "citrus" in name_lower
    ):

        apple_or_citrus_indices.append(i)


if len(apple_or_citrus_indices) == 0:

    print()
    print("No apple/citrus classes found.")

else:

    print()

    for true_index in apple_or_citrus_indices:

        actual_name = class_names[true_index]

        total = int(
            np.sum(confusion_matrix[true_index])
        )

        correct = int(
            confusion_matrix[
                true_index,
                true_index
            ]
        )

        print()
        print(
            f"ACTUAL CLASS: {actual_name}"
        )

        print(
            f"Correct: {correct}/{total}"
        )

        if total > 0:

            print(
                f"Accuracy: "
                f"{correct / total * 100:.2f}%"
            )


        print("Predicted as:")

        confusion_entries = []


        for predicted_index in range(num_classes):

            count = int(
                confusion_matrix[
                    true_index,
                    predicted_index
                ]
            )

            if (
                count > 0
                and
                predicted_index != true_index
            ):

                confusion_entries.append(
                    (
                        count,
                        class_names[predicted_index]
                    )
                )


        confusion_entries.sort(
            reverse=True
        )


        if len(confusion_entries) == 0:

            print("  No incorrect predictions.")

        else:

            for count, predicted_name in confusion_entries[:10]:

                print(
                    f"  -> "
                    f"{predicted_name}: "
                    f"{count}"
                )


# ============================================================
# SAVE CONFUSION MATRIX
# ============================================================

OUTPUT_FILE = "reports/confusion_matrix.csv"


os.makedirs(
    "reports",
    exist_ok=True
)


print()
print("Saving confusion matrix...")

with open(
    OUTPUT_FILE,
    "w",
    newline="",
    encoding="utf-8"
) as f:

    writer = csv.writer(f)

    writer.writerow(
        ["Actual / Predicted"] + class_names
    )

    for i, class_name in enumerate(class_names):

        writer.writerow(
            [class_name]
            +
            confusion_matrix[i].tolist()
        )


print(
    "Saved:",
    OUTPUT_FILE
)


# ============================================================
# FINISHED
# ============================================================

print()
print("=" * 75)
print("EVALUATION COMPLETED")
print("=" * 75)