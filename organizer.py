
import os

folder_path = "/home/flavio/Projects/FilesOrganizer/test_folder"
included_extentions = ['jpg','jpeg', 'bmp', 'png', 'gif']
file_names = [fn for fn in os.listdir(folder_path)
              if any(fn.endswith(ext) for ext in included_extentions)]

print(file_names)




