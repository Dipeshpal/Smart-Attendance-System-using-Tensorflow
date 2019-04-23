import cv2

faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
video_capture = cv2.VideoCapture(0)


def cam_attendance():
    i = 0
    while i != 20:
        # Capture frame-by-frame
        retval, frame = video_capture.read()
        frame = cv2.flip(frame, 1, 0)

        cv2.imwrite('media/check_images/' + 'File ' + str(i) + '.png', frame)
        i = int(i)
        i = i + 1
        print("Save: ", i)
        cv2.waitKey(20)

        # cv2.imshow('Video', frame)

        if i == 20:
            # video_capture.release()
            # cv2.waitKey(20)
            # cv2.destroyAllWindows()
            # cv2.waitKey(20)
            break
