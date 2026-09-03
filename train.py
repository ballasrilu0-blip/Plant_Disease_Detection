# =============================================================================
# PLANT DISEASE DETECTION USING EFFICIENTNETB0
# =============================================================================
#
# Deep Learning Model:
#     EfficientNetB0 (ImageNet)
#
# TensorFlow:
#     2.21+
#
# Features:
#     Transfer Learning
#     Fine Tuning
#     Resume Training
#     Automatic Checkpoints
#     TensorBoard
#     CSV Logger
#     EarlyStopping
#     ReduceLROnPlateau
#     Class Weights
#     Confusion Matrix
#     Classification Report
#     Accuracy/Loss Graphs
#
# IMPORTANT:
# Training has a FIXED final epoch.
# This prevents:
#
#     54 -> 74
#     55 -> 75
#     56 -> 76
#
# from happening when training is resumed.
# =============================================================================


# =============================================================================
# IMPORTS
# =============================================================================

import os
import sys
import time
import random
import pickle
import warnings

from pathlib import Path
from datetime import datetime

import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
import seaborn as sns

from sklearn.utils.class_weight import compute_class_weight

from sklearn.metrics import (
    confusion_matrix,
    classification_report
)

from tensorflow.keras import Model

from tensorflow.keras.models import load_model

from tensorflow.keras.layers import (
    Input,
    Dense,
    Dropout,
    BatchNormalization,
    GlobalAveragePooling2D
)

from tensorflow.keras.applications import EfficientNetB0

from tensorflow.keras.optimizers import AdamW

from tensorflow.keras.callbacks import (
    ModelCheckpoint,
    EarlyStopping,
    ReduceLROnPlateau,
    TensorBoard,
    CSVLogger,
    Callback
)


# =============================================================================
# GLOBAL CONFIGURATION
# =============================================================================

warnings.filterwarnings("ignore")

SEED = 42

random.seed(SEED)

np.random.seed(SEED)

tf.random.set_seed(SEED)

AUTOTUNE = tf.data.AUTOTUNE


print("\nTensorFlow Version :", tf.__version__)


# =============================================================================
# PROJECT PATHS
# =============================================================================

PROJECT_DIR = Path(__file__).resolve().parent

DATASET_DIR = PROJECT_DIR / "dataset"

TRAIN_DIR = DATASET_DIR / "train"

VALIDATION_DIR = DATASET_DIR / "validation"

TEST_DIR = DATASET_DIR / "test"


MODEL_DIR = PROJECT_DIR / "models"

REPORT_DIR = PROJECT_DIR / "reports"

LOG_DIR = PROJECT_DIR / "logs"


MODEL_DIR.mkdir(
    exist_ok=True
)

REPORT_DIR.mkdir(
    exist_ok=True
)

LOG_DIR.mkdir(
    exist_ok=True
)


# =============================================================================
# TRAINING CONFIGURATION
# =============================================================================

IMAGE_SIZE = (224, 224)

BATCH_SIZE = 32


# -------------------------------------------------------------------------
# TRAINING PHASES
# -------------------------------------------------------------------------

TRANSFER_EPOCHS = 30

FINE_TUNE_EPOCHS = 20


# -------------------------------------------------------------------------
# IMPORTANT FIX
# -------------------------------------------------------------------------
#
# DO NOT calculate the final epoch like this:
#
#     fine_tune_start_epoch + FINE_TUNE_EPOCHS
#
# because the endpoint will increase every time training resumes.
#
# Your current checkpoint is already at epoch 54.
# Therefore the current training run is capped at epoch 74.
#
# -------------------------------------------------------------------------

FINAL_TRAINING_EPOCH = 74


# -------------------------------------------------------------------------
# LEARNING RATES
# -------------------------------------------------------------------------

LEARNING_RATE = 3e-4

FINE_TUNE_LEARNING_RATE = 3e-6


# -------------------------------------------------------------------------
# DROPOUT
# -------------------------------------------------------------------------

DROPOUT_1 = 0.30

DROPOUT_2 = 0.20


# -------------------------------------------------------------------------
# DENSE LAYER
# -------------------------------------------------------------------------

DENSE_UNITS = 512


# -------------------------------------------------------------------------
# CALLBACK SETTINGS
# -------------------------------------------------------------------------

PATIENCE = 8

REDUCE_FACTOR = 0.3

REDUCE_PATIENCE = 3

MIN_LR = 1e-7


# =============================================================================
# OUTPUT FILES
# =============================================================================

BEST_MODEL_PATH = (
    MODEL_DIR / "best_model.keras"
)

CHECKPOINT_MODEL_PATH = (
    MODEL_DIR / "checkpoint.keras"
)

LAST_MODEL_PATH = (
    MODEL_DIR / "last_model.keras"
)

FINAL_MODEL_PATH = (
    MODEL_DIR / "final_model.keras"
)

CURRENT_EPOCH_PATH = (
    MODEL_DIR / "current_epoch.txt"
)

HISTORY_PATH = (
    MODEL_DIR / "history.pkl"
)

LABELS_PATH = (
    MODEL_DIR / "labels.txt"
)

CLASS_INDEX_PATH = (
    MODEL_DIR / "class_indices.pkl"
)

MODEL_SUMMARY_PATH = (
    MODEL_DIR / "model_summary.txt"
)

CSV_LOG_PATH = (
    REPORT_DIR / "training_log.csv"
)

CLASSIFICATION_REPORT_PATH = (
    REPORT_DIR / "classification_report.txt"
)

CONFUSION_MATRIX_PATH = (
    REPORT_DIR / "confusion_matrix.png"
)

ACCURACY_GRAPH_PATH = (
    REPORT_DIR / "accuracy.png"
)

LOSS_GRAPH_PATH = (
    REPORT_DIR / "loss.png"
)

TRAINING_SUMMARY_PATH = (
    REPORT_DIR / "training_summary.txt"
)

TENSORBOARD_LOG_DIR = (
    LOG_DIR /
    datetime.now().strftime(
        "%Y%m%d-%H%M%S"
    )
)


# =============================================================================
# HELPER FUNCTION
# =============================================================================

def print_header(title):
    """
    Display a formatted section header.
    """

    print(
        "\n" + "=" * 80
    )

    print(
        title.center(80)
    )

    print(
        "=" * 80
    )


# =============================================================================
# DISPLAY TRAINING CONFIGURATION
# =============================================================================

def display_training_strategy():

    print_header(
        "MODEL READY FOR TRAINING"
    )

    print(
        "Training Strategy:"
    )

    print(
        f"  Transfer Learning      : "
        f"Up to {TRANSFER_EPOCHS} epochs"
    )

    print(
        f"  Fine Tuning            : "
        f"{FINE_TUNE_EPOCHS} epochs"
    )

    print(
        f"  FIXED FINAL EPOCH      : "
        f"{FINAL_TRAINING_EPOCH}"
    )

    print(
        f"  Initial Learning Rate  : "
        f"{LEARNING_RATE}"
    )

    print(
        f"  Fine-Tune Learning Rate: "
        f"{FINE_TUNE_LEARNING_RATE}"
    )

    print(
        "\n  EarlyStopping     : Enabled"
    )

    print(
        "  ReduceLROnPlateau : Enabled"
    )

    print(
        "  Class Weights     : Enabled"
    )

    print(
        "  AdamW Optimizer   : Enabled"
    )


# =============================================================================
# DISPLAY CALLBACK SETTINGS
# =============================================================================

def display_callback_settings():

    print_header(
        "TRAINING CALLBACK SETTINGS"
    )

    print(
        f"EarlyStopping Patience : "
        f"{PATIENCE}"
    )

    print(
        f"Reduce LR Factor       : "
        f"{REDUCE_FACTOR}"
    )

    print(
        f"Reduce LR Patience     : "
        f"{REDUCE_PATIENCE}"
    )

    print(
        f"Minimum Learning Rate  : "
        f"{MIN_LR}"
    )

    print(
        f"Best Model Path        : "
        f"{BEST_MODEL_PATH}"
    )
# =============================================================================
# DATASET VERIFICATION
# =============================================================================

def verify_dataset():
    """
    Verify the training, validation and testing folders.

    Returns:
        num_classes : Number of disease classes
        total_images : Total number of images
    """

    print_header(
        "VERIFYING DATASET"
    )

    # -------------------------------------------------------------------------
    # Check required directories
    # -------------------------------------------------------------------------

    required_directories = [
        TRAIN_DIR,
        VALIDATION_DIR,
        TEST_DIR
    ]

    for directory in required_directories:

        if not directory.exists():

            raise FileNotFoundError(
                f"Dataset directory not found:\n{directory}"
            )


    # -------------------------------------------------------------------------
    # Count images
    # -------------------------------------------------------------------------

    image_extensions = {
        ".jpg",
        ".jpeg",
        ".png",
        ".bmp",
        ".webp"
    }


    def count_images(directory):

        count = 0

        for file in directory.rglob("*"):

            if (
                file.is_file()
                and
                file.suffix.lower()
                in image_extensions
            ):

                count += 1

        return count


    train_count = count_images(
        TRAIN_DIR
    )

    validation_count = count_images(
        VALIDATION_DIR
    )

    test_count = count_images(
        TEST_DIR
    )


    # -------------------------------------------------------------------------
    # Get class names from training directory
    # -------------------------------------------------------------------------

    class_directories = sorted(

        [
            directory
            for directory in TRAIN_DIR.iterdir()
            if directory.is_dir()
        ]

    )


    num_classes = len(
        class_directories
    )


    total_images = (

        train_count
        +
        validation_count
        +
        test_count

    )


    # -------------------------------------------------------------------------
    # Display dataset information
    # -------------------------------------------------------------------------

    print(
        f"Training       : "
        f"{train_count:>8} Images"
    )

    print(
        f"Validation     : "
        f"{validation_count:>8} Images"
    )

    print(
        f"Testing        : "
        f"{test_count:>8} Images"
    )

    print()

    print(
        f"Total Classes : "
        f"{num_classes}"
    )

    print(
        f"Total Images  : "
        f"{total_images}"
    )


    # -------------------------------------------------------------------------
    # Basic validation
    # -------------------------------------------------------------------------

    if num_classes == 0:

        raise ValueError(
            "No class folders were found inside the training directory."
        )


    if train_count == 0:

        raise ValueError(
            "No training images were found."
        )


    if validation_count == 0:

        raise ValueError(
            "No validation images were found."
        )


    if test_count == 0:

        raise ValueError(
            "No testing images were found."
        )


    return (
        num_classes,
        total_images
    )


