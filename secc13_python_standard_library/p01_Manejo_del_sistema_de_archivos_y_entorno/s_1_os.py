
import os

# Obtener el directorio actual de trabajo
#
#  cwd   = current work directory
#
print("\n\nDirectorio actual:", os.getcwd())


# -------------------------------------
# Listar archivos y carpetas del directorio actual
print("\n\nContenido del directorio:")
print(os.listdir())


# -------------------------------------
# Crear un nuevo directorio
nuevo_directorio = "mi_carpeta"
if not os.path.exists(nuevo_directorio):
    os.mkdir(nuevo_directorio)  # Crea la carpeta si no existe
    print(f"\n\nCarpeta '{nuevo_directorio}' creada.")
else:
    print(f"\n\nLa carpeta '{nuevo_directorio}' ya existe.")


# -------------------------------------
# Crear un subdirectorio dentro de otro
ruta_completa = "otra_carpeta/subcarpeta" 
os.makedirs(ruta_completa, exist_ok=True)
print(f"\n\nSubcarpeta creada en: {ruta_completa}")


# -------------------------------------
# Obtener el nombre del sistema operativo
print("\n\nSistema operativo:", os.name)


# -------------------------------------
# Obtener una variable de entorno (como el PATH)
path_env = os.environ.get("PATH")
print("\n\nVariable de entorno PATH (solo una parte):", path_env[:100], "...")


# -------------------------------------
print("\n\nScript finalizado.")
