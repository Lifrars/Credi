import tkinter
from tkinter import *
from Segundopaso import Segundo
from primerpaso import Primero
from Cuestionario import Evalua
#from Conceptos import Concep
class Paso(tkinter.Toplevel):

    def __init__(self,venta_prin):
        tkinter.Toplevel.__init__(self)
        self.venta_prin=venta_prin
        self.geometry ("300x200")
        self.title("Pasos")
        self.resizable(1,1)
        self.iconbitmap("bolsa.ico")
        self.config(background="#91e7bb")


#Crear un Frame
        self.lbl1=Button(self,text="Afiliate",bg="white",command=self.ir_venta_dos,height=2,width=30)
        self.lbl1.grid(row=0,column=0,sticky=W,columnspan=2,padx=10,pady=5)
        self.lbl2=Button(self,text="Aplica a un Credito Hipotecario",command=self.ir_venta_tres,bg="white",height=2,width=30)
        self.lbl2.grid(row=1,column=0,sticky=W,columnspan=2,padx=10,pady=5)
        self.lbl4=Button(self,text="Cuestionario",command=self.ir_venta_cuatro,bg="white",height=2,width=30)
        self.lbl4.grid(row=2,column=0,sticky=W,columnspan=2,padx=10,pady=5)
    
#Boton para devolverse
        self.devolverse = Button(self, text="Volver",command=self.volver,)
        self.devolverse.grid(row=2,column=2,sticky=W,columnspan=2,padx=10,pady=5)
        self.devolverse.config(bg="#23BAC4", fg="white")
  # def ir_venta_seis(self):
    #    self.withdraw()
    #    Crud(self.venta_prin,self)
     #   self.destroy()
   # def ir_venta_cinco(self):
   #     self.withdraw()
    #    Concep(self.venta_prin,self)Parametros ,Revisar
     #   self.destroy()
    def ir_venta_cuatro(self):
        self.withdraw()
        Evalua(self.venta_prin,self)
        self.destroy()
        
    def ir_venta_tres(self):
        self.withdraw()
        Segundo(self.venta_prin,self)
        self.destroy()

    def ir_venta_dos(self):
        self.withdraw()
        Primero(self.venta_prin,self)
        self.destroy()

    def volver(self):
        self.venta_prin.update()
        self.venta_prin.deiconify()
        self.destroy()


