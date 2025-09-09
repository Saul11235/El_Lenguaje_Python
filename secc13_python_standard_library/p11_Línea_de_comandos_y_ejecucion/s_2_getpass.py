
import getpass

# Pedir contraseña sin mostrarla en pantalla
input('coloque pass (la contraña esperada es hola)\n\n')
password = getpass.getpass("Introduce tu contraseña: ")

# Mostrar mensaje sin revelar la contraseña
print("Contraseña recibida (no se muestra en pantalla).")

# Ejemplo simple de verificación
if password == "hola":
    print("¡Acceso concedido!")
else:
    print("Acceso denegado.")
