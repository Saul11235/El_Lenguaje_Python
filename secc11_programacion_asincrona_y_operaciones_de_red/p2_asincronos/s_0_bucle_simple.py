
from time import sleep

# Función para imprimir "Hola cada 10 segundos"
def saludo_10_segundos():
    for _ in range(5):  # Ejecutará el bucle 5 veces
        print(f"bucle simple    : A.{_} : Hola cada 10 segundos")
        sleep(10)

# Función para imprimir "Hola cada 7 segundos"
def saludo_7_segundos():
    for _ in range(5):  # Ejecutará el bucle 5 veces
        print(f"bucle simple    : B.{_} : Hola cada  7 segundos")
        sleep(7)

# Función principal que ejecuta ambos bucles simultáneamente

saludo_10_segundos()
saludo_7_segundos()


input("\nFin bucles simples\n")
