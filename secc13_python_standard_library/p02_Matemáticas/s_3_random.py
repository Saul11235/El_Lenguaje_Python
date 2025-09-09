
import random

# 1. Número aleatorio entre 0 y 1 (float)
print("Número aleatorio entre 0 y 1:", random.random())

# 2. Número entero aleatorio entre dos valores (incluye ambos)
print("Número entero aleatorio entre 1 y 10:", random.randint(1, 10))

# 3. Número entero aleatorio en rango (sin incluir el último)
print("Número entero aleatorio entre 0 y 9:", random.randrange(10))

# 4. Elegir un elemento aleatorio de una lista
frutas = ["manzana", "banana", "naranja", "pera"]
eleccion = random.choice(frutas)
print("Fruta aleatoria elegida:", eleccion)

# 5. Elegir múltiples elementos aleatorios (sin repetición)
seleccionadas = random.sample(frutas, 2)
print("Frutas seleccionadas (2 sin repetición):", seleccionadas)

# 6. Mezclar aleatoriamente una lista (in-place)
print("Lista original:", frutas)
random.shuffle(frutas)
print("Lista mezclada:", frutas)

# 7. Número aleatorio con distribución gaussiana (normal)
num_gauss = random.gauss(mu=0, sigma=1)  # media 0, desviación estándar 1
print("Número con distribución gaussiana:", num_gauss)

# 8. Semilla para reproducibilidad
random.seed(123)
print("Número aleatorio con semilla 123:", random.random())

print("\nFin del script random.")
