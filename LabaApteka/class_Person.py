# -*- coding: cp1251 -*-
class Person(object):
    """
    Класс Покупатель.
    
    Атрибуты:

    'name': **Строка** с именем пользователя

    'phnoe_number': **Число** с номером телефона пользователя

    'order':*массив* с объектами класса **Order**
    
    """
    def __init__(self):
        """
        Конструктор создает пустого покупателя.
        """
        self.name=""
        self.phone_number=""
        self.order=[]

    def add_order(self,order):
        """
        Метод для добавления заказа.
        
        Аргументы:

        'order' : Объект класса **Order**
        """
        self.order=self.order+[order]

    def add_phone_number(self,phone_number):
        """
        Метод для добавления номера телефона.
        
        Аргументы:

        'phone_number' : **Число** с номером телефона пользователя        
        """
        self.phone_number=phone_number

    def add_name(self,name):
        """
        Метод для добваления имени покупателя.
        
        Аргументы:

        'name' :**Строка** с именем покупателя        
        """
        self.name=name
