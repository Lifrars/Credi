import tkinter
from tkinter import *
class Ayu(tkinter.Toplevel):
    def __init__(self,venta_prin):
        tkinter.Toplevel.__init__(self)
        self.venta_prin=venta_prin
        self.geometry ("300x150")
        self.title("Ayuda ")
        self.resizable(1,1)
        self.config(background="#ffffff")
        self.iconbitmap("bolsa.ico")
        

        self.lbl2=Label(self,text="Contactenos ")
        self.lbl2.pack(fill="x")
        self.lbl2.config(font=("Calibri",12))
        self.lbl3=Label(self,text="weslyandres2018@gmail.com")
        self.lbl3.pack(fill="x")
        self.lbl3.config(font=("Calibri",12))
        self.lbl4=Label(self,text="Juan121@gmail.com")
        self.lbl4.pack(fill="x")
        self.lbl4.config(font=("Calibri",12))
        self.devolver = Button(self, text="Volver",command=self.volver)
        self.devolver.pack(fill="x")
        self.devolver.config(bg="#91e7bb", fg="black")
    def volver(self):
        self.venta_prin.update()
        self.venta_prin.deiconify()
        self.destroy()
