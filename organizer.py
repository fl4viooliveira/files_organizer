
import os
from pathlib import Path

folder_path = "/home/flavio/Projects/FilesOrganizer/test_folder/"
included_extentions = ['jpg','jpeg', 'bmp', 'png', 'gif']

with os.scandir(folder_path) as it:
    for entry in it:
        if not entry.name.startswith('.') and entry.is_file():
            print(entry.name)

for root, subdirs, files in os.walk(folder_path):
    print(root, subdirs)

# files_names = [fn for fn in os.listdir(folder_path)
#               if any(fn.endswith(ext) for ext in included_extentions)]
#
# print(files_names)





