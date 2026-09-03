import tensorflow as tf
import os

MODEL_PATH = "models/best_model.keras"
TEST_DIR = "dataset/test"

IMG_SIZE = (224, 224)
BATCH_SIZE = 32

print("=" * 60)
print("MODEL ACCURACY EVALUATION")
print("=" * 60)

# Check model
if not os.path.exists(MODEL_PATH):
    print(f"\n❌ Model not found:")
    print(MODEL_PATH)
    print("\nCheck the files inside models/ and tell me the model filename.")
    raise SystemExit

# Check test dataset
if not os.path.exists(TEST_DIR):
    print(f"\n❌ Test dataset not found:")
    print(TEST_DIR)
    raise SystemExit

print("\nLoading model...")
model = tf.keras.models.load_model(MODEL_PATH)

print("Loading test dataset...")

test_data = tf.keras.utils.image_dataset_from_directory(
    TEST_DIR,
    image_size=IMG_SIZE,
    batch_size=BATCH_SIZE,
    shuffle=False
)

print("\nNumber of classes:", len(test_data.class_names))
print("Classes:", test_data.class_names)

print("\nEvaluating...")

loss, accuracy = model.evaluate(
    test_data,
    verbose=1
)

print("\n" + "=" * 60)
print("FINAL RESULT")
print("=" * 60)

print(f"Test Loss     : {loss:.4f}")
print(f"Test Accuracy : {accuracy * 100:.2f}%")

print("=" * 60)