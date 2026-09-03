"""
==============================================================================
Plant Disease Detection Using Deep Learning and Image Analytics
File        : preprocess.py
Description : Complete Dataset Preprocessing Pipeline
Author      : Your Name
Version     : 1.0
==============================================================================
Pipeline
1. Scan Dataset
2. Validate Images
3. Remove Corrupted Images
4. Remove Duplicate Images
5. Dataset Analysis
6. Standardize Class Names
7. Merge Datasets
8. Resize Images
9. Train/Validation/Test Split
10. Dataset Report
11. Generate labels.txt
==============================================================================
"""
import os
import cv2
import shutil
import hashlib
import random
import warnings
import pandas as pd
import numpy as np
from PIL import Image
from tqdm import tqdm
from collections import Counter
from sklearn.model_selection import train_test_split
warnings.filterwarnings("ignore")
PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
DATASET_DIR = os.path.join(PROJECT_DIR, "dataset")
RAW_DATASET = os.path.join(DATASET_DIR, "raw_dataset")
CLEANED_DATASET = os.path.join(DATASET_DIR, "cleaned_dataset")
MERGED_DATASET = os.path.join(DATASET_DIR, "merged_dataset")
TRAIN_DATASET = os.path.join(DATASET_DIR, "train")
VALIDATION_DATASET = os.path.join(DATASET_DIR, "validation")
TEST_DATASET = os.path.join(DATASET_DIR, "test")
OUTPUT_DIR = os.path.join(DATASET_DIR, "outputs")
MODEL_DIR = os.path.join(PROJECT_DIR, "models")
LABEL_FILE = os.path.join(MODEL_DIR, "labels.txt")
REPORT_FILE = os.path.join(OUTPUT_DIR, "dataset_report.csv")
LOG_FILE = os.path.join(OUTPUT_DIR, "preprocessing_log.txt")
IMAGE_SIZE = (224, 224)
TRAIN_SPLIT = 0.80
VALIDATION_SPLIT = 0.10
TEST_SPLIT = 0.10
RANDOM_STATE = 42
SUPPORTED_EXTENSIONS = (
    ".jpg",
    ".jpeg",
    ".png",
    ".bmp",
    ".tif",
    ".tiff",
    ".webp"
)
SKIP_FOLDERS = {
    "metadata",
    "outputs"
}
def create_directories():
    folders = [
        CLEANED_DATASET,
        MERGED_DATASET,
        TRAIN_DATASET,
        VALIDATION_DATASET,
        TEST_DATASET,
        OUTPUT_DIR,
        MODEL_DIR
    ]
    for folder in folders:
        os.makedirs(folder, exist_ok=True)
def header(title):
    print("\n")
    print("=" * 80)
    print(title.center(80))
    print("=" * 80)
def log(message):
    print(message)
    with open(LOG_FILE, "a", encoding="utf-8") as file:
        file.write(message + "\n")
def is_image(filename):
    return filename.lower().endswith(SUPPORTED_EXTENSIONS)
def image_hash(filepath):
    md5 = hashlib.md5()
    with open(filepath, "rb") as file:
        while True:
            data = file.read(4096)
            if not data:
                break
            md5.update(data)
    return md5.hexdigest()
def standardize_class_name(name):
    name = name.lower()
    name = name.replace("-", "_")
    name = name.replace(" ", "_")
    name = name.replace("__", "_")
    return name.strip("_")
def copy_image(source, destination):
    os.makedirs(
        os.path.dirname(destination),
        exist_ok=True
    )
    shutil.copy2(source, destination)
def resize_image(source, destination):
    image = cv2.imread(source)
    if image is None:
        return False
    image = cv2.resize(
        image,
        IMAGE_SIZE,
        interpolation=cv2.INTER_AREA
    )
    os.makedirs(
        os.path.dirname(destination),
        exist_ok=True
    )
    cv2.imwrite(destination, image)
    return True
