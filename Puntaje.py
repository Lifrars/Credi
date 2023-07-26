import tkinter
from tkinter import ttk
from tkinter import *
import sqlite3

class Crud(tkinter.Tk):
	base = 'puntaje.db'
	def edita__valores(self,nuevo_nombre,Nombre,nuevo_punta,Puntaje,nueva_ciudad,Ciudad):
		query='UPDATE punta SET Nombre=?,Ciudad=?,Puntaje=? WHERE Nombre=? AND Ciudad=? AND Puntaje=? '
		parameters=(nuevo_nombre,nueva_ciudad,nuevo_punta,Nombre,Ciudad,Puntaje)
		self.run_query(query,parameters)
		self.edit_wind.destroy()
		self.consulta()

	def Actualizar(self):
		try:
			self.trv.item(self.trv.selection())['text']
		except IndexError as e:
			return
		Nombre=  self.trv.item(self.trv.selection())['values'][1]
		Ciudad=  self.trv.item(self.trv.selection())['values'][2]
		Puntaje= self.trv.item(self.trv.selection())['values'][4]
		self.edit_wind=Toplevel()
		self.edit_wind.title("Actualizar")
		self.edit_wind.geometry("400x400")
		self.edit_wind.iconbitmap("bolsa.ico")
		self.edit_wind.config(background="#4cd17a")

		frame=LabelFrame(self.edit_wind,text="Actualizar Valores", font=("Calibri",21))
		frame.pack(fill="both", expand="yes",padx=20,pady=10)

		Label(frame, text="Nombre Actual",width=15,font=("Calibri",10)).grid(row=2,column=1,padx=10,pady=20)
		Entry(frame, textvariable=StringVar(frame,value = Nombre), state='readonly').grid(row=2,column=2)

		Label(frame,text="Nuevo Nombre",width=15,font=("Calibri",10)).grid(row=3,column=1)
		nuevo_nombre=Entry(frame)
		nuevo_nombre.grid(row=3,column=2)

		Label(frame, text="Puntaje actual",width=15,font=("Calibri",10)).grid(row=4,column=1,padx=10,pady=20)
		Entry(frame, textvariable=StringVar(frame,value = Puntaje), state='readonly').grid(row=4,column=2)

		Label(frame,text="Puntaje nuevo",width=15,font=("Calibri",10)).grid(row=5,column=1)
		nuevo_punta=Entry(frame)
		nuevo_punta.grid(row=5,column=2)

		Label(frame, text="Ciudad Actual",width=15,font=("Calibri",10)).grid(row=6,column=1,padx=10,pady=20)
		Entry(frame, textvariable=StringVar(frame,value = Ciudad), state='readonly').grid(row=6,column=2)

		Label(frame,text="Ciudad Nueva",width=15,font=("Calibri",10)).grid(row=7,column=1)
		nueva_ciudad=Entry(frame)
		nueva_ciudad.grid(row=7,column=2)

		Button(frame,text="Actualizar",command=lambda:self.edita__valores(nuevo_nombre.get(),Nombre,nuevo_punta.get(),Puntaje,nueva_ciudad.get(),Ciudad), width=12,height=2).grid(row=8,column=2, pady=20)


	def Eliminar(self):
		try:
			self.trv.item(self.trv.selection())['text']
		except 	IndexError as e:
			return
		Nombre = self.trv.item(self.trv.selection())['text']
		query='DELETE FROM punta WHERE Nombre = ?'
		self.run_query(query,(Nombre,))
		self.consulta()

	def Agregar(self):
		if self.validation():
			query = "INSERT INTO punta VALUES(?,?,?,?,?)"
			parameters=(self.ent1.get(),self.ent2.get(),self.ent3.get(),self.ent4.get(),self.ent5.get())
			self.run_query(query, parameters)
			self.ent1.delete(0,	END)
			self.ent2.delete(0,	END)
			self.ent3.delete(0,	END)
			self.ent4.delete(0,	END)
			self.ent5.delete(0,	END)
		else:
			print("No se ha guardado")
		self.consulta()

	def validation(self):
		return len(self.ent1.get()) != 0 and len(self.ent2.get()) !=0 and len(self.ent3.get()) !=0 and len(self.ent4.get()) !=0 and len(self.ent5.get()) !=0

	def consulta(self):
		book=self.trv.get_children()
		for element in book:
			self.trv.delete(element)
		query='SELECT Identificacion,Nombre,Ciudad,Edad,Puntaje FROM punta'
		rows=self.run_query(query)
		for row in rows:
			self.trv.insert('',0,text=row[1],values=row)
			
	def run_query(self,query,parameters=()):
		with sqlite3.connect(self.base) as conn:
			cursor=conn.cursor()
			result=cursor.execute(query,parameters)
			conn.commit()
			return result

	def __init__(self,venta_prin):
		tkinter.Toplevel.__init__(self,)
		self.venta_prin = venta_prin
		
		self.title("Guardar tu puntaje")
		self.geometry("900x500")
		self.iconbitmap("bolsa.ico")
		self.resizable(0,0)



		self.frame1=LabelFrame(self,bg='#4cd17a')
		self.frame2=LabelFrame(self,bg="#4cd17a")

		self.frame1.pack(padx=10,pady=10)
		self.frame2.pack(padx=200,pady=0,anchor=NW,fill="x")
		self.frame2.config(height="400")

		self.style = ttk.Style()
		self.style.configure("mystyle.Treeview", highlightthickness=0, bd=0, font=('Calibri', 13))
		self.style.configure("mystyle.Treeview.Heading", font=('Calibri', 20,'bold')) 
		self.style.layout("mystyle.Treeview", [('mystyle.Treeview.treearea', {'sticky': 'nswe'})])

		self.trv=ttk.Treeview(self.frame1,columns=(1,2,3,4,5),show="headings",height="14",style="mystyle.Treeview")

		
		self.frame1.config(height="600")
		self.trv.pack()
		
		self.trv.column("#1", width= 140)
		self.trv.column("#2", width = 200)
		self.trv.column("#3", width =200)
		self.trv.column("#4", width =200)
		self.trv.column("#5", width =200)

		self.trv.heading(1, text="Cédula",anchor=NW)
		self.trv.heading(2, text="Nombre",anchor=NW)
		self.trv.heading(3, text="Ciudad",anchor=NW)
		self.trv.heading(4, text="Edad",anchor=NW)
		self.trv.heading(5, text="Puntaje",anchor=NW)
		

		self.consulta()

		self.lbl1=Label(self.frame2,text="Cédula",fg='black',bg='#62d6bc', width=20)
		self.lbl1.grid(row=0,column=0,padx=5,pady=4)	
		self.ent1=Entry(self.frame2,width=30,)
		self.ent1.grid(row=0,column=1,padx=5,pady=3)	

		self.lbl2=Label(self.frame2,text="Nombre",fg='black',bg='#62d6bc', width=20)
		self.lbl2.grid(row=1,column=0,padx=5,pady=4)	
		self.ent2=Entry(self.frame2,width=30)
		self.ent2.grid(row=1,column=1,padx=5,pady=3)
				
		self.lbl3=Label(self.frame2,text="Ciudad",fg='black',bg='#62d6bc', width=20)
		self.lbl3.grid(row=2,column=0,padx=5,pady=4)
		self.ent3=Entry(self.frame2,width=30)
		self.ent3.grid(row=2,column=1,padx=5,pady=3)

		self.lbl4=Label(self.frame2,text="Edad",fg='black',bg='#62d6bc', width=20)
		self.lbl4.grid(row=3,column=0,padx=5,pady=3)
		self.ent4=Entry(self.frame2,width=30)
		self.ent4.grid(row=3,column=1,padx=5,pady=3)

		self.lbl5=Label(self.frame2,text="Puntaje",fg='black',bg='#62d6bc', width=20)
		self.lbl5.grid(row=4,column=0,padx=5,pady=4)	
		self.ent5=Entry(self.frame2,width=30)
		self.ent5.grid(row=4,column=1,padx=5,pady=3)
		
	



		self.btn1=Button(self.frame2,text="Crear",font=("Calibri",12),fg='black',bg='#62d6bc',command=self.Agregar,width=11)
		self.btn1.grid(row=1,column=5)

		self.btn2=Button(self.frame2,text="Borrar",font=("Calibri",12),fg='black',bg='#62d6bc',command=self.Eliminar,width=11 )
		self.btn2.grid(row=2,column=5)

		self.btn3=Button(self.frame2,text="Actualizar",font=("Calibri",12),fg='black',bg='#62d6bc',command=self.Actualizar,width=11)
		self.btn3.grid(row=3,column=5)

		self.devolverse = Button(self, text="Inicio",font=("Calibri",14), command=self.volver)
		self.devolverse.place(x=750, y=400, width=100, height=40)
		self.devolverse.config(bg="#62d6bc", fg="black")
		
	def volver(self):
		self.venta_prin.update()
		self.venta_prin.deiconify()
		self.destroy()
