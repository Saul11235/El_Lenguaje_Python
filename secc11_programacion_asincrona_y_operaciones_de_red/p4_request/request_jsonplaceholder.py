import requests

# URL de la API 
url = 'https://jsonplaceholder.typicode.com/posts/1'

# Hacer una solicitud GET
response = requests.get(url)

# Verificar que la solicitud fue exitosa
if response.status_code == 200:
    datos = response.json()  # Convertir JSON a diccionario de Python
    print("\nTítulo del post:", datos['title'])
    print("\nContenido:", datos['body'])
else:
    print("\nError al hacer la solicitud:", response.status_code)
