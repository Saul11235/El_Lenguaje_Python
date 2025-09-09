
import cmath

# 1. Crear un número complejo
z = 2 + 3j
print("Número complejo z:", z)

# 2. Obtener la parte real e imaginaria
print("Parte real de z:", z.real)
print("Parte imaginaria de z:", z.imag)

# 3. Módulo (magnitud) y fase (ángulo)
modulo = abs(z)
fase = cmath.phase(z)
print("Módulo de z:", modulo)
print("Fase (ángulo en radianes) de z:", fase)

# 4. Convertir fase a grados
grados = cmath.phase(z) * 180 / cmath.pi
print("Fase en grados:", grados)

# 5. Conjugado de un número complejo
conjugado = z.conjugate()
print("Conjugado de z:", conjugado)

# 6. Operaciones trigonométricas con números complejos
print("Seno de z:", cmath.sin(z))
print("Coseno de z:", cmath.cos(z))
print("Tangente de z:", cmath.tan(z))

# 7. Logaritmo y raíz cuadrada de un número complejo
print("Logaritmo natural de z:", cmath.log(z))
print("Raíz cuadrada de z:", cmath.sqrt(z))

# 8. Exponencial
print("Exponencial de z:", cmath.exp(z))

print("\nFin del script cmath.")
