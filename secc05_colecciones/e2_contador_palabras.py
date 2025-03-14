#
# CONTADOR DE PALABRAS Y CARACTERES
#
# Hacer un programa que lea un texto, y 
# cuente las palabras, luego recursivamente 
# cuente las palabras e informe el número 
# de letras, y palabras recursivamente contadas
#

txt=input('\nIngrese texto > ')

# contadores
nPalabra=0
nCaracteres=0

for palabra in txt.split():
    nPalabra+=1
    nCaracteres+=len(palabra)
    print("\nPALABRA",nPalabra,":",palabra)
    print("CARACTERES:",len(palabra))

print('\n\tRESUMEN:')
print('\ttotal palabras   :',nPalabra)
print('\ttotal caracteres :',nCaracteres)

input()
