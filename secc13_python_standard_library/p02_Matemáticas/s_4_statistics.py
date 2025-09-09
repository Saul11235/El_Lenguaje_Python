
import statistics

# Datos de ejemplo
datos = [10, 15, 20, 15, 30, 25, 15, 10]

# 1. Media aritmética
media = statistics.mean(datos)
print("Media:", media)

# 2. Mediana (valor central)
mediana = statistics.median(datos)
print("Mediana:", mediana)

# 3. Moda (valor más frecuente)
moda = statistics.mode(datos)
print("Moda:", moda)

# 4. Media geométrica (producto de datos, ideal para tasas de crecimiento)
media_geometrica = statistics.geometric_mean(datos)
print("Media geométrica:", media_geometrica)

# 5. Media armónica (ideal para promedios de velocidades)
media_armonica = statistics.harmonic_mean(datos)
print("Media armónica:", media_armonica)

# 6. Varianza (medida de dispersión)
varianza = statistics.variance(datos)
print("Varianza:", varianza)

# 7. Desviación estándar
desviacion = statistics.stdev(datos)
print("Desviación estándar:", desviacion)

# 8. Datos agrupados: calcular mediana baja y mediana alta (en caso de datos pares)
mediana_baja = statistics.median_low(datos)
mediana_alta = statistics.median_high(datos)
print("Mediana baja:", mediana_baja)
print("Mediana alta:", mediana_alta)

print("\nFin del script statistics.")
