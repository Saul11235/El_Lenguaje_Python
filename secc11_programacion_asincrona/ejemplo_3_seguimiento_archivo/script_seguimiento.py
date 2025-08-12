
import asyncio
import os

ARCHIVO = "archivo.txt"

def contar_palabras_y_hola(texto):
    palabras = texto.split()
    total = len(palabras)
    hola_count = sum(1 for p in palabras if p.lower() == "hola")
    return total, hola_count

def leer_archivo():
    try:
        with open(ARCHIVO, 'r', encoding='utf-8') as f:
            return f.read()
    except Exception:
        return ""

async def seguimiento_archivo():
    if not os.path.exists(ARCHIVO):
        open(ARCHIVO, 'w').close()

    contenido_anterior = ""

    while True:
        contenido = await asyncio.to_thread(leer_archivo)

        if contenido != contenido_anterior:
            total, hola = contar_palabras_y_hola(contenido)
            print(f"\nArchivo actualizado:")
            print(f"Total de palabras: {total}")
            print(f"'hola' aparece: {hola} veces")
            contenido_anterior = contenido

        await asyncio.sleep(1)

async def main():
    await seguimiento_archivo()

if __name__ == "__main__":
    asyncio.run(main())
