
import threading
import os
import csv

# Diccionario global para almacenar resultados
resultados = {}
lock = threading.Lock()  # Para acceso seguro a resultados

def procesar_csv(ruta_archivo):
    try:
        with open(ruta_archivo, 'r') as f:
            lector = csv.reader(f)
            numeros = [float(fila[0]) for fila in lector if fila]  # ignorar filas vacías

        suma = sum(numeros)
        promedio = suma / len(numeros) if numeros else 0
        maximo = max(numeros) if numeros else None

        with lock:
            resultados[os.path.basename(ruta_archivo)] = {
                'suma': suma,
                'promedio': promedio,
                'maximo': maximo
            }

    except Exception as e:
        with lock:
            resultados[os.path.basename(ruta_archivo)] = {
                'error': str(e)
            }

def main():
    directorio = 'datos'  # Puedes cambiar este nombre de carpeta
    if not os.path.isdir(directorio):
        print(f"El directorio '{directorio}' no existe.")
        return

    archivos = [f for f in os.listdir(directorio) if f.endswith('.txt')]
    if not archivos:
        print("No se encontraron archivos de texto en el directorio.")
        return

    hilos = []
    for archivo in archivos:
        ruta_completa = os.path.join(directorio, archivo)
        hilo = threading.Thread(target=procesar_csv, args=(ruta_completa,))
        hilo.start()
        hilos.append(hilo)

    for hilo in hilos:
        hilo.join()

    print("\n--- Resultados Consolidados ---")
    for archivo, datos in resultados.items():
        print(f"\nArchivo: {archivo}")
        if 'error' in datos:
            print(f"  Error: {datos['error']}")
        else:
            print(f"  Suma: {datos['suma']}")
            print(f"  Promedio: {datos['promedio']}")
            print(f"  Máximo: {datos['maximo']}")

if __name__ == '__main__':
    main()
