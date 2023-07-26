from cgitb import text
import tkinter
from tkinter import *
import tkinter as tk
class Vinum(tkinter.Tk):
    def __init__(self):
        super().__init__()
        self.title("VINUM")
        self.geometry("899x600")
        def ctrlEvent(event):
            if(12==event.state and event.keysym=='c' ):
                return
            else:
                return "break"


        readOnlyText = tk.Text(self)
        readOnlyText.insert(1.0,"ABCDEF")
        readOnlyText.bind("<Key>", lambda e: ctrlEvent(e))
        readOnlyText.pack()

     
        self.mainloop()
Vinum()