import streamlit as st
import tensorflow as tf
from transformers import ViTFeatureExtractor, TFViTForImageClassification
from PIL import Image
import numpy as np
from transformers import ViTImageProcessor, ViTForImageClassification
import torch

# Load the pre-trained model
model = TFViTForImageClassification.from_pretrained('google/vit-base-patch16-224')
feature_extractor = ViTFeatureExtractor.from_pretrained('google/vit-base-patch16-224')

# Set Streamlit app title and description
st.title("Food Image Classifier")
st.write("Upload an image of food and get a prediction!")

# Define colors and styles
main_color = "#FF5722"
secondary_color = "#FFFFFF"
background_color = "#F5F5F5"
text_color = "#333333"
button_color = "#4CAF50"
button_hover_color = "#45A049"

# Set page background color
st.markdown(
    f"""
    <style>
    body {{
        background-color: {background_color};
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# Set page style
st.markdown(
    f"""
    <style>
    .title {{
        color: {main_color};
        text-align: center;
        font-size: 36px;
        margin-bottom: 20px;
    }}
    .upload {{
        padding: 20px;
        background-color: {secondary_color};
        border-radius: 10px;
        margin-bottom: 20px;
    }}
    .prediction {{
        padding: 20px;
        background-color: {secondary_color};
        border-radius: 10px;
        margin-bottom: 20px;
    }}
    .btn-primary {{
        background-color: {button_color};
        color: {secondary_color};
        padding: 10px 20px;
        border-radius: 5px;
        border: none;
        cursor: pointer;
        font-weight: bold;
        transition: background-color 0.3s;
    }}
    .btn-primary:hover {{
        background-color: {button_hover_color};
    }}
    </style>
    """,
    unsafe_allow_html=True
)



# Load the ViT model and image processor
processor = ViTImageProcessor.from_pretrained('google/vit-base-patch16-224')
model = ViTForImageClassification.from_pretrained('google/vit-base-patch16-224')

# Function to preprocess the image
def preprocess_image(image):
    image = image.resize((224, 224))
    image = np.array(image)
    inputs = processor(images=image, return_tensors="pt")
    return inputs

# Function to make predictions
def predict_image(image):
    inputs = preprocess_image(image)
    outputs = model(**inputs)
    logits = outputs.logits
    predicted_class_idx = logits.argmax(-1).item()
    label = model.config.id2label[predicted_class_idx]
    confidence = torch.softmax(logits, dim=-1)[0, predicted_class_idx].item()
    return label, confidence


# Display image upload option
uploaded_image = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"], key="fileUploader")

# Perform prediction if image is uploaded
if uploaded_image is not None:
    # Open and display the uploaded image
    image = Image.open(uploaded_image)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    # Make prediction on the image
    label, confidence = predict_image(image)

    # Display the prediction results
    st.markdown("<div class='prediction'>", unsafe_allow_html=True)
    st.write(f"<p style='color:{main_color}; font-size: 24px; margin-bottom: 10px;'>Prediction:</p>", unsafe_allow_html=True)
    st.write(f"<p style='color:{text_color}; font-size: 18px; margin-bottom: 0;'>{label}</p>", unsafe_allow_html=True)
    st.write(f"<p style='color:{text_color}; font-size: 16px; margin-bottom: 10px;'>Confidence: {confidence:.2f}</p>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

# Add a footer with attribution
st.markdown(
    f"""
    <footer style='text-align: center; margin-top: 50px; color: {text_color};'>
        Made with ❤️ by Script Kiddies<br>
    </footer>
    """,
    unsafe_allow_html=True
)