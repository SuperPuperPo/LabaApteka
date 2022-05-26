# -*- coding: cp1251 -*-
class Person(object):
    """
    ����� ����������.
    
    ��������:

    'name': **������** � ������ ������������

    'phnoe_number': **�����** � ������� �������� ������������

    'order':*������* � ��������� ������ **Order**
    
    """
    def __init__(self):
        """
        ����������� ������� ������� ����������.
        """
        self.name=""
        self.phone_number=""
        self.order=[]

    def add_order(self,order):
        """
        ����� ��� ���������� ������.
        
        ���������:

        'order' : ������ ������ **Order**
        """
        self.order=self.order+[order]

    def add_phone_number(self,phone_number):
        """
        ����� ��� ���������� ������ ��������.
        
        ���������:

        'phone_number' : **�����** � ������� �������� ������������        
        """
        self.phone_number=phone_number

    def add_name(self,name):
        """
        ����� ��� ���������� ����� ����������.
        
        ���������:

        'name' :**������** � ������ ����������        
        """
        self.name=name
