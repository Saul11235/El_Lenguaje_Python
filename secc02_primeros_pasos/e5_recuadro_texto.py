# RECUADRO TEXTO ASCII
#
# Hacer un programa que lea un texto y 
# genere un recuadro ASCII con dicha palabra
#
#   XXXXXXXXXXXXXXXXXXXXXX
#   X                    X 
#   X  ESTO ES UN TEXTO  X 
#   X                    X
#   XXXXXXXXXXXXXXXXXXXXXX
#

txt=input("Ingrese su texto: ")

print("")

print("\t"+(len(txt)+6)*"X")
print("\t"+"X"+(len(txt)+4)*" "+"X")
print("\tX  "+txt+"  X")
print("\t"+"X"+(len(txt)+4)*" "+"X")
print("\t"+(len(txt)+6)*"X")

input()

