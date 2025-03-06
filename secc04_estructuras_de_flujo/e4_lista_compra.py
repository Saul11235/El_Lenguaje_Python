#
# LISTA DE COMPRA
#
# Utilizando un bucle while y un contador 
# que lea y actualice un string de varias 
# lineas, y al final muestre una lista de 
# compra, con todos los elementos ingresados por el usuario

print("\n LISTA DE COMPRAS \n")

limite=int(input("¿Cuantas cosas vamos a comprar?: "))
contador=0

# definimos una variable llamada lista
lista="""
     MI LISTA DE COMPRAS
   -----------------------
"""

while contador<limite:
    contador=contador+1
    insumo=input(" insumo > ")
    lista=lista+"- "+str(contador)+" : "+insumo+"\n"

print("\nlista generada:")
print(lista)
input()

