# CAMBIO EN UNA ORACIÓN
#
# Hacer un programa que cambie el contenido 
# de una oración cambiando una palabra, 
# leyendo la palabra a cambiar y la palabra para hacer el cambio
#
# El perro corre feliz    ->   El gato corre feliz
#

oracion=input("Ingrese su oración: ")
objetivo=input("str objetivo: ")
reemplazo=input("str reemplazo: ")

print("")
print("ORACION ORIGINAL:")
print(oracion)
print("")
print("ORACION REEMPLAZO:")
print(oracion.replace(objetivo,reemplazo))

input()


