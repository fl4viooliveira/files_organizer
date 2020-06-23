
import os
from pathlib import Path

folder_path = "/home/flavio/Projects/FilesOrganizer/test_folder/"
included_extentions = ['.jpg', '.jpeg', '.bmp', '.png', '.gif']
cwd = os.getcwd()

for root, dirs, files in os.walk(folder_path):
    for file in files:
        if file.endswith(tuple(included_extentions)):
            print(os.path.join(root, file))


