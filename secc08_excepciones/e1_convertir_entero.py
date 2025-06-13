# CONVERTIR ENTERO
#
# Escribe una función convertir_a_entero(valor) 
# que intente convertir el argumento valor a entero. 
# Si no puede (por ejemplo si recibe "hola"), 
# debe manejar la excepción y devolver
# "No se pudo convertir a entero".
#

def convertir_a_entero(valor):
    try:
        # Intentamos convertir el valor a entero
        resultado = int(valor)
        return resultado
    except ValueError:
        # Si ocurre un ValueError (por ejemplo si valor es "hola"), se maneja aquí
        return "No se pudo convertir a entero"

# Ejemplos de uso:
print(convertir_a_entero("123"))   # 123
print(convertir_a_entero("hola"))  # No se pudo convertir a entero
print(convertir_a_entero(45.6))    # 45 (trunca el decimal)
