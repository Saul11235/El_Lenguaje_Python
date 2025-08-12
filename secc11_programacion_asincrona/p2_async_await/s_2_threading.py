
import threading
import time

# Función para imprimir "Hola cada 10 segundos"
def saludo_10_segundos():
    for _ in range(5):  # Ejecutará el bucle 5 veces
        print(f"bucle threading : A.{_} : Hola cada 10 segundos")
        time.sleep(10)  # Pausa de 10 segundos

# Función para imprimir "Hola cada 7 segundos"
def saludo_7_segundos():
    for _ in range(5):  # Ejecutará el bucle 5 veces
        print(f"bucle threading : B.{_} : Hola cada 7  segundos")
        time.sleep(7)  # Pausa de 7 segundos

# Crear los hilos
hilo_10_segundos = threading.Thread(target=saludo_10_segundos)
hilo_7_segundos = threading.Thread(target=saludo_7_segundos)

# Iniciar los hilos
hilo_10_segundos.start()
hilo_7_segundos.start()

# Esperar a que ambos hilos terminen
hilo_10_segundos.join()
hilo_7_segundos.join()

input("\nFin ciclo threading\n")
