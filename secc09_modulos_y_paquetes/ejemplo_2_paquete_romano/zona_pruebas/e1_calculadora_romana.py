# CALCULADORA ROMANA
#
# Cree un programa que sume y multiplique 
# dos números leídos por el usuario 
# (a través de input), y mostrará los 
# resultados cómo números romanos, obtenidos 
# de una clase llamada romano( ver sección clases y objetos)
#

from romano import romano

input('\n  CALCULADORA ROMANA\n')

x=int(input(" Numero x : "))
y=int(input(" Numero x : "))

print("")
print("x   = ",x,romano(x))
print("y   = ",y,romano(y))
print("")
print("x+y = ",x+y,romano(x+y))
print("x-y = ",x-y,romano(x-y))
print("x*y = ",x*y,romano(x*y))
print("x^y = ",x**y,romano(x**y))


input()