# =============================================================================
# DATASET MANAGER
# =============================================================================

class DatasetManager:
    """
    Loads the training, validation and testing datasets.

    Directory structure expected:

        dataset/
        ├── train/
        │   ├── class_1/
        │   ├── class_2/
        │   └── ...
        │
        ├── validation/
        │   ├── class_1/
        │   ├── class_2/
        │   └── ...
        │
        └── test/
            ├── class_1/
            ├── class_2/
            └── ...
    """


    def __init__(self):

        self.image_size = IMAGE_SIZE

        self.batch_size = BATCH_SIZE

        self.class_names = None

        self.num_classes = None


    # =========================================================================
    # LOAD SINGLE DATASET
    # =========================================================================

    def _load_dataset(
        self,
        directory,
        shuffle=False
    ):
        """
        Load images from a directory using image_dataset_from_directory.
        """

        dataset = tf.keras.utils.image_dataset_from_directory(

            directory,

            labels="inferred",

            label_mode="int",

            image_size=self.image_size,

            batch_size=self.batch_size,

            shuffle=shuffle,

            seed=SEED

        )


        return dataset


    # =========================================================================
    # LOAD ALL DATASETS
    # =========================================================================

    def load_datasets(self):

        print_header(
            "LOADING DATASETS"
        )


        # ---------------------------------------------------------------------
        # Training Dataset
        # ---------------------------------------------------------------------

        print(
            "Loading Training Dataset..."
        )


        train_dataset = self._load_dataset(

            TRAIN_DIR,

            shuffle=True

        )


        # ---------------------------------------------------------------------
        # Validation Dataset
        # ---------------------------------------------------------------------

        print(
            "\nLoading Validation Dataset..."
        )


        validation_dataset = self._load_dataset(

            VALIDATION_DIR,

            shuffle=False

        )


        # ---------------------------------------------------------------------
        # Test Dataset
        # ---------------------------------------------------------------------

        print(
            "\nLoading Test Dataset..."
        )


        test_dataset = self._load_dataset(

            TEST_DIR,

            shuffle=False

        )


        # ---------------------------------------------------------------------
        # Get class names
        # ---------------------------------------------------------------------

        self.class_names = (

            train_dataset.class_names

        )


        self.num_classes = len(

            self.class_names

        )


        # ---------------------------------------------------------------------
        # Verify class names across datasets
        # ---------------------------------------------------------------------

        if (
            validation_dataset.class_names
            !=
            self.class_names
        ):

            raise ValueError(
                "Training and validation class names do not match."
            )


        if (
            test_dataset.class_names
            !=
            self.class_names
        ):

            raise ValueError(
                "Training and testing class names do not match."
            )


        # ---------------------------------------------------------------------
        # Display information
        # ---------------------------------------------------------------------

        print(
            "\nDatasets Loaded Successfully"
        )

        print(
            f"Number of Classes : "
            f"{self.num_classes}"
        )

        print(
            f"Batch Size        : "
            f"{self.batch_size}"
        )

        print(
            f"Image Size        : "
            f"{self.image_size[0]} x "
            f"{self.image_size[1]}"
        )


        return (

            train_dataset,

            validation_dataset,

            test_dataset,

            self.class_names,

            self.num_classes

        )


# =============================================================================
# SAVE CLASS LABELS
# =============================================================================

def save_labels(
    class_names
):
    """
    Save class names to labels.txt.
    """

    with open(

        LABELS_PATH,

        "w",

        encoding="utf-8"

    ) as file:

        for class_name in class_names:

            file.write(
                f"{class_name}\n"
            )


    print(
        "labels.txt Saved"
    )


# =============================================================================
# SAVE CLASS INDICES
# =============================================================================

def save_class_indices(
    class_names
):
    """
    Save class-to-index mapping.
    """

    class_indices = {

        class_name: index

        for index, class_name
        in enumerate(class_names)

    }


    with open(

        CLASS_INDEX_PATH,

        "wb"

    ) as file:

        pickle.dump(

            class_indices,

            file

        )


    print(
        "class_indices.pkl Saved"
    )


# =============================================================================
# DATASET VERIFICATION + LOADING COMPLETE
# =============================================================================
# =============================================================================
# DATA PREPROCESSING
# =============================================================================

def prepare_dataset(
    dataset,
    training=False
):
    """
    Prepare a TensorFlow dataset for efficient training.

    Training:
        Dataset is shuffled when it is loaded.

    Validation/Test:
        Dataset remains deterministic.

    Prefetching allows TensorFlow to prepare the next batch
    while the current batch is being processed.
    """

    dataset = dataset.prefetch(
        AUTOTUNE
    )

    return dataset


# =============================================================================
# PREPARE ALL DATASETS
# =============================================================================

def prepare_all_datasets(
    train_dataset,
    validation_dataset,
    test_dataset
):
    """
    Prepare train, validation and test datasets.
    """

    print_header(
        "PREPARING DATASETS"
    )


    print(
        "Preparing Training Dataset..."
    )

    train_dataset = prepare_dataset(

        train_dataset,

        training=True

    )


    print(
        "Preparing Validation Dataset..."
    )

    validation_dataset = prepare_dataset(

        validation_dataset,

        training=False

    )


    print(
        "Preparing Test Dataset..."
    )

    test_dataset = prepare_dataset(

        test_dataset,

        training=False

    )


    print(
        "\nDataset Preparation Completed"
    )


    return (

        train_dataset,

        validation_dataset,

        test_dataset

    )


# =============================================================================
# COLLECT TRAINING LABELS
# =============================================================================

def collect_training_labels(
    train_dataset
):
    """
    Collect all labels from the training dataset.

    These labels are used to calculate class weights.
    """

    print_header(
        "COLLECTING TRAINING LABELS"
    )


    all_labels = []


    for images, labels in train_dataset:

        # Convert TensorFlow tensor to NumPy
        labels = labels.numpy()

        all_labels.extend(
            labels.tolist()
        )


    all_labels = np.array(

        all_labels,

        dtype=np.int32

    )


    print(
        f"Total Training Labels Collected : "
        f"{len(all_labels)}"
    )


    return all_labels


# =============================================================================
# CALCULATE CLASS WEIGHTS
# =============================================================================

def calculate_class_weights(
    train_dataset,
    num_classes
):
    """
    Calculate balanced class weights.

    Classes with fewer training images receive a larger weight.
    Classes with many images receive a smaller weight.

    This helps reduce the effect of class imbalance.
    """

    print_header(
        "CALCULATING CLASS WEIGHTS"
    )


    labels = collect_training_labels(

        train_dataset

    )


    # -------------------------------------------------------------------------
    # Find classes actually present in the training data
    # -------------------------------------------------------------------------

    unique_classes = np.unique(

        labels

    )


    # -------------------------------------------------------------------------
    # Calculate balanced weights
    # -------------------------------------------------------------------------

    calculated_weights = compute_class_weight(

        class_weight="balanced",

        classes=unique_classes,

        y=labels

    )


    # -------------------------------------------------------------------------
    # Create dictionary
    # -------------------------------------------------------------------------

    class_weights = {

        int(class_index): float(weight)

        for class_index, weight
        in zip(
            unique_classes,
            calculated_weights
        )

    }


    # -------------------------------------------------------------------------
    # Make sure every expected class has a weight
    # -------------------------------------------------------------------------

    for class_index in range(

        num_classes

    ):

        if class_index not in class_weights:

            class_weights[
                class_index
            ] = 1.0


    # -------------------------------------------------------------------------
    # Display weights
    # -------------------------------------------------------------------------

    print(
        "\nClass Weights:"
    )


    for class_index in sorted(

        class_weights.keys()

    ):

        print(

            f"Class {class_index:>3} : "
            f"{class_weights[class_index]:.4f}"

        )


    return class_weights


# =============================================================================
# DATASET INFORMATION
# =============================================================================

def display_dataset_information(
    train_dataset,
    validation_dataset,
    test_dataset,
    class_names
):
    """
    Display dataset statistics.
    """

    print_header(
        "DATASET INFORMATION"
    )


    train_batches = (

        tf.data.experimental.cardinality(

            train_dataset

        ).numpy()

    )


    validation_batches = (

        tf.data.experimental.cardinality(

            validation_dataset

        ).numpy()

    )


    test_batches = (

        tf.data.experimental.cardinality(

            test_dataset

        ).numpy()

    )


    print(
        f"Number of Classes : "
        f"{len(class_names)}"
    )


    print(
        f"Training Batches : "
        f"{train_batches}"
    )


    print(
        f"Validation Batches : "
        f"{validation_batches}"
    )


    print(
        f"Testing Batches : "
        f"{test_batches}"
    )


    print(
        "\nFirst 10 Classes:"
    )


    for index, class_name in enumerate(

        class_names[:10]

    ):

        print(

            f"{index:>3} : "
            f"{class_name}"

        )


# =============================================================================
# DATA PREPROCESSING COMPLETE
# =============================================================================
# =============================================================================
# BUILD MODEL
# =============================================================================

