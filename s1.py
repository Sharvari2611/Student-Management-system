from tkinter import *
from tkinter.messagebox import *
from tkinter.scrolledtext import *
from sqlite3 import *
import matplotlib.pyplot as plt
import bs4
import lxml
import numpy as np
from pandas import DataFrame
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk

global rno, name, marks
def add():
	addst.deiconify()
	root.withdraw()
def add_back():
	root.deiconify()
	addst.withdraw()
def view():
	view_stdata.delete(1.0,END)
	view.deiconify()
	root.withdraw()
	con=None
	try:
		con=connect("student_database.db")
		cur=con.cursor()
		sql="select * from student"
		cur.execute(sql)
		data=cur.fetchall()
		msg="  "
		for d in data:
			msg=msg+"#\nRollno = " + str(d[0]) + ", Name = " + str(d[1]) + ", Marks = " + str(d[2])+ "\n"
		view_stdata.insert(INSERT,msg)
	except Exception as e:
		showerror("Issue",e)
	finally:
		if con is not None:
			con.close()

def view_back():
	root.deiconify()
	view.withdraw()
def update():
	updt.deiconify()
	root.withdraw()
def update_save():
	con =None
	try:
		con=connect("student_database.db")
		print("connected")
		cur=con.cursor()
		sql="update student set name = '%s',marks ='%d' where rno ='%d'"
		s=updt_entRno.get()
		n=updt_entName.get()
		m=updt_entMarks.get()
		if (len(s)==0 and len(n)==0 and len(m)==0):
					showerror("Mistake","Rollno Name and Marks are not entered\nPlease fill the details properly")
					return
		else:
			if len(s)==0:
				showerror("Mistake","Data entered is not proper.\nRollno should not be empty")
				updt_entRno.delete(0,END)
				updt_entName.delete(0,END)
				updt_entMarks.delete(0,END)
				return
			elif not s.isdigit():
				showerror("Mistake","Data entered is not proper.\nRoll no should be integer")
				updt_entRno.delete(0,END)
				updt_entName.delete(0,END)
				updt_entMarks.delete(0,END)
				return
			else:
				rno=int(s)
			if len(n)==0:
				showerror("Mistake","Data entered is not proper.\nName should not be empty")
				updt_entRno.delete(0,END)
				updt_entName.delete(0,END)
				updt_entMarks.delete(0,END)
				return
			elif not n.isalpha(): 
				showerror("Mistake","Data entered is not proper.\nName should contain only alphabets")
				updt_entRno.delete(0,END)
				updt_entName.delete(0,END)
				updt_entMarks.delete(0,END)
				return
			elif len(n) < 2:
				showerror("Mistake","Data entered is not proper.\nEnter proper name")
				updt_entRno.delete(0,END)
				updt_entName.delete(0,END)
				updt_entMarks.delete(0,END)
				return
			else:
				name=str(n)
			if not m.isdigit():
				showerror("Mistake","Data entered is not proper.\nMarks should contain only digits")
				updt_entRno.delete(0,END)
				updt_entName.delete(0,END)
				updt_entMarks.delete(0,END)
				return
			elif  (int(m) < 0) or (int(m) > 100):
				showerror("Mistake","Data entered is not proper.\nPlease enter valid marks between 0-100")
				updt_entRno.delete(0,END)
				updt_entName.delete(0,END)
				updt_entMarks.delete(0,END)
				return		
			else:
				marks=int(m)
			if len(str(rno)) != 0 and len(name) != 0 and len(str(marks)) != 0:
						cur.execute(sql % (name,marks,rno))
						con.commit()		
						if cur.rowcount > 0:
							showinfo("Success","Record updated")
							updt_entRno.delete(0,END)
							updt_entName.delete(0,END)
							updt_entMarks.delete(0,END)
						else:
							showerror("Mistake","Record does not exits")
							updt_entRno.delete(0,END)
							updt_entName.delete(0,END)
							updt_entMarks.delete(0,END)
	except Exception as e:
		showerror("Insertion issue",e)
	finally:
		if con is not None:
			con.close()
			updt_entRno.delete(0,END)
			updt_entName.delete(0,END)
			updt_entMarks.delete(0,END)
			updt_entRno.focus()	
