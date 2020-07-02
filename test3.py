
from tkinter import *
from tkinter.ttk import *


master = Tk()
master.geometry("175x200")

# Changed this do StringVar() without anything in it and set the beginning value to 1
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
    Radiobutton(master, text=text, variable=v,
                value=value).pack(side=TOP, ipady=5)

# Created a function that runs every time the button gets clicked (see the command=quitbutton in the Button widget) and gets the value of the button that is selected
def quitbutton():
    print(v.get())
    # master.quit() uncomment this line if you want to close the window after clicking the button

# Changed the function which gets called by changing the word after command=
quit_btn = Button(master, text="Quit", command=quitbutton, width=10)
quit_btn.pack()

master.mainloop()

