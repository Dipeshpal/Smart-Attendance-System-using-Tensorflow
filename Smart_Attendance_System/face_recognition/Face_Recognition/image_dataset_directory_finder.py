import os


def find_dir(r):
    try:
        arr = os.listdir('face_recognition/Face_Recognition/images_dataset')
        ans = arr[r].split()
        return ans[0], ans[1]
    except:
        print("Error")