def reset_output_folders():
    folders = [
        CLEANED_DATASET,
        MERGED_DATASET,
        TRAIN_DATASET,
        VALIDATION_DATASET,
        TEST_DATASET
    ]
    for folder in folders:
        if os.path.exists(folder):
            shutil.rmtree(folder)
        os.makedirs(folder)
def initialize():
    create_directories()
    if os.path.exists(LOG_FILE):
        os.remove(LOG_FILE)
    header("PLANT DISEASE DATASET PREPROCESSING")
    log("Initialization Completed")
def scan_dataset():
    header("STEP 1 : SCANNING DATASET")
    dataset_summary = []
    total_datasets = 0
    total_classes = 0
    total_images = 0
    image_formats = Counter()
    if not os.path.exists(RAW_DATASET):
        log("ERROR : Raw dataset folder not found.")
        return dataset_summary
    for dataset in sorted(os.listdir(RAW_DATASET)):
        if dataset.lower() in SKIP_FOLDERS:
            continue
        dataset_path = os.path.join(RAW_DATASET, dataset)
        if not os.path.isdir(dataset_path):
            continue
        total_datasets += 1
        dataset_classes = 0
        dataset_images = 0
        log("-" * 80)
        log(f"Dataset : {dataset}")
        for root, dirs, files in os.walk(dataset_path):
            image_count = 0
            for file in files:
                if is_image(file):
                    image_count += 1
                    dataset_images += 1
                    total_images += 1
                    extension = os.path.splitext(file)[1].lower()
                    image_formats[extension] += 1
            if image_count > 0:
                dataset_classes += 1
        total_classes += dataset_classes
        dataset_summary.append({
            "Dataset": dataset,
            "Classes": dataset_classes,
            "Images": dataset_images
        })
        log(f"Classes : {dataset_classes}")
        log(f"Images  : {dataset_images}")
    header("DATASET SUMMARY")
    log(f"Total Datasets : {total_datasets}")
    log(f"Total Classes  : {total_classes}")
    log(f"Total Images   : {total_images}")
    log("\nImage Formats")
    for fmt, count in image_formats.items():
        log(f"{fmt:<8} : {count}")
    return dataset_summary
def analyze_dataset():
    header("STEP 2 : ANALYZING DATASET")
    class_counter = Counter()
    dataset_counter = Counter()
    image_counter = 0
    for dataset in sorted(os.listdir(RAW_DATASET)):
        if dataset.lower() in SKIP_FOLDERS:
            continue
        dataset_path = os.path.join(RAW_DATASET, dataset)
        if not os.path.isdir(dataset_path):
            continue
        for root, dirs, files in os.walk(dataset_path):
            image_files = [
                file
                for file in files
                if is_image(file)
            ]
            if len(image_files) == 0:
                continue
            class_name = standardize_class_name(
                os.path.basename(root)
            )
            class_counter[class_name] += len(image_files)
            dataset_counter[dataset] += len(image_files)
            image_counter += len(image_files)
    log("\nTop 20 Largest Classes\n")
    for cls, count in class_counter.most_common(20):
        log(f"{cls:<40} {count}")
    return class_counter
def dataset_statistics(class_counter):
    header("STEP 3 : DATASET STATISTICS")
    counts = list(class_counter.values())
    if len(counts) == 0:
        log("Dataset Empty")
        return
    log(f"Total Classes       : {len(counts)}")
    log(f"Largest Class       : {max(counts)}")
    log(f"Smallest Class      : {min(counts)}")
    log(f"Average Images      : {sum(counts)//len(counts)}")
    log(f"Total Images        : {sum(counts)}")
def save_dataset_report(class_counter):
    header("STEP 4 : SAVING REPORT")
    report = []
    for cls, count in sorted(class_counter.items()):
        report.append({
            "Class": cls,
            "Images": count
        })
    df = pd.DataFrame(report)
    df.to_csv(
        REPORT_FILE,
        index=False
    )
    log("Dataset Report Saved")
    log(REPORT_FILE)
