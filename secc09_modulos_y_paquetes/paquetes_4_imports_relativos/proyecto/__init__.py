# ejemplo de paquete con modulos anidados
#
#  proyecto/
#  |-- __init__.py  <--- Estamos aqui
#  |-- Modulo1.py
#  |-- Modulo2.py 
#  |-- Paquete1/
#  |   |-- __init__.py
#  |   |-- Modulo11.py
#  |   `-- Paquete11/
#  |       `-- __init__.py
#  `-- Paquete2/
#      |-- __init__.py
#      `-- Modulo21.py
#


contenido = "Hola desde: proyecto/__init__.py"


from .Paquete2.Modulo21 import contenido as c1
print(c1)


from .Modulo2 import contenido as c2
print(c2)


