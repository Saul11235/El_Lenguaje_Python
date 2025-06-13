# NIVEL DE ACCESO
#
# Define una excepción personalizada 
# AccesoDenegadoError. Luego crea una función 
# acceder_al_sistema(nivel) que reciba un número 
# entre 1 y 5. Si nivel es menor que 3, lanza 
# AccesoDenegadoError con un mensaje.
# Si es válido, devuelve "Acceso autorizado".
#

# Definimos una excepción personalizada
class AccesoDenegadoError(Exception):
    """Excepción lanzada cuando el nivel de acceso es insuficiente."""
    pass

# Función que valida el nivel de acceso
def acceder_al_sistema(nivel):
    if nivel < 3:
        # Lanzamos nuestra excepción personalizada
        raise AccesoDenegadoError("Acceso denegado: nivel insuficiente.")
    else:
        return "Acceso autorizado"

# Ejemplos de uso
try:
    print(acceder_al_sistema(4))  # Acceso autorizado
    print(acceder_al_sistema(2))  # Lanza AccesoDenegadoError
except AccesoDenegadoError as error:
    print("Error:", error)
