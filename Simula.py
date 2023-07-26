##Crear una instancia de Tk
from tkinter import * 
from turtle import heading, width
miventana= Tk()
miventana.geometry ("1200x1200")
miventana.title("Consulta Terminos")
miventana.resizable(0,0)
miventana.config(background="#F3E3E6")
#Traes Ventana
def Credito():
    ventana_significa=Toplevel()
    ventana_significa.title("Credito")
    ventana_significa.geometry("899x600")
    ventana_significa.resizable(0,0)
    ventana_significa.config(bg='#F5FFFC')
    lbl=Label(ventana_significa,text="Hola").pack()
    bot=Button(ventana_significa,text="Pro")
    bot.place(x=20,y=50,width=300,height=300)

def Cesantia():
    ventana_cesantia=Toplevel()
    ventana_cesantia.title("Cesantia")
    ventana_cesantia.geometry("899x600")
    ventana_cesantia.resizable(0,0)
    ventana_cesantia.config(bg='#F5FFFC')
    lbl=Label(ventana_cesantia,text="Hola").pack()

def Ahorro():
    ventana_ahorro=Toplevel()
    ventana_ahorro.title("aHORRO")
    ventana_ahorro.geometry("899x600")
    ventana_ahorro.resizable(0,0)
    ventana_ahorro.config(bg='#F5FFFC')
    lbl=Label(ventana_ahorro,text="Hola").pack()

def Fondo():
    ventana_fondo=Toplevel()
    ventana_fondo.title("Fondo")
    ventana_fondo.geometry("899x600")
    ventana_fondo.resizable(0,0)
    ventana_fondo.config(bg='#F5FFFC')
    lbl=Label(ventana_fondo,text="Hola").pack()

def vivienda():
    ventana_vivi=Toplevel()
    ventana_vivi.title("Vivienda")
    ventana_vivi.geometry("899x600")
    ventana_vivi.resizable(0,0)
    ventana_vivi.config(bg='#F5FFFC')
    lbl=Label(ventana_vivi,text="Hola").pack()
    framevivi=Frame(ventana_vivi,background="Blue",)
    framevivi.place(x=0,y=0,width=93,height=253)
    btn=Button(framevivi,text="Perro").pack()

def enti():
    ventana_enti=Toplevel()
    ventana_enti.title("Entidad")
    ventana_enti.geometry("899x600")
    ventana_enti.resizable(0,0)
    ventana_enti.config(bg='#F5FFFC')
    lbl=Label(ventana_enti,text="Hola").pack()

#Crear un Frame

btb1=Button(miventana,text="Credito",bg="white",height=1,width=30,command=Credito)
btb1.grid(row=0,column=0,sticky=W,columnspan=2,padx=10,pady=5)
lbl2=Button(miventana,text="Cesantia",bg="white",height=1,width=30,command=Cesantia)
lbl2.grid(row=1,column=0,sticky=W,columnspan=2,padx=10,pady=5)
lbl3=Button(miventana,text="Ahorro Voluntario",bg="white",height=1,width=30,command=Ahorro)
lbl3.grid(row=2,column=0,sticky=W,columnspan=2,padx=10,pady=5)
lbl4=Button(miventana,text="Fondo Nacional del Ahorro",bg="white",height=1,width=30,command=Fondo)
lbl4.grid(row=3,column=0,sticky=W,columnspan=2,padx=10,pady=5)
lbl5=Button(miventana,text="Vivienda",bg="white",height=1,width=30,command=vivienda)
lbl5.grid(row=4,column=0,sticky=W,columnspan=2,padx=10,pady=5)
lbl6=Button(miventana,text="Entidad Financiera",bg="white",height=1,width=30,command=enti)
lbl6.grid(row=5,column=0,sticky=W,columnspan=2,padx=10,pady=5)



miventana.mainloop()
#mostrar funcion 
