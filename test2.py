
from tkinter import *
from tkinter import filedialog
from tkinter.ttk import *
from tkinter import ttk





def browsefunc():
    folderpath = filedialog.askdirectory()
    pathlabel.config(text=folderpath)
    print(str(folderpath))

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


window = Tk()

window.title("Tkinter Test")

window.minsize(640, 400)


chk_state = BooleanVar()

chk_state.set(False)

chk = Checkbutton(window, text='Images', var=chk_state)

chk.grid(column=1, row=1, padx=20, pady=20)


chk1_state = BooleanVar()

chk1_state.set(False)

chk1 = Checkbutton(window, text='Videos', var=chk1_state)

chk1.grid(column=2, row=1, padx=20, pady=20)


chk2_state = BooleanVar()

chk2_state.set(False)

chk2 = Checkbutton(window, text='Audio', var=chk2_state)

chk2.grid(column=3, row=1, padx=20, pady=20)


chk3_state = BooleanVar()

chk3_state.set(False)

chk3 = Checkbutton(window, text='Documents', var=chk3_state)

chk3.grid(column=4, row=1, padx=20, pady=20)

btn = Button(window, text="Quit", command=window.quit)

btn.grid(column=1, row=3, padx=20, pady=20)

window.mainloop()