
import calendar

# 1. Mostrar un calendario mensual como texto
print("Calendario de septiembre 2025:")
print(calendar.month(2025, 9))

# 2. Mostrar calendario anual completo
print("Calendario completo del año 2025:")
print(calendar.calendar(2025))

# 3. Saber si un año es bisiesto
print("¿2024 es bisiesto?", calendar.isleap(2024))
print("¿2025 es bisiesto?", calendar.isleap(2025))

# 4. Cuántos días tiene febrero de 2024 (bisiesto)
dias_en_febrero = calendar.monthrange(2024, 2)
print("Febrero 2024: empieza en día", dias_en_febrero[0], "y tiene", dias_en_febrero[1], "días")

# 5. Saber qué día de la semana cae una fecha (lunes=0, domingo=6)
dia_semana = calendar.weekday(2025, 9, 5)
print("El 5 de septiembre de 2025 cae en:", calendar.day_name[dia_semana])

# 6. Mostrar nombres de los días y meses
print("Nombres de los días de la semana:")
print(list(calendar.day_name))

print("Nombres de los meses:")
print(list(calendar.month_name))

# 7. Crear un calendario como lista de semanas (cada semana es una lista de días)
print("Calendario estructurado de septiembre 2025:")
estructura = calendar.monthcalendar(2025, 9)
for semana in estructura:
    print(semana)

print("\nFin del script calendar.")
