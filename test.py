
from tkinter import *
from tkinter import ttk
from tkinter import filedialog



class Root (Tk):
    def __init__(self):
        super(Root, self).__init__()
        self.title("Tkinter Dialog Widget")
        self.minsize(640, 400)
        self.wm_iconbitmap()
        # self.configure(background = '#4D4D4D')

        self.labelFrame = ttk.LabelFrame(self, text="Open a Folder")
        self.labelFrame.grid(column=0, row=1, padx=20, pady=20)

        self.button()


    def button(self):
        self.button = ttk.Button(self.labelFrame, text="Browse a Folder", command=self.fileDialog)
        self.button.grid(column=1, row=1)


    def fileDialog(self):
        self.foldername = filedialog.askdirectory()
        self.label=ttk.Label(self.labelFrame, text="")
        self.label.grid(column=1, row=2)
        self.label.configure(text=self.foldername)



if __name__ == '__main__':
    root = Root()
    root.mainloop()
