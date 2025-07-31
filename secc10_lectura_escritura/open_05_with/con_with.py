# ejemplo con with

with open('archivo.txt','r') as file:
    print( file.read() )

# no fue necesario cerrar el archivo
# la conexion termina al final
