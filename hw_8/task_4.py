import os
from os import listdir
from os import path


def my_listdir(dir_path, flag=True):
    contents = []
    folders = []
    files = []
    for subj in listdir(dir_path):
        subj_path = dir_path + '\\' + subj
        if path.isfile(subj_path):
            files.append(subj)
        if path.isdir(subj_path):
            folders.append(subj)
            contents.append(my_listdir(subj_path, flag=False))
    if flag:
        contents.insert(0, (dir_path, folders, files))
        print(contents)
    else:
        return dir_path, folders, files
    
