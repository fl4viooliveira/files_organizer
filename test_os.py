# todo - test functionalities

import os
from pathlib import Path

cur_dir = Path.cwd()
print(cur_dir)

path = '/FilesOrganizer/test_folder'
path_empty = '/home/flavio/Projects/FilesOrganizer/empty'

# This method is used to check whether the given path points to an existing file or directory or not.
obj = Path(path)
print(obj.exists())

# This method is used to check whether the given path is a directory or not.
obj2 = Path(path_empty)
print(obj2.is_dir())

# the directory empty or not
dir = os.listdir(path)
dir2 = os.listdir(path_empty)

if len(dir) == 0:
    print("Empty directory")
else:
    print("Not empyt directory")

if len(dir2) == 0:
    print("Empty directory")
else:
    print("Not empyt directory")



print(os.name)
print(os.getcwd())

