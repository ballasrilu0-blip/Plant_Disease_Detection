"""
==========================================================
Plant Disease Detection

Dataset Splitter

Splits merged_dataset into

80% Train
10% Validation
10% Test

==========================================================
"""

import os
import shutil

from tqdm import tqdm

from sklearn.model_selection import train_test_split

# ==========================================================
# PROJECT PATHS
# ==========================================================

PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))

DATASET_DIR = os.path.join(PROJECT_DIR, "dataset")

MERGED_DATASET = os.path.join(DATASET_DIR, "merged_dataset")

TRAIN_DIR = os.path.join(DATASET_DIR, "train")

VALIDATION_DIR = os.path.join(DATASET_DIR, "validation")

TEST_DIR = os.path.join(DATASET_DIR, "test")

# ==========================================================
# SPLIT SETTINGS
# ==========================================================

TRAIN_RATIO = 0.80

VALIDATION_RATIO = 0.10

TEST_RATIO = 0.10

RANDOM_STATE = 42

IMAGE_EXTENSIONS = (

    ".jpg",

    ".jpeg",

    ".png",

    ".bmp",

    ".tif",

    ".tiff",

    ".webp"

)

# ==========================================================
# HEADER
# ==========================================================

def header(title):

    print()

    print("=" * 70)

    print(title)

    print("=" * 70)

# ==========================================================
# IMAGE CHECK
# ==========================================================

def is_image(file):

    return file.lower().endswith(IMAGE_EXTENSIONS)

# ==========================================================
# DELETE OLD SPLITS
# ==========================================================

def remove_old_split():

    header("REMOVING OLD SPLITS")

    for folder in [

        TRAIN_DIR,

        VALIDATION_DIR,

        TEST_DIR

    ]:

        if os.path.exists(folder):

            shutil.rmtree(folder)

            print("Deleted :", folder)

# ==========================================================
# CREATE NEW SPLITS
# ==========================================================

def create_directories():

    header("CREATING DATASET FOLDERS")

    os.makedirs(TRAIN_DIR, exist_ok=True)

    os.makedirs(VALIDATION_DIR, exist_ok=True)

    os.makedirs(TEST_DIR, exist_ok=True)

    print("Folders Created Successfully")
    # ==========================================================
# COPY IMAGES
# ==========================================================

def copy_images(images, destination):

    os.makedirs(destination, exist_ok=True)

    count = 0

    for image in tqdm(images, leave=False):

        shutil.copy2(

            image,

            os.path.join(

                destination,

                os.path.basename(image)

            )

        )

        count += 1

    return count


# ==========================================================
# SPLIT ONE CLASS
# ==========================================================

def split_class(class_name):

    class_path = os.path.join(MERGED_DATASET, class_name)

    images = [

        os.path.join(class_path, img)

        for img in os.listdir(class_path)

        if is_image(img)

    ]

    total_images = len(images)

    # Skip extremely small classes
    if total_images < 5:

        print(f"Skipping {class_name} ({total_images} images)")

        return 0, 0, 0

    train_images, remaining_images = train_test_split(

        images,

        train_size=0.80,

        random_state=RANDOM_STATE,

        shuffle=True

    )

    # If remaining images are too few,
    # keep one for validation and one for test.

    if len(remaining_images) < 2:

        validation_images = remaining_images
        test_images = []

    else:

        validation_images, test_images = train_test_split(

            remaining_images,

            test_size=0.5,

            random_state=RANDOM_STATE,

            shuffle=True

        )

    train_folder = os.path.join(TRAIN_DIR, class_name)

    validation_folder = os.path.join(VALIDATION_DIR, class_name)

    test_folder = os.path.join(TEST_DIR, class_name)

    train_count = copy_images(train_images, train_folder)

    validation_count = copy_images(validation_images, validation_folder)

    test_count = copy_images(test_images, test_folder)

    return train_count, validation_count, test_count


# ==========================================================
# SPLIT COMPLETE DATASET
# ==========================================================

