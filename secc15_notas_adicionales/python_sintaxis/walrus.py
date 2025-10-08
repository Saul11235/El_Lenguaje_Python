# operador walrus :=
# introducido desde python 3.8
# PEP 572
# sirve para declarar una variable 
# al mismo tiempo que se define un argumento
# sirve para evitar crear codigo redundante

def miFuncion( miArgumento):
    print("llamado desde funcion:",miArgumento)

# antes analicemos cómo se hacían las asignaciones antes del walrus

var1 = "contenido 1"
miFuncion( var1 )
print(var1)


# en este ejemplo definiremos una función al
# mismo tiempo que declaramos un argumento

miFuncion ( var2 :=  "contenido 2")
print( var2 )






