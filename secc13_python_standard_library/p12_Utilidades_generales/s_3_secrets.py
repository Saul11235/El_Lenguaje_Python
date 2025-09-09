
import secrets
import string

# 1. Generar un número aleatorio seguro entre 0 y 9
numero = secrets.randbelow(10)
print("Número aleatorio seguro (0-9):", numero)

# 2. Elegir un carácter aleatorio seguro de un conjunto
letra = secrets.choice(string.ascii_letters)
print("Letra aleatoria segura:", letra)

# 3. Generar una contraseña segura de 12 caracteres (letras + dígitos)
alfabeto = string.ascii_letters + string.digits
password_segura = ''.join(secrets.choice(alfabeto) for _ in range(12))
print("Contraseña segura generada:", password_segura)

# 4. Generar un token hexadecimal seguro (ej. para autenticación)
token = secrets.token_hex(16)  # 16 bytes = 32 caracteres hex
print("Token hexadecimal seguro:", token)
