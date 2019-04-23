from .Video_to_Image_Split import extraction, rotate
from .face_recognition import choice, choice2
from .fetch import fetching
import shutil
import os
import cv2
from .attendance_camera import cam_attendance

# Find current face_train.py directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# From base directory find images_data-set directory
image_dir = os.path.join(BASE_DIR, ".../media/check_image")


def move(src, dest):
    shutil.move(src, dest)


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


def start_training():
    # create Dataset
    extraction.start_creating_dataset()

    # Create / Rotate images in image dataset
    rotate.rotate()

    # ML Training module call with choice 2 with OPENCV
    # choice2(2)

    # Training with TF
    # choice_tf()


def start_check_image():
    print("CWD: ", os.getcwd())
    for root, dirs, files in os.walk('media/check_image'):
        for file in files:
            if file.endswith("png") or file.endswith("jpg"):
                path, label = get_path_and_label(root, file)
                print("Checking Image: ", path)
                img = cv2.imread(path)

                # move(img, 'face_recognition/Face_Recognition/check_image')
                # print("line 56")
                # Check Image
                choice(3, img)
                os.remove(path)


def fetch_data(roll_no):
    try:
        enrollment_no, name, total_days, total_present_days, precentage = fetching(roll_no)
        return enrollment_no, name, total_days, total_present_days, precentage
    except:
        enrollment_no = 'Not Found'
        name = 'Not Found'
        total_days = 'Not Found'
        total_present_days = 'Not Found'
        precentage = 'Not Found'
        return enrollment_no, name, total_days, total_present_days, precentage


def camera_attendance_start():
    cam_attendance()
