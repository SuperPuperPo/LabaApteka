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
        label = tk.Label(master=frame,text="По вашему запросу ничего не найдено!")
        label.pack()

        


tovar1=Tovar("Гематогоген","C ёжиком",49)
tovar2=Tovar("Миг","И голова не болит",120)
tovar3=Tovar("Йод","В карандаше",134)
tovar4=Tovar("Зелёнка","В баночке",37)
tovar5=Tovar("Аскорбиновая кислота","Аскорбинка",29)
tovar6=Tovar("ТераФлю","пачка 10 шт., лимон",350)


window = tk.Tk()

window.columnconfigure(0, weight=1, minsize=100)
window.columnconfigure(1, weight=3, minsize=200)
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
button2= tk.Button(master=frame,text="Поиск",command=lambda:serch(window))
button2.pack(side=tk.RIGHT)

frame=tk.Frame(master=window)
frame.grid(row=1,column=2)
button3= tk.Button(master=frame,text="Корзина")
button3.pack()




window.mainloop()