def updt_back():
	root.deiconify()
	updt.withdraw()
def delete():
	dlt.deiconify()
	root.withdraw()
def del_save():
	con =None
	try:
		con=connect("student_database.db")
		cur=con.cursor()
		sql="delete from student where rno = '%d'"
		srno=dlt_entRno.get()
		if len(srno)==0:
			showerror("Mistake","Roll no should not be empty")
			dlt_entRno.delete(0,END)
			dlt_entRno.focus()
			return
		elif not srno.isdigit() :
			showerror("Mistake","Roll no should be integer")
			dlt_entRno.delete(0,END)
			dlt_entRno.focus()
			return
		else:
			rno=int(srno)
		cur.execute(sql % (rno))
		con.commit()
		if cur.rowcount > 0:
			showinfo("success","record deleted")
			dlt_entRno.delete(0,END)
			dlt_entRno.focus()
			return
		else:
			showerror("Mistake","record does not exits")
			dlt_entRno.delete(0,END)
			dlt_entRno.focus()
			return
		view_stdata.delete(DELETE,rno)
	except Exception as e:
		showerror("insertion issue",e)
	finally:
		if con is not None:
			con.close()
		dlt_entRno.delete(0,END)
		dlt_entRno.focus()
		return
def del_back():
	root.deiconify()
	dlt.withdraw()
def graph_back():
	graph.withdraw()
	root.deiconify()
def barchart():
	con=None
	try:
		root.withdraw()
		name,marks=[],[]
		con=connect("student_database.db")
		cur=con.cursor()
		sql="select * from student"
		cur.execute(sql)
		data=cur.fetchall()
		for d in data:
			name.append(str(d[1]))
			marks.append(int(d[2]))
			#print(name)
			#print(marks)
	
		data1 = {'student name':name,'student marks':marks}
		df1 = DataFrame(data1,columns=['student name','student marks'])
		#print(data1)

		global graph
		graph=Toplevel(root)
		graph.title("Bar Chart")
		graph.geometry("850x670+270+20")
	
		figure1 = plt.Figure(figsize=(8,8), dpi=69)
		ax1 = figure1.add_subplot(111)
		bar1 = FigureCanvasTkAgg(figure1,graph)
		bar1.get_tk_widget().pack(pady=5)
		df1 = df1[['student name','student marks']].groupby('student name').sum()
		df1.plot(kind='bar', legend=True,ax=ax1)
		ax1.set_title('Students performance')
		
		graph_lblTy=Label(graph,text="Thank you :)\n Please return to homepage and then exit",font=('arial',13,'bold'))
		graph_btnBack=Button(graph,text="Back to Homepage",font=('arial',13,'bold'),command=graph_back)
	
		graph_lblTy.pack(pady=10)
		graph_btnBack.pack(pady=10)	
	except Exception as e:
			graph.withdraw()	
			showerror("Error","Bar chart cannot be displayed.\nThere are no records stored.\nPlease store the records first")
			root.deiconify()
	finally:
		if con is not None:
				con.close()
		

