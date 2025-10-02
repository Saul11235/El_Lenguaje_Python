
import sys

# 1. Mostrar la versión de Python que se está usando
print("\nVersión de Python:")
print(sys.version)
print()

# 2. Ver la lista de argumentos pasados al script
print("\nArgumentos desde la línea de comandos:")
print(sys.argv)
print("Cantidad de argumentos:", len(sys.argv))
print()

# 3. Acceder a la plataforma del sistema
print("\nPlataforma del sistema operativo:")
print(sys.platform)
print()

# 4. Mostrar el path de búsqueda de módulos
print("\nRutas donde Python busca módulos para importar:")
for ruta in sys.path:
    print("-", ruta)

# 5. Imprimir mensajes de error a stderr
print("\nMensaje normal (stdout)")
print("Este es un error (stderr)", file=sys.stderr)

# 6. Comprobar el tamaño de un objeto en memoria
tamaño = sys.getsizeof("Hola mundo")
print(f"\nTamaño en memoria de la cadena 'Hola mundo': {tamaño} bytes")

print("\nFin del script sys.")