def build_model(num_classes):
    """
    Build the Plant Disease Detection model using EfficientNetB0.

    The model uses:
        - Data augmentation
        - EfficientNetB0 pretrained on ImageNet
        - Global Average Pooling
        - Batch Normalization
        - Dropout
        - Dense classification layer
        - L2 regularization
    """

    print_header(
        "BUILDING MODEL"
    )


    # =========================================================================
    # DATA AUGMENTATION
    # =========================================================================

    data_augmentation = tf.keras.Sequential(

        [

            # Randomly flip images horizontally and vertically
            tf.keras.layers.RandomFlip(
                "horizontal_and_vertical"
            ),

            # Slight rotation
            tf.keras.layers.RandomRotation(
                0.10
            ),

            # Random zoom
            tf.keras.layers.RandomZoom(
                height_factor=0.15,
                width_factor=0.15
            ),

            # Small translation
            tf.keras.layers.RandomTranslation(
                height_factor=0.08,
                width_factor=0.08
            ),

            # Slight contrast variation
            tf.keras.layers.RandomContrast(
                0.15
            )

        ],

        name="DataAugmentation"

    )


    # =========================================================================
    # LOAD EFFICIENTNETB0
    # =========================================================================

    print(
        "Loading EfficientNetB0 with ImageNet weights..."
    )


    base_model = EfficientNetB0(

        include_top=False,

        weights="imagenet",

        input_shape=(

            IMAGE_SIZE[0],

            IMAGE_SIZE[1],

            3

        )

    )


    # =========================================================================
    # FREEZE BASE MODEL
    # =========================================================================

    # During the first training phase, EfficientNetB0 is frozen.
    # Only the newly created classification layers are trained.

    base_model.trainable = False


    # =========================================================================
    # INPUT
    # =========================================================================

    inputs = Input(

        shape=(

            IMAGE_SIZE[0],

            IMAGE_SIZE[1],

            3

        ),

        name="input_image"

    )


    # =========================================================================
    # DATA AUGMENTATION
    # =========================================================================

    x = data_augmentation(

        inputs

    )


    # =========================================================================
    # EFFICIENTNET PREPROCESSING
    # =========================================================================

    x = tf.keras.applications.efficientnet.preprocess_input(

        x

    )


    # =========================================================================
    # FEATURE EXTRACTION
    # =========================================================================

    x = base_model(

        x,

        training=False

    )


    # =========================================================================
    # GLOBAL AVERAGE POOLING
    # =========================================================================

    x = GlobalAveragePooling2D(

        name="global_average_pooling"

    )(

        x

    )


    # =========================================================================
    # BATCH NORMALIZATION
    # =========================================================================

    x = BatchNormalization(

        name="head_batch_norm_1"

    )(

        x

    )


    # =========================================================================
    # DROPOUT
    # =========================================================================

    x = Dropout(

        DROPOUT_1,

        name="dropout_1"

    )(

        x

    )


    # =========================================================================
    # DENSE CLASSIFICATION LAYER
    # =========================================================================

    x = Dense(

        DENSE_UNITS,

        activation="relu",

        kernel_regularizer=tf.keras.regularizers.l2(

            1e-5

        ),

        name="dense_1"

    )(

        x

    )


    # =========================================================================
    # SECOND BATCH NORMALIZATION
    # =========================================================================

    x = BatchNormalization(

        name="head_batch_norm_2"

    )(

        x

    )


    # =========================================================================
    # SECOND DROPOUT
    # =========================================================================

    x = Dropout(

        DROPOUT_2,

        name="dropout_2"

    )(

        x

    )


    # =========================================================================
    # OUTPUT LAYER
    # =========================================================================

    outputs = Dense(

        num_classes,

        activation="softmax",

        name="predictions"

    )(

        x

    )


    # =========================================================================
    # CREATE FINAL MODEL
    # =========================================================================

    model = Model(

        inputs=inputs,

        outputs=outputs,

        name="PlantDiseaseEfficientNetB0"

    )


    # =========================================================================
    # DISPLAY MODEL INFORMATION
    # =========================================================================

    print(
        "\nImproved Model Created Successfully"
    )


    print(
        f"Number of Output Classes : "
        f"{num_classes}"
    )


    print(
        f"Image Input Shape        : "
        f"{IMAGE_SIZE[0]} x "
        f"{IMAGE_SIZE[1]} x 3"
    )


    return (

        model,

        base_model

    )


# =============================================================================
# MODEL INFORMATION
# =============================================================================

def display_model_information(
    model
):
    """
    Display the number of trainable and non-trainable parameters.
    """

    print_header(
        "MODEL INFORMATION"
    )


    trainable_parameters = np.sum(

        [

            np.prod(
                variable.shape
            )

            for variable in model.trainable_variables

        ]

    )


    non_trainable_parameters = np.sum(

        [

            np.prod(
                variable.shape
            )

            for variable in model.non_trainable_variables

        ]

    )


    print(
        f"Trainable Parameters    : "
        f"{trainable_parameters:,}"
    )


    print(
        f"Non-Trainable Parameters: "
        f"{non_trainable_parameters:,}"
    )


    print(
        f"Total Parameters        : "
        f"{trainable_parameters + non_trainable_parameters:,}"
    )


# =============================================================================
# SAVE MODEL SUMMARY
# =============================================================================

def save_model_summary(
    model
):
    """
    Save the complete Keras model summary.
    """

    print_header(
        "SAVING MODEL SUMMARY"
    )


    with open(

        MODEL_SUMMARY_PATH,

        "w",

        encoding="utf-8"

    ) as file:

        model.summary(

            print_fn=lambda line:
            file.write(
                line + "\n"
            )

        )


    print(
        f"Model Summary Saved : "
        f"{MODEL_SUMMARY_PATH}"
    )


# =============================================================================
# PART 4 COMPLETE
# =============================================================================
# =============================================================================
# COMPILE MODEL
# =============================================================================

def compile_model(
    model,
    learning_rate=LEARNING_RATE
):
    """
    Compile the model using AdamW.

    AdamW provides weight decay regularization and clipnorm
    helps keep training stable.
    """

    print_header(
        "COMPILING MODEL"
    )

    optimizer = AdamW(

        learning_rate=learning_rate,

        weight_decay=1e-5,

        clipnorm=1.0

    )


    model.compile(

        optimizer=optimizer,

        loss="sparse_categorical_crossentropy",

        metrics=[

            "accuracy",

            tf.keras.metrics.SparseTopKCategoricalAccuracy(

                k=3,

                name="top_3_accuracy"

            )

        ]

    )


    print(
        "Model Compiled Successfully"
    )

    print(
        f"Learning Rate : "
        f"{learning_rate}"
    )


    return model


# =============================================================================
# TRAINING STATE CALLBACK
# =============================================================================

class TrainingStateCallback(Callback):
    """
    Save the current training epoch after every completed epoch.
    """

    def __init__(
        self,
        phase
    ):

        super().__init__()

        self.phase = phase


    def on_epoch_end(
        self,
        epoch,
        logs=None
    ):

        # Keras epoch is zero-based.
        completed_epoch = epoch + 1

        # Never save an epoch greater than our fixed limit.
        if completed_epoch > FINAL_TRAINING_EPOCH:

            completed_epoch = FINAL_TRAINING_EPOCH


        save_current_state(

            completed_epoch,

            self.phase

        )


# =============================================================================
# CREATE TRAINING CALLBACKS
# =============================================================================

def create_callbacks(
    phase="transfer"
):
    """
    Create callbacks used during training.
    """

    print_header(
        f"CREATING CALLBACKS - {phase.upper()}"
    )


    callbacks = [

        # ---------------------------------------------------------------------
        # BEST MODEL
        # ---------------------------------------------------------------------

        ModelCheckpoint(

            filepath=str(
                BEST_MODEL_PATH
            ),

            monitor="val_loss",

            mode="min",

            save_best_only=True,

            verbose=1

        ),


        # ---------------------------------------------------------------------
        # LATEST CHECKPOINT
        # ---------------------------------------------------------------------

        ModelCheckpoint(

            filepath=str(
                CHECKPOINT_MODEL_PATH
            ),

            monitor="val_loss",

            mode="min",

            save_best_only=False,

            verbose=0

        ),


        # ---------------------------------------------------------------------
        # EARLY STOPPING
        # ---------------------------------------------------------------------

        EarlyStopping(

            monitor="val_loss",

            mode="min",

            patience=PATIENCE,

            restore_best_weights=True,

            verbose=1

        ),


        # ---------------------------------------------------------------------
        # REDUCE LEARNING RATE
        # ---------------------------------------------------------------------

        ReduceLROnPlateau(

            monitor="val_loss",

            mode="min",

            factor=REDUCE_FACTOR,

            patience=REDUCE_PATIENCE,

            min_lr=MIN_LR,

            verbose=1

        ),


        # ---------------------------------------------------------------------
        # TENSORBOARD
        # ---------------------------------------------------------------------

        TensorBoard(

            log_dir=str(
                TENSORBOARD_LOG_DIR
            ),

            histogram_freq=1,

            write_graph=True,

            update_freq="epoch"

        ),


        # ---------------------------------------------------------------------
        # CSV LOGGER
        # ---------------------------------------------------------------------

        CSVLogger(

            filename=str(
                CSV_LOG_PATH
            ),

            append=True

        ),


        # ---------------------------------------------------------------------
        # SAVE CURRENT TRAINING STATE
        # ---------------------------------------------------------------------

        TrainingStateCallback(

            phase=phase

        )

    ]


    print(
        f"Callbacks Created for Phase : "
        f"{phase}"
    )


    return callbacks


# =============================================================================
# PART 5 COMPLETE
# =============================================================================
# =============================================================================
# SAVE CURRENT TRAINING STATE
# =============================================================================

def save_current_state(
    epoch,
    phase
):
    """
    Save the current training epoch and phase.

    The epoch is capped at FINAL_TRAINING_EPOCH so the saved
    training state can never go beyond the fixed final epoch.
    """

    epoch = min(
        int(epoch),
        FINAL_TRAINING_EPOCH
    )

    with open(
        CURRENT_EPOCH_PATH,
        "w",
        encoding="utf-8"
    ) as file:

        file.write(
            f"{epoch}\n"
        )

        file.write(
            f"{phase}\n"
        )


# =============================================================================
# LOAD CURRENT TRAINING STATE
# =============================================================================

def load_current_state():
    """
    Load the previously saved epoch and training phase.

    Returns:
        epoch
        phase
    """

    if not CURRENT_EPOCH_PATH.exists():

        print(
            "No previous training state found."
        )

        return (
            0,
            "transfer"
        )


    try:

        with open(
            CURRENT_EPOCH_PATH,
            "r",
            encoding="utf-8"
        ) as file:

            lines = file.readlines()


        if len(lines) == 0:

            return (
                0,
                "transfer"
            )


        saved_epoch = int(
            lines[0].strip()
        )


        if len(lines) >= 2:

            saved_phase = (
                lines[1].strip()
            )

        else:

            saved_phase = "transfer"


        # Never allow a saved state above the fixed final epoch.
        saved_epoch = min(
            saved_epoch,
            FINAL_TRAINING_EPOCH
        )


        print(
            f"Loaded Training State:"
        )

        print(
            f"  Epoch : {saved_epoch}"
        )

        print(
            f"  Phase : {saved_phase}"
        )


        return (
            saved_epoch,
            saved_phase
        )


    except Exception as error:

        print(
            "\nWARNING: Could not read "
            "training state."
        )

        print(
            error
        )


        return (
            0,
            "transfer"
        )


# =============================================================================
# SAVE TRAINING HISTORY
# =============================================================================

