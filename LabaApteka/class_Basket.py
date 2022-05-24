# -*- coding: cp1251 -*-
class Basket(object):
    """
    Класс Корзина.
    """
    def __init__(self):
        """
        Конструктор создает пустую корзину.
        """
        self.tovars=[]
        self.tovars_count=[]

    def add_tovar(self,tovar):
        """
        Метод для добавления товара в корзину.
        
        Аргументы:

        'tovar' : Объект класса **Tovar**
        """
        k=0
        if self.tovars!=[]:
            for i in range(0,len(self.tovars)):
                if self.tovars[i]==tovar:
                    self.tovars_count[i]=self.tovars_count[i]+1
                    k=1
                    print("+")
                    print(tovar.name)
                    print(self.tovars_count[i])
                    break
            if k==0:
                self.tovars=self.tovars+[tovar]
                self.tovars_count=self.tovars_count+[1]
                print("+")
                print(tovar.name)
                print(1)

        else:
            self.tovars=self.tovars+[tovar]
            self.tovars_count=self.tovars_count+[1]
            print("+")
            print(tovar.name)
            print(1)

    def delete_tovar(self,tovar):
        """
        Метод для удаления товара из корзины.
        
        Аргументы:

        'tovar' : Объект класса **Tovar**
        """
        for i in range(0,len(tovars)):
            if tovar==self.tovars[i]:
                self.tovars.pop(i)
                self.tovars_count.pop(i)
                break

    def change_tovar_count(self,tovar,need_count):
        """
        Метод для изменения количества товара в корзине.

        Аргументы:

        'tovar' : Объект класса **Tovar**

        'need_count' : **Число** с необходимым количеством товара
        """
     
        if need_count<=0:
            for i in range(0,len(tovars)):
                if tovar==self.tovars[i]:
                    self.tovars.pop(i)
                    self.tovars_count.pop(i)
                    break
        else:
            for i in range(0,len(tovars)):
                if tovar==self.tovars[i]:
                    self.tovars_count[i]=need_count
                    break

    def clear_basket(self):
        """
        Метод для отчистки корзины.
        """
        self.tovars=[]
        self.tobars_count=[]



