import requests
from random import choice

# URL de la API para buscar por nombre
pais = choice(["argentina","españa","peru","chile","mexico"])
url = f"https://restcountries.com/v3.1/name/{pais}"

# Hacer la solicitud GET
response = requests.get(url)

# Verificar que la solicitud fue exitosa
if response.status_code == 200:
    datos = response.json()[0]  # Tomamos el primer resultado de la lista

    nombre = datos['name']['common']
    capital = datos['capital'][0]
    poblacion = datos['population']
    region = datos['region']
    monedas = list(datos['currencies'].keys())

    print(f"País: {nombre}")
    print(f"Capital: {capital}")
    print(f"Población: {poblacion}")
    print(f"Región: {region}")
    print(f"Moneda(s): {', '.join(monedas)}")

else:
    print("Error al obtener los datos:", response.status_code)
