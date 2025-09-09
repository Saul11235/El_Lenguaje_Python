
import json

# 1. Diccionario Python
datos = {
    "nombre": "Ana",
    "edad": 28,
    "ciudad": "Madrid",
    "hobbies": ["leer", "viajar", "programar"],
    "casada": False
}

# 2. Convertir diccionario a cadena JSON (serializar)
json_str = json.dumps(datos)
print("Datos en formato JSON (string):")
print(json_str)
print()

# 3. Convertir JSON (string) a diccionario Python (deserializar)
datos_cargados = json.loads(json_str)
print("Datos cargados desde JSON (diccionario):")
print(datos_cargados)
print()

# 4. Guardar JSON en archivo
with open('datos.json', 'w') as f:
    json.dump(datos, f)

# 5. Leer JSON desde archivo
with open('datos.json', 'r') as f:
    datos_archivo = json.load(f)
print("Datos leídos desde archivo JSON:")
print(datos_archivo)
print()

# 6. Serializar con indentación para mejor legibilidad
json_legible = json.dumps(datos, indent=4)
print("JSON con indentación:")
print(json_legible)

print("\nFin del script json.")
