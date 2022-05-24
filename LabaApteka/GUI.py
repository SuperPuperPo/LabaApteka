# -*- coding: cp1251 -*-
import tkinter  as tk
from tkinter.tix import TEXT
from class_Tovar import Tovar
from class_Basket import Basket
from class_Person import Person
from class_Order import Order

def button_tovar_delete(tovar):
    basket.delete_tovar(tovar)
    create_basket()

def button_tovar_count_change(tovar,entry_count):
    basket.change_tovar_count(tovar,entry_count)
    create_basket()

def create_person():
    for widget in main_frame.winfo_children():
        widget.destroy()
    
    person_frame=tk.Frame(master=main_frame)
    person_frame.grid(row=0,column=0,padx=5, pady=15, sticky="w")
    labael_name=tk.Label(master=person_frame,text="Имя:")
    labael_name.pack()

    person_frame=tk.Frame(master=main_frame)
    person_frame.grid(row=1,column=0,padx=5, pady=15, sticky="w")
    labael_name=tk.Label(master=person_frame,text="Телефон:")
    labael_name.pack()

    person_frame=tk.Frame(master=main_frame)
    person_frame.grid(row=0,column=2,padx=5, pady=15, sticky="w")
    entry_name=tk.Entry(master=person_frame)
    entry_name.insert(0,person.name)
    entry_name.pack()

    person_frame=tk.Frame(master=main_frame)
    person_frame.grid(row=1,column=2,padx=5, pady=15, sticky="w")
    entry_phone_number=tk.Entry(master=person_frame)
    entry_phone_number.insert(0,person.phone_number)
    entry_phone_number.pack()

    person_frame=tk.Frame(master=main_frame)
    person_frame.grid(row=2,column=0,padx=5, pady=15)
    button_add=tk.Button(master=person_frame,text="Применить",command=lambda:add_person_info(entry_name.get(),entry_phone_number.get()))
    button_add.pack()

def add_person_info(name,number):
    person.add_Name(name)
    print(person.name)
    person.add_phone_number(number)
    print(person.phone_number)






def create_serch():
    serch_string=entry.get()
    tovar_list=Tovar.serch(serch_string)
    for widget in main_frame.winfo_children():
        widget.destroy()
    if tovar_list!=[]:
        tovar_frame=tk.Frame(master=main_frame)
        tovar_frame.grid(row=0,column=0,padx=5, pady=15)
        labael_name=tk.Label(master=tovar_frame,text="Название")
        labael_name.pack()

        tovar_frame=tk.Frame(master=main_frame)
        tovar_frame.grid(row=0,column=1,padx=5, pady=15)
        labael_name=tk.Label(master=tovar_frame,text="Опис.")
        labael_name.pack()

        tovar_frame=tk.Frame(master=main_frame)
        tovar_frame.grid(row=0,column=2,padx=5, pady=15)
        labael_name=tk.Label(master=tovar_frame,text="Цена шт.")
        labael_name.pack()

        tovar_frame=tk.Frame(master=main_frame)
        tovar_frame.grid(row=0,column=3,padx=5, pady=15)
        labael_name=tk.Label(master=tovar_frame,text="Добавить")
        labael_name.pack()

        for i in range (0,len(tovar_list)):
            add_tovar_in_main_frame(tovar_list[i],i+1)
    else:
        tovar_frame=tk.Frame(master=main_frame)
        tovar_frame.grid(row=1,column=0)
        labael_name=tk.Label(master=tovar_frame,text="Ничего не найдено(")
        labael_name.pack()

