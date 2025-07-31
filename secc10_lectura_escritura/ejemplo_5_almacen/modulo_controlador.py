# 
# APLICACION ALMACEN
#
# -------------------------------------------------------
#
#
#    +------------+                 +-------------+
#    |   MODELO   |-----+   +-------|    VISTA    |
#    +------------+     |   |       +-------------+
#       ^               |   |                   ^
#       |     Notificar |   |   Acción usuario  |
#       |               V   V                   |
#       |         +---------------+             |
#       +---------|  CONTROLADOR  |-------------+
#   Actualizar    +---------------+        Actualizar
#
#
# -------------------------------------------------------

from modulo_modelo import modelo
from modulo_vista  import vista

from json import dumps, loads


#----------------------------------------------------
# nota el siguiente codigo obtiene la ruta de la carpeta actual
from pathlib import Path
this_path=Path(__file__).resolve().parent
#----------------------------------------------------


class controlador:

    def __init__(self):
        #coloca otros obj como atributos
        self.modelo = modelo()
        self.vista  = vista()
        self.vista.configurar_controlador(self)


    def get_modelo(self):
        return self.modelo

    def get_vista(self):
        return self.vista


    def guardar(self):
        # obtiene diccionario con los datos del almacen
        diccionario=self.modelo.get_dict()

        # texto json del diccionario codificado
        texto_json=dumps(diccionario,indent=4)

        # escribiendo archivo JSON
        with open(f'{this_path}/almacen.json','w',encoding='utf-8') as file:
            file.write(texto_json)  
            print('almacen.json -->  generado')



    def abrir(self):
        # decodifica almacen
        with open(f'{this_path}/almacen.json','r',encoding='utf-8') as file:
            contenido=loads(file.read())

        #  configurando el diccionario
        self.modelo.set_dict(contenido)





# -----------------------------

if __name__=="__main__":
    controlador()
