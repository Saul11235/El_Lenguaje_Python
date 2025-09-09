
import time

# 1. Obtener el tiempo actual en segundos desde el "epoch" (1 de enero de 1970)
timestamp = time.time()
print("Timestamp actual:", timestamp)

# 2. Convertir timestamp a estructura local
estructura_tiempo = time.localtime(timestamp)
print("Estructura local:", estructura_tiempo)

# 3. Formatear fecha legible desde estructura
formato_legible = time.strftime("%d/%m/%Y %H:%M:%S", estructura_tiempo)
print("Fecha formateada:", formato_legible)

# 4. Parsear string a estructura de tiempo
texto = "05/09/2025 18:30:00"
estructura_desde_texto = time.strptime(texto, "%d/%m/%Y %H:%M:%S")
print("Texto parseado a estructura:", estructura_desde_texto)

# 5. Pausar ejecución del programa por segundos
print("Esperando 2 segundos...")
time.sleep(2)
print("¡Listo!")

# 6. Medir cuánto tarda una operación
inicio = time.time()
for _ in range(1000000):
    pass  # Algo que tarda
fin = time.time()
print("Tiempo transcurrido:", fin - inicio, "segundos")

print("\nFin del script time.")
