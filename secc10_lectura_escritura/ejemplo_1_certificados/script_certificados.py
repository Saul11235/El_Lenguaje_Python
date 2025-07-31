#
# GENERADOR DE CERTIFICADOS
#
# Cree un script python que genere diplomas (archivos 
# de texto plano con nombre y número de certificado). 
# Teniendo una lista con los nombres de los participantes de un curso.

# -------------------------------------

#  primero definiremos una función que escribira 
#  un archivo de acuerdo a un nombre y un nro de certificado

def escribe_Diploma(nombre,numero):
    nombreArchivo=f'DIPLOMA_{numero}.txt'
    contenido=f'''
  +---------------------------+
  |   C E R T I F I C A D O   |
  +---------------------------+

 Otorgado a: {nombre} por haber concluido
 su capacitación en el Lenguaje Python

 certificado N° {numero}
 '''
    with open(nombreArchivo,"w",encoding='utf-8') as f:
        f.write(contenido)
    print(nombreArchivo,"creado y otorgado a",nombre)

# -------------------------------------
# creamos una lista con todos los nombres obtenidos del archivo

with open('lista.txt','r',encoding='utf-8') as file:
    lista=[x.replace("\n","") for x in file.readlines()]

# -------------------------------------
# recorremos la lista y pasamos por contador 
# para numerar los certificados

contador = 0

for nombre in lista:
    contador += 1
    escribe_Diploma(nombre,contador)

