# ejemplo escritura
file = open('archivo.txt','r') 

# colocar una coleccion con varios str
contenido = file.readlines()
file.close()

contador=0
for linea in contenido:
    contador+=1
    print(contador,':',[linea])
