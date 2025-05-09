#
# SOFTWARE DE MATRICULAS
#
# Cree sistema de clases que abstraigan 
# personas, hereden a 2 clases estudiantes 
# y profesores, una clase llamada curso, así
# cómo gestione los métodos para hacer las 
# consultas y generación de informes con listas 
# de estudiantes, generación de informes con 
# estudiantes por docente, y lista de cursos
# para cada estudiante.
#

# -------------------------------------------------------

class Persona:
    def __init__(self, nombre, dni):
        self.nombre = nombre
        self.dni = dni

    def __str__(self):
        return f"{self.nombre} ({self.dni})"

# -------------------------------------------------------

class Estudiante(Persona):
    def __init__(self, nombre, dni):
        super().__init__(nombre, dni)
        self.cursos = []

    def matricular(self, curso):
        if curso not in self.cursos:
            self.cursos.append(curso)
            curso.agregar_estudiante(self)

    def listar_cursos(self):
        return [curso.nombre for curso in self.cursos]

# -------------------------------------------------------

class Profesor(Persona):
    def __init__(self, nombre, dni):
        super().__init__(nombre, dni)
        self.cursos = []

    def asignar_curso(self, curso):
        if curso not in self.cursos:
            self.cursos.append(curso)
            curso.asignar_profesor(self)

    def estudiantes_por_docente(self):
        estudiantes = set()
        for curso in self.cursos:
            estudiantes.update(curso.estudiantes)
        return list(estudiantes)

# -------------------------------------------------------

class Curso:
    def __init__(self, nombre):
        self.nombre = nombre
        self.profesor = None
        self.estudiantes = []

    def asignar_profesor(self, profesor):
        self.profesor = profesor

    def agregar_estudiante(self, estudiante):
        if estudiante not in self.estudiantes:
            self.estudiantes.append(estudiante)

    def listar_estudiantes(self):
        return [est.nombre for est in self.estudiantes]

    def __str__(self):
        return f"Curso: {self.nombre}, Profesor: {self.profesor.nombre if self.profesor else 'Sin asignar'}"

# -------------------------------------------------------


# Crear estudiantes
e1 = Estudiante("Ana Torres", "12345678")
e2 = Estudiante("Luis Pérez", "87654321")

# Crear profesor
p1 = Profesor("Dra. Gómez", "11223344")

# Crear cursos
c1 = Curso("Matemáticas")
c2 = Curso("Física")

# Asignar profesor a cursos
p1.asignar_curso(c1)
p1.asignar_curso(c2)

# Matricular estudiantes en cursos
e1.matricular(c1)
e1.matricular(c2)
e2.matricular(c2)

# Informes
print("\n--- Cursos por estudiante ---")
for est in [e1, e2]:
    print(f"{est.nombre}: {est.listar_cursos()}")

print("\n--- Estudiantes por docente ---")
for est in p1.estudiantes_por_docente():
    print(est)

print("\n--- Estudiantes por curso ---")
for curso in [c1, c2]:
    print(f"{curso.nombre}: {curso.listar_estudiantes()}")
