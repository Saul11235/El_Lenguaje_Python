#
# Ejemplo de archivos
# esto dependerá de 
#


path_file = './archivo_2.txt'


# ejemplo de uso

file = open(path_file,'w') 
file.write(f'creado usando \'{path_file}\'')
file.close()

input(f'{path_file} fue creado!\n')
