import streamlit as st
import tensorflow as tf
from PIL import Image, ImageOps
import numpy as np
import dummy_classifier
from io import StringIO, BytesIO
from tensorflow.keras.utils import load_img


st.set_option('deprecation.showfileUploaderEncoding', False)

# Streamlit app
st.title("Rice Image Classifier")
st.write("Upload an image of rice.")

# File upload
buffer = st.file_uploader("Choose an image file", type=["jpg", "jpeg", "png"])

# Display the uploaded image
if buffer is not None:
    image = Image.open(buffer)
    st.image(image, caption="Uploaded Image", use_column_width=True)
    image_array = np.array(image)
    #st.write("NumPy array shape:", image_array.shape)
    
    # Make prediction on the uploaded image
    if st.button("Classify"):
        # Preprocess the image
        im = dummy_classifier.preprocess_image(image_array)

        # Make a prediction
        prediction = dummy_classifier.prediction(im)

        st.write(f"Prediction: {prediction}")