def create_basket():
    tovar_list=basket.tovars
    tovar_count=basket.tovars_count
    summa=0
    for widget in main_frame.winfo_children():
        widget.destroy()
    if tovar_list!=[]:
        tovar_frame=tk.Frame(master=main_frame)
        tovar_frame.grid(row=0,column=0,padx=5, pady=15)
        labael_name=tk.Label(master=tovar_frame,text="Название")
        labael_name.pack()

        tovar_frame=tk.Frame(master=main_frame)
        tovar_frame.grid(row=0,column=1,padx=5, pady=15)
        labael_name=tk.Label(master=tovar_frame,text="Опис.")
        labael_name.pack()

        tovar_frame=tk.Frame(master=main_frame)
        tovar_frame.grid(row=0,column=2,padx=5, pady=15)
        labael_name=tk.Label(master=tovar_frame,text="Цена шт.")
        labael_name.pack()

        tovar_frame=tk.Frame(master=main_frame)
        tovar_frame.grid(row=0,column=3,padx=5, pady=15)
        labael_name=tk.Label(master=tovar_frame,text="Кол-во")
        labael_name.pack()

        tovar_frame=tk.Frame(master=main_frame)
        tovar_frame.grid(row=0,column=4,padx=5, pady=15)
        labael_name=tk.Label(master=tovar_frame,text="Цена общ.")
        labael_name.pack()

        tovar_frame=tk.Frame(master=main_frame)
        tovar_frame.grid(row=0,column=5,padx=5, pady=15)
        labael_name=tk.Label(master=tovar_frame,text="Изменить")
        labael_name.pack()
 
        tovar_frame=tk.Frame(master=main_frame)
        tovar_frame.grid(row=0,column=6,padx=5, pady=15)
        labael_name=tk.Label(master=tovar_frame,text="Удалить")
        labael_name.pack()

        for i in range (0,len(tovar_list)):
            summa=summa+tovar_list[i].price*tovar_count[i]
            add_basket_in_main_frame(tovar_list[i],tovar_count[i],i+1)

        tovar_frame=tk.Frame(master=main_frame)
        tovar_frame.grid(row=len(tovar_list)+2,column=3,padx=5, pady=20)
        labael_name=tk.Label(master=tovar_frame,text="Итого")
        labael_name.pack()

        tovar_frame=tk.Frame(master=main_frame)
        tovar_frame.grid(row=len(tovar_list)+2,column=4,padx=5, pady=20, sticky="w")
        labael_name=tk.Label(master=tovar_frame,text=str(summa)+"Р.")
        labael_name.pack()

    else:
        tovar_frame=tk.Frame(master=main_frame)
        tovar_frame.grid(row=1,column=0)
        labael_name=tk.Label(master=tovar_frame,text="Корзина пуста(")
        labael_name.pack()

def add_basket_in_main_frame(tovar,count,i):
    tovar_frame=tk.Frame(master=main_frame)
    tovar_frame.grid(row=i,column=0,padx=5, pady=5, sticky="w")
    labael_name=tk.Label(master=tovar_frame,text=tovar.name,justify="left")
    labael_name.pack()
    
    tovar_frame=tk.Frame(master=main_frame)
    tovar_frame.grid(row=i,column=1,padx=5, pady=5, sticky="w")
    labael_desc=tk.Label(master=tovar_frame,text=tovar.desc,justify="left")
    labael_desc.pack()

    tovar_frame=tk.Frame(master=main_frame)
    tovar_frame.grid(row=i,column=2,padx=5, pady=5, sticky="w")
    labael_price=tk.Label(master=tovar_frame,text=str(tovar.price)+"Р.")
    labael_price.pack()

    tovar_frame=tk.Frame(master=main_frame)
    tovar_frame.grid(row=i,column=3,padx=5, pady=5, sticky="w")
    entry_count=tk.Entry(master=tovar_frame)
    entry_count.insert(0,str(count))
    entry_count.pack()

    tovar_frame=tk.Frame(master=main_frame)
    tovar_frame.grid(row=i,column=4,padx=5, pady=5, sticky="w")
    labael_price=tk.Label(master=tovar_frame,text=str(tovar.price*count)+"Р.")
    labael_price.pack()
    
    tovar_frame=tk.Frame(master=main_frame)
    tovar_frame.grid(row=i,column=5,padx=5, pady=5)
    Button_add=tk.Button(master=tovar_frame,text="+",command=lambda:button_tovar_count_change(tovar,entry_count.get()))
    Button_add.pack()

    tovar_frame=tk.Frame(master=main_frame)
    tovar_frame.grid(row=i,column=6,padx=5, pady=5)
    Button_delete=tk.Button(master=tovar_frame,text="X",command=lambda:button_tovar_delete(tovar))
    Button_delete.pack()

    

def add_tovar_in_main_frame(tovar,i):
    
    tovar_frame=tk.Frame(master=main_frame)
    tovar_frame.grid(row=i,column=0,padx=10, pady=5, sticky="w")
    labael_name=tk.Label(master=tovar_frame,text=tovar.name)
    labael_name.pack()

    tovar_frame=tk.Frame(master=main_frame)
    tovar_frame.grid(row=i,column=1,padx=10, pady=5, sticky="w")
    labael_desc=tk.Label(master=tovar_frame,text=tovar.desc)
    labael_desc.pack()

    tovar_frame=tk.Frame(master=main_frame)
    tovar_frame.grid(row=i,column=2,padx=10, pady=5, sticky="w")
    labael_price=tk.Label(master=tovar_frame,text=str(tovar.price)+"Р.")
    labael_price.pack()

    tovar_frame=tk.Frame(master=main_frame)
    tovar_frame.grid(row=i,column=3,padx=10, pady=5)
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
button1= tk.Button(master=frame,text="Профиль",command=lambda:create_person())
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
button3= tk.Button(master=frame,text="Корзина",command=lambda:create_basket())
button3.pack()

frame=tk.Frame(master=window)
frame.grid(row=2,column=1)
main_frame=tk.Frame(master=frame)
main_frame.pack()

window.mainloop()
