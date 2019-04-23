import cv2
import pickle

# load har-cascade classifier
face_cascade = cv2.CascadeClassifier("cascade\haarcascade_frontalface_default.xml")

# recognizer
recognizer = cv2.face.LBPHFaceRecognizer_create()

# read trainer
recognizer.read("trainer.yml")

labels = {}
with open("labels.pickle", 'rb') as f:
    og_labels = pickle.load(f)
    labels = {v: k for k, v in og_labels.items()}

# open window
cap = cv2.VideoCapture(0)

# Continuously capture frame
while(True):
    # capture frame by frame
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BAYER_BG2BGR)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)        # options
    for (x,y,h,w) in frame:
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]

        # recognizer
        id_, conf = recognizer.predict(roi_gray)
        if conf>50:
            print(id_)
            print(labels[id_])

        img_item = "capture_image.png"
        cv2.imwrite(img_item, roi_gray)

        color = (255, 0, 0)
        stroke = 2
        end_cord_x = x+w
        end_cord_y = y+h

        cv2.rectangle(frame, (x, y), (end_cord_x, end_cord_y))

    cv2.imshow("Frame", frame)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

# when everything done release capture
cap.release()
cv2.destroyAllWindows()


