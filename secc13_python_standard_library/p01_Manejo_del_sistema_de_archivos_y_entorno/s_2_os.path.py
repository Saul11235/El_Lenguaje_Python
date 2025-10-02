import os

#
#  os.path    modulo de manejo de rutas de archivos
#

# Ruta de ejemplo (puedes ajustarla según tu sistema)
ruta_ejemplo = "mi_carpeta/archivo.txt"


#-------------------------------------
# Obtener la ruta absoluta de un archivo o carpeta
ruta_absoluta = os.path.abspath(ruta_ejemplo)
print("\n\n","Ruta absoluta:", ruta_absoluta)


#-------------------------------------
# Verificar si una ruta existe
existe = os.path.exists(ruta_ejemplo)
print("\n\n","¿Existe la ruta?", existe)


#-------------------------------------
# Saber si una ruta es un archivo
es_archivo = os.path.isfile(ruta_ejemplo)
print("\n\n","¿Es un archivo?", es_archivo)


#-------------------------------------
# Saber si una ruta es una carpeta
es_carpeta = os.path.isdir("mi_carpeta")
print("\n\n","¿Es una carpeta?", es_carpeta)


#-------------------------------------
# Obtener el nombre del archivo desde una ruta
nombre_archivo = os.path.basename(ruta_ejemplo)
print("\n\n","Nombre del archivo:", nombre_archivo)


#-------------------------------------
# Obtener solo el directorio (sin el archivo)
solo_directorio = os.path.dirname(ruta_ejemplo)
print("\n\n","Solo el directorio:", solo_directorio)


#-------------------------------------
# Dividir ruta en (directorio, archivo)
partes = os.path.split(ruta_ejemplo)
print("\n\n","Partes (directorio, archivo):", partes)


#-------------------------------------
# Unir rutas de forma segura (evita errores de slashes entre sistemas)
nueva_ruta = os.path.join("mi_carpeta", "subcarpeta", "documento.pdf")
print("\n\n","Ruta unida con join:", nueva_ruta)


#-------------------------------------
# Obtener la extensión de un archivo
nombre, extension = os.path.splitext(ruta_ejemplo)
print("\n\n","Nombre sin extensión:", nombre)
print("Extensión del archivo:", extension)


print("\n\n","Fin del script os.path")
