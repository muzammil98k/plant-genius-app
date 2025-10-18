import streamlit as st
import tensorflow as tf
from PIL import Image
import numpy as np
import time
import base64  # New import to handle local background file

# Import the new animation functions
from animations import show_animation

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Plant Genius 🌿",
    page_icon="🌿",
    layout="wide"
)

# --- NEW: FUNCTION TO LOAD LOCAL BACKGROUND ---


def get_base64_of_bin_file(bin_file):
    """Encodes a binary file (like an image or gif) to a base64 string."""
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()


def set_background(file_path):
    """Sets the background of the Streamlit app using a local file."""
    base64_string = get_base64_of_bin_file(file_path)
    st.markdown(f"""
        <style>
        .stApp {{
            background-image: url("data:image/gif;base64,{base64_string}");
            background-size: cover;
            background-attachment: fixed;
        }}
        /* Other styles remain the same */
        [data-testid="stAppViewContainer"] > .main {{
            background-color: rgba(0, 0, 0, 0.6);
            border-radius: 15px;
            padding: 2rem;
        }}
        h1, h2, h3, h4, h5, h6, .stMarkdown, .stFileUploader, .stMetric, label {{
            color: white !important;
        }}
        [data-testid="stSidebar"] > div:first-child {{
            background-color: rgba(15, 23, 15, 0.7);
            border-radius: 15px;
        }}
        .st-expander {{
            background-color: rgba(255, 255, 255, 0.1);
            border-radius: 10px;
        }}
        </style>
        """,
                unsafe_allow_html=True
                )


# Set the background using your local GIF
set_background('assets/background.gif')

# --- MODEL AND CLASS NAMES ---


@st.cache_resource
def load_model():
    model = tf.keras.models.load_model('plant_disease_model.keras')
    return model


# Class names list remains the same...
class_names = [
    'Apple___Apple_scab', 'Apple___Black_rot', 'Apple___Cedar_apple_rust', 'Apple___healthy',
    'Blueberry___healthy', 'Cherry_(including_sour)___Powdery_mildew', 'Cherry_(including_sour)___healthy',
    'Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot', 'Corn_(maize)___Common_rust_',
    'Corn_(maize)___Northern_Leaf_Blight', 'Corn_(maize)___healthy', 'Grape___Black_rot',
    'Grape___Esca_(Black_Measles)', 'Grape___Leaf_blight_(Isariopsis_Leaf_Spot)', 'Grape___healthy',
    'Orange___Haunglongbing_(Citrus_greening)', 'Peach___Bacterial_spot', 'Peach___healthy',
    'Pepper,_bell___Bacterial_spot', 'Pepper,_bell___healthy', 'Potato___Early_blight',
    'Potato___Late_blight', 'Potato___healthy', 'Raspberry___healthy', 'Soybean___healthy',
    'Squash___Powdery_mildew', 'Strawberry___Leaf_scorch', 'Strawberry___healthy',
    'Tomato___Bacterial_spot', 'Tomato___Early_blight', 'Tomato___Late_blight',
    'Tomato___Leaf_Mold', 'Tomato___Septoria_leaf_spot', 'Tomato___Spider_mites Two-spotted_spider_mite',
    'Tomato___Target_Spot', 'Tomato___Tomato_Yellow_Leaf_Curl_Virus', 'Tomato___Tomato_mosaic_virus',
    'Tomato___healthy'
]
model = load_model()

# --- SIDEBAR ---
with st.sidebar:
    st.title("About Plant Genius")
    # --- FIXED: Added the text back to the sidebar ---
    st.write(
        "This app uses a Deep Learning model to identify plant diseases from leaf images. "
        "It was trained on a dataset of over 87,000 images across 38 classes."
    )
    st.subheader("How to Use")
    st.write(
        "1. **Upload an image:** Click the 'Browse files' button.\n"
        "2. **Get your prediction:** The model will analyze the image and display the result."
    )
    st.info("Created with ❤️ using Python, TensorFlow, and Streamlit.")

# --- MAIN PAGE ---
st.title("Plant Genius: Your AI Plant Doctor 🩺")
st.write("Upload a leaf image and let our AI tell you if it's healthy or has a disease.")

col1, col2 = st.columns([1, 1.2])

with col1:
    uploaded_file = st.file_uploader(
        "Choose a leaf image...",
        type=["jpg", "jpeg", "png"],
        label_visibility="collapsed"  # Hides the default label
    )

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    with col1:
        st.image(image, use_column_width=True, caption="Your Leaf Image")

    with st.spinner('The AI is performing a check-up... 🧠'):
        time.sleep(1)
        # Prediction logic remains the same...
        img_array = np.array(image)
        img_resized = tf.image.resize(img_array, (128, 128))
        img_rescaled = img_resized / 255.0
        img_expanded = np.expand_dims(img_rescaled, axis=0)
        prediction = model.predict(img_expanded)
        confidence = np.max(prediction)
        predicted_class_index = np.argmax(prediction)
        full_prediction_name = class_names[predicted_class_index]
        name_parts = full_prediction_name.split('___')
        plant_name = name_parts[0].replace('_', ' ')
        disease_name = name_parts[1].replace('_', ' ')

    with col2:
        st.subheader("Diagnosis Result")
        if disease_name.lower() == 'healthy':
            st.success(
                f"**Result:** This **{plant_name}** leaf looks **Healthy**!")
            show_animation("healthy")  # Use the new animation function
        else:
            st.warning(
                f"**Result:** This **{plant_name}** leaf appears to have **{disease_name}**.")
            show_animation("sick")  # Use the new animation function

        with st.expander("View Confidence Score"):
            st.metric(label="**Model Confidence**",
                      value=f"{confidence * 100:.2f}%")
            st.progress(float(confidence))
else:
    with col2:
        show_animation("welcome", height=300)  # Use the new animation function
