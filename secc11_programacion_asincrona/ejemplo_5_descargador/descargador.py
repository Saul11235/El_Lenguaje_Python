#
#  DESCARGADOR SITIOS WEB
#
# Cree un programa que lea una lista de URLs 
# desde un archivo de texto plano (urls.txt). 
# Cada línea del archivo contiene una URL. Use un hilo 
# por cada descarga para descargar las páginas y guardar 
# su contenido en archivos de texto individuales 
# (pagina_1.html, pagina_2.html, etc.).


import threading
import requests

def descargar_pagina(url, numero):
    try:
        print(f"Descargando {url} ...")
        respuesta = requests.get(url, timeout=10)
        nombre_archivo = f"pagina_{numero}.html"
        with open(nombre_archivo, 'w', encoding='utf-8') as archivo:
            archivo.write(respuesta.text)
        print(f"Guardado en {nombre_archivo}")
    except Exception as e:
        print(f"Error al descargar {url}: {e}")

def main():
    try:
        with open('urls.txt', 'r') as archivo:
            urls = [linea.strip() for linea in archivo if linea.strip()]
    except FileNotFoundError:
        print("El archivo 'urls.txt' no existe.")
        return

    hilos = []
    for i, url in enumerate(urls, start=1):
        hilo = threading.Thread(target=descargar_pagina, args=(url, i))
        hilo.start()
        hilos.append(hilo)

    for hilo in hilos:
        hilo.join()

    print("Descarga finalizada.")

if __name__ == '__main__':
    main()
