# Herencia 1
#-----------------------

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

#-----------------------

class estudiante(persona):
    cursos    = []

    def matricular(self,curso):
        self.cursos.append(curso) 

    def verCursos(self):
        print('Cursos matriculados:')
        for x in self.cursos: print(' -', x) 

#-----------------------

est1 = estudiante()
est1.nombre    = 'Paola Guzman'
est1.edad      =  23
est1.direccion = 'Calle alegría 12'
est1.matricular ('Inglés')
est1.matricular ('Matemática')
est1.matricular ('Programación')
 
est2 = estudiante()
est2.nombre    = 'José Molina'
est2.edad      =  47
est2.direccion = 'Av. Manantial 35'
est2.matricular ('Inglés')
est2.matricular ('Dibujo técnico')
est2.matricular ('Programación')

#-----------------------
# podremos usar estos objetos en nuestro código

for alumno in [est1,est2]:
    alumno.saludar()  #clase persona
    alumno.verCursos() #clase estudiante
    


