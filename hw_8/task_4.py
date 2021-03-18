import os
from os import listdir
from os import path


def my_listdir(way):
    for subj in listdir(way):
        temp = way + '\\' + subj
        if path.isfile(temp):
            print(path.abspath(temp))
        elif path.isdir(temp):
            print(my_listdir(temp))


my_listdir('D:\Downloads')
