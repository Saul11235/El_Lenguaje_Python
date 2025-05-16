# ejemplo de codigo

class persona:
    nombre    = '' 
    edad      = 0
    direccion = '' 

    def saludar(self):
        print('hola me llamo', self.nombre)

    def datos(self):
        print('Nombre:', self.nombre)
        print('Edad:', self.edad)
        print('Direccion:', self.direccion)

    def esMayorQue(self,otraEdad):
        if   otraEdad>self.edad :print('es mayor')
        elif otraEdad<self.edad :print('es menor')
        else:  print('tienen la misma edad') 


obj1 = persona()
obj1.nombre    = 'Pedro Perez'
obj1.edad      =  25
obj1.direccion = 'Calle rosas 25'

obj2 = persona()
obj2.nombre    = 'Ana Tapia'
obj2.edad      =  8
obj2.direccion = 'Pasaje geranios 14'

obj3 = persona()
obj3.nombre    = 'Mario Farfan'
obj3.edad      =  50
obj3.direccion = 'Jirón margaritas 93'



obj1.saludar()
obj2.saludar()
obj3.saludar()

print('')

obj1.datos()
obj2.datos()
obj3.datos()

print('')

for x in range(0,50,5):
    obj1.esMayorQue(x)




