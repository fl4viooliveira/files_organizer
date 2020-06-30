
from tkinter import *
from tkinter.ttk import *


window = Tk()

window.title("Tkinter Test")

window.geometry('350x200')


chk_state = BooleanVar()

chk_state.set(False)

chk = Checkbutton(window, text='Images', var=chk_state)

chk.grid(column=1, row=1)


chk1_state = BooleanVar()

chk1_state.set(False)

chk1 = Checkbutton(window, text='Videos', var=chk1_state)

chk1.grid(column=2, row=1)


chk2_state = BooleanVar()

chk2_state.set(False)

chk2 = Checkbutton(window, text='Audio', var=chk2_state)

chk2.grid(column=3, row=1)


chk3_state = BooleanVar()

chk3_state.set(False)

chk3 = Checkbutton(window, text='Documents', var=chk3_state)

chk3.grid(column=4, row=1)





btn = Button(window, text="Quit", command=window.quit)

btn.grid(column=1, row=3)



window.mainloop()
