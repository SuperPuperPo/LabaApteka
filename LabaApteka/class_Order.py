# -*- coding: cp1251 -*-
class Order(object):
        """Класс Заказ."""
        def __init__(self,basket):
            """
            Конструктор на вход подается корзина с товарами.
            
            Аргументы:

            'tovar' : Объект класса **Basket**
            """
            total_price=0
            self.tovars=[]
            self.tovars_count=[]
            for i in range(0,len(basket.tovars)):
                self.tovars=self.tovars+[basket.tovars[i]]
                self.tovars_count=self.tovars+[basket.tovars_count[i]]
            for i in range(0,len(self.tovars)):
                total_price=total_price+self.tovars[i].price
            self.price=total_price
            self.ststus="Создается"
            basket.clear_basket
            if basket.tovars==[]:
                self.ststus="Корзина пуста"
                print("Корзина пуста!")

        def add_status(self,status):
            """
            Метод для присваивания статуса.
            
            Аргументы:

            'status' : **Строка** с необходимым статусом
            """
            self.ststus=status