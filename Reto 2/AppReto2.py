import streamlit as st
import tensorflow as tf
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

# Load tokenizer and model
tokenizer = AutoTokenizer.from_pretrained("bert-base-cased")
model = AutoModelForSequenceClassification.from_pretrained("bert-base-cased", num_labels=2)

# Funtion to tokenize data
def tokenize_text(text):
    return tokenizer(text, 
                     max_length=280, 
                     truncation=True, 
                     padding="max_length",
                     return_tensors="pt")

# Function to predict sentiment
def predict_sentiment(text):
    # Tokenize text
    tokenized_input = tokenize_text(text)
    # Get prediction
    outputs = model(**tokenized_input)
    probs = torch.nn.functional.softmax(outputs.logits, dim=-1)
    return probs.detach().numpy()[0]

# Set Streamlit app title and description
st.title("Review Processor")
st.write("Leave us your comments in the box below!")

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

# Add a text area
text = st.text_area("Your review", height=100)

# Add a button
if st.button("Submit"):
    st.write("Your review is being processed...")
    # Get prediction
    probs = predict_sentiment(text)
    # Show prediction
    if probs[1] > probs[0]:
        st.write("Thank you for your kind words! We are glad you enjoyed our service. :)")
    else:
        st.write("We are sorry you did not enjoy our service. We are continuously working to improve. :(")