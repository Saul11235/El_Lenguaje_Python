# operador walrus :=
# introducido desde python 3.8
# sirve para declarar una variable 
# al mismo tiempo que se define un argumento
# sirve para evitar crear codigo redundante


def miFuncion( miArgumento):
    print("llamado desde funcion:",miArgumento)

# en este ejemplo definiremos una función al
# mismo tiempo que declaramos un argumento

miFuncion( miVariable:="contenido")

# miVariable se ha creado al ser
# definida en un argumento

print(miVariable)

