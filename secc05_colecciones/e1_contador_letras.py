#
# CONTADOR DE LETRAS
#
# Hacer un programa que lea un texto, y 
# cuente las letras que la componen y 
# cuantas veces se repiten en todo el texto 
#

txt=input('\nIngrese texto > ')
print("")

for char in set(list(txt)):
    rep=txt.count(char)
    print(f"caracter '{char}' se repite {rep} veces")

input()
