import os


directory = "filtered_files"
cwd = os.getcwd()
path = os.path.join(cwd, directory)

os.mkdir(path)
print("Directory '% s' created" % directory)

#TODO: integrate with the main script