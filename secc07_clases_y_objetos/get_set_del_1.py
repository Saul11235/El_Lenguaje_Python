# Ejemplo 1 getters setters deleters
#----------------------------

class persona:
    def __init__(self, nombre):self._nombre = nombre 
 
    def getNombre(self):
        print("Obteniendo el nombre...")
        return self._nombre
 
    def setNombre(self, nuevo_nombre):
        print("Asignando nuevo nombre...")
        if nuevo_nombre!="": self._nombre = nuevo_nombre
        else:  print("Nombre inválido")
 
    def delNombre(self):
        print("Eliminando el nombre...")
        del self._nombre

#----------------------------

# Ejemplo de uso de atributos a traves de metodos controlados

p = persona("Jose")

# obtener el valor de un atributo y manipularlo
nombre=p.getNombre()
nombre=nombre.upper()
nombre+=" Luis"

# configurar el atributo
p.setNombre(nombre)

# obtener el atributo modificado
print(p.getNombre())



