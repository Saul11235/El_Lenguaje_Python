import os

# Ruta de ejemplo (puedes ajustarla según tu sistema)
ruta_ejemplo = "mi_carpeta/archivo.txt"

# Obtener la ruta absoluta de un archivo o carpeta
ruta_absoluta = os.path.abspath(ruta_ejemplo)
print("Ruta absoluta:", ruta_absoluta)

# Verificar si una ruta existe
existe = os.path.exists(ruta_ejemplo)
print("¿Existe la ruta?", existe)

# Saber si una ruta es un archivo
es_archivo = os.path.isfile(ruta_ejemplo)
print("¿Es un archivo?", es_archivo)

# Saber si una ruta es una carpeta
es_carpeta = os.path.isdir("mi_carpeta")
print("¿Es una carpeta?", es_carpeta)

# Obtener el nombre del archivo desde una ruta
nombre_archivo = os.path.basename(ruta_ejemplo)
print("Nombre del archivo:", nombre_archivo)

# Obtener solo el directorio (sin el archivo)
solo_directorio = os.path.dirname(ruta_ejemplo)
print("Solo el directorio:", solo_directorio)

# Dividir ruta en (directorio, archivo)
partes = os.path.split(ruta_ejemplo)
print("Partes (directorio, archivo):", partes)

# Unir rutas de forma segura (evita errores de slashes entre sistemas)
nueva_ruta = os.path.join("mi_carpeta", "subcarpeta", "documento.pdf")
print("Ruta unida con join:", nueva_ruta)

# Obtener la extensión de un archivo
nombre, extension = os.path.splitext(ruta_ejemplo)
print("Nombre sin extensión:", nombre)
print("Extensión del archivo:", extension)

# Normalizar una ruta (corrige slashes duplicados o incorrectos)
ruta_rara = "mi_carpeta//subcarpeta\\archivo.txt"
ruta_normalizada = os.path.normpath(ruta_rara)
print("Ruta normalizada:", ruta_normalizada)

# Comparar si dos rutas son iguales (en sistemas sensibles a mayúsculas/minúsculas puede variar)
ruta1 = os.path.abspath("mi_carpeta/archivo.txt")
ruta2 = os.path.abspath("./mi_carpeta/archivo.txt")
print("¿Rutas iguales?:", os.path.samefile(ruta1, ruta2) if os.path.exists(ruta1) else "No existen para comparar")

print("Fin del script os.path")
