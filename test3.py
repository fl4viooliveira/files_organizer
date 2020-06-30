import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import filedialog

# class Application(tk.Frame):
#     def __init__(self, master=None):
#         super().__init__(master)
#         self.master = master
#         self.minsize(640, 400)
#         self.pack()
#         self.create_widgets()
#
#     def create_widgets(self):
#         self.hi_there = tk.Button(self)
#         self.hi_there["text"] = "Hello World\n(click me)"
#         self.hi_there["command"] = self.say_hi
#         self.hi_there.pack(side="top")
#
#         self.quit = tk.Button(self, text="QUIT", fg="red",
#                               command=self.master.destroy)
#         self.quit.pack(side="bottom")
#
#     def say_hi(self):
#         print("hi there, everyone!")
#
#
# root = tk.Tk()
# app = Application(master=root)
# app.mainloop()


class Path (Tk):
    def __init__(self):
        super(Path, self).__init__()
        self.title("Tkinter Dialog Widget")
        self.minsize(640, 400)
        # self.configure(background = '#4D4D4D')

        self.labelFrame = ttk.LabelFrame(self, text="Open a Folder")
        self.labelFrame.grid(column=0, row=1, padx=20, pady=20)

        self.button()


    def button(self):
        self.button = ttk.Button(self.labelFrame, text="Browse a Folder", command=self.folderDialog)
        self.button.grid(column=1, row=1)


    def folderDialog(self):
        self.foldername = filedialog.askdirectory()
        self.label=ttk.Label(self.labelFrame, text="")
        self.label.grid(column=1, row=2)
        self.label.configure(text=self.foldername)

        print(str(self.foldername))

    def button_q(self):
        self.quit = ttk.Button(self, text="QUIT", fg="red", command=self.master.destroy)
        self.quit.pack(side="bottom")


path = Path()
path.mainloop()
