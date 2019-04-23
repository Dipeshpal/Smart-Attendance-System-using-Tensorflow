from face_recognition.Face_Recognition import start as st
from face_recognition.Face_Recognition_with_TF.scripts import control_flow as cf

# # With OpenCV Check Image
# def start():
#     st.start_check_image()


# With TF Check Image, Capture image with camera
def start():
    cf.start_all_with_capture_image()


# With TF Check Image, Without capture image (submit image)
def start2():
    cf.start_all_without_capture_image()


# OpenCV Check Image, Capture image with camera
def start_camera_attendance():
    st.camera_attendance_start()
