
import base64

# Texto original
texto = "Hola mundo!"

# 1. Codificar texto a bytes y luego a base64
texto_bytes = texto.encode('utf-8')
texto_base64 = base64.b64encode(texto_bytes)
print("Texto codificado en base64:", texto_base64)

# 2. Decodificar base64 a bytes y luego a texto
texto_decodificado = base64.b64decode(texto_base64).decode('utf-8')
print("Texto decodificado:", texto_decodificado)

# 3. Codificar archivo binario (ejemplo: imagen o cualquier archivo)
datos_binarios = b"\x00\xFF\x10\x80"
datos_b64 = base64.b64encode(datos_binarios)
print("Datos binarios codificados:", datos_b64)
