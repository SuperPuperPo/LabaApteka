# -*- coding: cp1251 -*-
import tkinter  as tk
from tkinter.tix import TEXT
from class_Tovar import Tovar
from class_Basket import Basket
from class_Person import Person
from class_Order import Order

def create_serch():
    serch_string=entry.get()
    tovar_list=Tovar.serch(serch_string)
    for widget in main_frame.winfo_children():
        widget.destroy()
    if tovar_list!=[]:
        for i in range (0,len(tovar_list)):
            add_tovar_in_main_frame(tovar_list[i],i)
    else:
        tovar_frame=tk.Frame(master=main_frame)
        tovar_frame.grid(row=1,column=0)
        labael_name=tk.Label(master=tovar_frame,text="Ничего не найдено(")
        labael_name.pack()

def create_basket():
    tovar_list=basket.tovars
    tovar_count=basket.tovars_count
    for widget in main_frame.winfo_children():
        widget.destroy()
    if tovar_list!=[]:
        for i in range (0,len(tovar_list)):
            add_tovar_in_main_frame(tovar_list[i],i)





def add_tovar_in_main_frame(tovar,i):

    tovar_frame=tk.Frame(master=main_frame)
    tovar_frame.grid(row=i,column=0)
    labael_name=tk.Label(master=tovar_frame,text=tovar.name)
    labael_name.pack()

    tovar_frame=tk.Frame(master=main_frame)
    tovar_frame.grid(row=i,column=1)
    labael_desc=tk.Label(master=tovar_frame,text=tovar.desc)
    labael_desc.pack()

    tovar_frame=tk.Frame(master=main_frame)
    tovar_frame.grid(row=i,column=2)
    labael_price=tk.Label(master=tovar_frame,text=str(tovar.price))
    labael_price.pack()

    tovar_frame=tk.Frame(master=main_frame)
    tovar_frame.grid(row=i,column=3)
    Button_add=tk.Button(master=tovar_frame,text="+",command=lambda:basket.add_tovar(tovar))
    Button_add.pack()




        

        

person=Person()
basket=Basket()
tovar1=Tovar("Гематогоген","C ёжиком",49)
tovar2=Tovar("Миг","И голова не болит",120)
tovar3=Tovar("Йод","В карандаше",134)
tovar4=Tovar("Зелёнка","В баночке",37)
tovar5=Tovar("Аскорбиновая кислота","Аскорбинка",29)
tovar6=Tovar("ТераФлю","пачка 10 шт., лимон",350)


window = tk.Tk()

window.columnconfigure(0, weight=1, minsize=100)
window.columnconfigure(1, weight=3, minsize=600)
window.columnconfigure(2, weight=1, minsize=100)

window.rowconfigure(0, weight=1, minsize=50)
window.rowconfigure(1, weight=1, minsize=50)
window.rowconfigure(2, weight=1, minsize=700)

frame=tk.Frame(master=window)
frame.grid(row=0,column=1)
label = tk.Label(master=frame,text="Аптека 24")
label.pack()

frame=tk.Frame(master=window)
frame.grid(row=1,column=0)
button1= tk.Button(master=frame,text="Профиль")
button1.pack()

frame=tk.Frame(master=window)
frame.grid(row=1,column=1)
entry = tk.Entry(master=frame,width=50)
entry.pack(side=tk.LEFT)
entry.pack(padx=5, pady=5)
button2= tk.Button(master=frame,text="Поиск",command=lambda:create_serch())
button2.pack(side=tk.RIGHT)

frame=tk.Frame(master=window)
frame.grid(row=1,column=2)
button3= tk.Button(master=frame,text="Корзина")
button3.pack()

frame=tk.Frame(master=window)
frame.grid(row=2,column=1)
main_frame=tk.Frame(master=frame)
main_frame.pack()










window.mainloop()
