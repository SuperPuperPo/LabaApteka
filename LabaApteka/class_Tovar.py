# -*- coding: cp1251 -*-
class Tovar(object):
    """
    Ęëŕńń Ňîâŕđ.

    Ŕňđčáóňű:

    'name' : **Ńňđîęŕ** ń íŕçâŕíčĺě ňîâŕđŕ

    'desc' : **Ńňđîęŕ** ń îďčńŕíčĺě ňîâŕđŕ

    'price' : **×čńëî** ń öĺííîé ňîâŕđŕ â đóáë˙ő

    """
    registry=[]
    """
    **Ěŕńńčâ**, ęîňîđűé őđŕíčň â ńĺáĺ âńĺ îáúĺęňű ęëŕńńŕ **Tovar**.
    """
    def __init__(self,name,desc,price):
        """
        Ęîíńňđóęňîđ ďđčíčěŕĺň čě˙, îďčńŕíčĺ č öĺíó ňîâŕđŕ.

        Ŕđăóěĺíňű:

        'name' : **Ńňđîęŕ** ń íŕçâŕíčĺě ňîâŕđŕ

        'desc' : **Ńňđîęŕ** ń îďčńŕíčĺě ňîâŕđŕ

        'price' : **×čńëî** ń öĺííîé ňîâŕđŕ â đóáë˙ő
        """

        self.registry.append(self)
        self.name=name
        self.desc=desc
        self.price=price

    def serch(serch_line):
        """Ěĺňîä äë˙ íŕőîćäĺíč˙ ňîâŕđîâ ďî ńňđîęĺ â îďčńŕíčč čëč čěĺíč.
        
        Ŕđăóěĺíňű:

        'serch_line' : **Ńňđîęŕ** äë˙ ďîčńęŕ ňîâŕđîâ

        Âîçâđŕůŕĺň:      

        'tovar_need' : **Ěŕńńčâ ń îáúĺęňŕěč ęëŕńńŕ Tovar** ó ęîňîđűő â îďčńŕíčč čëč čěĺíč ĺńňü čńęîěŕ˙ ńňđîęŕ 
                
        """
        tovar_need=[]
        for tovar in Tovar.registry:
            tovar_name=tovar.name.lower()
            tovar_desc=tovar.desc.lower()
            if (tovar_name.find(serch_line.lower())!=-1) or (tovar_desc.find(serch_line.lower())!=-1):
                print("Íŕéäĺí ňîâŕđ")
                print("Íŕçâŕíčĺ:"+tovar.name)
                print("Îďčńŕíčĺ:"+tovar.desc)
                print("Îďčńŕíčĺ:"+str(tovar.price)+"Đóá.")
                print("")
                tovar_need=tovar_need+[tovar]
        if tovar_need==[]:
            print("Ňîâŕđű íĺ íŕéäĺíű!!!")
        return tovar_need




 




