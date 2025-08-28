
import asyncio

# Función asíncrona para imprimir "Hola cada 10 segundos"
async def saludo_10_segundos():
    for _ in range(5):  # Ejecutará el bucle 5 veces
        print(f"bucle asyncio   : A.{_} : Hola cada 10 segundos")
        await asyncio.sleep(10)

# Función asíncrona para imprimir "Hola cada 7 segundos"
async def saludo_7_segundos():
    for _ in range(5):  # Ejecutará el bucle 5 veces
        print(f"bucle asyncio   : B.{_} : Hola cada  7 segundos")
        await asyncio.sleep(7)

# Función principal que ejecuta ambos bucles simultáneamente
async def main():
    # Ejecuta las dos funciones en paralelo
    await asyncio.gather(
        saludo_10_segundos(),
        saludo_7_segundos()
    )

# Ejecutar el programa
asyncio.run(main())

input("\nFin ciclo asyncio\n")
