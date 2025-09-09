
import textwrap

# Texto largo sin formato
texto = """
Python es un lenguaje de programación interpretado cuya filosofía hace hincapié en la legibilidad de su código.
Se trata de un lenguaje multiparadigma, ya que soporta orientación a objetos, programación imperativa y funcional.
"""

# 1. Ajustar el texto a un ancho específico (wrap)
envuelto = textwrap.fill(texto, width=50)
print("Texto envuelto (máx. 50 caracteres por línea):")
print(envuelto)

# 2. Agregar sangría inicial a cada línea
sangrado = textwrap.indent(envuelto, prefix="→ ")
print("\nTexto con sangría:")
print(sangrado)

# 3. Quitar sangría de líneas (dedent)
con_sangria = "    Línea 1\n    Línea 2\n    Línea 3"
sin_sangria = textwrap.dedent(con_sangria)
print("\nTexto original con sangría:\n", con_sangria)
print("Texto sin sangría:\n", sin_sangria)

# 4. Acortar texto largo con "..."
resumen = textwrap.shorten(texto, width=60, placeholder="...")
print("\nTexto resumido con shorten:")
print(resumen)

# 5. Convertir texto a lista de líneas
lineas = textwrap.wrap(texto, width=40)
print("\nTexto como lista de líneas (máx. 40 caracteres):")
for linea in lineas:
    print(linea)

print("\nFin del script textwrap.")
