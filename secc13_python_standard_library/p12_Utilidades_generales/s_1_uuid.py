
import uuid

# 1. Generar un UUID aleatorio (versión 4)
id_aleatorio = uuid.uuid4()
print("UUID aleatorio (v4):", id_aleatorio)

# 2. Generar un UUID basado en el nombre y espacio (v3 o v5)
namespace = uuid.NAMESPACE_DNS
nombre = "openai.com"
id_nombre_v3 = uuid.uuid3(namespace, nombre)
id_nombre_v5 = uuid.uuid5(namespace, nombre)

print("UUID basado en nombre (v3):", id_nombre_v3)
print("UUID basado en nombre (v5):", id_nombre_v5)

# 3. Convertir UUID a string
print("UUID como string:", str(id_aleatorio))

# 4. Crear UUID a partir de un string (parsing)
id_parseado = uuid.UUID(str(id_aleatorio))
print("UUID parseado:", id_parseado)

print("\nFin del script uuid.")
