
from datetime import datetime, date, time, timedelta

# 1. Obtener la fecha y hora actual
ahora = datetime.now()
print("Fecha y hora actual:", ahora)

# 2. Crear una fecha específica
cumple = date(1995, 9, 5)
print("Cumpleaños:", cumple)

# 3. Crear una hora específica
hora = time(14, 30)
print("Hora específica:", hora)

# 4. Acceder a componentes de una fecha/hora
print("Año:", ahora.year)
print("Mes:", ahora.month)
print("Día:", ahora.day)
print("Hora:", ahora.hour)
print("Minuto:", ahora.minute)
print("Segundo:", ahora.second)

# 5. Formatear fecha/hora como texto
formateado = ahora.strftime("%d/%m/%Y %H:%M:%S")
print("Fecha formateada:", formateado)

# 6. Parsear texto a objeto datetime
texto = "2025-09-05 18:45"
convertido = datetime.strptime(texto, "%Y-%m-%d %H:%M")
print("Texto convertido a datetime:", convertido)

# 7. Operaciones con fechas (timedelta)
mañana = ahora + timedelta(days=1)
ayer = ahora - timedelta(days=1)
print("Mañana será:", mañana)
print("Ayer fue:", ayer)

# 8. Diferencia entre fechas
navidad = date(2025, 12, 25)
hoy = date.today()
dias_para_navidad = (navidad - hoy).days
print("Días hasta Navidad:", dias_para_navidad)

print("\nFin del script datetime.")
