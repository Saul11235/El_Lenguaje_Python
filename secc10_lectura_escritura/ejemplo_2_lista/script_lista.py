#
# EDITOR DE LISTA
#
# Cree un programa de línea de comandos que lea 
# un archivo local de texto y permita respectivamente:
#  - Colocar una línea adicional
#  - Eliminar la ultima línea
#  - Salir del programa
#
# ---------------------------------------------

#----------------------------------------------------
# nota el siguiente codigo obtiene la ruta de la carpeta actual
from pathlib import Path
this_path=Path(__file__).resolve().parent
#----------------------------------------------------


class lista:

    def __init__(self):
        self.lineas=[]
        self.__leer_lineas()

    # --------------------------------------

    def __leer_lineas(self):
        'funcion que decodifica lista.txt a self.lineas'
        with open(f'{this_path}/lista.txt','r',encoding='utf-8') as file:
            self.lineas=list([x.replace('\n','') for x in file.readlines()])

    def __escribir_lineas(self):
        'funcion que codifica self.lineas a lista.txt'
        with open(f'{this_path}/lista.txt','w',encoding='utf-8') as file:
            file.write('\n'.join(self.lineas))

    # --------------------------------------

    def print_encabezado(self):
        print('\nSCRIPT LISTA.txt')
        print('\n-----------------------------\n')
        print('\n'.join(self.lineas))
        print('\n-----------------------------')


    def input_comando(self):
        print('\n COMANDOS : (1) nueva linea  (2) borrar ultima linea')
        print(  '            (3) guardar      (4) salir')
        comando=input('\n  >>  ').replace(" ","")
        if   comando=='1':                   # Nueva Linea
            self.lineas.append(input('\n NUEVA LINEA >> '))
        elif comando=='2':                   # Borrar ultima linea
            try   : self.lineas.pop()
            except: print(' No se pudo borrar linea')
        elif comando=='3':                   # Guardar
            print(' Archivo guardado')
            self.__escribir_lineas()
        elif comando=='4':                   # Salir
            exit()
        else:                                # no realizar ninguna accion
            print(' Comando no reconocido')
        self.lanzar()

    # --------------------------------------

    def lanzar(self):
        self.print_encabezado()
        self.input_comando()


if __name__=='__main__':
    input('\n Programa editor de lista\n')
    lista().lanzar()
