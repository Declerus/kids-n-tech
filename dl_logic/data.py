import tensorflow as tf
import numpy as np
import os
import matplotlib.pyplot as plt


# images=tf.data.Dataset.list_files('data/*/*')
images=tf.data.Dataset.list_files('/mnt/c/Users/Jim/Desktop/data/*/*')
for image in images.take(6):
    print(image.numpy())
image_count=len(images)
#########################
print(image_count)

train_size=int(image_count*0.8)

train_ds=images.take(train_size)
test_ds=images.skip(train_size)

print(len(train_ds), len(test_ds))

#extract the labels from subfolders
#CODE STARTS
# s='C:\\Users\\Jim\\Desktop\\data\\Microprocessor\\microprocessor1279.jpg'
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