def save_history(
    history
):
    """
    Save training history to disk.
    """

    if history is None:

        return


    with open(
        HISTORY_PATH,
        "wb"
    ) as file:

        pickle.dump(
            history,
            file
        )


# =============================================================================
# LOAD TRAINING HISTORY
# =============================================================================

def load_history():
    """
    Load previous training history if available.
    """

    if not HISTORY_PATH.exists():

        return None


    try:

        with open(
            HISTORY_PATH,
            "rb"
        ) as file:

            history = pickle.load(
                file
            )


        print(
            "Previous training history loaded."
        )


        return history


    except Exception as error:

        print(
            "\nWARNING: Could not load "
            "training history."
        )

        print(
            error
        )


        return None


# =============================================================================
# MERGE TRAINING HISTORIES
# =============================================================================

def merge_histories(
    old_history,
    new_history
):
    """
    Combine previous and newly generated Keras histories.
    """

    if old_history is None:

        old_history = {}


    merged_history = {

        key: list(value)

        for key, value
        in old_history.items()

    }


    if new_history is None:

        return merged_history


    # Keras History object
    if hasattr(
        new_history,
        "history"
    ):

        new_data = (
            new_history.history
        )

    else:

        new_data = new_history


    for key, values in new_data.items():

        if key not in merged_history:

            merged_history[key] = []


        merged_history[key].extend(

            list(values)

        )


    return merged_history


# =============================================================================
# CHECK RESUME TRAINING
# =============================================================================

def check_resume_training():
    """
    Check whether a previous model/checkpoint exists.

    Returns:
        resume_training
        saved_epoch
        saved_phase
        model
        history
    """

    print_header(
        "CHECKING PREVIOUS TRAINING"
    )


    saved_epoch, saved_phase = (
        load_current_state()
    )


    history = load_history()


    # =========================================================================
    # CHECKPOINT DOES NOT EXIST
    # =========================================================================

    if not CHECKPOINT_MODEL_PATH.exists():

        print(
            "No previous checkpoint found."
        )

        print(
            "A new model will be created."
        )


        return (

            False,

            0,

            "transfer",

            None,

            history

        )


    # =========================================================================
    # CHECKPOINT EXISTS
    # =========================================================================

    print(
        "Previous checkpoint found."
    )


    print(
        f"Last Saved Epoch : "
        f"{saved_epoch}"
    )


    print(
        f"Last Training Phase : "
        f"{saved_phase}"
    )


    # =========================================================================
    # ALREADY COMPLETED
    # =========================================================================

    if (
        saved_epoch >= FINAL_TRAINING_EPOCH
        and
        saved_phase == "completed"
    ):

        print(
            "\nTraining has already reached "
            "the fixed final epoch."
        )


        try:

            model = load_model(

                str(
                    CHECKPOINT_MODEL_PATH
                )

            )


            print(
                "Completed model loaded successfully."
            )


            return (

                True,

                FINAL_TRAINING_EPOCH,

                "completed",

                model,

                history

            )


        except Exception as error:

            print(
                "\nWARNING: Could not load "
                "completed checkpoint."
            )

            print(
                error
            )


            return (

                False,

                0,

                "transfer",

                None,

                history

            )


    # =========================================================================
    # LOAD CHECKPOINT
    # =========================================================================

    print(
        "\nLoading previous checkpoint..."
    )


    try:

        model = load_model(

            str(
                CHECKPOINT_MODEL_PATH
            )

        )


        print(
            "Previous model loaded successfully."
        )


        return (

            True,

            saved_epoch,

            saved_phase,

            model,

            history

        )


    except Exception as error:

        print(
            "\nWARNING: Could not load "
            "previous checkpoint."
        )


        print(
            error
        )


        print(
            "\nStarting with a new model."
        )


        return (

            False,

            0,

            "transfer",

            None,

            history

        )


# =============================================================================
# PART 6 COMPLETE
# =============================================================================
# =============================================================================
# TRANSFER LEARNING TRAINING
# =============================================================================

def train_transfer_learning(
    model,
    train_dataset,
    validation_dataset,
    class_weights,
    initial_epoch=0,
    previous_history=None
):
    """
    Phase 1:
    Train only the classification head while EfficientNetB0
    remains frozen.
    """

    print_header(
        "PHASE 1 - TRANSFER LEARNING"
    )


    print(
        "EfficientNetB0 base layers are frozen."
    )

    print(
        "Training the classification head..."
    )


    # =========================================================================
    # CREATE CALLBACKS
    # =========================================================================

    callbacks = create_callbacks(
        phase="transfer"
    )


    # =========================================================================
    # CHECK WHETHER TRANSFER LEARNING IS COMPLETE
    # =========================================================================

    if initial_epoch >= TRANSFER_EPOCHS:

        print(
            "\nTransfer learning phase "
            "has already been completed."
        )

        return (

            model,

            previous_history,

            initial_epoch

        )


    # =========================================================================
    # TRAIN TRANSFER LEARNING
    # =========================================================================

    history = model.fit(

        train_dataset,

        validation_data=validation_dataset,

        epochs=TRANSFER_EPOCHS,

        initial_epoch=initial_epoch,

        class_weight=class_weights,

        callbacks=callbacks,

        verbose=1

    )


    # =========================================================================
    # MERGE HISTORY
    # =========================================================================

    combined_history = merge_histories(

        previous_history,

        history

    )


    # =========================================================================
    # SAVE HISTORY
    # =========================================================================

    save_history(

        combined_history

    )


    # =========================================================================
    # CALCULATE COMPLETED EPOCH
    # =========================================================================

    number_of_epochs_completed = len(

        history.history.get(
            "loss",
            []
        )

    )


    completed_epoch = (

        initial_epoch

        +

        number_of_epochs_completed

    )


    # =========================================================================
    # KEEP TRANSFER LEARNING WITHIN ITS LIMIT
    # =========================================================================

    completed_epoch = min(

        completed_epoch,

        TRANSFER_EPOCHS

    )


    print(
        "\nTransfer Learning Phase Completed."
    )


    print(
        f"Last Completed Epoch : "
        f"{completed_epoch}"
    )


    return (

        model,

        combined_history,

        completed_epoch

    )


# =============================================================================
# PART 7 COMPLETE
# =============================================================================
# =============================================================================
# FINE-TUNING
# =============================================================================

def fine_tune_model(
    model,
    base_model,
    train_dataset,
    validation_dataset,
    class_weights,
    previous_history=None,
    fine_tune_start_epoch=0
):
    """
    Phase 2:
    Fine-tune the upper layers of EfficientNetB0.

    IMPORTANT:
    The final training epoch is FIXED at FINAL_TRAINING_EPOCH.

    Example:

        Start = 54
        End   = 74

    If interrupted at 60:

        Start = 60
        End   = 74

    The end will NEVER become 80, 81, 82, etc.
    """

    print_header(
        "PHASE 2 - FINE-TUNING"
    )


    # =========================================================================
    # UNFREEZE EFFICIENTNETB0
    # =========================================================================

    print(
        "Unfreezing EfficientNetB0..."
    )


    base_model.trainable = True


    # =========================================================================
    # SELECT UPPER LAYERS FOR FINE-TUNING
    # =========================================================================

    total_layers = len(
        base_model.layers
    )


    # Keep approximately the first 70% frozen.
    fine_tune_at = int(
        total_layers * 0.70
    )


    print(
        f"Total EfficientNet Layers : "
        f"{total_layers}"
    )


    print(
        f"Frozen Layers             : "
        f"{fine_tune_at}"
    )


    print(
        f"Trainable Upper Layers    : "
        f"{total_layers - fine_tune_at}"
    )


    # =========================================================================
    # FREEZE LOWER LAYERS
    # =========================================================================

    for layer in base_model.layers[
        :fine_tune_at
    ]:

        layer.trainable = False


    # =========================================================================
    # KEEP BATCH NORMALIZATION FROZEN
    # =========================================================================

    for layer in base_model.layers:

        if isinstance(
            layer,
            BatchNormalization
        ):

            layer.trainable = False


    # =========================================================================
    # RECOMPILE WITH SMALL LEARNING RATE
    # =========================================================================

    print(
        "\nRecompiling model for fine-tuning..."
    )


    model = compile_model(

        model,

        learning_rate=FINE_TUNE_LEARNING_RATE

    )


    # =========================================================================
    # CREATE CALLBACKS
    # =========================================================================

    callbacks = create_callbacks(

        phase="fine_tune"

    )


    # =========================================================================
    # FIXED FINAL EPOCH
    # =========================================================================

    # IMPORTANT:
    #
    # NEVER do this:
    #
    # total_fine_tune_epochs = (
    #     fine_tune_start_epoch +
    #     FINE_TUNE_EPOCHS
    # )
    #
    # That is what caused the ending epoch to increase every time.
    #
    # We always use the fixed value from Part 1:
    #
    # FINAL_TRAINING_EPOCH = 74

    total_fine_tune_epochs = (
        FINAL_TRAINING_EPOCH
    )


    print(
        f"\nFine-Tuning Start Epoch : "
        f"{fine_tune_start_epoch}"
    )


    print(
        f"Fine-Tuning End Epoch   : "
        f"{total_fine_tune_epochs}"
    )


    print(
        f"Learning Rate           : "
        f"{FINE_TUNE_LEARNING_RATE}"
    )


    # =========================================================================
    # CHECK IF TRAINING IS ALREADY COMPLETE
    # =========================================================================

    if (
        fine_tune_start_epoch
        >=
        FINAL_TRAINING_EPOCH
    ):

        print_header(
            "FINE-TUNING ALREADY COMPLETED"
        )


        print(
            f"Saved Epoch : "
            f"{fine_tune_start_epoch}"
        )


        print(
            f"Final Epoch : "
            f"{FINAL_TRAINING_EPOCH}"
        )


        print(
            "\nNo additional training will be performed."
        )


        save_current_state(

            FINAL_TRAINING_EPOCH,

            "completed"

        )


        return (

            model,

            previous_history,

            FINAL_TRAINING_EPOCH

        )


    # =========================================================================
    # START FINE-TUNING
    # =========================================================================

    print(
        "\nStarting fine-tuning..."
    )


    history = model.fit(

        train_dataset,

        validation_data=validation_dataset,

        # FIXED ENDING EPOCH
        epochs=FINAL_TRAINING_EPOCH,

        # Resume from the saved epoch
        initial_epoch=fine_tune_start_epoch,

        # Handle class imbalance
        class_weight=class_weights,

        callbacks=callbacks,

        verbose=1

    )


    # =========================================================================
    # MERGE OLD + NEW HISTORY
    # =========================================================================

    combined_history = merge_histories(

        previous_history,

        history

    )


    # =========================================================================
    # SAVE HISTORY
    # =========================================================================

    save_history(

        combined_history

    )


    # =========================================================================
    # CALCULATE COMPLETED EPOCH
    # =========================================================================

    epochs_completed = len(

        history.history.get(

            "loss",

            []

        )

    )


    completed_epoch = (

        fine_tune_start_epoch

        +

        epochs_completed

    )


    # =========================================================================
    # NEVER ALLOW EPOCH ABOVE 74
    # =========================================================================

    completed_epoch = min(

        completed_epoch,

        FINAL_TRAINING_EPOCH

    )


    # =========================================================================
    # SAVE TRAINING STATE
    # =========================================================================

    if (
        completed_epoch
        >=
        FINAL_TRAINING_EPOCH
    ):

        save_current_state(

            FINAL_TRAINING_EPOCH,

            "completed"

        )

        print(
            f"\nTraining reached the final epoch: "
            f"{FINAL_TRAINING_EPOCH}"
        )

    else:

        save_current_state(

            completed_epoch,

            "fine_tune"

        )

        print(
            f"\nTraining stopped at epoch: "
            f"{completed_epoch}"
        )


    # =========================================================================
    # DISPLAY RESULT
    # =========================================================================

    print(
        "\nFine-Tuning Phase Completed."
    )


    print(
        f"Last Completed Epoch : "
        f"{completed_epoch}"
    )


    print(
        f"Maximum Allowed Epoch: "
        f"{FINAL_TRAINING_EPOCH}"
    )


    return (

        model,

        combined_history,

        completed_epoch

    )


