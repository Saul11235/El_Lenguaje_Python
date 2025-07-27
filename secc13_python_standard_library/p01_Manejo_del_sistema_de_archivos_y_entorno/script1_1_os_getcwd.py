
import os

# Obtener el directorio actual
directorio_actual = os.getcwd()
print(f"Directorio actual: {directorio_actual}")

# Listar archivos y carpetas en el directorio actual
contenido = os.listdir(directorio_actual)
print("\nContenido del directorio:")
for nombre in contenido:
    print(f"- {nombre}")
