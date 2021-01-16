from tkinter import *

class toolbar_frame(Frame):
    def __init__(self, parent = None, **kw):
        Frame.__init__(self, parent, **kw)
        self.root = parent
    
    def add_button(self, text="", background="white", foreground="black", bd="0"):
        Button(self, text=text, background=background, foreground=foreground, bd=bd).pack(side="left")

class toolbar_canvas(Canvas):
    def __init__(self, parent = None, **kw):
        Canvas.__init__(self, parent, **kw)
        self.root = parent
