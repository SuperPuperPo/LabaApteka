# -*- coding: cp1251 -*-
from class_Tovar import Tovar
from class_Basket import Basket
from class_Person import Person
from class_Order import Order
person=Person()
basket=Basket()
tovar1=Tovar("�����������","C ������",49)
tovar2=Tovar("���","� ������ �� �����",120)
tovar3=Tovar("���","� ���������",134)
tovar4=Tovar("������","� �������",37)
tovar5=Tovar("������������ �������","����������",29)
tovar6=Tovar("�������","����� 10 ��., �����",350)
qwe=Tovar.serch("��")
for i in range(0,len(qwe)):
    basket.add_tovar(qwe[i])
tovar1.desc

order=Order(basket)
print(order.price)

from pdoc import text
f=open("class_Basket.md","w")
f.write(text("class_Basket"))
f.close
