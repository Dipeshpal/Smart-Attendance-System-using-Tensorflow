import cv2
import numpy as np
from . import attend
from . import image_dataset_directory_finder


def check(clf, img_file):
    # test start
    print("Reading image")
    # print(type(img_file))
    # test = cv2.imread('face_recognition/Face_Recognition/capture_image.jpg')
    test = img_file

    face_cascade = cv2.CascadeClassifier("face_recognition/Face_Recognition/cascades/haarcascade_frontalface_default.xml")

    gray = cv2.cvtColor(test, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)

    ft = []

    for (x, y, w, h) in faces:
        roi = np.array(gray[y:y + h, x:x + w])
        roi = np.resize(roi, [150, 150])
        ft.append(roi)

    ft = np.array(ft)

    try:
        # 3d array to 2d array
        nsamp, nx, ny = ft.shape
        d2_test_dataset = ft.reshape((nsamp, nx * ny))

        prediction_face = clf.predict(d2_test_dataset)
        print("Face: ", prediction_face)

        prediction_face = prediction_face[0]

        # find dir name respected to predicted face
        name, roll = image_dataset_directory_finder.find_dir(prediction_face)

        print("Face Detected: ", name)
        print("Roll Number: ", roll)

        attend.attendance(roll, name, 'p')

        # if prediction_face == 0:
        #     print("Gayyur")
        #     roll_no = 22
        #     name = 'Gayyur'
        #     ans = attend.attendance(roll_no, name, 'p')
        #     print("Ans: ", ans)
        # elif prediction_face == 1:
        #     roll_no = 74
        #     name = 'Totlaney'
        #     attend.attendance(roll_no, name, 'p')
        # else:
        #     print("Dont' know")

    #         Find face folder name roll and call attendance
    except:
        print("Face not found")
