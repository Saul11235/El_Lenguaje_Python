
import pickle

# 1. Crear un objeto Python complejo (diccionario con listas y tuplas)
datos = {
    'nombre': 'Carlos',
    'edad': 35,
    'intereses': ['fútbol', 'música', 'programación'],
    'activo': True
}

# 2. Serializar el objeto y guardarlo en un archivo binario
with open('datos.pkl', 'wb') as archivo:
    pickle.dump(datos, archivo)
print("Objeto serializado y guardado en 'datos.pkl'")

# 3. Leer el archivo y deserializar el objeto
with open('datos.pkl', 'rb') as archivo:
    datos_cargados = pickle.load(archivo)
print("Objeto cargado desde archivo:")
print(datos_cargados)

print("\nFin del script pickle.")
