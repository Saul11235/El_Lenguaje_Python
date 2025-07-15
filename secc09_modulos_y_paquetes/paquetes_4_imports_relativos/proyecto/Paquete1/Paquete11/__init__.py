# ejemplo de paquete con modulos anidados
#
#  proyecto/
#  |-- __init__.py
#  |-- Modulo1.py
#  |-- Modulo2.py 
#  |-- Paquete1/
#  |   |-- __init__.py
#  |   |-- Modulo11.py
#  |   `-- Paquete11/
#  |       `-- __init__.py  <--- Estamos aqui
#  `-- Paquete2/
#      |-- __init__.py
#      `-- Modulo21.py
#

contenido = "Hola desde: proyecto/Paquete1/Paquete11/__init__.py"

from ..Modulo11 import contenido as c
print(c)
