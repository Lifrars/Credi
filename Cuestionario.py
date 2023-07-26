

import tkinter
from tkinter import *

class Evalua(tkinter.Toplevel):
    def __init__(self,venta_prin,venta_secu):
        tkinter.Toplevel.__init__(self)
        self.venta_prin=venta_prin
        self.venta_secu=venta_secu
        self.geometry ("800x670")
        self.title("Conceptos")
        self.resizable(0,0)
        self.config(background="white")
        self.iconbitmap("bolsa.ico")
        self.guia=Label(self,text="Evalua tus Conocimientos",font = ("Cambria", 14), bg = "#56CD63", fg = "black", width = "500", height = "2").pack()
        #Pregunta 1
        self.Cuestion1=IntVar()
        self.Cuestion2=IntVar()
        self.Cuestion3=IntVar()
        self.Cuestion4=IntVar()
        self.Cuestion5=IntVar()
        self.Cuestion6=IntVar()
        

 
        
        self.pregu1=Label(self,bg="#7ae2ad",text="1. ¿Qué es una Cesantía?" )
        self.pregu1.place(x=0,y=50)
    
        self.pre1=Radiobutton(self,bg="white",text="Ahorro al que tienes derecho por estar trabajando con un contrato laboral",variable=self.Cuestion1,value=1)
        self.pre1.place(x=10,y=80)

        self.pre2=Radiobutton(self,bg="white",text="Un valor que se la da al conyugue",variable=self.Cuestion1,value=2)
        self.pre2.place(x=10,y=110)

        self.pre3=Radiobutton(self,bg="white",text="Una forma de ahorro en donde inviertes tus criptos",variable=self.Cuestion1,value=3)
        self.pre3.place(x=10,y=140)

        self.pre4=Radiobutton(self,bg="white",text="Un lugar del FNA en donde guardas todos tus ahorros",variable=self.Cuestion1,value=4)
        self.pre4.place(x=10,y=170)

        #Pregunta2 
        
        self.lbl2=Label(self,bg="#7ae2ad",text="¿Qué es el Ahorro Voluntario?").place(x=0,y=200)
        self.preg1=Radiobutton(self,bg="white",text="Una forma de ahorrar nuestro dinero",variable=self.Cuestion2,value=1)
        self.preg1.place(x=10,y=230)

        self.preg2=Radiobutton(self,bg="white",text="Un plan de ahorro mensual que haces de forma voluntaria",variable=self.Cuestion2,value=2)
        self.preg2.place(x=10,y=260)

        self.preg3=Radiobutton(self,bg="white",text="Un plan de ahorro mensual que haces de forma obligatoria ",variable=self.Cuestion2,value=3)
        self.preg3.place(x=10,y=290)
        
        self.preg4=Radiobutton(self,bg="white",text="Es un ahorro que haces durante años para ingresar a un credito",variable=self.Cuestion2,value=4)
        self.preg4.place(x=10,y=320)
       # Pregunta3
        
        self.lbl3=Label(self,bg="#7ae2ad",text="3.Es una prestación social ,que se le da al trabajador bajo un contrato laboral").place(x=0,y=350)
        self.pregu1=Radiobutton(self,bg="white",text="Ahorro Voluntario",variable=self.Cuestion3,value=1)
        self.pregu1.place(x=10,y=380)

        self.pregu2=Radiobutton(self,bg="white",text="Credito Hipotecario",variable=self.Cuestion3,value=2)
        self.pregu2.place(x=10,y=410)

        self.pregu3=Radiobutton(self,bg="white",text="Cesantia",variable=self.Cuestion3,value=3)
        self.pregu3.place(x=10,y=440)
        
        self.pregu4=Radiobutton(self,bg="white",text="Fondo Nacional Ahorro",variable=self.Cuestion3,value=4)
        self.pregu4.place(x=10,y=470)
        #Pregunta#4
        
        self.lbl4=Label(self,bg="#7ae2ad",text="4.¿Qué es un crédito hipotecario").place(x=0,y=500)
        self.pregun1=Radiobutton(self,bg="white",text="Prestamo,que te permite obtener tu vivienda",variable=self.Cuestion4,value=1)
        self.pregun1.place(x=10,y=530)

        self.pregun2=Radiobutton(self,bg="white",text="Un valor que utilizas para fines personales",variable=self.Cuestion4,value=2)
        self.pregun2.place(x=10,y=560)

        self.pregun3=Radiobutton(self,bg="white",text="Una forma de ahorro en el FNA",variable=self.Cuestion4,value=3)
        self.pregun3.place(x=10,y=590)
        
        self.pregun4=Radiobutton(self,bg="white",text="Prestamo de dinero para gastar en muebles",variable=self.Cuestion4,value=4)
        self.pregun4.place(x=10,y=620)
        #Pregunta5
        
        self.lbl5=Label(self,bg="#7ae2ad",text="5.¿Como te puedes afiliar al FNA?").place(x=430,y=50)

        self.pregunt1=Radiobutton(self,bg="white",text="A tráves de un Crédito Personal",variable=self.Cuestion5,value=1)
        self.pregunt1.place(x=440,y=80)

        self.pregunt2=Radiobutton(self,bg="white",text="A tráves de una recomendación",variable=self.Cuestion5,value=2)
        self.pregunt2.place(x=440,y=110)

        self.pregunt3=Radiobutton(self,bg="white",text="A tráves de un Crédito Hipotecario",variable=self.Cuestion5,value=3)
        self.pregunt3.place(x=440,y=140)

        self.pregunt4=Radiobutton(self,bg="white",text="A tráves del Ahorro Voluntario o Crédito por Cesantías",variable=self.Cuestion5,value=4)
        self.pregunt4.place(x=440,y=170)
        #Pregunta6
        
        self.lbl6=Label(self,bg="#7ae2ad",text="6. Una vez afiliado al Fondo Nacional del Ahorro").place(x=430,y=200)
        self.cu1=Radiobutton(self,bg="white",text="Puedes aplicar a un subsidio de vivienda",variable=self.Cuestion6,value=1)
        self.cu1.place(x=440,y=230)

        self.cu2=Radiobutton(self,bg="white",text="Puedes relajarte y no hacer nada ",variable=self.Cuestion6,value=2)
        self.cu2.place(x=440,y=260)

        self.cu3=Radiobutton(self,bg="white",text="Puedes retirar un monto igual al valor de tu vivienda",variable=self.Cuestion6,value=3)
        self.cu3.place(x=440,y=290)
        
        self.cu4=Radiobutton(self,bg="white",text="Puedes acceder a un credito Hipotecario para tu vivienda",variable=self.Cuestion6,value=4)
        self.cu4.place(x=440,y=320)
        #Botones
        self.btn=Button(self,text="Evaluar",command=self.valor)
        self.btn.place(x=500,y=400)
        self.btn.config(bg="#64dd9f",fg="black")
        self.btn=Button(self,text="Borrar Resultado",command=self.elimina)
        self.btn.place(x=550,y=400)
        self.btn.config(bg="#64dd9f",fg="black")
        self.devolver = Button(self, text="Inicio",command=self.volver)
        self.devolver.place(x=700, y=540, width=100, height=40)
        self.devolver.config(bg="#91e7bb", fg="black")
        self.res=0
        self.resultado=0
        
    def valor(self):
        if self.Cuestion1.get()==1:
            self.res=self.res+1
        elif self.Cuestion2.get()==2:
            self.res=self.res+1
        elif self.Cuestion3.get()==3:
            self.res=self.res+1
        elif self.Cuestion4.get()==1:
            self.res=self.res+1
        elif self.Cuestion5.get()==4:
            self.res=self.res+1
        elif self.Cuestion6.get()==4:
            self.res=self.res+1

        if self.res==1:
            self.resultado=self.resultado+0.8
        elif self.res==2:
            self.resultado=self.resultado+1.6
        elif self.res==3:
            self.resultado=self.resultado+2.4
        elif self.res==4:
            self.resultado=self.resultado+3.3
        elif self.res==5:
            self.resultado=self.resultado+4.1
        elif self.res==6:
            self.resultado=self.resultado+5.0
        

        
        
        self.fra=Label(self,text="Resultado= "+str(self.resultado))
        self.fra.place(x=500,y=430)
        self.fra.config(font = ("Cambria", 14),bg = "#56CD63", fg = "black", width = "20", height = "2")

    def elimina(self):
        
        if self.res>0 and self.res<7:

            self.fra.destroy()
            self.res=0
        
            
        
    def volver(self):
        self.venta_prin.update()
        self.venta_prin.deiconify()
        self.destroy()    


        

        
        



