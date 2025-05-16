# Herencia 2
#-----------------------

# creando clases animal y volador
class animal:
    def __init__(self,nombre): self.nombre=nombre
    def comer(self):           print(f'{self.nombre} esta comiendo')

#-----------------------

class volador: 
    def volar(self):           print('esta volando por los cielos')

#-----------------------

# creando clase ave que heredará de animal y volador
class ave(animal,volador): 
    def cantar(self):          print(f'{self.nombre} esta cantando')

# definiendo objetos

pajarito = ave('gorrion')

pajarito.comer()
pajarito.volar()
pajarito.cantar()


