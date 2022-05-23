from pdoc import text
f=open("AutoDoc.md",mode="w",encoding="utf-8")
f.write(text("class_Basket")+ '\n')
f.write(text("class_Order")+ '\n')
f.write(text("class_Person")+ '\n')
f.write(text("class_Tovar")+ '\n')
f.close


