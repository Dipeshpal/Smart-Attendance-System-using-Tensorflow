import cv2
import os


def split(folder, source_video):
    dir_name = folder
    os.mkdir(dir_name)

    video_name = source_video
    vidcap = cv2.VideoCapture(video_name)
    count = 0
    success = True
    while success:
        success, image = vidcap.read()
        cv2.imwrite(os.path.join(dir_name, "frame%d.jpg" % count), image)
        print('Read a new frame: ', success)
        count += 1
