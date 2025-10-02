
from pathlib import Path

# Crear un objeto Path que representa el directorio actual
ruta_actual = Path.cwd()
print("\nDirectorio actual:", ruta_actual)

# Crear una ruta relativa a partir del directorio actual
ruta_archivo = ruta_actual / "mi_carpeta" / "archivo.txt"
print("\nRuta combinada:", ruta_archivo)

# Verificar si la ruta existe
print("\n¿Existe la ruta?", ruta_archivo.exists())

# Verificar si es un archivo
print("\n¿Es un archivo?", ruta_archivo.is_file())

# Verificar si es un directorio
print("\n¿Es un directorio?", ruta_archivo.is_dir())

# Obtener el nombre del archivo
print("\nNombre del archivo:", ruta_archivo.name)

# Obtener la extensión del archivo
print("\nExtensión del archivo:", ruta_archivo.suffix)

# Obtener la carpeta padre
print("\nDirectorio padre:", ruta_archivo.parent)

# Crear un directorio (si no existe)
nueva_carpeta = Path("nueva_carpeta")
nueva_carpeta.mkdir(exist_ok=True)
print("\nCarpeta 'nueva_carpeta' creada (si no existía).")

# Crear subdirectorios de forma recursiva
subcarpeta = Path("nueva_carpeta/subcarpeta1/subcarpeta2")
subcarpeta.mkdir(parents=True, exist_ok=True)
print("\nSubcarpetas creadas con éxito.")

# Listar archivos en un directorio
print("\nContenido de 'nueva_carpeta':")
for archivo in nueva_carpeta.iterdir():
    print("-", archivo.name)

print("Fin del script pathlib.")
