# -*- coding: cp1251 -*-
from class_Tovar import Tovar
from class_Basket import Basket
from class_Person import Person
from class_Order import Order
person=Person()
basket=Basket()
tovar1=Tovar("�����������","C ������","������2",49)
tovar2=Tovar("���","� ������ �� �����","������2",120)
tovar3=Tovar("���","� ���������","������2",134)
tovar4=Tovar("������","� �������","������2",37)
tovar5=Tovar("������������ �������","����������","������2",29)
tovar6=Tovar("�������","����� 10 ��., �����","������2",350)
qwe=Tovar.serch("��")
for i in range(0,len(qwe)):
    basket.add_tovar(qwe[i])

order=Order(basket)
print(order.price)

