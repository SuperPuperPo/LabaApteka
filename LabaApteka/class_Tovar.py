# -*- coding: cp1251 -*-
class Tovar(object):
    """
    ����� �����.

    ��������:

    'name' : **������** � ��������� ������

    'desc' : **������** � ��������� ������

    'price' : **�����** � ������ ������ � ������

    """
    registry=[]
    """
    **������**, ������� ������ � ���� ��� ������� ������ **Tovar**.
    """
    def __init__(self,name,desc,price):
        """
        ����������� ��������� ���, �������� � ���� ������.

        ���������:

        'name' : **������** � ��������� ������

        'desc' : **������** � ��������� ������

        'price' : **�����** � ������ ������ � ������
        """
        self.registry.append(self)
        self.name=name
        self.desc=desc
        self.price=price

    def serch(serch_line):
        """����� ��� ���������� ������� �� ������ � �������� ��� �����.
        
        ���������:

        'serch_line' : **������** ��� ������ �������

        ����������:      

        'tovar_need' : **������ � ��������� ������ Tovar** � ������� � �������� ��� ����� ���� ������� ������ 
                
        """
        tovar_need=[]
        for tovar in Tovar.registry:
            tovar_name=tovar.name.lower()
            tovar_desc=tovar.desc.lower()
            if (tovar_name.find(serch_line.lower())!=-1) or (tovar_desc.find(serch_line.lower())!=-1):
                print("������ �����")
                print("��������:"+tovar.name)
                print("��������:"+tovar.desc)
                print("��������:"+str(tovar.price)+"�")
                print("")
                tovar_need=tovar_need+[tovar]
        if tovar_need==[]:
            print("������ �� �������")
        return tovar_need




 




