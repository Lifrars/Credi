import tkinter
from tkinter import *
class Segundo(tkinter.Toplevel):
    def __init__(self,venta_prin,venta_secu):
        tkinter.Toplevel.__init__(self)
        self.venta_prin=venta_prin
        self.venta_secu=venta_secu
        self.title("Paso 2")
        self.geometry("800x500")
        self.resizable(0,0)
        self.config(background="white")
        self.guia=Label(self,text="Aplicar a Credito Hipotecario",font = ("Cambria", 14), bg = "#25aabe", fg = "black", width = "80", height = "2")
        self.guia.place(x=1,y=1)
        self.frame2=Frame(self,bg="#c1ecbe",width=800,height=200)
        self.frame2.place(x=0,y=50)
        self.lbl1=Label(self,width=105,height=10,text="Ahora bien ,te encuentras afiliado al FNA\n con un dinero en tu Fondo ya sea de Cesantia o por Ahorro Voluntario,\n Puedes aplicar para un credito Hipotecario,en las siguientes opciones\n-Credito Para Compra de Vivienda Nueva\n-Credito de Compra para Vivienda Usada\n-Construccion en Lote propio")
        self.lbl1.place(x=0,y=45)
        self.lbl1.config(bg="#c1ecbe",font=("Calibri",12))
        
        self.img1=PhotoImage(file="Nueva.png")
        self.lblimg1=Label(self,width=750,height=300,image=self.img1).place(x=0,y=250)
        
        self.devolver = Button(self, text="Inicio",command=self.venta_principal)
        self.devolver.place(x=650, y=250, width=100, height=40)
        self.devolver.config(bg="#91e7bb", fg="black")

    def venta_principal(self):
        self.venta_prin.update()
        self.venta_prin.deiconify()
        self.destroy()
