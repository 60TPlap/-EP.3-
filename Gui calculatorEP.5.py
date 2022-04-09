from tkinter import *
from tkinter import ttk, messagebox

GUI = Tk()
GUI.title('โปรแกรมคำนวณล็อตตาลี่')
GUI.geometry('700x700')

bg = PhotoImage(file='car.png')

BG = Label(GUI, image=bg)
BG.pack()

L = Label(GUI,text='กรุณากรอกจำนวณล็อตตาลี่',font=(None,20))
L.pack()

v_quantity = StringVar()
E1 = ttk.Entry(GUI, textvariable=v_quantity, font=(None,20))
E1.pack()

def Cal():
	try:
		quan = float(v_quantity.get())
		cale = quan * 80 #80ต่อใบ
		messagebox.showinfo('ราคาทั้งหมด','ราคาล็อตตาลี่ทั้งหมด {} บาท'.format(cale))
		v_quantity.set('1')
	except:
		messagebox.showwarning('กรอกผิด','กรุณากรอกเฉพาะตัวเลขเท่านั้น')
		v_quantity.set('1')
A = ttk.Button(GUI, text='คำนวณ',command=Cal)
A.pack(ipadx=30,ipady=20)

GUI.mainloop()



