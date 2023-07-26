
from tkinter import *

from pkg_resources import to_filename



miventana= Tk()
miventana.geometry ("650x650")
miventana.title("Simular Credito")
miventana.resizable(True,True)
miventana.config(background="#F3E3E6")

entrada=Entry(miventana,bg="white",fg="black")
entrada.grid(row=1,column=3,padx=100,sticky=W)
img=PhotoImage(file="Fondo.png")
lbl=Label(miventana,image=img).grid(row=5,column=0)
opcion=IntVar()
def opciones():

    if opcion.get() ==1:
        etiqueta.config(text="Ahorro voluntario")
        res=entrada.get()
        med_cuo=Label(miventana,text="Tu Cuota sera de = <Aqui va Vlor cuota"+str(res))
        med_cuo.grid(row=2,column=3)
        med_cuo.configure(font=("Arial",12))
        med_cuo.config(bg="white", fg="#68a7dc")
        
    elif opcion.get() ==2:
        res=entrada.get()*9
        etiqueta.config(text="Credito por Cesantia")

Radiobutton(miventana,text="Ahorro Voluntario",variable=opcion,value=1,command=opciones).grid(row=0,column=0)
Radiobutton(miventana,text="Credito por Cesantia",variable=opcion,value=2,command=opciones).grid(row=0,column=1)

labecredito=Label(miventana,text="Digite el monto ",bg="white",fg="black")
labecredito.grid(row=0,column=3,padx=100,sticky=W)

etiqueta=Label(miventana)
etiqueta.grid(row=1,column=0,columnspan=2)

miventana.mainloop()

