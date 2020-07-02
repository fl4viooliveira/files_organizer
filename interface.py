
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
# v.set(None)


options = {
          "RadioButton 1": "a",
          "RadioButton 2": "b",
          "RadioButton 3": "c",
          "RadioButton 4": "d",
          "RadioButton 5": "e"
}

for (text, value) in options.items():
    Radiobutton(root, text=text, variable=v,
                value=value).pack(side=TOP, ipady=5)

# Created a function that runs every time the button gets clicked (see the command=quitbutton in the Button widget) and gets the value of the button that is selected
def quitbutton():
    print(v.get())
    # master.quit() uncomment this line if you want to close the window after clicking the button

# Changed the function which gets called by changing the word after command=
quit_btn = Button(root, text="Choose", command=quitbutton, width=10)
quit_btn.pack()


quit = ttk.Button( text="Confirm", command=quit)
quit.pack(side="bottom", padx=20, pady=20)

mainloop()