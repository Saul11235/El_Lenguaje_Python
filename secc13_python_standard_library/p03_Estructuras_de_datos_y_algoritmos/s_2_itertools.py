
import itertools

# 1. count: genera números infinitos empezando desde un número dado
print("Contador infinito (mostrando los primeros 5 números empezando en 10):")
contador = itertools.count(10)
for _ in range(5):
    print(next(contador), end=' ')
print('\n')

# 2. cycle: cicla infinitamente sobre una secuencia
colores = ['rojo', 'verde', 'azul']
ciclo = itertools.cycle(colores)
print("Ciclo infinito sobre la lista de colores (primeros 7 elementos):")
for _ in range(7):
    print(next(ciclo), end=' ')
print('\n')

# 3. repeat: repite un objeto un número específico de veces (o infinito si no se indica)
print("Repetir 'Hola' 3 veces:")
for x in itertools.repeat('Hola', 3):
    print(x)

# 4. chain: encadena varias iterables en una sola secuencia
lista1 = [1, 2, 3]
lista2 = ['a', 'b', 'c']
combinada = itertools.chain(lista1, lista2)
print("\nEncadenar listas 1 y 2:")
for elem in combinada:
    print(elem, end=' ')
print('\n')

# 5. combinations: combina elementos sin repetir, el orden no importa
letras = ['A', 'B', 'C']
print("Combinaciones de 2 letras:")
for combo in itertools.combinations(letras, 2):
    print(combo)

# 6. permutations: permutaciones donde el orden sí importa
print("\nPermutaciones de 2 letras:")
for perm in itertools.permutations(letras, 2):
    print(perm)

# 7. product: producto cartesiano (combinaciones con repetición)
print("\nProducto cartesiano de letras con repetición 2:")
for prod in itertools.product(letras, repeat=2):
    print(prod)

# 8. islice: cortar iteradores (como slicing para listas)
print("\nPrimeros 4 números de count empezando en 100 (usando islice):")
for num in itertools.islice(itertools.count(100), 4):
    print(num)

print("\nFin del script itertools.")
