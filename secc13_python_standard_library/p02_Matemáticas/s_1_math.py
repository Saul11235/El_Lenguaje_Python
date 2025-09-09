
import math

# 1. Constantes matemáticas
print("Constantes:")
print("π (pi):", math.pi)
print("e (número de Euler):", math.e)
print()

# 2. Raíz cuadrada
print("Raíz cuadrada de 25:", math.sqrt(25))

# 3. Potencias
print("2 elevado a la 3:", math.pow(2, 3))  # Devuelve float
print("2 ** 3 (nativo de Python):", 2 ** 3)  # Devuelve int si posible
print()

# 4. Valor absoluto
print("Valor absoluto de -10:", math.fabs(-10))

# 5. Redondeo hacia abajo y hacia arriba
print("Redondeo hacia abajo (floor) de 3.9:", math.floor(3.9))
print("Redondeo hacia arriba (ceil) de 3.1:", math.ceil(3.1))
print()

# 6. Logaritmos
print("Logaritmo base e de 10:", math.log(10))  # Natural
print("Logaritmo base 10 de 1000:", math.log10(1000))
print()

# 7. Trigonometría (en radianes)
angulo_rad = math.radians(90)  # Convierte 90 grados a radianes
print("Seno de 90°:", math.sin(angulo_rad))
print("Coseno de 90°:", math.cos(angulo_rad))
print("Tangente de 90°:", math.tan(angulo_rad))
print()

# 8. Factorial
print("Factorial de 5:", math.factorial(5))

# 9. Máximo común divisor (GCD)
print("MCD de 12 y 18:", math.gcd(12, 18))

# 10. Funciones hipotenusa y distancia
print("Hipotenusa de triángulo (3, 4):", math.hypot(3, 4))  # Equivale a sqrt(3² + 4²)

print("\nFin del script math.")
