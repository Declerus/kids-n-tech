#!/usr/bin/env python
# coding: utf-8

# In[1]:


from tensorflow.keras.applications import ResNet50

# Create an instance of the ResNet50 model
model = ResNet50(weights='imagenet')

# Optional: Print a summary of the model architecture
model.summary()


# In[2]:


import tensorflow as tf
import numpy as np
import os
import matplotlib.pyplot as plt


images=tf.data.Dataset.list_files('/mnt/e/Lewagon_Project/mouse_cleaned/resized_png/mouse/*')
for image in images.take(3):
    print(image)
    
image_count=len(images)
print(image_count)


# In[3]:


import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# Load the image file
image = mpimg.imread("/mnt/e/Lewagon_Project/mouse_cleaned/resized_png/mouse/08WBAV853XST.png")

# Display the image
plt.imshow(image)
plt.axis('off')
plt.show()


# In[4]:


from PIL import Image
import numpy as np
import os

folder_path = "/mnt/e/Lewagon_Project/dummy"  # Replace with the path to your folder

# Get a list of all PNG files in the folder
png_files = [file for file in os.listdir(folder_path) if file.endswith(".png")]

# Iterate over each PNG file
for file_name in png_files:
    # Open the image file
    file_path = os.path.join(folder_path, file_name)
    image = Image.open(file_path)

    # Convert the image to a NumPy array
    image_array = np.array(image)

    # Process the image array as needed
    # ...

    # Print the shape and data type of the array
    print("Array shape:", image_array.shape)
    print("Array data type:", image_array.dtype)
    print(image_array)


# In[5]:


train_size=int(image_count*0.8)

train_ds=images.take(train_size)
test_ds=images.skip(train_size)
def get_label(file_path):
    return tf.strings.split(file_path, os.path.sep)[-2]
# print(get_label(s))
#CODE ENDS

#extract the images
def process_image(file_path):
    labels=get_label(file_path)
    img=tf.io.read_file(file_path)
    img=tf.image.decode_jpeg(img)
    img=tf.image.resize(img,[128,128])
    return labels, img


#ALL LABELS and images
for img,label in train_ds.map(process_image).take(4):
    print(img)
    print(label)
    


# In[6]:


import tensorflow as tf


# Specify the directory containing the images
data_dir = "/mnt/e/Lewagon_Project/dummy"

# Create a TensorFlow dataset from the directory
dataset = tf.keras.utils.image_dataset_from_directory(
    data_dir,
    image_size=(224, 224),
    batch_size=32,
    validation_split=0.2,
    seed=42,
    subset="training"
)



# In[7]:


ds_training = tf.keras.utils.image_dataset_from_directory(
    data_dir,
    labels='inferred',
    label_mode='int',
    class_names=None,
    color_mode='rgb',
    batch_size=32,
    image_size=(256, 256),
    shuffle=True,
    seed=29,
    validation_split=0.2,
    subset='training',
    interpolation='bilinear',
    follow_links=False,
    crop_to_aspect_ratio=False
)
ds_validation = tf.keras.utils.image_dataset_from_directory(
    data_dir,
    labels='inferred',
    label_mode='int',
    class_names=None,
    color_mode='rgb',
    batch_size=32,
    image_size=(256, 256),
    shuffle=True,
    seed=29,
    validation_split=0.2,
    subset='validation',
    interpolation='bilinear',
    follow_links=False,
    crop_to_aspect_ratio=False
)



left_ds, right_ds = tf.keras.utils.split_dataset(ds_validation, left_size=0.5)


# In[8]:


dataset = dataset.prefetch(buffer_size=tf.data.AUTOTUNE)

# Map labels to one-hot encoded format
num_classes = 4 # Number of classes in ImageNet
dataset = dataset.map(lambda x, y: (x, tf.one_hot(y, num_classes)))

# Compile the model
model.compile(
    optimizer='adam',
    loss='categorical_crossentropy', 
    metrics = 'accuracy')

# Train the model

# Evaluate the model
results = model.evaluate(dataset)

print("Evaluation results:")
for metric_name, result in zip(model.metrics_names, results):
    print(f"{metric_name}: {result}")


# In[ ]:


from tensorflow.keras.applications.resnet50 import ResNet50

model = ResNet50(weights='imagenet', include_top=False, input_shape=(224, 224, 3))
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, GlobalAveragePooling2D

# Create a new model instance
new_model = Sequential()

# Add the pre-trained ResNet-50 model as the base
new_model.add(model)

# Add a global average pooling layer to reduce spatial dimensions
new_model.add(GlobalAveragePooling2D())

# Add a fully connected layer for classification with 4 units (one for each class)

