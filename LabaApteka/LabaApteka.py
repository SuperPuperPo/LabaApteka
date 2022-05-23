# -*- coding: cp1251 -*-
from class_Tovar import Tovar
from class_Basket import Basket
from class_Person import Person
from class_Order import Order
person=Person()
basket=Basket()
tovar1=Tovar("Гематогоген","C ёжиком",49)
tovar2=Tovar("Миг","И голова не болит",120)
tovar3=Tovar("Йод","В карандаше",134)
tovar4=Tovar("Зелёнка","В баночке",37)
tovar5=Tovar("Аскорбиновая кислота","Аскорбинка",29)
tovar6=Tovar("ТераФлю","пачка 10 шт., лимон",350)
qwe=Tovar.serch("Ёж")
for i in range(0,len(qwe)):
    basket.add_tovar(qwe[i])
tovar1.desc

order=Order(basket)
print(order.price)

from pdoc import text
f=open("class_Basket.md","w")
f.write(text("class_Basket"))
f.close
