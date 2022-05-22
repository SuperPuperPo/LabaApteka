# -*- coding: cp1251 -*-
class Basket(object):
    def __init__(self):
        self.tovars=[]
        self.tovars_count=[]

    def add_tovar(self,tovar):
        self.tovars=self.tovars+[tovar]
        self.tovars_count=self.tovars_count+[1]

    def delete_tovar(tovar):
        for i in range(0,len(tovars)):
            if tovar==self.tovars[i]:
                self.tovars.pop(i)
                self.tovars_count.pop(i)
                break

    def change_tovar_count(self,tovar,need_count):
        if need_count==0:
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
        self.tovars=[]
        self.tobars_count=[]