def save_student():
	con =None
	try:
		con=connect("student_database.db")
		cur=con.cursor()
		sql="insert into student values('%d','%s','%d')"
		s=addst_entRno.get()
		n=addst_entName.get()
		m=addst_entMarks.get()
		if (len(s)==0 or len(n)==0 or len(m)==0):
					showerror("Mistake","Rollno,Name or Marks are not entered\nPlease enter the details first")
					return
		else:
			if len(s)==0:
				showerror("Mistake","Data entered is not proper.\nRoll no cannot be empty")
				addst_entRno.delete(0,END)
				addst_entName.delete(0,END)
				addst_entMarks.delete(0,END)
				return
			elif not s.isdigit():
				showerror("Mistake","Data entered is not proper.\nRoll no should be integer")
				addst_entRno.delete(0,END)
				addst_entName.delete(0,END)
				addst_entMarks.delete(0,END)
				return
			else:
				rno=int(s)
			if len(n)==0:
				showerror("Mistake","Data entered is not proper.\nName should not be empty")
				addst_entRno.delete(0,END)				
				addst_entName.delete(0,END)
				addst_entMarks.delete(0,END)
				return
			elif not n.isalpha():
				showerror("Mistake","Data entered is not proper.\nName should contain only alphabets")
				addst_entRno.delete(0,END)
				addst_entName.delete(0,END)
				addst_entMarks.delete(0,END)
				return
			elif len(n) < 2 :
				showerror("Mistake","Invalid name.\nPlease enter a proper name")
				addst_entRno.delete(0,END)
				addst_entName.delete(0,END)
				addst_entMarks.delete(0,END)
				return		
			else:	
				name=n
			if not m.isdigit():
				showerror("Mistake","Data entered is not proper.\nMarks should contain only digits")	
				addst_entRno.delete(0,END)
				addst_entName.delete(0,END)
				addst_entMarks.delete(0,END)
				return		
			elif  (int(m) <= 0) or (int(m) >= 100):
				showerror("Mistake","Please enter valid marks between 0-100")
				addst_entRno.delete(0,END)
				addst_entName.delete(0,END)
				addst_entMarks.delete(0,END)
				return				
			else:	
				marks=int(m)
				if len(str(rno))== 0 and len(n) == 0 and len(str(m))== 0:
					showerror("Mistake","Roll no, name and marks cannot be empty")

				if len(str(rno))!= 0 and len(n) != 0 and len(str(m))!= 0:
						cur.execute(sql % (rno,name,marks))
						con.commit()
						showinfo("success","Row Inserted")
		
	except Exception as e:
			con.rollback()
			showerror("Issue","Roll no already exists")
	finally:
			if con is not None:
				con.close()
			addst_entRno.delete(0,END)
			addst_entName.delete(0,END)
			addst_entMarks.delete(0,END)
			addst_entRno.focus()

root=Tk()
root.title("Student managment system")
root.geometry("970x670+200+20")

def on_close():
	if askokcancel("Quit","Do u want to quit ???"):
		con=connect("student_database.db")
		print("connected")
		cur=con.cursor()
		sql="delete from student"
		cur.execute(sql)
		con.commit()	
		root.destroy()
root.protocol("WM_DELETE_WINDOW",on_close)	

import socket
import requests
try:
	google = ("www.google.com", 80 )
	socket.create_connection(google)

	city =str("mumbai")
	a1 = "http://api.openweathermap.org/data/2.5/weather?units=metric"
	a2 = "&appid=c6e315d09197cec231495138183954bd"
	a3 = "&q=" + city 

	web_address = a1 + a2 + a3
	res1 = requests.get(web_address)

	data = res1.json()
	print("temperature :",data['main']['temp'])
	temp=data['main']['temp']

	res2=requests.get("https://www.brainyquote.com/quote_of_the_day")
	
	s=bs4.BeautifulSoup(res2.text,'lxml')

	data=s.find('img',{"class":"p-qotd"})
		
	quote=data['alt']

except OSError as e:
	print("issue ", e)

btnAdd=Button(root,text="Add",width=15,font=('arial',18,'bold'),command=add)
btnView=Button(root,text="View",width=15,font=('arial',18,'bold'),command=view)
btnUpdate=Button(root,text="Update",width=15,font=('arial',18,'bold'),command=update)
btnDelete=Button(root,text="Delete",width=15,font=('arial',18,'bold'),command=delete)
btnShowChart=Button(root,text="Show Chart",width=15,font=('arial',18,'bold'),command=barchart)
lblLocTemp=Label(root,text=" Location : Mumbai "+" & "+" Temperature : " + str(temp),width=37,font=('arial',15),relief="ridge",bd=3)
lblQuote=Label(root,width=90,text="'''"+str(quote)+"'''",font=('arial',15,'italic','bold'),bd=5)

