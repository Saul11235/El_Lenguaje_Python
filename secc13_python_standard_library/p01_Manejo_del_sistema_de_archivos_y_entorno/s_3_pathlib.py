
from pathlib import Path

# Crear un objeto Path que representa el directorio actual
ruta_actual = Path.cwd()
print("Directorio actual:", ruta_actual)

# Crear una ruta relativa a partir del directorio actual
ruta_archivo = ruta_actual / "mi_carpeta" / "archivo.txt"
print("Ruta combinada:", ruta_archivo)

# Verificar si la ruta existe
print("¿Existe la ruta?", ruta_archivo.exists())

# Verificar si es un archivo
print("¿Es un archivo?", ruta_archivo.is_file())

# Verificar si es un directorio
print("¿Es un directorio?", ruta_archivo.is_dir())

# Obtener el nombre del archivo
print("Nombre del archivo:", ruta_archivo.name)

# Obtener la extensión del archivo
print("Extensión del archivo:", ruta_archivo.suffix)

# Obtener el nombre del archivo sin la extensión
print("Nombre sin extensión:", ruta_archivo.stem)

# Obtener la carpeta padre
print("Directorio padre:", ruta_archivo.parent)

# Crear un directorio (si no existe)
nueva_carpeta = Path("nueva_carpeta")
nueva_carpeta.mkdir(exist_ok=True)
print("Carpeta 'nueva_carpeta' creada (si no existía).")

# Crear subdirectorios de forma recursiva
subcarpeta = Path("nueva_carpeta/subcarpeta1/subcarpeta2")
subcarpeta.mkdir(parents=True, exist_ok=True)
print("Subcarpetas creadas con éxito.")

# Listar archivos en un directorio
print("Contenido de 'nueva_carpeta':")
for archivo in nueva_carpeta.iterdir():
    print("-", archivo.name)

# Cambiar nombre o mover un archivo (comentado para seguridad)
# archivo_a_renombrar = Path("archivo_viejo.txt")
# archivo_a_renombrar.rename("archivo_nuevo.txt")

# Eliminar un archivo o directorio (comentado para seguridad)
# Path("archivo.txt").unlink()        # Para archivos
# Path("carpeta_vacia").rmdir()      # Para carpetas vacías

print("Fin del script pathlib.")
