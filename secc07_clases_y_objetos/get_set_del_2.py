# Ejemplo 2 getters setters deleters
#----------------------------

class persona:
    def __init__(self, nombre):self._nombre = nombre 

    @property      #  Getter
    def nombre(self):
        print("Obteniendo el nombre...")
        return self._nombre

    @nombre.setter  # Setter
    def nombre(self, nuevo_nombre):
        print("Asignando nuevo nombre...")
        if nuevo_nombre != "": self._nombre = nuevo_nombre
        else:  print("Nombre inválido")

    @nombre.deleter  #  Deleter
    def nombre(self):
        print("Eliminando el nombre...")
        del self._nombre
#----------------------------

# Ejemplo de uso de atributos a traves de metodos controlados

p = persona("Jose")

# obtener el valor de un atributo y manipularlo

print(p.nombre)
p.nombre+=" Luis"

# obtener el atributo modificado
print(p.nombre)




