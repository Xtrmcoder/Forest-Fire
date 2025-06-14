import streamlit as st
import numpy as np
from tensorflow.keras.models import load_model
from PIL import Image

# Set up app config
st.set_page_config(page_title="Fire Detection from Satellite", layout="centered")

st.title("🔥 Fire Detection from Satellite Images")
st.write("Upload a satellite image to detect the presence of **Fire** or **No Fire**.")

# Load model (cache it to avoid reloading)
@st.cache_resource
def load_fire_model():
    return load_model("fire_detection_model.h5")

model = load_fire_model()

# Class labels (adjust based on your training)
class_names = ["No Fire", "Fire 🔥"]

# File uploader
uploaded_file = st.file_uploader("📷 Upload Satellite Image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="Uploaded Image", use_column_width=True)

    # Resize and normalize image (adjust shape based on model)
    input_shape = (64, 64)
    image_resized = image.resize(input_shape)
    img_array = np.array(image_resized) / 255.0
    img_array = img_array.reshape(1, *input_shape, 3)  # Add batch dimension

    if st.button("🧠 Detect Fire"):
        with st.spinner("Analyzing image..."):
            prediction = model.predict(img_array)[0]  # Get the prediction vector
            predicted_class = np.argmax(prediction)
            confidence = prediction[predicted_class] * 100

        st.subheader("🔍 Result:")
        st.success(f"Prediction: *{class_names[predicted_class]}*")
        st.info(f"Confidence: *{confidence:.2f}%*")
