
import tkinter
from tkinter import *


#Importanten preguntar al profe
class Simula(tkinter.Toplevel):

    def __init__(self,venta_prin):
        tkinter.Toplevel.__init__(self)
        self.venta_prin=venta_prin
        self.title("Simula Credito")
        self.geometry("500x400")
        self.resizable(1,1)
        self.config(background="white")
        self.iconbitmap("bolsa.ico")
        self.guia=Label(self,text="Simular tu credito",font = ("Cambria", 14), bg = "#56CD63", fg = "black", width = "50", height = "2")
        self.guia.place(x=1,y=1)

        self.varDes=StringVar(self)
        self.varDes.set('Seleccionar...')
        
        self.opciones=["Vivienda Nueva","Vivienda Usada","Lote para Construccion"]
        self.deslizar=OptionMenu(self, self.varDes, *self.opciones).place(x=40,y=135)

        
        self.labecredito=Label(self,text="Digite el Valor de su Vivienda ",bg="#64dd9f",fg="black",)
        self.labecredito.place(x=300,y=80)
        self.entrada=Entry(self,bg="#d9d9d9",fg="black")
        self.entrada.place(x=300,y=100)

        self.labeaños=Label(self,text="Plazo en años ",bg="#64dd9f",fg="black",)
        self.labeaños.place(x=300,y=130)
        self.años=Entry(self,bg="#d9d9d9",fg="black")
        self.años.place(x=300,y=150)


        

        self.btn1=Button(self,bg="#bdf0d6",text="Simula",width=8,command=self.simular_cred)
        self.btn1.place(x=300,y=170)
        self.btn1=Button(self,bg="#bdf0d6",text="Eliminar",width=8,command=self.destor)
        self.btn1.place(x=365,y=170)            
        self.devolver = Button(self, text="Inicio",command=self.venta_principal)
        self.devolver.place(x=370, y=340, width=100, height=40)
        self.devolver.config(bg="#91e7bb", fg="black")        
        
    def simular_cred(self):
        if (self.varDes.get()=="Vivienda Nueva"):
                res=int(self.entrada.get())
                financia=int(self.entrada.get())*0.8
                cuota=int(self.años.get())*12
                valnetocuota=float((financia)/int(cuota))
                tas=float(12)
                self.lbl1=Label(self,bg="#91e7bb",text="Tu valor de vivienda es de = ")
                self.lbl1.place(x=120,y=200)
                self.lble1=Label(self,text="{:,}".format(res))
                self.lble1.place(x=320,y=200)
                self.lbl2=Label(self,bg="#91e7bb",text="El valor monto a financiar es de = ")
                self.lbl2.place(x=120,y=220)
                self.lble2=Label(self,text="{:,}".format(financia))
                self.lble2.place(x=320,y=220)
                self.lbl3=Label(self,bg="#91e7bb",text="Plazo de años = ")
                self.lbl3.place(x=120,y=240)
                self.lble3=Label(self,text=str(self.años.get()))
                self.lble3.place(x=320,y=240)
                self.lbl4=Label(self,bg="#91e7bb",text="Cuotas = ")
                self.lbl4.place(x=120,y=260)
                self.lble4=Label(self,text= str(cuota))
                self.lble4.place(x=320,y=260)
                self.lbl5=Label(self,bg="#91e7bb",text="Valor Cuotas = ")
                self.lbl5.place(x=120,y=280)
                self.lble5=Label(self,text="{:,}".format(valnetocuota))
                self.lble5.place(x=320,y=280)
                self.lbl6=Label(self,bg="#91e7bb",text="Tasa de interes Anual = ")
                self.lbl6.place(x=120,y=300)
                self.lble6=Label(self,text=str(tas)+"%")
                self.lble6.place(x=320,y=300)           
        else:
            if (self.varDes.get()=="Vivienda Usada"):
                res=int(self.entrada.get())
                financia=int(self.entrada.get())*0.8
                cuota=int(self.años.get())*12
                valnetocuota=float((int(res)-financia)/cuota)
                tas=float(9)
                self.lbl1=Label(self,bg="#91e7bb",text="Tu valor de vivienda es de = ")
                self.lbl1.place(x=120,y=200)
                self.lble1=Label(self,text="{:,}".format(res))
                self.lble1.place(x=320,y=200)
                self.lbl2=Label(self,bg="#91e7bb",text="El valor monto a financiar es de = ")
                self.lbl2.place(x=120,y=220)
                self.lble2=Label(self,text="{:,}".format(financia))
                self.lble2.place(x=320,y=220)
                self.lbl3=Label(self,bg="#91e7bb",text="Plazo de años = ")
                self.lbl3.place(x=120,y=240)
                self.lble3=Label(self,text=str(self.años.get()))
                self.lble3.place(x=320,y=240)
                self.lbl4=Label(self,bg="#91e7bb",text="Cuotas = ")
                self.lbl4.place(x=120,y=260)
                self.lble4=Label(self,text= str(cuota))
                self.lble4.place(x=320,y=260)
                self.lbl5=Label(self,bg="#91e7bb",text="Valor Cuotas = ")
                self.lbl5.place(x=120,y=280)
                self.lble5=Label(self,text="{:,}".format(valnetocuota))
                self.lble5.place(x=320,y=280)
                self.lbl6=Label(self,bg="#91e7bb",text="Tasa de interes Anual = ")
                self.lbl6.place(x=120,y=300)
                self.lble6=Label(self,text=str(tas)+"%")
                self.lble6.place(x=320,y=300)
            else:
                if (self.varDes.get()=="Lote para Construccion"):
                    res=int(self.entrada.get())
                    financia=int(self.entrada.get())*0.85
                    
                    cuota=int(self.años.get())*12
                    valnetocuota=float((financia)/int(cuota))
                    tas=float(10)
                    self.lbl1=Label(self,bg="#91e7bb",text="Tu valor de vivienda es de = ")
                    self.lbl1.place(x=120,y=200)
                    self.lble1=Label(self,text="{:,}".format(res))
                    self.lble1.place(x=320,y=200)
                    self.lbl2=Label(self,bg="#91e7bb",text="El valor monto a financiar es de = ")
                    self.lbl2.place(x=120,y=220)
                    self.lble2=Label(self,text="{:,}".format(financia))
                    self.lble2.place(x=320,y=220)
                    self.lbl3=Label(self,bg="#91e7bb",text="Plazo de años = ")
                    self.lbl3.place(x=120,y=240)
                    self.lble3=Label(self,text=str(self.años.get()))
                    self.lble3.place(x=320,y=240)
                    self.lbl4=Label(self,bg="#91e7bb",text="Cuotas = ")
                    self.lbl4.place(x=120,y=260)
                    self.lble4=Label(self,text= str(cuota))
                    self.lble4.place(x=320,y=260)
                    self.lbl5=Label(self,bg="#91e7bb",text="Valor Cuotas = ")
                    self.lbl5.place(x=120,y=280)
                    self.lble5=Label(self,text="{:,}".format(valnetocuota))
                    self.lble5.place(x=320,y=280)
                    self.lbl6=Label(self,bg="#91e7bb",text="Tasa de interes Anual = ")
                    self.lbl6.place(x=120,y=300)
                    self.lble6=Label(self,text=str(tas)+"%")
                    self.lble6.place(x=320,y=300)

    def destor (self):
        self.lbl1.destroy ()
        self.lbl2.destroy ()
        self.lbl3.destroy ()
        self.lbl4.destroy ()
        self.lbl5.destroy ()
        self.lbl6.destroy()
        self.lble1.destroy ()
        self.lble2.destroy ()
        self.lble3.destroy ()
        self.lble4.destroy ()
        self.lble5.destroy ()
        self.lble6.destroy ()
        self.entrada.delete(0,END)
        self.años.delete(0,END)
    def venta_principal(self):
        self.venta_prin.update()
        self.venta_prin.deiconify()
        self.destroy()


