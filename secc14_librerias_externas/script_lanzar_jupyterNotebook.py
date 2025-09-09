#  antes instalar jupyter lab
#
#  pip install notebook
#

import os
from os import system

# Obtener la ruta del directorio donde se encuentra el script
script_directory = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_directory)

print('lanzando jupyter notebook\n Ctrl+C para cerrar\n')
system('jupyter notebook')  
