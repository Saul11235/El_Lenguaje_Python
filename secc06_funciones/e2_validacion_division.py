# VALIDACION DE NUMEROS DE UNA DIVISION
#
# Crea un decorador que valide los parámetros 
# de una función que calcula la división de 
# dos números. El decorador debe asegurarse 
# de que el denominador no sea cero. Si el 
# denominador es cero, debe devolver un mensaje 
# de error indicando que no se puede dividir por cero.

# Decorador que valida que el denominador no sea cero
def validar_denominador(func):
    def envoltorio(a, b):
        if b == 0:
            return "No se puede dividir por cero"
        return func(a, b)
    return envoltorio

# Función que divide dos números, decorada con el decorador de validación
@validar_denominador
def dividir(a, b):
    return a / b

# Prueba de la función con un denominador válido
resultado = dividir(10, 2)
print(resultado)  # Salida: 5.0

# Prueba de la función con un denominador inválido (cero)
resultado = dividir(10, 0)
print(resultado)  # Salida: No se puede dividir por cero
