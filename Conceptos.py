
import tkinter
from tkinter import *
class Concep(tkinter.Toplevel):
  def __init__(self,ventana_prin):
      tkinter.Toplevel.__init__(self)
      self.venta_prin=ventana_prin
      #self,ventana_sec=ventana_sec
      self.geometry ("1500x650")
      self.title("Conceptos")
      self.resizable(0,0)
      self.state('zoomed')
      self.iconbitmap("bolsa.ico")
      self.attributes("-fullscreen",0)
      self.config(background="#ebf9e9")
      #Frame
      self.frame1=Frame(self,bg="#ebf9e9",width=450,height=350)
      self.frame1.place(x=0,y=0)
      self.frame1.config(cursor="pirate",relief="sunken",bd=2)

      self.frame2=Frame(self,bg="#ebf9e9",width=450,height=350)
      self.frame2.place(x=450,y=0)
      self.frame2.config(cursor="pirate",relief="sunken",bd=2)

      self.frame3=Frame(self,bg="#ebf9e9",width=470,height=350)
      self.frame3.place(x=900,y=0)
      self.frame3.config(cursor="pirate",relief="sunken",bd=2)

      self.frame4=Frame(self,bg="#ebf9e9",width=450,height=350)
      self.frame4.place(x=0,y=350)
      self.frame4.config(cursor="pirate",relief="sunken",bd=2)

      self.frame5=Frame(self,bg="#ebf9e9",width=450,height=350)
      self.frame5.place(x=450,y=350)
      self.frame5.config(cursor="pirate",relief="sunken",bd=2)
                
      self.frame6=Frame(self,bg="#ebf9e9",width=470,height=350)
      self.frame6.place(x=900,y=350)
      self.frame6.config(cursor="pirate",relief="sunken",bd=2)
      #Credito
      self.guia1=Label(self,text="Crédito",font = ("Cambria", 14),relief="sunken",cursor="pirate", bg = "#56CD63", fg = "black",bd=0, width = "45", height = "2").place(x=0,y=0)
      self.guia2=Label(self,text="Ahorro Voluntario",font = ("Cambria", 14),relief="sunken",cursor="pirate", bg = "#56CD63", fg = "black",bd=1, width = "45", height = "2").place(x=450,y=0)
      self.guia3=Label(self,text="Vivienda",font = ("Cambria", 14),relief="sunken",cursor="pirate", bg = "#56CD63", fg = "black",bd=1, width = "47", height = "2").place(x=900,y=0)
      self.guia4=Label(self,text="Entidad Financiera",font = ("Cambria", 14),relief="sunken",cursor="pirate", bg = "#56CD63", fg = "black",bd=1, width = "45", height = "2").place(x=0,y=350)
      self.guia5=Label(self,text="Fondo Nacional del Ahorro",font = ("Cambria", 14),relief="sunken",cursor="pirate", bg = "#56CD63", fg = "black",bd=1, width = "45", height = "2").place(x=450,y=350)
      self.guia6=Label(self,text="Cesantía",font = ("Cambria", 14),relief="sunken",cursor="pirate", bg = "#56CD63", fg = "black",bd=1, width = "47", height = "2").place(x=900,y=350)
      self.lbl1=Label(self,text="Fondo Nacional del Ahorro")

      self.imge1=PhotoImage(file="Credito.png")
      self.lblimge1=Label(self,image=self.imge1,height=170,width=280)#,command=self.traer_concepto)
      self.lblimge1.place(x=80,y=50)
      self.lbl1=Label(self,text="Un crédito es un préstamo de dinero que se da a una persona\ncon el compromiso de que esta devuelva el  valor recibido,\nsumado a un porcentaje de intereses a pagar en un\ntiempo determinado, el cual se define entre el acreedor y el\ndeudor",justify=LEFT)
      self.lbl1.place(x=10,y=220)
      self.lbl1.config(bg="#ebf9e9",font=("Calibri",12))
        
      self.img2=PhotoImage(file="Ahorro.png")
      self.lblimg2=Label(self,image=self.img2,height=135,width=290).place(x=520,y=50)
      self.lbl2=Label(self,text="Plan de ahorro mensual, por un tiempo determinado, que te\nayuda y es requisito previo para conseguir vivienda. A través\n de la suscripción de un contrato, te afilias al FNA\ncomprometiéndote a realizar depósitos de dinero, \npor un valor y tiempo determinado, hasta cumplir la meta\ndel ahorro en el plazo convenido.",justify=LEFT)
      self.lbl2.place(x=460,y=210)
      self.lbl2.config(bg="#ebf9e9",font=("Calibri",12))

      self.img3=PhotoImage(file="Vivienda.png")
      self.lblimg3=Label(self,image=self.img3,height=160,width=280)
      self.lblimg3.place(x=970,y=50)
      self.lbl3=Label(self,text="La vivienda es una edificación cuya principal función es\nofrecer refugio y habitación a las personas, protegiéndolas de las\n inclemencias climáticas y de otras amenazas.\nOtras denominaciones de vivienda son: apartamento,\naposento, casa, domicilio, estancia, hogar",justify=LEFT)
      self.lbl3.place(x=910,y=220)
      self.lbl3.config(bg="#ebf9e9",font=("Calibri",12))

      self.img4=PhotoImage(file="Entidad.png")
      self.lblimg4=Label(self,image=self.img4,height=140,width=270).place(x=70,y=400)
      self.lbl4=Label(self,text="Una entidad financiera es una agrupación cuyo giro es ofrecer\nservicios financieros en el área de la banca, valores y seguros.\n Su oferta considera desde la intermediación, comercialización de\nseguros, créditos y asesoramiento, entre otros.",justify=LEFT)
      self.lbl4.place(x=10,y=550)
      self.lbl4.config(bg="#ebf9e9",font=("Calibri",12))

      self.img5=PhotoImage(file="Fondo.png")
      self.lblimg5=Label(self,image=self.img5,height=140,width=230).place(x=550,y=400)
      self.lbl5=Label(self,text="Institución bancaria colombiana para administrar las cesantías\n de los empleados públicos y trabajadores oficiales;e transformó\n en una empresa Industrial y comercial del Estado, de carácter\n financiero del orden nacional, lo cual le permitió\n ampliar su mercado al sector privado.",justify=LEFT)
      self.lbl5.place(x=460,y=550)
      self.lbl5.config(bg="#ebf9e9",font=("Calibri",12))

      self.img6=PhotoImage(file="Cesantia.png")
      self.lblimg6=Label(self,image=self.img6,height=140,width=230).place(x=1000,y=400)
      self.lbl6=Label(self,text="Una forma de ahorro obligatorio,Es una prestación social en donde\nel empleador de be pagar un adiccional salario ordinario a sus\ntrabajadores que se debe consignar en fondo específico escogido\n por el empleado ",justify=LEFT)
      self.lbl6.place(x=910,y=550)
      self.lbl6.config(bg="#ebf9e9",font=("Calibri",12))
        
      self.devolver = Button(self, text="Volver",command=self.volver)
      self.devolver.place(x=1250, y=650, width=100, height=40)
      self.devolver.config(bg="#61cb51", fg="black")
        
      

  def volver(self):
      self.venta_prin.update()
      self.venta_prin.deiconify()
      self.destroy()
