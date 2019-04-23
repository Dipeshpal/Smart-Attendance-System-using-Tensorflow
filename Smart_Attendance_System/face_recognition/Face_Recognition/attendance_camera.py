import cv2
import sys

faceCascade = cv2.CascadeClassifier("face_recognition/Face_Recognition/cascades/haarcascade_frontalface_default.xml")
video_capture = cv2.VideoCapture(0)


def cam_attendance():
    i = 0
    count = 0
    while count != 50:
        # Capture frame-by-frame
        retval, frame = video_capture.read()
        frame = cv2.flip(frame, 1, 0)

        # Convert to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detect features specified in Haar Cascade
        faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(50, 50)
        )
        print(type(faces))
        # Draw a rectangle around recognized faces
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (50, 50, 200), 2)

            sub_face = frame[y:y + h, x:x + w]
            i = str(i)
            cv2.imwrite('media/check_image/' + 'File ' + i + '.jpg', sub_face)
            i = int(i)
            i = i + 1
            count = count+1
            print("Save: ", count)
            cv2.waitKey(20)

            if count == 50:
                break

        # Display the resulting frame
        cv2.imshow('Video', frame)

        # Exit the camera view
        if cv2.waitKey(1) & 0xFF == ord('q'):
            sys.exit()
