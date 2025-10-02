
import string

# 1. Constantes útiles
print("Letras minúsculas:", string.ascii_lowercase)
print("Letras mayúsculas:", string.ascii_uppercase)
print("Todas las letras:", string.ascii_letters)
print("Dígitos:", string.digits)
print("Caracteres hexadecimales:", string.hexdigits)
print("Caracteres de puntuación:", string.punctuation)
print("Caracteres imprimibles:", string.printable)
print()

# 2. Eliminar puntuación de un texto
texto = "Hello! How are you? :)"
texto_sin_puntuacion = ''.join(c for c in texto if c not in string.punctuation)
print("Texto sin puntuación:", texto_sin_puntuacion)

# 3. Usar Template para reemplazar variables en una cadena
from string import Template

plantilla = Template("Hola, $nombre. Hoy es $dia.")
mensaje = plantilla.substitute(nombre="Ana", dia="viernes")
print("\nMensaje con Template:", mensaje)

# 4. Crear una contraseña aleatoria usando letras y dígitos
import random
caracteres = string.ascii_letters + string.digits
password = ''.join(random.choices(caracteres, k=10))
print("\nContraseña generada:", password)

print("\nFin del script string.")
