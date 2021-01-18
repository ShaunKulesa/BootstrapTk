from tkinter import *
import os

class toolbar(Frame):
    def __init__(self, parent = None, **kw):
        Frame.__init__(self, parent, **kw)
        self.root = parent
    
    def add_button(self, text="", background="white", foreground="black", bd="0", height=0, side="left"):
        Button(self, text=text, background=background, foreground=foreground, bd=bd, height=height).pack(side=side, fill="x")

class filelist(Listbox):
    def __init__(self, parent = None, **kw):
        Listbox.__init__(self, parent, **kw, bg="#252526", fg="white")
        self.root = parent
    
    def add_files(self, folder=""):
        files = os.listdir(folder)
        print(files)
        for file in files:
            self.insert(1, file)
