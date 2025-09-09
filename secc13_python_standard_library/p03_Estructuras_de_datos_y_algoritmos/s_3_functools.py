
import functools

# 1. functools.partial: crea una nueva función con algunos argumentos "predefinidos"
def potencia(base, exponente):
    return base ** exponente

# Crear función cuadrado (exponente=2) usando partial
cuadrado = functools.partial(potencia, exponente=2)
print("5 al cuadrado:", cuadrado(5))  # base=5

# Crear función cubo (exponente=3)
cubo = functools.partial(potencia, exponente=3)
print("2 al cubo:", cubo(2))
print()

# 2. functools.lru_cache: memoriza (cachea) resultados de función para evitar cálculos repetidos
@functools.lru_cache(maxsize=32)
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print("Fibonacci de 10:", fibonacci(10))
print("Fibonacci de 15:", fibonacci(15))
print()

# 3. functools.wraps: decorador para preservar metadata de funciones decoradas
def mi_decorador(func):
    @functools.wraps(func)
    def envoltura(*args, **kwargs):
        print(f"Llamando a {func.__name__}")
        return func(*args, **kwargs)
    return envoltura

@mi_decorador
def saludar(nombre):
    "Saluda a la persona pasada como argumento"
    print(f"Hola, {nombre}!")

saludar("Ana")
print("Nombre de la función:", saludar.__name__)
print("Docstring:", saludar.__doc__)

print("\nFin del script functools.")
