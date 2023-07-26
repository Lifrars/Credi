import tkinter
from tkinter import *
import subprocess

#Importanten preguntar al profe
class Primero(tkinter.Toplevel):
    def __init__(self,venta_prin,venta_secu):
        tkinter.Toplevel.__init__(self)
        self.venta_prin=venta_prin
        self.venta_secu=venta_secu
        self.title("Paso")
        self.geometry("800x300")
        self.resizable(1,1)
        self.config(background="white")
        self.guia=Label(self,text="Primer Paso",font = ("Cambria", 14), bg = "#25aabe", fg = "black", width = "80", height = "2")
        self.guia.place(x=1,y=1)
        self.frame1=Frame(self,bg="#83d87c",width=400,height=200)
        self.frame1.place(x=0,y=50)
        self.frame2=Frame(self,bg="#c1ecbe",width=400,height=200)
        self.frame2.place(x=400,y=50)
        self.lbl1=Label(self,bg="#83d87c",width=50,height=10,text="AFILIARSE POR AHORRO VOLUNTARIO\n-Para aplicar ,lo primero que tendremos que hacer es acercarnos\n a cualquier Fondo Nacional del Ahorro\n-Una vez alli se te preguntara con aspectos relacionados a tu trabajo\ny cuantos ganas cada mes, y cual es el valor que quieras ahorrar\n Realizados los anteriores pasos:\n Se te entregara un documento para tus consignaciones,\nen donde tendras que consignar durante los siguientes 12 meses  ").place(x=10,y=60)
        self.lbl2=Label(self,bg="#c1ecbe",text="AFILIARSE POR CREDITO DE CESANTIAS\nEs un prestacion social a la que tiene derecho todo trabajador con un \ncontrato laboral\nEn primer lugar, donde ejerces tu \ntrabajo le diras a tu empleador que guardes tus cesantias en el \nFondo Nacional del Ahorro").place(x=410,y=80)
        self.btn1=Button(self,bg="#25aabe",width=25,height=3,text="Formulario Unico de Registro",command=self.formular).place(x=300,y=250)
        
        self.devolver = Button(self, text="Inicio",command=self.venta_principal)
        self.devolver.place(x=600, y=250, width=100, height=40)
        self.devolver.config(bg="#91e7bb", fg="black")

    def formular(self):
        path = 'Formulario Unico.pdf'
        subprocess.Popen([path], shell=True)

    def venta_principal(self):
        self.venta_prin.update()
        self.venta_prin.deiconify()
        self.destroy()

    def volver(self):
        self.venta_secu.update()
        self.venta_secu.deiconify()
        self.destroy
        

