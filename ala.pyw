import tkinter
from tkinter import *
from Conceptos import Concep
from Pagina_pasos import Paso
from Compromisos import Compro
from Puntaje import Crud
from Ayuda import Ayu
from defsimula import Simula
class Ventana(tkinter.Tk):
        def __init__(self):

                super().__init__()
                
                self.geometry ("1500x700")
                self.title("Pagina Principal")
                self.resizable(0,0)
                self.state('zoomed')
                self.config(background="#F3E3E6")
                self.iconbitmap("bolsa.ico")
                
#Crear Frame
                self.frame1=Frame(self,bg="white",width=450,height=350)
                self.frame1.place(x=0,y=0)
                self.frame1.config(cursor="pirate",relief="sunken",bd=2)

                self.frame2=Frame(self,bg="white",width=450,height=350)
                self.frame2.place(x=450,y=0)
                self.frame2.config(cursor="pirate",relief="sunken",bd=2)

                self.frame3=Frame(self,bg="white",width=470,height=350)
                self.frame3.place(x=900,y=0)
                self.frame3.config(cursor="pirate",relief="sunken",bd=2)

                self.frame4=Frame(self,bg="white",width=450,height=350)
                self.frame4.place(x=0,y=350)
                self.frame4.config(cursor="pirate",relief="sunken",bd=2)

                self.frame5=Frame(self,bg="white",width=450,height=350)
                self.frame5.place(x=450,y=350)
                self.frame5.config(cursor="pirate",relief="sunken",bd=2)
                
                self.frame6=Frame(self,bg="white",width=470,height=350)
                self.frame6.place(x=900,y=350)
                self.frame6.config(cursor="pirate",relief="sunken",bd=2)

                self.img1=PhotoImage(file="Imagenin2-PhotoRoom.png")
                self.lblimg1=Button(self,image=self.img1,height=180,width=290,command=self.traer_concepto)
                self.lblimg1.place(x=520,y=30)
       # self.btn1.place(x=150,y=10)
                self.img2=PhotoImage(file="Imagen3-PhotoRoom.png")
                self.lblimg2=Button(self,image=self.img2,height=180,width=290,command=self.trae_crud)
                self.lblimg2.place(x=970,y=30)

       # self.btn2.place(x=000,y=000)
                self.img3=PhotoImage(file="Imagen4.png")
                self.lblimg3=Button(self,image=self.img3,command=self.traer_simula,height=180,width=290).place(x=70,y=380)
 
                self.img4=PhotoImage(file="Imagen5.png")
                self.lblimg4=Button(self,image=self.img4,height=180,width=290,command=self.traer_compro).place(x=520,y=380)
                self.img5=PhotoImage(file="Imagen6.png")
                self.lblimg5=Button(self,image=self.img5,height=180,width=290,command=self.traer_ayuda).place(x=970,y=380)
       # self.btn4.place(x=000,y=400)
                self.img=PhotoImage(file="imagen1.png")
                self.lblimg=Button(self,image=self.img,height=180,width=290,command=self.traer_venta).place(x=70,y=30)

                
                self.cerrarvent = Button(self, text="Salir",command=self.salir)
                self.cerrarvent.place(x=1200, y=600, width=100, height=40)
                self.cerrarvent.config(bg="red", fg="white")  
#Cajas de texto en pantalla              
                self.lbl1=Label(self,bg="white",text="Guía paso a paso ",font=("Cambria",12))
                self.lbl1.place(x=150,y=220)
                self.lblE1=Label(self,text="Bienvenido, está es nuestra guía paso a paso ,encontraras\n como ingresar a un crédito por medio de Ahorro Voluntario\n o por Cesantías",justify=CENTER)
                self.lblE1.config(bg="white",font=("Calibri",12))
                self.lblE1.place(x=20,y=250)

                self.lbl2=Label(self,bg="white",text="Concepto ",font=("Cambria",12))
                self.lbl2.place(x=630,y=220)
                self.lble2=Label(self,text="Aquí encontraras algunos de los conceptos que necesitas\n atender ,para aprender a ingresar a un crédito para\n tu vivienda",justify=CENTER)
                self.lble2.place(x=480,y=250)
                self.lble2.config(bg="white",font=("Calibri",12))

                self.lbl3=Label(self,bg="white",text="Guarda tu puntaje ",font=("Cambria",12))
                self.lbl3.place(x=1050,y=220)
                self.lble3=Label(self,text="Aquí podrás guardar tu puntaje ,y compararlo\n con otras personas",justify=CENTER)
                self.lble3.place(x=970,y=250)
                self.lble3.config(bg="white",font=("Calibri",12))

                self.lbl4=Label(self,bg="white",text="Simular de Credito ",font=("Cambria",12))
                self.lbl4.place(x=140,y=570)
                self.lble4=Label(self,text="Simula tu crédito, para hacerte una idea\n de las finanzas y recursos que tendrás que manejar",justify=CENTER)
                self.lble4.place(x=40,y=610)
                self.lble4.config(bg="white",font=("Calibri",12))

                self.lbl5=Label(self,bg="white",text="Compromisos y responsabilidades ",font=("Cambria",12))
                self.lbl5.place(x=550,y=570)
                self.lbl5=Label(self,text="Al ingresar a un crédito ,hay cosas que se deben de tomar\n en cuenta ,a continuación veras las sugerencias\npara ingresar a tu crédito",justify=CENTER)
                self.lbl5.place(x=480,y=610)
                self.lbl5.config(bg="white",font=("Calibri",12))

                self.lbl6=Label(self,bg="white",text="Ayuda ",font=("Cambria",12))
                self.lbl6.place(x=1080,y=570)
                self.mainloop()
        

        def trae_crud(self):
                self.withdraw()
                Crud(self)
        def traer_venta (self):
                self.withdraw()
                Paso(self)

        def traer_compro (self):
                self.withdraw()
                Compro(self)

        def traer_concepto (self):
                self.withdraw()
                Concep(self)
        def traer_ayuda(self):
                self.withdraw()
                Ayu(self)
        def traer_simula(self):
                self.withdraw()
                Simula(self)

        def salir (self):
                self.destroy()




#Como hacer hacer un objeto para guardar el texto.que no sea Label
#ScrollRab 
#Interfaz que manejo 

Ventana()