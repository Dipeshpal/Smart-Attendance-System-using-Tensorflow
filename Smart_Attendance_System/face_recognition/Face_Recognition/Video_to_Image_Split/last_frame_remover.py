import os


def remover(file_name):
    for root, dirs, files in os.walk(file_name):
        i = 0
        for file in files:
            if file.endswith('.jpg'):
                i = i+1
    print(i)
    i = i-1
    os.remove(file_name + '/frame' + str(i)+'.jpg')
