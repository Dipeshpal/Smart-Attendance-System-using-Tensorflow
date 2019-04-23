import xlrd
from . import video_down
from . import split
from . import last_frame_remover
import os
import shutil
from . import link_genrator


def start_creating_dataset():
    file_loc = "media/sv.xlsx"
    workbook = xlrd.open_workbook(file_loc)
    sh = workbook.sheet_by_index(0)
    no_ro = sh.nrows

    for rol in range(1, no_ro):
        file_name = str(sh.cell_value(rol, 0)) + ' ' + str(sh.cell_value(rol, 1))
        link = str(sh.cell_value(rol, 2))
        link = link_genrator.link_edit(link)
        video_down.dwn_video(link, file_name)
        split.split(file_name, 'videos/' + file_name + '.mp4')
        last_frame_remover.remover(file_name)
        video_delete(file_name)
        move(file_name, 'face_recognition/Face_Recognition_with_TF/tf_files/images')

    os.remove("media/sv.xlsx")


def video_delete(file_name1):
    os.remove('videos/' + file_name1 + '.mp4')


def move(src, dest):
    shutil.move(src, dest)