# =============================================================================
# LOAD BEST MODEL
# =============================================================================

def load_best_trained_model():
    """
    Load the best model saved during training.
    """

    print_header(
        "LOADING BEST TRAINED MODEL"
    )


    if BEST_MODEL_PATH.exists():

        print(
            f"Loading Best Model:\n"
            f"{BEST_MODEL_PATH}"
        )


        try:

            best_model = load_model(

                str(
                    BEST_MODEL_PATH
                )

            )


            print(
                "\nBest Model Loaded Successfully"
            )


            return best_model


        except Exception as error:

            print(
                "\nWARNING: Could not load "
                "best model."
            )


            print(
                error
            )


    else:

        print(
            "\nBest model file was not found."
        )


    print(
        "The currently trained model will be used."
    )


    return None


# =============================================================================
# PART 8 COMPLETE
# =============================================================================
# =============================================================================
# FINAL MODEL EVALUATION
# =============================================================================

def evaluate_model(
    model,
    test_dataset
):
    """
    Evaluate the final trained model on the test dataset.

    Returns:
        evaluation_results : dictionary containing loss,
                             accuracy and Top-3 accuracy.
    """

    print_header(
        "FINAL MODEL EVALUATION"
    )

    print(
        "Evaluating model on the test dataset..."
    )


    # =========================================================================
    # EVALUATE MODEL
    # =========================================================================

    evaluation_results = model.evaluate(

        test_dataset,

        verbose=1,

        return_dict=True

    )


    # =========================================================================
    # DISPLAY RESULTS
    # =========================================================================

    print(
        "\nFinal Test Results:"
    )


    for metric_name, metric_value in (
        evaluation_results.items()
    ):

        print(
            f"{metric_name:<20} : "
            f"{metric_value:.6f}"
        )


    # =========================================================================
    # DISPLAY TEST ACCURACY
    # =========================================================================

    if "accuracy" in evaluation_results:

        test_accuracy = (
            evaluation_results["accuracy"]
        )


        print(
            "\n" + "=" * 60
        )


        print(
            f"FINAL TEST ACCURACY : "
            f"{test_accuracy * 100:.2f}%"
        )


        print(
            "=" * 60
        )


    # =========================================================================
    # DISPLAY TOP-3 ACCURACY
    # =========================================================================

    if "top_3_accuracy" in evaluation_results:

        top_3_accuracy = (
            evaluation_results["top_3_accuracy"]
        )


        print(
            f"FINAL TOP-3 ACCURACY : "
            f"{top_3_accuracy * 100:.2f}%"
        )


    return evaluation_results


# =============================================================================
# COLLECT PREDICTIONS
# =============================================================================

def collect_predictions(
    model,
    test_dataset
):
    """
    Collect actual labels, predicted labels and prediction probabilities.
    """

    print_header(
        "COLLECTING TEST PREDICTIONS"
    )


    true_labels = []

    predicted_labels = []

    prediction_probabilities = []


    # =========================================================================
    # FIND NUMBER OF TEST BATCHES
    # =========================================================================

    total_batches = (

        tf.data.experimental.cardinality(

            test_dataset

        ).numpy()

    )


    print(
        f"Total Test Batches : "
        f"{total_batches}"
    )


    # =========================================================================
    # PROCESS TEST DATA
    # =========================================================================

    for batch_index, (
        images,
        labels
    ) in enumerate(
        test_dataset
    ):


        # ---------------------------------------------------------------------
        # PREDICT
        # ---------------------------------------------------------------------

        predictions = model.predict(

            images,

            verbose=0

        )


        # ---------------------------------------------------------------------
        # GET PREDICTED CLASS
        # ---------------------------------------------------------------------

        predicted_classes = np.argmax(

            predictions,

            axis=1

        )


        # ---------------------------------------------------------------------
        # SAVE TRUE LABELS
        # ---------------------------------------------------------------------

        true_labels.extend(

            labels.numpy().tolist()

        )


        # ---------------------------------------------------------------------
        # SAVE PREDICTED LABELS
        # ---------------------------------------------------------------------

        predicted_labels.extend(

            predicted_classes.tolist()

        )


        # ---------------------------------------------------------------------
        # SAVE PROBABILITIES
        # ---------------------------------------------------------------------

        prediction_probabilities.extend(

            predictions.tolist()

        )


        # ---------------------------------------------------------------------
        # DISPLAY PROGRESS
        # ---------------------------------------------------------------------

        if (

            (batch_index + 1) % 10 == 0

            or

            (batch_index + 1) == total_batches

        ):

            print(

                f"Processed Batch "
                f"{batch_index + 1}/"
                f"{total_batches}"

            )


    # =========================================================================
    # CONVERT TO NUMPY
    # =========================================================================

    true_labels = np.array(

        true_labels,

        dtype=np.int32

    )


    predicted_labels = np.array(

        predicted_labels,

        dtype=np.int32

    )


    prediction_probabilities = np.array(

        prediction_probabilities,

        dtype=np.float32

    )


    # =========================================================================
    # DISPLAY INFORMATION
    # =========================================================================

    print(
        "\nPrediction Collection Completed"
    )


    print(
        f"Total Test Images : "
        f"{len(true_labels)}"
    )


    return (

        true_labels,

        predicted_labels,

        prediction_probabilities

    )


# =============================================================================
# MANUAL ACCURACY VERIFICATION
# =============================================================================

def calculate_manual_accuracy(
    true_labels,
    predicted_labels
):
    """
    Calculate accuracy directly from actual and predicted labels.

    This verifies the accuracy returned by model.evaluate().
    """

    print_header(
        "MANUAL ACCURACY VERIFICATION"
    )


    total_predictions = len(

        true_labels

    )


    if total_predictions == 0:

        print(
            "No predictions available."
        )

        return 0.0


    # =========================================================================
    # COUNT CORRECT PREDICTIONS
    # =========================================================================

    correct_predictions = np.sum(

        true_labels == predicted_labels

    )


    # =========================================================================
    # CALCULATE ACCURACY
    # =========================================================================

    accuracy = (

        correct_predictions

        /

        total_predictions

    )


    # =========================================================================
    # DISPLAY
    # =========================================================================

    print(
        f"Correct Predictions : "
        f"{correct_predictions}"
    )


    print(
        f"Total Predictions   : "
        f"{total_predictions}"
    )


    print(
        f"Manual Accuracy     : "
        f"{accuracy * 100:.2f}%"
    )


    return float(
        accuracy
    )


# =============================================================================
# MANUAL TOP-K ACCURACY
# =============================================================================

def calculate_top_k_accuracy(
    true_labels,
    prediction_probabilities,
    k=3
):
    """
    Calculate Top-K accuracy manually.

    For Top-3 accuracy, the prediction is considered correct
    if the actual disease class is among the model's three
    highest-probability predictions.
    """

    print_header(
        f"MANUAL TOP-{k} ACCURACY"
    )


    if len(true_labels) == 0:

        return 0.0


    # =========================================================================
    # NUMBER OF CLASSES
    # =========================================================================

    num_classes = (
        prediction_probabilities.shape[1]
    )


    k = min(

        k,

        num_classes

    )


    # =========================================================================
    # GET TOP-K PREDICTIONS
    # =========================================================================

    top_k_predictions = np.argsort(

        prediction_probabilities,

        axis=1

    )[:, -k:]


    # =========================================================================
    # COUNT CORRECT TOP-K PREDICTIONS
    # =========================================================================

    correct_predictions = 0


    for index, true_label in enumerate(

        true_labels

    ):

        if true_label in top_k_predictions[index]:

            correct_predictions += 1


    # =========================================================================
    # CALCULATE TOP-K ACCURACY
    # =========================================================================

    top_k_accuracy = (

        correct_predictions

        /

        len(true_labels)

    )


    print(
        f"Correct Top-{k} Predictions : "
        f"{correct_predictions}"
    )


    print(
        f"Total Test Images          : "
        f"{len(true_labels)}"
    )


    print(
        f"Top-{k} Accuracy            : "
        f"{top_k_accuracy * 100:.2f}%"
    )


    return float(
        top_k_accuracy
    )


# =============================================================================
# SAVE EVALUATION RESULTS
# =============================================================================

