#
# RECOMENDACION DE UNA MASCOTA
#
# Hacer un programa que en base a preguntas 
# si y no recomiende una mascota al usuario
#
#  -------------------------------------------
#      	        Mucho     Mucho 
#               espacio   cuidado   Acuatico   
#  -------------------------------------------
#  Peces Koi	SI	      SI	    SI
#  Gran Danés	SI	      SI	    NO
#  Goldfish	    SI	      NO	    SI
#  Gato	        SI	      NO	    NO
#  Pez payaso	NO	      SI	    SI
#  Hamster	    NO	      SI	    NO
#  Peces Cebra	NO	      NO	    SI
#  Periquito	NO	      NO	    NO
#  -------------------------------------------

print("\nRECOMENDACION DE MASCOTA\n")

espacio="si" == input("¿tienes espacio? (si-no) > ")
cuidado="si" == input("¿le darás mucho cuidado? (si-no) > ")
acuatico="si" == input("¿te gustan los animales acuaticos? (si-no) > ")

print("")

if espacio and cuidado and acuatico:
    print("Te recomiendo los peces Koi")
elif espacio and cuidado and not acuatico:
    print("Te recomiendo el Gran danés")
elif espacio and not cuidado and acuatico:
    print("Te recomiendo el Gold Fish")
elif espacio and not cuidado and not acuatico:
    print("Te recomiendo un gato")
elif not espacio and cuidado and acuatico:
    print("Te recomiendo un pez payaso")
elif not espacio and cuidado and not acuatico:
    print("Te recomiendo un Hamster")
elif not espacio and not cuidado and acuatico:
    print("te recomiendo los peces cebra")
elif not espacio and not cuidado and not acuatico:
    print("Te recomiendo un Periquito")

input()

