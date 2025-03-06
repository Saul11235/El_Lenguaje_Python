#
# MAESTRA DE EDUCACION INICIAL
#
# Una maestra de educación inicial requiere 
# un programa que le ayude a hacer canciones 
# para sus estudiantes, el programa recibirá 
# un texto, y si encuentra una P, cambiará 
# todo todo por PAR
# Si encuentra una M cambiará todo por MAN, 
# y si no encuentra coincidencias 
# cambiará todas las vocales por A
#


texto=input("\n Ingrese el texto > ")

if "p" in texto or "P" in texto:
    texto=texto.replace("p","par").replace("P","PAR")
elif "m" in texto or "m" in texto:
    texto=texto.replace("m","man").replace("M","MAN")
else:
    texto=texto.replace("e","a").replace("i","a").replace("o","a").replace("u","a")
    texto=texto.replace("E","A").replace("I","A").replace("O","A").replace("U","A")

print("\n texto para canción:\n\t",texto,"\n")

input()
