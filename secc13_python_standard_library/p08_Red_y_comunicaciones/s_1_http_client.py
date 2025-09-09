
import http.client

# 1. Conectarse a un servidor (ejemplo: www.python.org)
conn = http.client.HTTPSConnection("www.python.org")

# 2. Enviar una solicitud GET a la ruta "/"
conn.request("GET", "/")

# 3. Obtener la respuesta del servidor
respuesta = conn.getresponse()

# 4. Mostrar código de estado y razón
print("Código de estado:", respuesta.status)
print("Razón:", respuesta.reason)

# 5. Leer y mostrar parte del contenido (cuerpo de la respuesta)
contenido = respuesta.read()
print("Contenido (primeros 300 bytes):")
print(contenido[:300].decode("utf-8", errors="ignore"))  # Mostrar solo parte y evitar errores de codificación

# 6. Cerrar la conexión
conn.close()

print("\nFin del script http.client.")
