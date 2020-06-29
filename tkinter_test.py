
from tkinter import *
from tkinter.ttk import *


window = Tk()

window.title("Tkinter Test")

window.geometry('350x200')

chk_state = BooleanVar()

chk_state.set(False)

chk = Checkbutton(window, text='Choose', var=chk_state)

chk.grid(column=1, row=1)

btn = Button(window, text="Click Me")

btn.grid(column=1, row=2)



window.mainloop()
