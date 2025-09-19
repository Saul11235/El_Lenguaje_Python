
# Definir los números complejos
z1 = 3 + 4j  # 3 es la parte real, 4 es la parte imaginaria
z2 = 2 - 5j  # 2 es la parte real, -5 es la parte imaginaria
z1 = complex(3, 4)  # 3 es la parte real, 4 es la parte imaginaria
z2 = complex(2, -5)  # 2 es la parte real, -5 es la parte imaginaria

# Operaciones aritméticas
suma = z1 + z2              # Suma de números complejos
resta = z1 - z2             # Resta de números complejos
producto = z1 * z2          # Multiplicación de números complejos
division = z1 / z2          # División de números complejos

# Funciones especiales
modulo_z1 = abs(z1)         # Módulo (valor absoluto) de z1
modulo_z2 = abs(z2)         # Módulo (valor absoluto) de z2
conjugado_z1 = z1.conjugate()  # Conjugado de z1
conjugado_z2 = z2.conjugate()  # Conjugado de z2

# Imprimir resultados
print(f"Suma: {suma}")
print(f"Resta: {resta}")
print(f"Producto: {producto}")
print(f"División: {division}")
print(f"Módulo de z1: {modulo_z1}")
print(f"Módulo de z2: {modulo_z2}")
print(f"Conjugado de z1: {conjugado_z1}")
print(f"Conjugado de z2: {conjugado_z2}")
