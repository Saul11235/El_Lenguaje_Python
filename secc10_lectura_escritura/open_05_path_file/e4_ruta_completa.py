#
# Ejemplo de archivos
# esto dependerá de 
#

#----------------------------------------------------
# nota el siguiente codigo obtiene la ruta de la carpeta actual

from pathlib import Path
this_path=Path(__file__).resolve().parent

#----------------------------------------------------


print(this_path)  # <- ruta de la carpeta actual


path_file = f'{this_path}/archivo_3.txt'


# ejemplo de uso

file = open(path_file,'w') 
file.write(f'creado usando \'{path_file}\'')
file.close()

input(f'{path_file} fue creado!\n')
