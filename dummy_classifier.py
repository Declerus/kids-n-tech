import tensorflow as tf 
from tensorflow import keras
import tensorflow_hub as hub
from tensorflow.keras.utils import load_img
from PIL import Image, ImageOps
import cv2
import numpy as np
from io import StringIO, BytesIO
from PIL import Image, ImageOps

df_labels = {0 : 'arborio',
             1 : 'basmati',
             2 : 'ipsala',
             3 : 'jasmine',
             4 : 'karacadag'}

def preprocess_image(image):
    
    if image.shape != (224, 224, 3):
        resized_img = cv2.resize(image, (224, 224))
        resized_img = np.array(resized_img)
        resized_img = resized_img/255.0
        resized_img = np.expand_dims(resized_img, axis=0)
    else:
        resized_img = np.array(image)
        resized_img = resized_img/255.0
        resized_img = np.expand_dims(resized_img, axis=0)
        
    return resized_img

model = tf.keras.models.load_model('rice_model.tf')

def prediction(preproc_image):
    y_pred = model.predict(preproc_image)
    label_indx = np.argmax(y_pred)
    return df_labels[label_indx]






