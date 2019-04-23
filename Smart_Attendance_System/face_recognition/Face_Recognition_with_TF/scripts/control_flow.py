import os
from . import attendance_camera
from . import detect
from . import attend


# Find current face_train.py directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# From base directory find images_data-set directory
image_dir = os.path.join(BASE_DIR, "check_image")


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


def start_all_with_capture_image():
    print("start_all_with_capture_image")
    attendance_camera.cam_attendance()
    print("Images Captured")

    # print("CWD: ", os.getcwd())
    for root, dirs, files in os.walk('media/check_images'):
        for file in files:
            if file.endswith("png") or file.endswith("jpeg") or file.endswith("jpg"):
                path, label = get_path_and_label(root, file)
                name, per = detect.control_flow(path)
                print(name)
                roll = name[-12:]
                print("Detected: ", name, " with accuracy: ", per * 100)
                attend.attendance(roll, name, 'p')
                os.remove(path)


def start_all_without_capture_image():
    print("start_all_without_capture_image")
    # attendance_camera.cam_attendance()
    # print("Images Captured")

    # print("CWD: ", os.getcwd())
    for root, dirs, files in os.walk('media/check_images'):
        for file in files:
            if file.endswith("png") or file.endswith("jpeg") or file.endswith("jpg"):
                path, label = get_path_and_label(root, file)
                name, per = detect.control_flow(path)
                roll = name[-12:]
                print("Detected: ", name, " with accuracy: ", per*100)
                attend.attendance(roll, name, 'p')
                os.remove(path)