def generate_labels(class_counter):
    header("STEP 5 : GENERATING LABELS")
    labels = sorted(
        class_counter.keys()
    )
    with open(
        LABEL_FILE,
        "w",
        encoding="utf-8"
    ) as file:
        for label in labels:
            file.write(label + "\n")
    log("labels.txt Generated")
def run_analysis():
    scan_dataset()
    class_counter = analyze_dataset()
    dataset_statistics(class_counter)
    save_dataset_report(class_counter)
    generate_labels(class_counter)
    return class_counter
def validate_images():
    header("STEP 6 : VALIDATING IMAGES")
    valid_images = 0
    corrupt_images = 0
    zero_byte_images = 0
    valid_list = []
    for dataset in sorted(os.listdir(RAW_DATASET)):
        if dataset.lower() in SKIP_FOLDERS:
            continue
        dataset_path = os.path.join(RAW_DATASET, dataset)
        if not os.path.isdir(dataset_path):
            continue
        log(f"\nChecking : {dataset}")
        for root, dirs, files in os.walk(dataset_path):
            for file in tqdm(files, leave=False):
                if not is_image(file):
                    continue
                path = os.path.join(root, file)
                try:
                    if os.path.getsize(path) == 0:
                        zero_byte_images += 1
                        continue
                    img = Image.open(path)
                    img.verify()
                    valid_images += 1
                    valid_list.append(path)
                except Exception:
                    corrupt_images += 1
    header("VALIDATION SUMMARY")
    log(f"Valid Images      : {valid_images}")
    log(f"Corrupt Images    : {corrupt_images}")
    log(f"Zero Byte Images  : {zero_byte_images}")
    return valid_list
def copy_valid_images(valid_list):
    header("STEP 7 : COPYING VALID IMAGES")
    if os.path.exists(CLEANED_DATASET):
        shutil.rmtree(CLEANED_DATASET)
    os.makedirs(CLEANED_DATASET)
    copied = 0
    for src in tqdm(valid_list):
        relative = os.path.relpath(src, RAW_DATASET)
        dst = os.path.join(
            CLEANED_DATASET,
            relative
        )
        os.makedirs(
            os.path.dirname(dst),
            exist_ok=True
        )
        shutil.copy2(src, dst)
        copied += 1
    log(f"\nImages Copied : {copied}")
def remove_duplicate_images():
    header("STEP 8 : REMOVING DUPLICATES")
    hashes = {}
    duplicate_count = 0
    for root, dirs, files in os.walk(CLEANED_DATASET):
        for file in tqdm(files, leave=False):
            if not is_image(file):
                continue
            path = os.path.join(root, file)
            try:
                h = image_hash(path)
                if h in hashes:
                    os.remove(path)
                    duplicate_count += 1
                else:
                    hashes[h] = path
            except Exception:
                continue
    log(f"\nDuplicate Images Removed : {duplicate_count}")
def remove_empty_folders():
    header("STEP 9 : REMOVING EMPTY FOLDERS")
    removed = 0
    for root, dirs, files in os.walk(
        CLEANED_DATASET,
        topdown=False
    ):
        if root == CLEANED_DATASET:
            continue
        if len(os.listdir(root)) == 0:
            try:
                os.rmdir(root)
                removed += 1
            except:
                pass
    log(f"Empty Folders Removed : {removed}")
def standardize_classes():
    header("STEP 10 : STANDARDIZING CLASS NAMES")
    renamed = 0
    for dataset in os.listdir(CLEANED_DATASET):
        dataset_path = os.path.join(
            CLEANED_DATASET,
            dataset
        )
        if not os.path.isdir(dataset_path):
            continue
        for root, dirs, files in os.walk(dataset_path):
            for folder in dirs:
                old_path = os.path.join(root, folder)
                new_name = standardize_class_name(folder)
                new_path = os.path.join(root, new_name)
                if old_path != new_path:
                    try:
                        os.rename(old_path, new_path)
                        renamed += 1
                    except:
                        pass
    log(f"Folders Renamed : {renamed}")
