from tkinter import *
from tkinter import filedialog
from tkinter.ttk import *
from tkinter import ttk


# path interface
root = Tk()
# root.geometry('350x200')
root.title("Tkinter Dialog Widget")
root.minsize(640, 400)

def browsefunc():
    folderpath = filedialog.askdirectory()
    pathlabel.config(text=folderpath)
    print(str(folderpath))

browsebutton = Button( text="Browse", command=browsefunc)
browsebutton.pack(side="top", padx=20, pady=20)

pathlabel = Label()
pathlabel.pack()

v = StringVar()


quit = ttk.Button( text="Confirm", command=quit)
quit.pack(side="bottom", padx=20, pady=20)

mainloop()



