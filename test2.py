
from tkinter import *
from tkinter import filedialog





root = Tk()
root.geometry('350x200')
def browsefunc():
    folderpath = filedialog.askdirectory()
    pathlabel.config(text=folderpath)
    print(str(folderpath))


browsebutton = Button(root, text="Browse", command=browsefunc)
browsebutton.pack()

pathlabel = Label(root)
pathlabel.pack()

btn = Button(root, text="Quit", command=root.quit)

btn.winfo_geometry()

mainloop()