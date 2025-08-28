
import asyncio

# Lista para llevar el control de cronómetros activos
cronometros_activos = []

async def cronometro(duracion, mensaje, id_crono):
    print(f"[{id_crono}] Cronómetro iniciado por {duracion} segundos.")
    await asyncio.sleep(duracion)
    print(f"[{id_crono}] Tiempo cumplido → {mensaje}")

async def entrada_usuario():
    print("Ingresa cronómetros en formato: <segundos> <mensaje>")
    print("Ejemplo: 5 café listo")
    print("Escribe 'exit' para salir.\n")

    loop = asyncio.get_event_loop()
    id_global = 1

    while True:
        linea = await loop.run_in_executor(None, input, "> ")

        if linea.strip().lower() == "exit":
            print("Saliendo... Esperando cronómetros activos.")
            break

        try:
            partes = linea.strip().split(" ", 1)
            duracion = int(partes[0])
            mensaje = partes[1] if len(partes) > 1 else "¡Tiempo cumplido!"

            id_crono = f"cron{id_global}"
            id_global += 1

            tarea = asyncio.create_task(cronometro(duracion, mensaje, id_crono))
            cronometros_activos.append(tarea)
        except (ValueError, IndexError):
            print("[!] Formato incorrecto. Usa: <segundos> <mensaje>")

    # Esperar que todos los cronómetros terminen
    if cronometros_activos:
        await asyncio.gather(*cronometros_activos)

async def main():
    await entrada_usuario()

if __name__ == "__main__":
    input('\n Ejemplo cronometro\n')
    asyncio.run(main())
