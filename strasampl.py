import os
import cv2
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.utils import shuffle

# Path to the directory of images
path = '/raw/'

# List of labels corresponding to each image
labels = []

# List of image paths
image_paths = []

for label in os.listdir(path):
    label_path = os.path.join(path, label)
    
    # Loop over each image in the subdirectory
    for image_name in os.listdir(label_path):
        image_path = os.path.join(label_path, image_name)
        
        # Load the image using OpenCV
        image = cv2.imread(image_path)
        
        # Append the image and its label to the lists
        image_paths.append(image)
        labels.append(label)

X = np.array(image_paths)
y = np.array(labels)

# Assuming you have a numpy array of images and their corresponding labels
# where X is the numpy array of images and y is the corresponding label
X, y = shuffle(X, y, random_state=42)

# Split the dataset into training and testing sets using a 80:20 split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.35, stratify=y, random_state=42)

# Print the size of the training and testing sets
print("Training Set:", len(X_train))
print("Testing Set:", len(X_test))