
import re

# 1. Buscar si un patrón aparece en un texto
texto = "Mi número es 123-456-7890"
patron = r"\d{3}-\d{3}-\d{4}"  # Patrón para un número de teléfono
coincidencia = re.search(patron, texto)
if coincidencia:
    print("Número encontrado:", coincidencia.group())

# 2. Encontrar todos los números en un texto
texto2 = "Hay 3 gatos, 4 perros y 12 peces."
numeros = re.findall(r"\d+", texto2)
print("Números encontrados:", numeros)

# 3. Reemplazar texto usando una expresión regular
oracion = "La contraseña es secreta"
nueva = re.sub(r"secreta", "********", oracion)
print("Texto censurado:", nueva)

# 4. Validar un correo electrónico (forma básica)
correo = "ejemplo@correo.com"
patron_correo = r"^[\w\.-]+@[\w\.-]+\.\w+$"
if re.match(patron_correo, correo):
    print("Correo válido:", correo)
else:
    print("Correo inválido")

# 5. Dividir un texto usando un separador (como split pero con regex)
frase = "uno, dos; tres/cuatro"
palabras = re.split(r"[,;/]+", frase)
print("Palabras separadas:", palabras)

print("\nFin del script re.")
