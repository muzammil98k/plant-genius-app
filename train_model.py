import tensorflow as tf
import os

# --- 1. VERIFY GPU SETUP ---
gpus = tf.config.list_physical_devices('GPU')
if gpus:
    try:
        for gpu in gpus:
            tf.config.experimental.set_memory_growth(gpu, True)
        logical_gpus = tf.config.list_logical_devices('GPU')
        print(
            f"✅ Found {len(gpus)} Physical GPUs, {len(logical_gpus)} Logical GPUs")
        print("TensorFlow will use the GPU for training.")
    except RuntimeError as e:
        print(e)
else:
    print("⚠️ No GPU found. TensorFlow will use the CPU.")


# --- 2. CONFIGURATION ---
IMAGE_SIZE = (128, 128)
BATCH_SIZE = 32
EPOCHS = 15

# Use the path you confirmed earlier
DATA_DIR = r'C:/Users/bond9/OneDrive/Desktop/project/Plant-Disease-Project/New Plant Diseases Dataset(Augmented)'

# --- 3. DATA LOADING & PREPROCESSING ---
train_dir = os.path.join(DATA_DIR, 'train')
valid_dir = os.path.join(DATA_DIR, 'valid')
test_dir = os.path.join(DATA_DIR, 'test')

# Load datasets
train_data = tf.keras.utils.image_dataset_from_directory(
    train_dir,
    labels='inferred',
    label_mode='categorical',
    image_size=IMAGE_SIZE,
    interpolation='nearest',
    batch_size=BATCH_SIZE,
    shuffle=True
)

validation_data = tf.keras.utils.image_dataset_from_directory(
    valid_dir,
    labels='inferred',
    label_mode='categorical',
    image_size=IMAGE_SIZE,
    interpolation='nearest',
    batch_size=BATCH_SIZE,
    shuffle=False
)

test_data = tf.keras.utils.image_dataset_from_directory(
    test_dir,
    labels='inferred',
    label_mode='categorical',
    image_size=IMAGE_SIZE,
    interpolation='nearest',
    batch_size=BATCH_SIZE,
    shuffle=False
)

# 💡 --- THE CRITICAL FIX ---
# Get class names from the original dataset object BEFORE mapping
class_names = train_data.class_names
num_classes = len(class_names)
# Print first 5 classes
print(f"Found {num_classes} classes: {class_names[:5]}...")


# Now, normalize the datasets
normalization_layer = tf.keras.layers.Rescaling(1./255)
train_data = train_data.map(lambda x, y: (normalization_layer(x), y))
validation_data = validation_data.map(lambda x, y: (normalization_layer(x), y))
test_data = test_data.map(lambda x, y: (normalization_layer(x), y))


# --- 4. BUILD THE CNN MODEL ---
model = tf.keras.Sequential([
    tf.keras.layers.InputLayer(input_shape=(IMAGE_SIZE[0], IMAGE_SIZE[1], 3)),
    tf.keras.layers.Conv2D(32, (3, 3), activation='relu'),
    tf.keras.layers.MaxPooling2D(2, 2),
    tf.keras.layers.Conv2D(64, (3, 3), activation='relu'),
    tf.keras.layers.MaxPooling2D(2, 2),
    tf.keras.layers.Conv2D(128, (3, 3), activation='relu'),
    tf.keras.layers.MaxPooling2D(2, 2),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dropout(0.5),
    tf.keras.layers.Dense(num_classes, activation='softmax')
])

model.summary()

# --- 5. COMPILE THE MODEL ---
model.compile(
    optimizer='adam',
    loss='categorical_crossentropy',
    metrics=['accuracy']
)

# --- 6. TRAIN THE MODEL ---
print("\n🚀 Starting model training...")
history = model.fit(
    train_data,
    validation_data=validation_data,
    epochs=EPOCHS
)
print("✅ Model training finished.")

# --- 7. SAVE THE MODEL ---
model.save("plant_disease_model.keras")
print("💾 Model saved as plant_disease_model.keras")

# --- 8. EVALUATE ON THE TEST SET ---
print("\n🧪 Evaluating model on the test dataset...")
test_loss, test_accuracy = model.evaluate(test_data)
print(f"\nTest Loss: {test_loss}")
print(f"Test Accuracy: {test_accuracy * 100:.2f}%")
