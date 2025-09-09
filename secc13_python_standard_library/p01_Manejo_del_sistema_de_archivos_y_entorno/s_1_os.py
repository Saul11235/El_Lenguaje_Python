
import os

# Obtener el directorio actual de trabajo
print("Directorio actual:", os.getcwd())

# Cambiar de directorio (esto depende del sistema operativo)
# os.chdir('/ruta/a/otro/directorio')  # Descomenta y cambia según tu sistema

# Listar archivos y carpetas del directorio actual
print("Contenido del directorio:")
print(os.listdir())

# Crear un nuevo directorio
nuevo_directorio = "mi_carpeta"
if not os.path.exists(nuevo_directorio):
    os.mkdir(nuevo_directorio)  # Crea la carpeta si no existe
    print(f"Carpeta '{nuevo_directorio}' creada.")
else:
    print(f"La carpeta '{nuevo_directorio}' ya existe.")

# Crear un subdirectorio dentro de otro
ruta_completa = os.path.join(nuevo_directorio, "subcarpeta")
os.makedirs(ruta_completa, exist_ok=True)
print(f"Subcarpeta creada en: {ruta_completa}")

# Obtener el nombre del sistema operativo
print("Sistema operativo:", os.name)

# Obtener una variable de entorno (como el PATH)
path_env = os.environ.get("PATH")
print("Variable de entorno PATH (solo una parte):", path_env[:100], "...")

# Renombrar un archivo o carpeta (comentado porque requiere un archivo existente)
# os.rename("archivo_viejo.txt", "archivo_nuevo.txt")

# Eliminar un archivo (comentado para seguridad)
# os.remove("archivo_a_borrar.txt")

# Eliminar una carpeta vacía
# os.rmdir("carpeta_a_eliminar")

# Eliminar carpeta y todo su contenido (requiere importar shutil)
# import shutil
# shutil.rmtree("carpeta_a_eliminar_con_todo")

print("Script finalizado.")
