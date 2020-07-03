
from tkinter import *
from tkinter import filedialog
from tkinter.ttk import *
import os
import shutil


# path interface
root = Tk()
# root.geometry('350x200')
root.title("Filter Files")
root.minsize(640, 400)

# These global variables will store the selected path and filter.
selected_path = None
selected_filter = None

def browsefunc():
    global selected_path  # Use global variable.
    folderpath = filedialog.askdirectory()
    pathlabel.config(text=folderpath)
    selected_path = str(folderpath)  # Set the selected path.
    print(str(folderpath))


browsebutton = Button( text="Browse", command=browsefunc)
browsebutton.pack(side="top", padx=20, pady=20)

pathlabel = Label()
pathlabel.pack()

v = StringVar()
# v.set(None)


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


for (text, value) in options.items():
    Radiobutton(root, text=text, variable=v,
                value=text).pack(side=TOP, ipady=5)  # Value should be the text (Eg.: a, b) because later you will use this key to get the value from "options" dict."

# Created a function that runs every time the button gets clicked (see the command=quitbutton in the Button widget) and gets the value of the button that is selected
def quitbutton():
    global selected_filter  # Use global variable.
    selected_filter = v.get()  # Set selected filter.
    root.quit()  # Should be destroyed the GUI to run the copy part.
    # master.quit() uncomment this line if you want to close the window after clicking the button

# Changed the function which gets called by changing the word after command=
quit_btn = Button(root, text="Choose", command=quitbutton, width=10)
quit_btn.pack()


mainloop()

print("Path: {}".format(selected_path))
print("Filter: {}".format(selected_filter))

# ---------------------------

# folder_path = "/home/flavio/Projects/FilesOrganizer/test_folder/"
dest_path = "/home/flavio/Projects/FilesOrganizer/paste_dir/"
cwd = os.getcwd()

for option in options:
    print(option + ") " + options.get(option)[0])

val = options.get(selected_filter)

# take the function from val
f_val = val[1]


def filter():
    for root, dirs, files in os.walk(selected_path):
        for file in files:
            print(file)
            if file.endswith(tuple(f_val())):
                fl = [os.path.join(root, file)]
                for i in fl:
                    yield i


def filter_files_and_move():
    filtered_files = filter()
    for i in filtered_files:
        shutil.copy(i, dest_path)
        print("Copied file: {}".format(i))


filter_files_and_move()  # Call the cipying function.