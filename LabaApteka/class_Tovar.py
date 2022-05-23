# -*- coding: cp1251 -*-
class Tovar(object):
    registry=[]
    def __init__(self,name,desc,price):
        self.registry.append(self)
        self.name=name
        self.desc=desc
        self.price=price

    def serch(serch_line):
        tovar_need=[]
        for tovar in Tovar.registry:
            tovar_name=tovar.name.lower()
            tovar_desc=tovar.desc.lower()
            if (tovar_name.find(serch_line.lower())!=-1) or (tovar_desc.find(serch_line.lower())!=-1):
                print("Найден товар")
                print("Название:"+tovar.name)
                print("Описание:"+tovar.desc)
                print("Описание:"+str(tovar.price)+"Руб.")
                print("")
                tovar_need=tovar_need+[tovar]
        if tovar_need==[]:
            print("Товары не найдены!!!")
        return tovar_need




 




