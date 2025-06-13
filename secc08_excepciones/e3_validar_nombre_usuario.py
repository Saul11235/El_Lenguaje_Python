# VALIDAR NOMBRE USUARIO
#
# Crea una función validar_usuario(nombre) 
# que reciba un string. Si el nombre tiene 
# menos de 3 caracteres, lanza un ValueError 
# con el mensaje "El nombre es demasiado corto".
# Si es válido, devuelve "Nombre aceptado".
# 

def validar_usuario(nombre):
    if len(nombre) < 3:
        # Lanzamos una excepción si el nombre es demasiado corto
        raise ValueError("El nombre es demasiado corto")
    else:
        return "Nombre aceptado"

# Ejemplos de uso:
try:
    print(validar_usuario("Ana"))     # Nombre aceptado
    print(validar_usuario("Jo"))      # Lanza ValueError
except ValueError as error:
    print("Error:", error)
