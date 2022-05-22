# -*- coding: cp1251 -*-
from class_Tovar import Tovar
from class_Basket import Basket
from class_Person import Person
from class_Order import Order
person=Person()
basket=Basket()
tovar1=Tovar("Гематогоген","C ёжиком","Аптека2",49)
tovar2=Tovar("Миг","И голова не болит","Аптека2",120)
tovar3=Tovar("Йод","В карандаше","Аптека2",134)
tovar4=Tovar("Зелёнка","В баночке","Аптека2",37)
tovar5=Tovar("Аскорбиновая кислота","Аскорбинка","Аптека2",29)
tovar6=Tovar("ТераФлю","пачка 10 шт., лимон","Аптека2",350)
qwe=Tovar.serch("Ёж")
for i in range(0,len(qwe)):
    basket.add_tovar(qwe[i])

order=Order(basket)
print(order.price)

