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
        self.phnoe_number=""
        self.order=[]

    def add_order(self,order):
        """
        ����� ��� ���������� ������.
        
        ���������:

        'order' : ������ ������ **Order**
        """
        self.order=self.order+[order]

    def add_phnoe_number(self,phone_number):
        """
        ����� ��� ���������� ������ ��������.
        
        ���������:

        'phone_number' : **�����** � ������� �������� ������������        
        """
        self.phnoe_number=phone_number

    def add_Name(self,name):
        """
        ����� ��� ���������� ����� ����������.
        
        ���������:

        'name' :**������** � ������ ����������        
        """
        self.name=name