btnAdd.pack(pady=15)
btnView.pack(pady=15)
btnUpdate.pack(pady=15)
btnDelete.pack(pady=15)
btnShowChart.pack(pady=15)
lblLocTemp.pack(pady=15)
lblQuote.pack(pady=15)

#ADD STUDENT WINDOW

addst=Toplevel(root)
addst.title("Add Student")
addst.geometry("850x600+270+45")

addst_lblRno=Label(addst,text="Enter Roll no :",font=('arial',18,'bold'))
addst_lblName=Label(addst,text="Enter Name :",font=('arial',18,'bold'))
addst_lblMarks=Label(addst,text="Enter Marks :",font=('arial',18,'bold'))
addst_entRno=Entry(addst,bd=5,font=('arial',18,'bold'))
addst_entName=Entry(addst,bd=5,font=('arial',18,'bold'))
addst_entMarks=Entry(addst,bd=5,font=('arial',18,'bold'))
addst_btnSave=Button(addst,text="Save",font=('arial',18,'bold'),command=save_student)
addst_btnBack=Button(addst,text="Back",font=('arial',18,'bold'),command=add_back)

addst_lblRno.pack(pady=15)
addst_entRno.pack(pady=15)
addst_lblName.pack(pady=15)
addst_entName.pack(pady=15)
addst_lblMarks.pack(pady=15)
addst_entMarks.pack(pady=15)
addst_btnSave.pack(pady=15)
addst_btnBack.pack(pady=15)

addst.withdraw()

#VIEW STUDENT WINDOW

view=Toplevel(root)
view.title("View Student database")
view.geometry("850x600+270+45")

view_stdata=ScrolledText(view,width=35,height=15,font=('arial',14,'bold'))
view_btnback=Button(view,text="Back",font=('arial',18,'bold'),command=view_back)

view_stdata.pack(pady=15)
view_btnback.pack(pady=15)
view.withdraw()

#UPDATE STUDENT WINDOW

updt=Toplevel(root)
updt.title("Update Student Database")
updt.geometry("850x600+270+45")

updt_lblRno=Label(updt,text="Enter Roll no :",font=('arial',18,'bold'))
updt_lblName=Label(updt,text="Enter Name :",font=('arial',18,'bold'))
updt_lblMarks=Label(updt,text="Enter Marks :",font=('arial',18,'bold'))
updt_entRno=Entry(updt,bd=5,font=('arial',18,'bold'))
updt_entName=Entry(updt,bd=5,font=('arial',18,'bold'))
updt_entMarks=Entry(updt,bd=5,font=('arial',18,'bold'))
updt_btnSave=Button(updt,text="Save",font=('arial',18,'bold'),command=update_save)
updt_btnBack=Button(updt,text="Back",font=('arial',18,'bold'),command=updt_back)

updt_lblRno.pack(pady=15)
updt_entRno.pack(pady=15)
updt_lblName.pack(pady=15)
updt_entName.pack(pady=15)
updt_lblMarks.pack(pady=15)
updt_entMarks.pack(pady=15)
updt_btnSave.pack(pady=15)
updt_btnBack.pack(pady=15)

updt.withdraw()

#DELETE WINDOW

dlt=Toplevel(root)
dlt.title("Delete a Student")
dlt.geometry("850x600+270+45")

dlt_lblRno=Label(dlt,text="Enter Roll no:",font=('arial',18,'bold'))
dlt_entRno=Entry(dlt,bd=5,font=('arial',18,'bold'))
dlt_btnSave=Button(dlt,text="Save",font=('arial',18,'bold'),command=del_save)
dlt_btnBack=Button(dlt,text="Back",font=('arial',18,'bold'),command=del_back)

dlt_lblRno.pack(pady=15)
dlt_entRno.pack(pady=15)
dlt_btnSave.pack(pady=15)
dlt_btnBack.pack(pady=15)

dlt.withdraw()

root.mainloop()

