# -*- coding: cp1251 -*-
import pytest
import class_Tovar 
import class_Basket 
import class_Person 
from class_Tovar import Tovar
from class_Basket import Basket
from class_Person import Person

def test_tovar_init():
    tovar1=Tovar("�����������","C ������",49)
    x=tovar1.desc
    assert x=="C ������"

def test_tovar_serch():
    tovar1=Tovar("�����������","C ������",49)
    tovar2=Tovar("���","� ������ �� �����",120)

    tovar6=Tovar("�������","����� 10 ��., �����",350)
    x=Tovar.serch("��")
    assert x[0].desc=="C ������"

def test_basket_init():
    basket=Basket()
    x=basket.tovars
    assert x==[]

def test_basket_add():
    basket=Basket()
    tovar1=Tovar("�����������","C ������",49)
    tovar2=Tovar("���","� ������ �� �����",120)
    basket.add_tovar(tovar2)
    basket.add_tovar(tovar1)
    x=basket.tovars[1].desc
    assert x=="C ������"

def test_basket_delete():
    basket=Basket()
    tovar1=Tovar("�����������","C ������",49)
    tovar2=Tovar("���","� ������ �� �����",120)
    basket.add_tovar(tovar2)
    basket.add_tovar(tovar1)
    basket.delete_tovar(tovar2)
    x=basket.tovars[0].desc
    assert x=="C ������"

def test_basket_change():
    basket=Basket()
    tovar1=Tovar("�����������","C ������",49)
    tovar2=Tovar("���","� ������ �� �����",120)
    tovar3=Tovar("���","� ���������",134)
    tovar4=Tovar("������","� �������",37)
    tovar5=Tovar("������������ �������","����������",29)
    basket.add_tovar(tovar1)
    basket.add_tovar(tovar2)
    basket.add_tovar(tovar3)
    basket.add_tovar(tovar4)
    basket.change_tovar_count(tovar3,12)
    x=basket.tovars_count[2]
    assert x==12

def test_basket_clear():
    basket=Basket()
    tovar1=Tovar("�����������","C ������",49)
    tovar2=Tovar("���","� ������ �� �����",120)
    tovar3=Tovar("���","� ���������",134)
    tovar4=Tovar("������","� �������",37)
    tovar5=Tovar("������������ �������","����������",29)
    basket.add_tovar(tovar1)
    basket.add_tovar(tovar2)
    basket.add_tovar(tovar3)
    basket.add_tovar(tovar4)
    basket.clear_basket()
    x=basket.tovars
    assert x==[]

def test_person_init():
    person=Person()
    x=person.name
    assert x==""

def test_person_addname():
    person=Person()
    person.add_name("����")
    x=person.name
    assert x=="����"

def test_person_addphone():
    person=Person()
    person.add_phone_number("89127887332")
    x=person.phone_number
    assert x=="89127887332"