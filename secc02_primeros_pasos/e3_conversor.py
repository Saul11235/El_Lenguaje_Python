# PROGRAMA QUE CONVIERTE UNIDADES
#
# Hacer un programa que lea una longitud en cm
# y realice las conversiones a pulgadas
# Y que muestre los resultados sin redondeo, 
# con redondeo a 2 decimales 
# y con redondeo al entero superior.
#
#  2.54cm   = 1 pulgada

cm=float(input("ingrese la long en cm: "))

pulgadas=cm/2.54

print("la long en pulgadas es",pulgadas)
print("la long en pulgadas es aproximadamente",round(pulgadas,2))

input()