def cleaning_pipeline():
    valid_images = validate_images()
    copy_valid_images(valid_images)
    remove_duplicate_images()
    remove_empty_folders()
    standardize_classes()
    header("DATASET CLEANING COMPLETED")
def merge_dataset():
    header("STEP 11 : MERGING DATASETS")
    if os.path.exists(MERGED_DATASET):
        shutil.rmtree(MERGED_DATASET)
    os.makedirs(MERGED_DATASET)
    merged_images = 0
    skipped_images = 0
    class_mapping = {}
    for dataset in sorted(os.listdir(CLEANED_DATASET)):
        dataset_path = os.path.join(CLEANED_DATASET, dataset)
        if not os.path.isdir(dataset_path):
            continue
        log(f"\nProcessing Dataset : {dataset}")
        for root, dirs, files in os.walk(dataset_path):
            image_files = [
                f for f in files
                if is_image(f)
            ]
            if len(image_files) == 0:
                continue
            class_name = standardize_class_name(
                os.path.basename(root)
            )
            class_mapping.setdefault(class_name, 0)
            destination_folder = os.path.join(
                MERGED_DATASET,
                class_name
            )
            os.makedirs(
                destination_folder,
                exist_ok=True
            )
            for file in tqdm(image_files, leave=False):
                source = os.path.join(root, file)
                filename = dataset + "_" + file
                destination = os.path.join(
                    destination_folder,
                    filename
                )
                try:
                    resize_image(
                        source,
                        destination
                    )
                    merged_images += 1
                    class_mapping[class_name] += 1
                except Exception:
                    skipped_images += 1
    header("MERGE SUMMARY")
    log(f"Merged Images  : {merged_images}")
    log(f"Skipped Images : {skipped_images}")
    return class_mapping
def class_distribution(class_mapping):
    header("STEP 12 : CLASS DISTRIBUTION")
    sorted_classes = sorted(
        class_mapping.items(),
        key=lambda x: x[1],
        reverse=True
    )
    for cls, count in sorted_classes:
        log(f"{cls:<40} {count}")
def verify_merged_dataset():
    header("STEP 13 : VERIFY MERGED DATASET")
    total_classes = 0
    total_images = 0
    for cls in sorted(os.listdir(MERGED_DATASET)):
        class_path = os.path.join(
            MERGED_DATASET,
            cls
        )
        if not os.path.isdir(class_path):
            continue
        images = [
            img
            for img in os.listdir(class_path)
            if is_image(img)
        ]
        total_classes += 1
        total_images += len(images)
        log(f"{cls:<40} {len(images)}")
    print()
    log(f"Total Classes : {total_classes}")
    log(f"Total Images  : {total_images}")
def save_class_report(class_mapping):
    header("STEP 14 : SAVING CLASS REPORT")
    report = []
    for cls, count in sorted(class_mapping.items()):
        report.append({
            "Class": cls,
            "Images": count
        })
    df = pd.DataFrame(report)
    report_path = os.path.join(
        OUTPUT_DIR,
        "merged_dataset_report.csv"
    )
    df.to_csv(
        report_path,
        index=False
    )
    log("Merged Dataset Report Saved")
    log(report_path)
def merging_pipeline():
    class_mapping = merge_dataset()
    class_distribution(class_mapping)
    verify_merged_dataset()
    save_class_report(class_mapping)
    header("DATASET MERGING COMPLETED")
