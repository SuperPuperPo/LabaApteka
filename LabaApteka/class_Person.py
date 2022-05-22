# -*- coding: cp1251 -*-
class Person(object):
    def __init__(self):
        self.name=""
        self.phnoe_number=""
        self.order=[]

    def add_order(self,order):
        self.order=self.order+[order]

    def add_phnoe_number(self,phone_number):
        self.phnoe_number=phone_number

    def add_Name(self,name):
        self.name=name
