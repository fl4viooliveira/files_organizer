from tkinter import *
from tkinter import filedialog
from tkinter.ttk import *
from tkinter import ttk


def browsefunc():
    folderpath = filedialog.askdirectory()
    pathlabel.config(text=folderpath)
    print(str(folderpath))


# path interface
root = Tk()
# root.geometry('350x200')
root.title("Tkinter Dialog Widget")
root.minsize(640, 400)

browsebutton = Button(root, text="Browse", command=browsefunc)
browsebutton.pack(side="top", padx=20, pady=20)

pathlabel = Label(root)
pathlabel.pack()

quit = ttk.Button(root, text="Confirm", command=root.quit)
quit.pack(side="bottom", padx=20, pady=20)

mainloop()


# file extention filter


master = Tk()
master.geometry("175x200")

# Tkinter string variable
# able to store any string value
v = StringVar(master, "1")

# Dictionary to create multiple buttons

options = {
          "RadioButton 1" : "1",
          "RadioButton 2" : "2",
          "RadioButton 3" : "3",
          "RadioButton 4" : "4",
          "RadioButton 5" : "5"
}

# Loop is used to create multiple Radiobuttons
# rather than creating each button separately

for (text, value) in options.items():
    Radiobutton(master, text=text, variable=v,
                value=value).pack(side=TOP, ipady=5)
print(options.items())

quit_btn = Button(master, text="Quit", command=master.quit, width=10)
quit_btn.pack()

# Infinite loop can be terminated by
# keyboard or mouse interrupt
# or by any predefined function (destroy())
mainloop()

