import streamlit as st
from PIL import Image
import torch
import torchvision.transforms as transforms
from torchvision.models import resnet50
import requests

# Load the pre-trained ResNet50 model
#model = resnet50(pretrained=True)
#model.eval()

# Define the transformations to be applied to the uploaded image
#transform = transforms.Compose([
#    transforms.Resize((224, 224)),
#    transforms.ToTensor(),
#    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
#])

# Function to make predictions on the uploaded image
def classify_image(image):
    image = transform(image).unsqueeze(0)
    output = model(image)
    _, predicted_idx = torch.max(output, 1)
    return predicted_idx.item()

# Streamlit app
st.title("Image Classifier App")
st.write("Upload an image and the app will classify it.")

# File upload
uploaded_file = st.file_uploader("Choose an image file", type=["jpg", "jpeg", "png"])

# Display the uploaded image
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    # Make prediction on the uploaded image
    if st.button("Classify"):
        # Convert PIL image to RGB
        image = image.convert("RGB")

        # Classify the image
        predicted_idx = classify_image(image)

        # Get the label for the predicted class (using ImageNet labels)
        response = requests.get("https://raw.githubusercontent.com/anishathalye/imagenet-simple-labels/master/imagenet-simple-labels.json")
        labels = response.json()
        predicted_label = labels[predicted_idx]

        st.write(f"Prediction: {predicted_label}")