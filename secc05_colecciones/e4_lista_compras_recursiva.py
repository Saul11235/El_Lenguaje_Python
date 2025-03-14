#
# LISTA DE COMPRAS RECURSIVA
#
# Hacer un programa que recursivamente 
# lea comandos de agregar o no elementos de 
# una lista de compra mediante un comando, y 
# al final muestre la lista concatenada, use 
# una lista para almacenar la información recolectada. 
#

print('\n LISTA RECURSIVA')

lista=[]
repetir=True

while repetir:
    if input("\n ¿nuevo elemento? (si-no) > ")=="si":
        nuevo=input(" >>> ")
        lista.append(nuevo)
    else: repetir = False


print('\nLISTA:\n - '+'\n - '.join(lista))
print('\nla lista tiene',len(lista),'elementos')
input()
