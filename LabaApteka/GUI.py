# -*- coding: cp1251 -*-
import tkinter  as tk
from class_Tovar import Tovar
from class_Basket import Basket
from class_Person import Person
from class_Order import Order

def serch(window):
    serch_string=entry.get()
    tovars=Tovar.serch(serch_string)
    if tovars==[]:
        frame=tk.Frame(master=window)
        frame.grid(row=2,column=1)
        label = tk.Label(master=frame,text="�� ������ ������� ������ �� �������!")
        label.pack()

        


tovar1=Tovar("�����������","C ������",49)
tovar2=Tovar("���","� ������ �� �����",120)
tovar3=Tovar("���","� ���������",134)
tovar4=Tovar("������","� �������",37)
tovar5=Tovar("������������ �������","����������",29)
tovar6=Tovar("�������","����� 10 ��., �����",350)


window = tk.Tk()

window.columnconfigure(0, weight=1, minsize=100)
window.columnconfigure(1, weight=3, minsize=200)
window.columnconfigure(2, weight=1, minsize=100)

window.rowconfigure(0, weight=1, minsize=50)
window.rowconfigure(1, weight=1, minsize=50)
window.rowconfigure(2, weight=1, minsize=700)

frame=tk.Frame(master=window)
frame.grid(row=0,column=1)
label = tk.Label(master=frame,text="������ 24")
label.pack()

frame=tk.Frame(master=window)
frame.grid(row=1,column=0)
button1= tk.Button(master=frame,text="�������")
button1.pack()

frame=tk.Frame(master=window)
frame.grid(row=1,column=1)
entry = tk.Entry(master=frame,width=50)
entry.pack(side=tk.LEFT)
entry.pack(padx=5, pady=5)
button2= tk.Button(master=frame,text="�����",command=lambda:serch(window))
button2.pack(side=tk.RIGHT)

frame=tk.Frame(master=window)
frame.grid(row=1,column=2)
button3= tk.Button(master=frame,text="�������")
button3.pack()




window.mainloop()
