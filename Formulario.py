# Inportar tkinter
import tkinter
from tkinter import *
from turtle import width
 
# Manipular los datos y enviar datos
def envia_dato():
  Usuario_info = Usuario.get()
  contraseña_info = contraseña.get()
  Nombre_info = Nombre.get()
  Edad_info = Edad.get()
  print(Usuario_info,"\t", contraseña_info,"\t", Nombre_info,"\t",Edad_info)
 
#  Abrir y escribir mis datos 
  file = open("Registracion.txt", "a")
  file.write(Usuario_info)
  file.write("\t")
  file.write(contraseña_info)
  file.write("\t")
  file.write(Nombre_info)
  file.write("\t")
  file.write(Edad_info)
  file.write("\t")
  file.write("\n")
  file.close()
  print(" Nuevo usuario registrado. Usuario: {} | Nombre: {}   ".format(Usuario_info, Nombre_info))
 
#  Borrar los datos 
  Usuario_entry.delete(0, END)
  contraseña_entry.delete(0, END)
  Nombre_entry.delete(0, END)
  Edad_entry.delete(0, END)

# Crear un instancia de Tk
miformulario = Tk()
miformulario.geometry("650x550")
miformulario.title("Guia para acceder a un credito ")
miformulario.resizable(False,False)
miformulario.config(background = "#213141")
main_title = Label(text = "Formulario Prototipo", font = ("Cambria", 14), bg = "#56CD63", fg = "black", width = "500", height = "2")
main_title.pack()

# Los cuadros de texto
Usuario_label = Label(text = "Usuario", bg = "#FFEEDD")
Usuario_label.place(x = 22, y = 70)
contraseña_label = Label(text = "Contraseña", bg = "#FFEEDD")
contraseña_label.place(x = 22, y = 130)
Nombre_label = Label(text = "Nombre", bg = "#FFEEDD")
Nombre_label.place(x = 22, y = 190)
Edad_label = Label(text = "Edad", bg = "#FFEEDD")
Edad_label.place(x = 22, y = 250)
 
# Obtener la informacion
Usuario = StringVar()
contraseña = StringVar()
Nombre = StringVar()
Edad=StringVar()

 
Usuario_entry = Entry(textvariable = Usuario, width = "40")
contraseña_entry = Entry(textvariable = contraseña, width = "40",  show = "*")
Nombre_entry = Entry(textvariable = Nombre, width = "40")
Edad_entry = Entry (textvariable= Edad,width="40")
 
Usuario_entry.place(x = 22, y = 100)
contraseña_entry.place(x = 22, y = 160)
Nombre_entry.place(x = 22, y = 220)
Edad_entry.place(x= 22,y = 280)
 
# Guardar y borrea informacion
submit_btn = Button(miformulario,text = "Guardarinfo", width = "30", height = "2", command = envia_dato, bg = "#00CD63")
submit_btn.place(x = 22, y = 320)

miformulario.mainloop()