def save_evaluation_results(
    evaluation_results,
    manual_accuracy,
    manual_top_3_accuracy
):
    """
    Save final evaluation results.
    """

    with open(

        TRAINING_SUMMARY_PATH,

        "a",

        encoding="utf-8"

    ) as file:

        file.write(
            "\n\n"
        )

        file.write(
            "=" * 80
            + "\n"
        )

        file.write(
            "FINAL TEST EVALUATION\n"
        )

        file.write(
            "=" * 80
            + "\n"
        )


        # ---------------------------------------------------------------------
        # KERAS RESULTS
        # ---------------------------------------------------------------------

        for (
            metric_name,
            metric_value
        ) in evaluation_results.items():

            file.write(

                f"{metric_name}: "
                f"{metric_value:.6f}\n"

            )


        # ---------------------------------------------------------------------
        # MANUAL ACCURACY
        # ---------------------------------------------------------------------

        file.write(

            f"\nManual Accuracy: "
            f"{manual_accuracy:.6f} "
            f"({manual_accuracy * 100:.2f}%)\n"

        )


        # ---------------------------------------------------------------------
        # MANUAL TOP-3 ACCURACY
        # ---------------------------------------------------------------------

        file.write(

            f"Manual Top-3 Accuracy: "
            f"{manual_top_3_accuracy:.6f} "
            f"({manual_top_3_accuracy * 100:.2f}%)\n"

        )


    print(
        f"\nEvaluation results saved to:\n"
        f"{TRAINING_SUMMARY_PATH}"
    )


# =============================================================================
# PART 9 COMPLETE
# =============================================================================
# =============================================================================
# CLASSIFICATION REPORT
# =============================================================================

def generate_classification_report(
    true_labels,
    predicted_labels,
    class_names
):
    """
    Generate and save the classification report.

    The report contains:

        Precision
        Recall
        F1-score
        Support

    for every plant-disease class.
    """

    print_header(
        "CLASSIFICATION REPORT"
    )

    # =========================================================================
    # GENERATE REPORT
    # =========================================================================

    report = classification_report(

        true_labels,

        predicted_labels,

        labels=np.arange(
            len(class_names)
        ),

        target_names=class_names,

        zero_division=0

    )


    # =========================================================================
    # DISPLAY REPORT
    # =========================================================================

    print(
        report
    )


    # =========================================================================
    # SAVE REPORT
    # =========================================================================

    with open(

        CLASSIFICATION_REPORT_PATH,

        "w",

        encoding="utf-8"

    ) as file:

        file.write(
            "PLANT DISEASE DETECTION\n"
        )

        file.write(
            "CLASSIFICATION REPORT\n"
        )

        file.write(
            "=" * 80
            + "\n\n"
        )

        file.write(
            report
        )


    print(
        "\nClassification report saved:"
    )

    print(
        CLASSIFICATION_REPORT_PATH
    )


    return report


# =============================================================================
# CONFUSION MATRIX
# =============================================================================

def generate_confusion_matrix(
    true_labels,
    predicted_labels,
    class_names
):
    """
    Generate and save the confusion matrix.

    Rows    = Actual classes
    Columns = Predicted classes
    """

    print_header(
        "CONFUSION MATRIX"
    )


    # =========================================================================
    # CALCULATE CONFUSION MATRIX
    # =========================================================================

    cm = confusion_matrix(

        true_labels,

        predicted_labels,

        labels=np.arange(
            len(class_names)
        )

    )


    # =========================================================================
    # DISPLAY MATRIX INFORMATION
    # =========================================================================

    print(
        f"Confusion Matrix Shape : "
        f"{cm.shape}"
    )


    # =========================================================================
    # CREATE FIGURE
    # =========================================================================

    plt.figure(

        figsize=(24, 20)

    )


    # =========================================================================
    # DRAW HEATMAP
    # =========================================================================

    sns.heatmap(

        cm,

        annot=False,

        fmt="d",

        cmap="Blues",

        xticklabels=class_names,

        yticklabels=class_names,

        cbar=True

    )


    # =========================================================================
    # LABELS
    # =========================================================================

    plt.title(

        "Plant Disease Detection - Confusion Matrix",

        fontsize=18

    )


    plt.xlabel(

        "Predicted Class",

        fontsize=14

    )


    plt.ylabel(

        "Actual Class",

        fontsize=14

    )


    # =========================================================================
    # ROTATE CLASS NAMES
    # =========================================================================

    plt.xticks(

        rotation=90,

        fontsize=8

    )


    plt.yticks(

        rotation=0,

        fontsize=8

    )


    # =========================================================================
    # SAVE FIGURE
    # =========================================================================

    plt.tight_layout()


    plt.savefig(

        CONFUSION_MATRIX_PATH,

        dpi=300,

        bbox_inches="tight"

    )


    plt.close()


    print(
        "\nConfusion matrix saved:"
    )


    print(
        CONFUSION_MATRIX_PATH
    )


    return cm


# =============================================================================
# CLASS-WISE ACCURACY
# =============================================================================

def calculate_class_wise_accuracy(
    confusion_matrix_data,
    class_names
):
    """
    Calculate accuracy for each disease class.

    Class accuracy:

        Correct predictions for class
        --------------------------------
        Total actual samples for class
    """

    print_header(
        "CLASS-WISE ACCURACY"
    )


    class_accuracies = {}


    # =========================================================================
    # CALCULATE ACCURACY FOR EACH CLASS
    # =========================================================================

    for index, class_name in enumerate(

        class_names

    ):

        total_actual = np.sum(

            confusion_matrix_data[index]

        )


        correct_predictions = (

            confusion_matrix_data[index][index]

        )


        if total_actual > 0:

            accuracy = (

                correct_predictions

                /

                total_actual

            )

        else:

            accuracy = 0.0


        class_accuracies[class_name] = (
            float(accuracy)
        )


        print(

            f"{index:>3} : "
            f"{class_name:<35} "
            f"{accuracy * 100:>7.2f}%"

        )


    return class_accuracies


# =============================================================================
# SAVE CLASS-WISE ACCURACY
# =============================================================================

def save_class_wise_accuracy(
    class_accuracies
):
    """
    Save class-wise accuracy results.
    """

    class_accuracy_path = (

        REPORT_DIR /
        "class_wise_accuracy.txt"

    )


    with open(

        class_accuracy_path,

        "w",

        encoding="utf-8"

    ) as file:

        file.write(

            "PLANT DISEASE DETECTION\n"

        )

        file.write(

            "CLASS-WISE ACCURACY\n"

        )

        file.write(

            "=" * 80
            + "\n\n"

        )


        for (

            class_name,

            accuracy

        ) in class_accuracies.items():

            file.write(

                f"{class_name:<40} "
                f"{accuracy * 100:.2f}%\n"

            )


    print(
        "\nClass-wise accuracy saved:"
    )


    print(
        class_accuracy_path
    )


# =============================================================================
# FIND BEST AND WORST CLASSES
# =============================================================================

def display_best_worst_classes(
    class_accuracies
):
    """
    Display the best and worst performing disease classes.
    """

    if not class_accuracies:

        return


    # =========================================================================
    # SORT CLASSES
    # =========================================================================

    sorted_classes = sorted(

        class_accuracies.items(),

        key=lambda item: item[1],

        reverse=True

    )


    print_header(
        "BEST AND WORST PERFORMING CLASSES"
    )


    # =========================================================================
    # BEST 5
    # =========================================================================

    print(
        "Top 5 Classes:"
    )


    for rank, (

        class_name,

        accuracy

    ) in enumerate(

        sorted_classes[:5],

        start=1

    ):

        print(

            f"{rank}. "
            f"{class_name} : "
            f"{accuracy * 100:.2f}%"

        )


    # =========================================================================
    # WORST 5
    # =========================================================================

    print(
        "\nBottom 5 Classes:"
    )


    for rank, (

        class_name,

        accuracy

    ) in enumerate(

        sorted_classes[-5:],

        start=1

    ):

        print(

            f"{rank}. "
            f"{class_name} : "
            f"{accuracy * 100:.2f}%"

        )


# =============================================================================
# PART 10 COMPLETE
# =============================================================================
# =============================================================================
# TRAINING GRAPHS
# =============================================================================

def plot_training_accuracy(
    history
):
    """
    Plot training and validation accuracy.
    """

    print_header(
        "GENERATING ACCURACY GRAPH"
    )

    if history is None:

        print(
            "No training history available."
        )

        return


    # =========================================================================
    # GET ACCURACY VALUES
    # =========================================================================

    accuracy = history.get(
        "accuracy",
        []
    )

    validation_accuracy = history.get(
        "val_accuracy",
        []
    )


    if len(accuracy) == 0:

        print(
            "Accuracy data not available."
        )

        return


    # =========================================================================
    # CREATE GRAPH
    # =========================================================================

    plt.figure(
        figsize=(12, 7)
    )


    epochs = range(
        1,
        len(accuracy) + 1
    )


    plt.plot(

        epochs,

        accuracy,

        label="Training Accuracy",

        linewidth=2

    )


    if len(validation_accuracy) > 0:

        plt.plot(

            epochs,

            validation_accuracy,

            label="Validation Accuracy",

            linewidth=2

        )


    # =========================================================================
    # GRAPH LABELS
    # =========================================================================

    plt.title(
        "Plant Disease Detection - Accuracy"
    )


    plt.xlabel(
        "Epoch"
    )


    plt.ylabel(
        "Accuracy"
    )


    plt.grid(
        True,
        alpha=0.3
    )


    plt.legend()


    plt.tight_layout()


    # =========================================================================
    # SAVE GRAPH
    # =========================================================================

    plt.savefig(

        ACCURACY_GRAPH_PATH,

        dpi=300,

        bbox_inches="tight"

    )


    plt.close()


    print(
        f"Accuracy graph saved:\n"
        f"{ACCURACY_GRAPH_PATH}"
    )


# =============================================================================
# TRAINING LOSS GRAPH
# =============================================================================

