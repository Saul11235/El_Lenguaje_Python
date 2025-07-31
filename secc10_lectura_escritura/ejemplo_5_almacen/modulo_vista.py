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

class vista:

    def __init__(self):
        self.controlador = None

    #---------------------------

    def configurar_controlador(self,controlador):
        self.controlador = controlador

    #---------------------------

    def lanzar(self):
        print('\n  COMANDOS  (1) resumen insumos   (2) nuevo insumo')
        print(  '            (3) Ingreso almacén   (4) Salida almacén')
        print(  '            (5) Guardar           (6) Salir')
        comando=input('\n >>> ').replace(" ","")
        if   comando=='1':               # <---- (1) resumen isumos
            self.comando_1_resumen()
        elif comando=="2":               # <---- (2) nuevo insumo
            self.comando_2_nuevo_insumo()
        elif comando=='3':               # <---- (3) nueva entrada
            self.comando_3_ingreso()
        elif comando=='4':               # <---- (4) nueva salida
            self.comando_4_salida()
        elif comando=='5':               # <---- (5) guardar
            self.comando_5_guardar()
        elif comando=='6':               # <---- (6) salir
            exit()
        self.lanzar()

    #---------------------------

    def comando_1_resumen(self):
        # NOTA:
        # el argumento self.controlador tiene el metodo get_modelo
        # este metodo devuelve el objeto modelo que abstra el almacen
        miModelo = self.controlador.get_modelo()
        miModelo.informeTotal()

    #---------------------------

    def comando_2_nuevo_insumo(self):
        # NOTA:
        # el argumento self.controlador tiene el metodo get_modelo
        # este metodo devuelve el objeto modelo que abstra el almacen
        try:
            nombreInsumo  =       input('\n NUEVO INSUMO   >>> ')
            costoUnitario = float(input(  ' COSTO UNITARIO >>> '))
            # ejecutando método en el objeto modelo
            miModelo = self.controlador.get_modelo()
            miModelo.nuevoInsumo(nombreInsumo,costoUnitario)
        except:
            print('\n OCURRIO UN ERROR \n')


    #---------------------------

    def comando_3_ingreso(self):
        # NOTA:
        # el argumento self.controlador tiene el metodo get_modelo
        # este metodo devuelve el objeto modelo que abstra el almacen
        try:
            nombreInsumo  =       input('\n INSUMO         >>> ')
            cantidad      = float(input(  ' CANT INGRESO   >>> '))
            # ejecutando método en el objeto modelo
            miModelo = self.controlador.get_modelo()
            miModelo.ingreso(nombreInsumo,cantidad)
        except:
            print('\n OCURRIO UN ERROR \n')


    #---------------------------

    def comando_4_salida(self):
        # NOTA:
        # el argumento self.controlador tiene el metodo get_modelo
        # este metodo devuelve el objeto modelo que abstra el almacen
        try:
            nombreInsumo  =       input('\n INSUMO         >>> ')
            cantidad      = float(input(  ' CANT SALIDA    >>> '))
            # ejecutando método en el objeto modelo
            miModelo = self.controlador.get_modelo()
            miModelo.salida(nombreInsumo,cantidad)
        except:
            print('\n OCURRIO UN ERROR \n')


    #---------------------------

    def comando_5_guardar(self):
        # en este caso se ha ejecutado un modelo del controlador
        self.controlador.guardar()




# -----------------------------

if __name__=="__main__":
    # 
    #  PRUEBA DE LANZAMIENTO DE VISTA
    #
    from modulo_controlador import controlador
    p=vista()
    p.configurar_controlador(controlador())
    p.lanzar()
