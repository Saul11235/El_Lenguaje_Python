import multiprocessing
import time

# Función para imprimir "Hola cada 10 segundos"
def saludo_10_segundos():
    for _ in range(5):  # Ejecutará el bucle 5 veces
        print(f"multiprocessing : A.{_} : Hola cada 10 segundos")
        time.sleep(10)  # Pausa de 10 segundos

# Función para imprimir "Hola cada 7 segundos"
def saludo_7_segundos():
    for _ in range(5):  # Ejecutará el bucle 5 veces
        print(f"multiprocessing : B.{_} : Hola cada 7  segundos")
        time.sleep(7)  # Pausa de 7 segundos

# Este bloque solo se ejecutará en el proceso principal
if __name__ == "__main__":
    # Crear los procesos
    proceso_10_segundos = multiprocessing.Process(target=saludo_10_segundos)
    proceso_7_segundos = multiprocessing.Process(target=saludo_7_segundos)

    # Iniciar los procesos
    proceso_10_segundos.start()
    proceso_7_segundos.start()

    # Esperar a que ambos procesos terminen
    proceso_10_segundos.join()
    proceso_7_segundos.join()

    input("\nFin multiprocessing\n")

