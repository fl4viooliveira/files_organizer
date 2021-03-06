
import os
import shutil


folder_path = "/home/flavio/Projects/FilesOrganizer/test_folder/"
dest_path = "/home/flavio/Projects/FilesOrganizer/paste_dir/"


def images():
    return [".jpeg", ".jpg", ".tiff", ".gif", ".bmp", ".png", ".bpg", "svg", ".heif", ".psd"]


def videos():
    return [".avi", ".flv", ".wmv", ".mov", ".mp4", ".webm", ".vob", ".mng", ".qt", ".mpg", ".mpeg", ".3gp", ".mkv"]


def audio():
    return [".aac", ".aa", ".aac", ".dvf", ".m4a", ".m4b", ".m4p", ".mp3", ".msv", "ogg", "oga", ".raw",
            ".vox", ".wav", ".wma"]


def documents():
    return [".oxps", ".epub", ".pages", ".docx", ".doc", ".fdf", ".ods", ".odt", ".pwi", ".xsn",
            ".xps", ".dotx", ".docm", ".dox", ".rvg", ".rtf", ".rtfd", ".wpd", ".xls", ".xlsx",
            ".ppt", "pptx", ".txt", ".in", ".out", ".pdf"]


def other():
    return []


def invalid_opt():
    print("Invalid choice")


options = {
    "a": ["Filter Images", images],
    "b": ["Filter Videos", videos],
    "c": ["Filter Audio", audio],
    "d": ["Filter Documents", documents],
    "e": ["Filter Others", other]
}

for option in options:
    print(option + ") " + options.get(option)[0])

choice = input("Please make Your choice: ")

val = options.get(choice)

# take the function from val
f_val = val[1]


def filter():
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(tuple(f_val())):
                fl = [os.path.join(root, file)]
                for i in fl:
                    yield i


def filter_files_and_move():
    filtered_files = filter()
    for i in filtered_files:
        shutil.copy(i, dest_path)
        print(i)


filter_files_and_move()
