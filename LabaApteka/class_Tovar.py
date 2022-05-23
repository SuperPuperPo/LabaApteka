# -*- coding: cp1251 -*-
class Tovar(object):
    """
    Класс Товар.

    Атрибуты:

    'name' : **Строка** с названием товара

    'desc' : **Строка** с описанием товара

    'price' : **Число** с ценной товара в рублях

    """
    registry=[]
    """
    **Массив**, который хранит в себе все объекты класса **Tovar**.
    """
    def __init__(self,name,desc,price):
        """
        Конструктор принимает имя, описание и цену товара.

        Аргументы:

        'name' : **Строка** с названием товара

        'desc' : **Строка** с описанием товара

        'price' : **Число** с ценной товара в рублях
        """
        self.registry.append(self)
        self.name=name
        self.desc=desc
        self.price=price

    def serch(serch_line):
        """Метод для нахождения товаров по строке в описании или имени.
        
        Аргументы:

        'serch_line' : **Строка** для поиска товаров

        Возвращает:      

        'tovar_need' : **Массив с объектами класса Tovar** у которых в описании или имени есть искомая строка 
                
        """
        tovar_need=[]
        for tovar in Tovar.registry:
            tovar_name=tovar.name.lower()
            tovar_desc=tovar.desc.lower()
            if (tovar_name.find(serch_line.lower())!=-1) or (tovar_desc.find(serch_line.lower())!=-1):
                print("Найден товар")
                print("Название:"+tovar.name)
                print("Описание:"+tovar.desc)
                print("Описание:"+str(tovar.price)+"Р")
                print("")
                tovar_need=tovar_need+[tovar]
        if tovar_need==[]:
            print("Товары не найдены")
        return tovar_need




 




