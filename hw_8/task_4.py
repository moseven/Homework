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
        elif path.isdir(subj_path):
            folders.append(subj)
            for i in my_listdir(subj_path, flag=False):
                contents.append(i)

    contents.insert(0, (dir_path, folders, files))

    if flag:
        print(contents)
    else:
        return contents
    
