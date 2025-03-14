#
# DATOS DE BIBLIOTECA
#
# Hacer un programa que recursivamente lea 
# comandos de agregar o no elementos a un 
# diccionario anidado, que almacenará otros 
# diccionarios conteniendo cantidades de un 
# libro (entero), autor (string) y titulo (string), 
# genere al final un informe detallando todos 
# los libros colocados por el usuario.
#

datos={}
repetir=True
contador=0

while repetir:
    if input("\n ¿nuevo elemento? (si-no) > ")=="si":
        contador+=1
        codigo="COD"+str(contador)
        datos[codigo]={
                'titulo':input('\ttitulo :'),
                'autor' :input('\tautor  :'),
                'cantidad':int(input('\tcant   :')),
                }
    else: repetir = False


print('\n INFORME DATOS BIBLIOTECA')
libros=0
for libro in datos:
    print('\tCODIGO:',libro)
    print('\t\tTITULO:',datos[libro]['titulo'])
    print('\t\tAUTOR :',datos[libro]['autor'])
    print('\t\tCANT  :',datos[libro]['cantidad'])
    libros+=datos[libro]['cantidad']
print(' NRO TOTAL LIBROS: ',libros)
input()
