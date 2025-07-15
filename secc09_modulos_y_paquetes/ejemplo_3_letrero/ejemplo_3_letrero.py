#
# ASCII ART
# 
# Utilice el gestor de paquetes pip 
# e instale el paquete art
# 
# pip  install art
# 
# (revise la documentacion) Y cree un script 
# que haga un letrero de bienvenida 
#

from art import text2art

input("\n  Letrero de Bienvenida\n")

# Crear arte en ASCII con el texto "Bienvenido"
letrero = text2art(input(" ingrese texto >>> "))

# Mostrar el letrero
print("")
print(letrero)

#detiene el programa
input()
