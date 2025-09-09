# 
#  La sintaxis de python 
#  se inspira del lenguaje natural
#


hayBanana=True
hayManzana=True


fruta = "banana" if hayBanana else "manzana"
print(fruta)

fruta = "banana" if hayBanana else "manzana" if hayManzana else "pera"
print(fruta)


# multiples variables en una expresion

x, y = 15, 20
print(x)
print(y)


primero, *resto = [1, 2, 3, 4]
print(primero)
print(resto)




