# este programa llausa el patron MVC

from modulo_controlador import controlador

input('\n PROGRAMA ALMACEN \n')

# creando objeto controlador
obj=controlador()

# abre el archivo local 
try:
    obj.abrir()
except:
    print('\n ERROR EN LECTURA DE ARCHIVOS \n')

# obtiene objeto VISTA y la lanza la aplicacion
obj.get_vista().lanzar() 

