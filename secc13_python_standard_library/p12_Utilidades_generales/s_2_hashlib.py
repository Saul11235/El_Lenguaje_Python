
import hashlib

# Texto que queremos hashear
texto = "hola mundo"

# 1. Crear un objeto hash para SHA-256
hash_sha256 = hashlib.sha256()

# 2. Alimentar el objeto con el texto codificado en bytes
hash_sha256.update(texto.encode('utf-8'))

# 3. Obtener el hash en formato hexadecimal
resultado = hash_sha256.hexdigest()

print(f"Texto original: {texto}")
print(f"Hash SHA-256: {resultado}")

# 4. Otra forma rápida (directa)
hash_md5 = hashlib.md5(texto.encode('utf-8')).hexdigest()
print(f"Hash MD5: {hash_md5}")
