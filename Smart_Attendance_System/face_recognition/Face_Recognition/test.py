import cv2
import os
import numpy as np

# Find current face_train.py directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# From base directory find images_data-set directory
image_dir = os.path.join(BASE_DIR, "images_dataset")

# load har-cascade classifier
face_cascade = cv2.CascadeClassifier("face_recognition/Face_Recognition/cascades/haarcascade_frontalface_default.xml")


def check(undetected_faces, detected_faces, faces, label, file):
    """
    This will find number of detected and undetected faces in images
    :param undetected_faces: undetected faces
    :param detected_faces: detected faces
    :param faces: faces detected in given array of image
    :param label: image folder name
    :param file: actual file (image/frames)
    :return: undetected_faces, detected_faces
    """
    if len(faces) == 0:
        # print("None: ", label, ": ", file)
        undetected_faces += 1
    else:
        print("Detected ", label, ": ", file)
        detected_faces += 1
    return undetected_faces, detected_faces


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


def testing(x_test, y_test):
    """
    This will create data-set
    :return: It will return training and testing data-set
    """
    detected_faces = 0
    undetected_faces = 0
    x_test_dataset = []
    y_test_dataset = []

    length = len(x_test)

    for i in range(length):
        a = x_test[i]
        b = y_test[i]

        # detect faces in image_array (Find region of interest (only face))
        faces = face_cascade.detectMultiScale(a, scaleFactor=1.5, minNeighbors=5)
        # loop through faces
        for (x, y, w, h) in faces:
            # Find pixels of face only with the help of faces("numpy array") form gray image(numpy array)
            # roi is region of interest (face only)
            roi = np.array(a[y:y + h, x:x + w])

            # resize all faces in 150*150 numpy array
            roi = np.resize(roi, [150, 150])

            # append roi to x_features (features)
            x_test_dataset.append(roi)

            # convert id_ (variable) into numpy array
            id_ = np.array(b)

            # append id (numpy array) in y_labels(list)
            y_test_dataset.append(id_)

    # convert x_features list into numpy array
    x_test_dataset = np.array(x_test_dataset)

    # 3d numpy array to 2d array
    num_features, nx, ny = x_test_dataset.shape
    features_dataset_test = x_test_dataset.reshape((num_features, nx * ny))

    # convert y_labels list into numpy array
    label_dataset_test = np.array(y_test_dataset)
    print("Testing Dataset created")
    return features_dataset_test, label_dataset_test
