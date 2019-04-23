import cv2
import os
import numpy as np

# Find current face_train.py directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# From base directory find images_data-set directory
image_dir = os.path.join(BASE_DIR, "images_dataset")


def get_path_and_label(root, file):
    """
    This will get the path of image and get the label of image folder
    :param root: root directory
    :param file: folder
    :return: path(actual image), label (folder name)
    """
    # path of image (path is image)
    path = os.path.join(root, file)
    # Grab name of folder / Grab image folder name and replace spaces to - and convert all into lower case
    label = os.path.basename(root).replace(" ", "-").lower()
    return path, label


def image2gray(image):
    """
    This will convert images to gary-scale image
    :param image: input image
    :return: gray-scale image
    """
    # convert images into Gray-scale image
    gary_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # gray_image type is numpy array
    return gary_image


def get_label_id(label, label_ids, current_id):
    """
    This will find labels (all images respected folder name) and create dictionary for all labels
    :param label: folder name
    :param label_ids: dictionary of all labels
    :param current_id: id respected to labels (initially=0)
    :return: label, label_ids, current_id, id_
    """
    # assign id to everyone #It is running for all images (check later)
    if label not in label_ids:
        label_ids[label] = current_id
        current_id += 1
    id_ = label_ids[label]
    return label, label_ids, current_id, id_


def create_dataset():
    """
    This will create data-set
    :return: It will return training and testing data-set
    """
    x_features = []
    y_labels = []
    label_ids = {}
    current_id = 0
    print("Starting dataset creation")
    print("Img Dir: ", image_dir)
    print("CWD: ", os.getcwd())
    # Look into image_dir and loop through all files in all directory under images_dataset
    for root, dirs, files in os.walk(image_dir):
        for file in files:
            if file.endswith("png") or file.endswith("jpg"):
                # print("File: ")

                path, label = get_path_and_label(root, file)

                # Read image
                image = cv2.imread(path)

                # image into gray-scale image
                gary_image = image2gray(image)

                # getting labels and ids of face detected image from frames (images_data-set)
                label, label_ids, current_id, id_ = get_label_id(label, label_ids, current_id)

                roi = np.array(gary_image)
                # append roi to x_features (features)
                x_features.append(roi)
                # convert id_ (variable) into numpy array
                id_ = np.array(id_)
                # append id (numpy array) in y_labels(list)
                y_labels.append(id_)

    # convert x_features list into numpy array
    features_dataset = np.array(x_features)
    print("convert x_features list into numpy array")
    # 3d numpy array to 2d array
    # num_features, nx, ny = x_features.shape
    # features_dataset = x_features.reshape((num_features, nx * ny))

    # convert y_labels list into numpy array
    label_dataset = np.array(y_labels)
    print("convert y_labels list into numpy array")
    return features_dataset, label_dataset

# features_dataset, label_dataset = create_dataset()

# print("Shape: ", features_dataset.shape)
# print("type: ", type(features_dataset))
#
# print("Shape: ", label_dataset.shape)
# print("type: ", type(label_dataset))