def split_dataset():
    header("STEP 15 : SPLITTING DATASET")
    for folder in [
        TRAIN_DATASET,
        VALIDATION_DATASET,
        TEST_DATASET
    ]:
        if os.path.exists(folder):
            shutil.rmtree(folder)
        os.makedirs(folder)
    train_count = 0
    validation_count = 0
    test_count = 0
    labels = []
    for cls in sorted(os.listdir(MERGED_DATASET)):
        class_path = os.path.join(
            MERGED_DATASET,
            cls
        )
        if not os.path.isdir(class_path):
            continue
        labels.append(cls)
        images = [
            os.path.join(class_path, img)
            for img in os.listdir(class_path)
            if is_image(img)
        ]
        if len(images) < 5:
            continue
        train_imgs, temp_imgs = train_test_split(
            images,
            test_size=0.20,
            random_state=RANDOM_STATE,
            shuffle=True
        )
        validation_imgs, test_imgs = train_test_split(
            temp_imgs,
            test_size=0.50,
            random_state=RANDOM_STATE,
            shuffle=True
        )
        for folder in [
            os.path.join(TRAIN_DATASET, cls),
            os.path.join(VALIDATION_DATASET, cls),
            os.path.join(TEST_DATASET, cls)
        ]:
            os.makedirs(folder, exist_ok=True)
        for img in train_imgs:
            shutil.copy2(
                img,
                os.path.join(
                    TRAIN_DATASET,
                    cls,
                    os.path.basename(img)
                )
            )
            train_count += 1
        for img in validation_imgs:
            shutil.copy2(
                img,
                os.path.join(
                    VALIDATION_DATASET,
                    cls,
                    os.path.basename(img)
                )
            )
            validation_count += 1
        for img in test_imgs:
            shutil.copy2(
                img,
                os.path.join(
                    TEST_DATASET,
                    cls,
                    os.path.basename(img)
                )
            )
            test_count += 1
    return labels, train_count, validation_count, test_count
def save_labels(labels):
    header("STEP 16 : SAVING LABELS")
    with open(
        LABEL_FILE,
        "w",
        encoding="utf-8"
    ) as file:
        for label in sorted(labels):
            file.write(label + "\n")
    log("labels.txt Created")
def verify_split():
    header("STEP 17 : VERIFY DATASET")
    folders = {
        "Train": TRAIN_DATASET,
        "Validation": VALIDATION_DATASET,
        "Test": TEST_DATASET
    }
    for name, folder in folders.items():
        classes = 0
        images = 0
        for cls in os.listdir(folder):
            class_path = os.path.join(folder, cls)
            if not os.path.isdir(class_path):
                continue
            classes += 1
            images += len([
                f
                for f in os.listdir(class_path)
                if is_image(f)
            ])
        log(f"{name:<12} Classes : {classes}")
        log(f"{name:<12} Images  : {images}")
        print()
def preprocessing_summary(
    train_count,
    validation_count,
    test_count
):
    header("PREPROCESSING SUMMARY")
    total = train_count + validation_count + test_count
    log(f"Training Images    : {train_count}")
    log(f"Validation Images  : {validation_count}")
    log(f"Testing Images     : {test_count}")
    log(f"Total Images       : {total}")
    log(f"Image Size         : {IMAGE_SIZE}")
    log(f"Train Split        : 80%")
    log(f"Validation Split   : 10%")
    log(f"Test Split         : 10%")
    log("\nDataset Ready For Training")
def run_complete_pipeline():
    initialize()
    scan_dataset()
    class_counter = analyze_dataset()
    dataset_statistics(class_counter)
    save_dataset_report(class_counter)
    generate_labels(class_counter)
    cleaning_pipeline()
    class_mapping = merge_dataset()
    class_distribution(class_mapping)
    verify_merged_dataset()
    save_class_report(class_mapping)
    labels, train_count, validation_count, test_count = split_dataset()
    save_labels(labels)
    verify_split()
    preprocessing_summary(
        train_count,
        validation_count,
        test_count
    )
    header("PREPROCESSING COMPLETED SUCCESSFULLY")
if __name__ == "__main__":
    run_complete_pipeline() 