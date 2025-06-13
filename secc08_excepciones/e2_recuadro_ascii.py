# RECUADRO ASCII ART
#
# corrija el programa visto en la seccion 2
# programa que genera un recuadro ASCII 
# leyendo via input el alto y ancho (en caracteres)
#
#   XXXXXXXXXXXXXXX
#   X             X
#   X             X
#   X             X 
#   X             X
#   XXXXXXXXXXXXXXX
#
#  colocque estructurs try except, para que se coloquen
#  valores iguales a 4, en alto y ancho en caso 
#  no se ingresen enteros positivos

try:
    alto=int(input("ingrese alto: "))
    if alto<4: alto=4
except: alto=4

try:
    ancho=int(input("ingrese ancho: "))
    if ancho<4: ancho=4
except: ancho=4


print("")
print("\t"+"X"*ancho+((alto-2)*("\n\tX"+(ancho-2)*" "+"X"))+"\n\t"+ancho*"X")
input()

