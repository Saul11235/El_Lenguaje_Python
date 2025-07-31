#
#  EDITOR SIMPLE
# 
# Cree una programa de edición de textos sencillo, 
# que permita crear y editar un archivo de texto 
# (reemplace el contenido por un string obtenido via input), 
# permita crear nuevos archivos y visualizar los archivos de 
# la carpeta actual, 
#
# -----------------------------------------

from print_files import print_files

#----------------------------------------------------
# nota el siguiente codigo obtiene la ruta de la carpeta actual
from pathlib import Path
this_path=Path(__file__).resolve().parent
#----------------------------------------------------


class editor:

    # ...............................

    def lanzar_editor(self):
        'metodo que lanza un editor en consola de comandos'
        print('\n-------------------\n')
        print_files()
        print('\n-------------------\n')
        print(' COMANDOS  (1) abrir archivo   (2) editar o crear archivo (3) salir')
        comando=input('\n >> ').replace(" ","")
        #-----------
        if   comando=="1":  # comando 1  --> abrir archivo
            self.comando_abrir()
        elif comando=="2":  # comando 2 --> crear o editar
            self.comando_editar()
        elif comando=="3":  # comando 3 --> Salir
            exit()
        self.lanzar_editor()   # <---- reinicia metodo

    # ...............................

    def comando_abrir(self):
        'metodo que crea un comando para abrir un archivo'
        nombre_archivo = input('\n  NOMBRE ARCHIVO    >>> ')
        nombre_archivo = f'{this_path}/{nombre_archivo}'
        try:
            with open(nombre_archivo,"r",encoding='utf-8') as file:
                print('\n-------------------\n')
                print(file.read())
                print('\n-------------------\n')
        except:
            print(f'\n  ERROR, {nombre_archivo} no se puede abrir\n')

    # ...............................

    def comando_editar(self):
        'metodo que crea un comando para editar o crear un archivo'
        nombre_archivo    = input('\n  NOMBRE ARCHIVO    >>> ')
        nombre_archivo    = f'{this_path}/{nombre_archivo}'
        contenido_archivo = input(  '  CONTENIDO ARCHIVO >>> ')
        try:
            with open(nombre_archivo,"w",encoding='utf-8') as file:
                file.write(contenido_archivo)
        except:
            print(f'\n  ERROR, {nombre_archivo} no se puede crear o editar\n')

    # ...............................

# -----------------------------------------

if __name__=='__main__':
    input('\n PROGRAMA EDITOR SIMPLE \n')
    editor().lanzar_editor()