def plot_training_loss(
    history
):
    """
    Plot training and validation loss.
    """

    print_header(
        "GENERATING LOSS GRAPH"
    )


    if history is None:

        print(
            "No training history available."
        )

        return


    # =========================================================================
    # GET LOSS VALUES
    # =========================================================================

    loss = history.get(
        "loss",
        []
    )

    validation_loss = history.get(
        "val_loss",
        []
    )


    if len(loss) == 0:

        print(
            "Loss data not available."
        )

        return


    # =========================================================================
    # CREATE GRAPH
    # =========================================================================

    plt.figure(
        figsize=(12, 7)
    )


    epochs = range(
        1,
        len(loss) + 1
    )


    plt.plot(

        epochs,

        loss,

        label="Training Loss",

        linewidth=2

    )


    if len(validation_loss) > 0:

        plt.plot(

            epochs,

            validation_loss,

            label="Validation Loss",

            linewidth=2

        )


    # =========================================================================
    # GRAPH LABELS
    # =========================================================================

    plt.title(
        "Plant Disease Detection - Loss"
    )


    plt.xlabel(
        "Epoch"
    )


    plt.ylabel(
        "Loss"
    )


    plt.grid(
        True,

        alpha=0.3

    )


    plt.legend()


    plt.tight_layout()


    # =========================================================================
    # SAVE GRAPH
    # =========================================================================

    plt.savefig(

        LOSS_GRAPH_PATH,

        dpi=300,

        bbox_inches="tight"

    )


    plt.close()


    print(
        f"Loss graph saved:\n"
        f"{LOSS_GRAPH_PATH}"
    )


# =============================================================================
# TOP-3 ACCURACY GRAPH
# =============================================================================

def plot_top_3_accuracy(
    history
):
    """
    Plot Top-3 training and validation accuracy if available.
    """

    print_header(
        "GENERATING TOP-3 ACCURACY GRAPH"
    )


    if history is None:

        return


    top_3_accuracy = history.get(

        "top_3_accuracy",

        []

    )


    validation_top_3_accuracy = history.get(

        "val_top_3_accuracy",

        []

    )


    if len(top_3_accuracy) == 0:

        print(
            "Top-3 accuracy data not available."
        )

        return


    # =========================================================================
    # CREATE GRAPH
    # =========================================================================

    plt.figure(

        figsize=(12, 7)

    )


    epochs = range(

        1,

        len(top_3_accuracy) + 1

    )


    plt.plot(

        epochs,

        top_3_accuracy,

        label="Training Top-3 Accuracy",

        linewidth=2

    )


    if len(
        validation_top_3_accuracy
    ) > 0:

        validation_epochs = range(

            1,

            len(
                validation_top_3_accuracy
            ) + 1

        )


        plt.plot(

            validation_epochs,

            validation_top_3_accuracy,

            label="Validation Top-3 Accuracy",

            linewidth=2

        )


    # =========================================================================
    # LABELS
    # =========================================================================

    plt.title(

        "Plant Disease Detection - Top-3 Accuracy"

    )


    plt.xlabel(
        "Epoch"
    )


    plt.ylabel(
        "Top-3 Accuracy"
    )


    plt.grid(

        True,

        alpha=0.3

    )


    plt.legend()


    plt.tight_layout()


    # =========================================================================
    # SAVE
    # =========================================================================

    top_3_graph_path = (

        REPORT_DIR /
        "top_3_accuracy.png"

    )


    plt.savefig(

        top_3_graph_path,

        dpi=300,

        bbox_inches="tight"

    )


    plt.close()


    print(
        f"Top-3 accuracy graph saved:\n"
        f"{top_3_graph_path}"
    )


# =============================================================================
# FIND BEST EPOCH
# =============================================================================

def find_best_epoch(
    history
):
    """
    Find the epoch with the best validation accuracy.
    """

    if history is None:

        return None


    validation_accuracy = history.get(

        "val_accuracy",

        []

    )


    if len(validation_accuracy) == 0:

        return None


    best_index = int(

        np.argmax(

            validation_accuracy

        )

    )


    best_epoch = best_index + 1


    best_accuracy = (

        validation_accuracy[
            best_index
        ]

    )


    print_header(
        "BEST VALIDATION RESULT"
    )


    print(
        f"Best Epoch            : "
        f"{best_epoch}"
    )


    print(
        f"Best Validation "
        f"Accuracy              : "
        f"{best_accuracy * 100:.2f}%"
    )


    return (

        best_epoch,

        float(best_accuracy)

    )


# =============================================================================
# SAVE FINAL MODEL
# =============================================================================

def save_final_model(
    model
):
    """
    Save the final trained model.

    The model is saved only after the training process has
    reached its intended final state.
    """

    print_header(
        "SAVING FINAL MODEL"
    )


    try:

        model.save(

            str(
                FINAL_MODEL_PATH
            )

        )


        print(
            "Final model saved successfully:"
        )


        print(
            FINAL_MODEL_PATH
        )


    except Exception as error:

        print(
            "\nERROR while saving final model:"
        )


        print(
            error
        )


        raise


# =============================================================================
# SAVE LAST MODEL
# =============================================================================

def save_last_model(
    model
):
    """
    Save the most recently trained model.
    """

    print_header(
        "SAVING LAST TRAINED MODEL"
    )


    try:

        model.save(

            str(
                LAST_MODEL_PATH
            )

        )


        print(
            "Last trained model saved successfully:"
        )


        print(
            LAST_MODEL_PATH
        )


    except Exception as error:

        print(
            "\nERROR while saving last model:"
        )


        print(
            error
        )


# =============================================================================
# SAVE TRAINING SUMMARY
# =============================================================================

def save_training_summary(
    history,
    completed_epoch
):
    """
    Save a concise summary of the training process.
    """

    print_header(
        "SAVING TRAINING SUMMARY"
    )


    with open(

        TRAINING_SUMMARY_PATH,

        "w",

        encoding="utf-8"

    ) as file:

        file.write(

            "PLANT DISEASE DETECTION\n"

        )

        file.write(

            "TRAINING SUMMARY\n"

        )

        file.write(

            "=" * 80
            + "\n\n"

        )


        file.write(

            f"Transfer Learning Epochs : "
            f"{TRANSFER_EPOCHS}\n"

        )


        file.write(

            f"Fine-Tuning Epochs       : "
            f"{FINE_TUNE_EPOCHS}\n"

        )


        file.write(

            f"Fixed Final Epoch        : "
            f"{FINAL_TRAINING_EPOCH}\n"

        )


        file.write(

            f"Completed Epoch          : "
            f"{completed_epoch}\n"

        )


        file.write(

            f"Initial Learning Rate    : "
            f"{LEARNING_RATE}\n"

        )


        file.write(

            f"Fine-Tune Learning Rate  : "
            f"{FINE_TUNE_LEARNING_RATE}\n"

        )


        # ---------------------------------------------------------------------
        # BEST EPOCH
        # ---------------------------------------------------------------------

        best_result = find_best_epoch(

            history

        )


        if best_result is not None:

            best_epoch, best_accuracy = (
                best_result
            )


            file.write(

                f"Best Validation Epoch   : "
                f"{best_epoch}\n"

            )


            file.write(

                f"Best Validation Accuracy: "
                f"{best_accuracy * 100:.2f}%\n"

            )


        file.write(

            "\nTraining Status          : "
            "COMPLETED\n"

        )


        file.write(

            "\nModel Files:\n"

        )


        file.write(

            f"Best Model   : "
            f"{BEST_MODEL_PATH}\n"

        )


        file.write(

            f"Last Model   : "
            f"{LAST_MODEL_PATH}\n"

        )


        file.write(

            f"Final Model  : "
            f"{FINAL_MODEL_PATH}\n"

        )


    print(
        f"Training summary saved:\n"
        f"{TRAINING_SUMMARY_PATH}"
    )


# =============================================================================
# GENERATE ALL TRAINING GRAPHS
# =============================================================================

def generate_training_graphs(
    history
):
    """
    Generate all available training graphs.
    """

    print_header(
        "GENERATING TRAINING GRAPHS"
    )


    if history is None:

        print(
            "Training history is not available."
        )

        return


    plot_training_accuracy(

        history

    )


    plot_training_loss(

        history

    )


    plot_top_3_accuracy(

        history

    )


    print(
        "\nAll available training graphs generated."
    )


# =============================================================================
# PART 11 COMPLETE
# =============================================================================
# =============================================================================
# PART 12
# MAIN PROGRAM
# =============================================================================

