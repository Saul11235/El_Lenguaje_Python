import requests

# URL de la API de SpaceX para el próximo lanzamiento
url = 'https://api.spacexdata.com/v4/launches/next'

# Hacer la solicitud GET
response = requests.get(url)

# Verificar que fue exitosa
if response.status_code == 200:
    datos = response.json()

    nombre = datos['name']
    fecha = datos['date_utc']
    detalles = datos.get('details', 'Sin detalles disponibles.')

    print(f"Próximo lanzamiento: {nombre}")
    print(f"Fecha (UTC): {fecha}")
    print(f"Detalles: {detalles}")

else:
    print("Error al obtener los datos:", response.status_code)