def split_dataset():

    header("SPLITTING MERGED DATASET")

    total_train = 0

    total_validation = 0

    total_test = 0

    classes = sorted(os.listdir(MERGED_DATASET))

    print()

    print("Total Classes :", len(classes))

    for cls in classes:

        class_path = os.path.join(

            MERGED_DATASET,

            cls

        )

        if not os.path.isdir(class_path):

            continue

        print()

        print("Processing :", cls)

        train_count, validation_count, test_count = split_class(cls)

        total_train += train_count

        total_validation += validation_count

        total_test += test_count

    return (

        total_train,

        total_validation,

        total_test

    )
# ==========================================================
# VERIFY DATASET
# ==========================================================

def verify_dataset():

    header("VERIFYING DATASET")

    datasets = {

        "Train": TRAIN_DIR,

        "Validation": VALIDATION_DIR,

        "Test": TEST_DIR

    }

    grand_total = 0

    for name, folder in datasets.items():

        class_count = 0

        image_count = 0

        if not os.path.exists(folder):

            continue

        for cls in sorted(os.listdir(folder)):

            class_path = os.path.join(folder, cls)

            if not os.path.isdir(class_path):

                continue

            images = [

                img

                for img in os.listdir(class_path)

                if is_image(img)

            ]

            class_count += 1

            image_count += len(images)

        grand_total += image_count

        print()

        print("=" * 50)

        print(name)

        print("=" * 50)

        print("Classes :", class_count)

        print("Images  :", image_count)

    print()

    print("=" * 70)

    print("TOTAL IMAGES :", grand_total)

    print("=" * 70)


# ==========================================================
# SAVE SPLIT REPORT
# ==========================================================

def save_report():

    header("SAVING REPORT")

    report_path = os.path.join(

        DATASET_DIR,

        "outputs",

        "split_dataset_report.csv"

    )

    os.makedirs(

        os.path.dirname(report_path),

        exist_ok=True

    )

    with open(report_path, "w", encoding="utf-8") as file:

        file.write("Dataset,Class,Images\n")

        datasets = {

            "Train": TRAIN_DIR,

            "Validation": VALIDATION_DIR,

            "Test": TEST_DIR

        }

        for dataset_name, folder in datasets.items():

            for cls in sorted(os.listdir(folder)):

                class_path = os.path.join(folder, cls)

                if not os.path.isdir(class_path):

                    continue

                images = [

                    img

                    for img in os.listdir(class_path)

                    if is_image(img)

                ]

                file.write(

                    f"{dataset_name},{cls},{len(images)}\n"

                )

    print("Report Saved")

    print(report_path)


# ==========================================================
# FINAL SUMMARY
# ==========================================================

def summary(train, validation, test):

    header("DATASET SUMMARY")

    total = train + validation + test

    print("Training Images   :", train)

    print("Validation Images :", validation)

    print("Testing Images    :", test)

    print("-" * 40)

    print("Total Images      :", total)

    print()

    print("Split Ratio")

    print("Train      : 80%")

    print("Validation : 10%")

    print("Test       : 10%")

    print()

    print("Dataset Ready For Training")
    # ==========================================================
# MAIN PIPELINE
# ==========================================================

def main():

    header("PLANT DISEASE DATASET SPLITTER")

    # Step 1
    remove_old_split()

    # Step 2
    create_directories()

    # Step 3
    train_count, validation_count, test_count = split_dataset()

    # Step 4
    verify_dataset()

    # Step 5
    save_report()

    # Step 6
    summary(

        train_count,

        validation_count,

        test_count

    )

    header("DATASET SPLITTING COMPLETED SUCCESSFULLY")

    print()

    print("=" * 70)

    print("YOUR DATASET IS READY FOR EFFICIENTNETB0 TRAINING")

    print("=" * 70)

    print()

    print("Merged Dataset")

    print(MERGED_DATASET)

    print()

    print("Training Dataset")

    print(TRAIN_DIR)

    print()

    print("Validation Dataset")

    print(VALIDATION_DIR)

    print()

    print("Testing Dataset")

    print(TEST_DIR)


# ==========================================================
# MAIN
# ==========================================================

if __name__ == "__main__":

    try:

        main()

    except KeyboardInterrupt:

        print()

        print("=" * 70)

        print("PROCESS INTERRUPTED")

        print("=" * 70)

    except Exception as error:

        print()

        print("=" * 70)

        print("ERROR OCCURRED")

        print("=" * 70)

        print(error)
        