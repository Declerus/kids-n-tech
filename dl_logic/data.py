import tensorflow as tf
import numpy as np
import os
import matplotlib.pyplot as plt


images=tf.data.Dataset.list_files('//wsl.localhost/Ubuntu/home/jamesd/code/Declerus/kids-n-tech/data/*/*')
for image in images.take(3):
    print(image.numpy())
image_count=len(images)
