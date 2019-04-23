import os
import cv2

# Find current face_train.py directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# From base directory find images_data-set directory
image_dir = os.path.join(BASE_DIR, "../images_dataset")


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


def rotate():
    print("Rotating Images in all Possible way")
    for root, dirs, files in os.walk(image_dir):
        for file in files:
            if file.endswith("png") or file.endswith("jpg"):
                path, label = get_path_and_label(root, file)

                img = cv2.imread(path)

                height, width = img.shape[:2]

                rotation_matrix = cv2.getRotationMatrix2D((width / 2, height / 2), 90, .85)
                rotated_image = cv2.warpAffine(img, rotation_matrix, (width, height))
                file_name = 'new1 ' + file
                path = root
                cv2.imwrite(os.path.join(path, file_name), rotated_image)

                file_name = cv2.imread(os.path.join(path, file_name))
                height, width = img.shape[:2]
                rotated_image = cv2.warpAffine(file_name, rotation_matrix, (width, height))
                file_name = 'new2 ' + file
                cv2.imwrite(os.path.join(path, file_name), rotated_image)

                file_name = cv2.imread(os.path.join(path, file_name))
                height, width = img.shape[:2]
                rotated_image = cv2.warpAffine(file_name, rotation_matrix, (width, height))
                file_name = 'new3 ' + file
                cv2.imwrite(os.path.join(path, file_name), rotated_image)

                file_name = cv2.imread(os.path.join(path, file_name))
                height, width = img.shape[:2]
                rotated_image = cv2.warpAffine(file_name, rotation_matrix, (width, height))
                file_name = 'new4 ' + file
                cv2.imwrite(os.path.join(path, file_name), rotated_image)