def main():

    # =========================================================================
    # START
    # =========================================================================

    print_header(
        "PLANT DISEASE DETECTION USING EFFICIENTNETB0"
    )


    print(
        f"TensorFlow Version : "
        f"{tf.__version__}"
    )


    # =========================================================================
    # 1. VERIFY DATASET
    # =========================================================================

    num_classes, total_images = (
        verify_dataset()
    )


    # =========================================================================
    # 2. LOAD DATASETS
    # =========================================================================

    dataset_manager = DatasetManager()


    (
        train_dataset,
        validation_dataset,
        test_dataset,
        class_names,
        num_classes

    ) = dataset_manager.load_datasets()


    # =========================================================================
    # 3. SAVE CLASS INFORMATION
    # =========================================================================

    print_header(
        "SAVING CLASS INFORMATION"
    )


    save_labels(
        class_names
    )


    save_class_indices(
        class_names
    )


    # =========================================================================
    # 4. PREPARE DATASETS
    # =========================================================================

    (
        train_dataset,
        validation_dataset,
        test_dataset

    ) = prepare_all_datasets(

        train_dataset,

        validation_dataset,

        test_dataset

    )


    # =========================================================================
    # 5. DISPLAY DATASET INFORMATION
    # =========================================================================

    display_dataset_information(

        train_dataset,

        validation_dataset,

        test_dataset,

        class_names

    )


    # =========================================================================
    # 6. CALCULATE CLASS WEIGHTS
    # =========================================================================

    class_weights = calculate_class_weights(

        train_dataset,

        num_classes

    )


    # =========================================================================
    # 7. DISPLAY TRAINING STRATEGY
    # =========================================================================

    display_training_strategy()


    display_callback_settings()


    # =========================================================================
    # 8. CHECK FOR PREVIOUS TRAINING
    # =========================================================================

    (
        resume_training,
        saved_epoch,
        saved_phase,
        loaded_model,
        training_history

    ) = check_resume_training()


    # =========================================================================
    # 9. COMPLETED TRAINING
    # =========================================================================
    #
    # If the checkpoint says:
    #
    #     Epoch = 74
    #     Phase = completed
    #
    # then there is absolutely no reason to train again.
    #
    # We load the model and go directly to evaluation.
    # =========================================================================

    if (

        resume_training

        and

        saved_phase == "completed"

        and

        saved_epoch >= FINAL_TRAINING_EPOCH

    ):

        print_header(
            "TRAINING ALREADY COMPLETED"
        )


        print(
            f"Saved Epoch : "
            f"{saved_epoch}"
        )


        print(
            f"Final Epoch : "
            f"{FINAL_TRAINING_EPOCH}"
        )


        model = loaded_model


        # ---------------------------------------------------------------------
        # Load best model if available
        # ---------------------------------------------------------------------

        best_model = load_best_trained_model()


        if best_model is not None:

            model = best_model


        completed_epoch = (
            FINAL_TRAINING_EPOCH
        )


    # =========================================================================
    # 10. NEW TRAINING
    # =========================================================================

    elif not resume_training:

        print_header(
            "CREATING NEW MODEL"
        )


        # ---------------------------------------------------------------------
        # Build EfficientNetB0
        # ---------------------------------------------------------------------

        (
            model,
            base_model

        ) = build_model(

            num_classes

        )


        display_model_information(

            model

        )


        save_model_summary(

            model

        )


        # ---------------------------------------------------------------------
        # Compile model
        # ---------------------------------------------------------------------

        model = compile_model(

            model,

            learning_rate=LEARNING_RATE

        )


        # ---------------------------------------------------------------------
        # Start from epoch 0
        # ---------------------------------------------------------------------

        training_history = None

        completed_epoch = 0


        # ---------------------------------------------------------------------
        # Save initial state
        # ---------------------------------------------------------------------

        save_current_state(

            0,

            "transfer"

        )


        # =========================================================================
        # 11. TRANSFER LEARNING
        # =========================================================================

        (
            model,
            training_history,
            completed_epoch

        ) = train_transfer_learning(

            model=model,

            train_dataset=train_dataset,

            validation_dataset=validation_dataset,

            class_weights=class_weights,

            initial_epoch=0,

            previous_history=training_history

        )


        # =========================================================================
        # 12. PREPARE FINE-TUNING
        # =========================================================================

        print_header(
            "PREPARING FINE-TUNING"
        )


        # EfficientNetB0 is inside the model.
        # Find the base model by name.

        base_model = None


        for layer in model.layers:

            if isinstance(
                layer,
                tf.keras.Model
            ):

                if (
                    "efficientnet"
                    in
                    layer.name.lower()
                ):

                    base_model = layer

                    break


        if base_model is None:

            raise ValueError(
                "EfficientNetB0 base model "
                "could not be found."
            )


        # =========================================================================
        # 13. FINE-TUNING
        # =========================================================================

        (
            model,
            training_history,
            completed_epoch

        ) = fine_tune_model(

            model=model,

            base_model=base_model,

            train_dataset=train_dataset,

            validation_dataset=validation_dataset,

            class_weights=class_weights,

            previous_history=training_history,

            fine_tune_start_epoch=completed_epoch

        )


    # =========================================================================
    # 14. RESUME EXISTING FINE-TUNING
    # =========================================================================

    else:

        print_header(
            "RESUMING PREVIOUS TRAINING"
        )


        print(
            f"Saved Epoch : "
            f"{saved_epoch}"
        )


        print(
            f"Saved Phase : "
            f"{saved_phase}"
        )


        model = loaded_model


        # ---------------------------------------------------------------------
        # Transfer learning already completed
        # ---------------------------------------------------------------------

        if saved_phase == "fine_tune":

            print(
                "\nTransfer learning was already completed."
            )


            print_header(
                "PREPARING FINE-TUNING"
            )


            # -----------------------------------------------------------------
            # Locate EfficientNetB0
            # -----------------------------------------------------------------

            base_model = None


            for layer in model.layers:

                if isinstance(
                    layer,
                    tf.keras.Model
                ):

                    if (
                        "efficientnet"
                        in
                        layer.name.lower()
                    ):

                        base_model = layer

                        break


            if base_model is None:

                raise ValueError(
                    "EfficientNetB0 base model "
                    "could not be found in "
                    "the loaded checkpoint."
                )


            # -----------------------------------------------------------------
            # Resume fine-tuning
            # -----------------------------------------------------------------

            (
                model,
                training_history,
                completed_epoch

            ) = fine_tune_model(

                model=model,

                base_model=base_model,

                train_dataset=train_dataset,

                validation_dataset=validation_dataset,

                class_weights=class_weights,

                previous_history=training_history,

                fine_tune_start_epoch=saved_epoch

            )


        # ---------------------------------------------------------------------
        # Unexpected phase
        # ---------------------------------------------------------------------

        elif saved_phase == "transfer":

            print(
                "\nResuming transfer learning..."
            )


            base_model = None


            for layer in model.layers:

                if isinstance(
                    layer,
                    tf.keras.Model
                ):

                    if (
                        "efficientnet"
                        in
                        layer.name.lower()
                    ):

                        base_model = layer

                        break


            if base_model is None:

                raise ValueError(
                    "EfficientNetB0 base model "
                    "could not be found."
                )


            base_model.trainable = False


            model = compile_model(

                model,

                learning_rate=LEARNING_RATE

            )


            (
                model,
                training_history,
                completed_epoch

            ) = train_transfer_learning(

                model=model,

                train_dataset=train_dataset,

                validation_dataset=validation_dataset,

                class_weights=class_weights,

                initial_epoch=saved_epoch,

                previous_history=training_history

            )


            # -------------------------------------------------------------
            # Fine-tuning after transfer learning
            # -------------------------------------------------------------

            (
                model,
                training_history,
                completed_epoch

            ) = fine_tune_model(

                model=model,

                base_model=base_model,

                train_dataset=train_dataset,

                validation_dataset=validation_dataset,

                class_weights=class_weights,

                previous_history=training_history,

                fine_tune_start_epoch=completed_epoch

            )


        else:

            raise ValueError(

                f"Unknown training phase: "
                f"{saved_phase}"

            )


    # =========================================================================
    # 15. SAVE LAST MODEL
    # =========================================================================

    save_last_model(

        model

    )


    # =========================================================================
    # 16. SAVE FINAL MODEL
    # =========================================================================

    if completed_epoch >= FINAL_TRAINING_EPOCH:

        save_final_model(

            model

        )


        save_current_state(

            FINAL_TRAINING_EPOCH,

            "completed"

        )


    else:

        print_header(
            "TRAINING NOT YET COMPLETE"
        )


        print(
            f"Current Epoch : "
            f"{completed_epoch}"
        )


        print(
            f"Final Epoch   : "
            f"{FINAL_TRAINING_EPOCH}"
        )


        print(
            "\nThe training state has been saved."
        )


    # =========================================================================
    # 17. GENERATE TRAINING GRAPHS
    # =========================================================================

    if training_history is not None:

        generate_training_graphs(

            training_history

        )


        find_best_epoch(

            training_history

        )


    # =========================================================================
    # 18. LOAD BEST MODEL FOR FINAL EVALUATION
    # =========================================================================

    best_model = load_best_trained_model()


    if best_model is not None:

        evaluation_model = best_model

    else:

        evaluation_model = model


    # =========================================================================
    # 19. FINAL TEST EVALUATION
    # =========================================================================

    evaluation_results = evaluate_model(

        evaluation_model,

        test_dataset

    )


    # =========================================================================
    # 20. COLLECT PREDICTIONS
    # =========================================================================

    (
        true_labels,
        predicted_labels,
        prediction_probabilities

    ) = collect_predictions(

        evaluation_model,

        test_dataset

    )


    # =========================================================================
    # 21. MANUAL ACCURACY
    # =========================================================================

    manual_accuracy = calculate_manual_accuracy(

        true_labels,

        predicted_labels

    )


    # =========================================================================
    # 22. MANUAL TOP-3 ACCURACY
    # =========================================================================

    manual_top_3_accuracy = calculate_top_k_accuracy(

        true_labels,

        prediction_probabilities,

        k=3

    )


    # =========================================================================
    # 23. CLASSIFICATION REPORT
    # =========================================================================

    generate_classification_report(

        true_labels,

        predicted_labels,

        class_names

    )


    # =========================================================================
    # 24. CONFUSION MATRIX
    # =========================================================================

    confusion_matrix_data = generate_confusion_matrix(

        true_labels,

        predicted_labels,

        class_names

    )


    # =========================================================================
    # 25. CLASS-WISE ACCURACY
    # =========================================================================

    class_accuracies = calculate_class_wise_accuracy(

        confusion_matrix_data,

        class_names

    )


    save_class_wise_accuracy(

        class_accuracies

    )


    display_best_worst_classes(

        class_accuracies

    )


    # =========================================================================
    # 26. SAVE EVALUATION RESULTS
    # =========================================================================

    save_evaluation_results(

        evaluation_results,

        manual_accuracy,

        manual_top_3_accuracy

    )


    # =========================================================================
    # 27. SAVE TRAINING SUMMARY
    # =========================================================================

    save_training_summary(

        training_history,

        completed_epoch

    )


    # =========================================================================
    # 28. FINAL MESSAGE
    # =========================================================================

    print_header(
        "TRAINING AND EVALUATION COMPLETED"
    )


    print(
        f"Final Training Epoch : "
        f"{completed_epoch}"
    )


    print(
        f"Fixed Maximum Epoch  : "
        f"{FINAL_TRAINING_EPOCH}"
    )


    if "accuracy" in evaluation_results:

        print(
            f"Test Accuracy        : "
            f"{evaluation_results['accuracy'] * 100:.2f}%"
        )


    if "top_3_accuracy" in evaluation_results:

        print(
            f"Test Top-3 Accuracy  : "
            f"{evaluation_results['top_3_accuracy'] * 100:.2f}%"
        )


    print(
        "\nModels:"
    )


    print(
        f"Best Model  : "
        f"{BEST_MODEL_PATH}"
    )


    print(
        f"Last Model  : "
        f"{LAST_MODEL_PATH}"
    )


    print(
        f"Final Model : "
        f"{FINAL_MODEL_PATH}"
    )


    print(
        "\nReports:"
    )


    print(
        f"{REPORT_DIR}"
    )


    print(
        "\nTraining finished successfully."
    )


# =============================================================================
# PROGRAM ENTRY POINT
# =============================================================================

if __name__ == "__main__":

    try:

        main()

    except KeyboardInterrupt:

        print(
            "\n\nTraining stopped manually by user."
        )

        print(
            "The latest checkpoint and "
            "training state have been saved."
        )


    except Exception as error:

        print(
            "\n\n" + "=" * 80
        )

        print(
            "TRAINING ERROR"
        )

        print(
            "=" * 80
        )


        print(
            f"\n{type(error).__name__}: "
            f"{error}"
        )


        print(
            "\nCheck the error above and "
            "correct the corresponding section."
        )


        raise


# =============================================================================
# END OF TRAIN.PY
# =============================================================================
