# 🔥 Fire Detection from Satellite Images

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://forest-fire-miwuzf68mw5wxxeql9pbag.streamlit.app/)

A lightweight deep learning web app built with Streamlit that allows users to **detect fire in satellite images** using a pre-trained convolutional neural network (CNN). Simply upload a satellite image and the model will classify it as either **Fire 🔥** or **No Fire**.

---

## 🚀 Demo

👉 **Live App**: [Click here to try it](https://forest-fire-miwuzf68mw5wxxeql9pbag.streamlit.app/)

---

## 🧠 How It Works

- The app uses a deep learning model (`fire_detection_model.h5`) trained on satellite imagery to identify fire incidents.
- Users can upload `.jpg`, `.jpeg`, or `.png` satellite images.
- Images are resized and preprocessed before prediction.
- The app displays:
  - The uploaded image
  - The predicted label (Fire / No Fire)
  - Model confidence score

---

## 📸 Screenshots

| Upload Image | Prediction Result |
|--------------|-------------------|
| ![upload](https://github.com/Xtrmcoder/Forest-Fire/blob/5cb1365ec0de92667519b6b5896a7383365258b7/Screenshot%202025-06-14%20152954.png) | ![result](https://github.com/Xtrmcoder/Forest-Fire/blob/70a114e70b84406ac4e6a1d38c79cfc7f932e79f/Screenshot%202025-06-14%20152954.png) |

---

## 🛠 Tech Stack

- **Frontend/UI**: [Streamlit](https://streamlit.io)
- **Model**: Keras (TensorFlow backend)
- **Image Handling**: Pillow (PIL)
- **Languages**: Python

---

## 📁 File Structure


# Forest-Fire
