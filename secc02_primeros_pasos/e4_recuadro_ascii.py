# RECUADRO ASCII ART
#
# Hacer un programa que genere un recuadro ASCII 
# leyendo via input el alto y ancho (en caracteres)
#
#   XXXXXXXXXXXXXXX
#   X             X
#   X             X
#   X             X 
#   X             X
#   XXXXXXXXXXXXXXX
#

alto=int(input("ingrese alto: "))
ancho=int(input("ingrese ancho: "))

print("")
print("\t"+"X"*ancho+(alto*("\n\tX"+(ancho-2)*" "+"X"))+"\n\t"+ancho*"X")

input()

