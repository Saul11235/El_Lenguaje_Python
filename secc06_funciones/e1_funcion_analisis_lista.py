# FUNCION ANALISIS LISTA
#
# Dado una lista de números enteros, escribe 
# una función que devuelva una nueva lista 
# que contenga los números de la lista original 
# elevados al cuadrado, pero solo aquellos números
# que sean impares. Usa una función lambda 
# junto con filter() y map() para resolverlo
#


# Lista original
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# definiendo funcion
def analisis(lista):
    numeros_impares = filter(lambda x: x % 2 != 0, lista)
    resultado = map(lambda x: x ** 2, numeros_impares)
    return list(resultado)

# Imprimir el resultado
print(numeros)
print(analisis(numeros))

