
import tkinter
from tkinter import *
class Compro(tkinter.Toplevel):

   def __init__(self,venta_prin):
      tkinter.Toplevel.__init__(self)
      self.venta_prin=venta_prin
      self.geometry ("700x500")
      self.title("Compromisos y responsabilidades")
      self.resizable(0,0)
      self.config(background="white")
      self.iconbitmap("bolsa.ico")
      self.frama1=Frame(self,bg="white",width=700,height=350).place(x=0,y=0)
      self.frama2=Frame(self,bg="white",width=700,height=350).place(x=700,y=0)
      self.frama3=Frame(self,bg="white",width=700,height=350).place(x=0,y=350)
      self.frama4=Frame(self,bg="white",width=700,height=350).place(x=700,y=350)
      self.lbl1=Label(self,text="Situación financiera y a tener en cuenta")
      self.lbl1.place(x=200,y=0)
      self.lbl1.configure(bg="#7ae2ad",font=("Cormorant",13))
      self.lbl2=Label(self,text="Plazo, mensualidades y tasa de interés")
      self.lbl2.place(x=200,y=110)
      self.lbl2.configure(bg="#7ae2ad",font=("Cormorant",13))
      self.lbl3=Label(self,text="Historial Crediticio")
      self.lbl3.place(x=250,y=210)
      self.lbl3.configure(bg="#7ae2ad",font=("Cormorant",13))
      self.lbl4=Label(self,text="Capacidad de pago")
      self.lbl4.place(x=250,y=330)
      self.lbl4.configure(bg="#7ae2ad",font=("Cormorant",13))

      self.lbltex=Label(self,bg="white",text="Es recomendable, recurrir a tu crédito solo cuando estes libre de otras deudas, ya que lo mejor\nes procurar que las condiciones de este crédito sean favorables respecto del anterior, es decir,\nuna tasa de interés y un Costo Anual Total (CAT) más bajos, mensualidades más cómodas y\nun plazo tan corto como sea posible.",justify="center")
      self.lbltex.place(x=1,y=30)
      self.lbltex.configure(font=("Cormorant",12))

      self.lbltex1=Label(self,bg="white",text="El plazo se refiere al tiempo que tomará liquidar por completo el monto del préstamo. Por otro lado,\nla tasa de interés es la renta que obtiene la institución financiera por el préstamo y las\nmensualidades es la cantidad que se pagará mes con mes hasta liquidar la deuda.",justify="center")
      self.lbltex1.place(x=1,y=140)
      self.lbltex1.configure(font=("Cormorant",12))

      self.lbltex2=Label(self,bg="white",text="Construir un buen historial crediticio no sólo implica tener acceso a más servicios financieros, \nsino también a mejores tasas de interés y condiciones de crédito en general.\nMantener un récord positivo en este aspecto es un tema de compromiso y responsabilidad\na largo plazo, que se convierte en un factor decisivo para decidir si es el mejor momento\npara obtener un crédito.",justify="center")
      self.lbltex2.place(x=1,y=230)
      self.lbltex2.configure(font=("Cormorant",12))

      self.lbltex3=Label(self,bg="white",text="Antes de solicitar un crédito vale la pena asegurarse de que tendrá capacidad\npara cubrir la deuda en su totalidad en el plazo\nestablecido. Eso significa estar seguro de que tendrá los ingresos necesarios para\npagar oportunamente,considerando todo tipo de posibles eventualidades y emergencias.",justify="center")
      self.lbltex3.place(x=1,y=355)
      self.lbltex3.configure(font=("Cormorant",12))
      self.devolver = Button(self, text="Volver",command=self.volver)
      self.devolver.place(x=500, y=450, width=100, height=40)
      self.devolver.config(bg="#91e7bb", fg="black")

      
   def volver(self):
        self.venta_prin.update()
        self.venta_prin.deiconify()
        self.destroy()
