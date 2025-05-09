# 
# ALMACEN
#
# Cree una clase llamada almacén, que admita 
# la creación de productos indicando precio 
# unitario, admita entradas y salidas.
# Permita el calculo del valor del inventario 
# Y permita generar informes de los montos de 
# ingreso y salida.
#
# Use salidas en la consola de comandos.
#

# -------------------------------------------------------

class almacen:

    def __init__(self):
        'Metodo constructor del objeto'
        self.moneda       = "$"
        self.decimales    = 2
        self.__inventario = {}
        self.__sumaTotal  = 0

    def nuevoInsumo(self,nombre,costoUni):
        'Metodo que define un nuevo insumo'
        if type(nombre)==str and (type(costoUni)==int or type(costoUni)==float):
            if nombre in self.__inventario.keys():
                print(f"\nError, el insummo '{nombre}' ya está definido")
            else:
                self.__inventario[nombre]=[costoUni,0]
                print(f"\nNUEVO INSUMO\t\t: '{nombre}'\n\tPrecio unitario : {round(costoUni,self.decimales)} {self.moneda}")
        else:print("\nError, no se pudo crear el insumo")

    def ingreso(self, nombre, cantidad):
        'Metodo que define un nuevo ingreso de insumo'
        if nombre in self.__inventario.keys():
            if type(cantidad)==int or type(cantidad)==float:
                self.__inventario[nombre][1] += cantidad
                costoUni  = self.__inventario[nombre][0]
                print(f"\n--> INGRESO\t\t:'{nombre}'\n\tCantidad\t: {cantidad}\n\tPrecio unitario\t: {round(costoUni,self.decimales)} {self.moneda}\n\tSubtotal\t: {round(cantidad*costoUni,self.decimales)} {self.moneda}")
            else:print(f"\nError, la cantidad del insummo '{nombre}' no es un número")
        else:print(f"\nError, el insummo '{nombre}' no existe")


    def salida(self, nombre, cantidad):
        if nombre in self.__inventario.keys():
            if type(cantidad)==int or type(cantidad)==float:
                self.__inventario[nombre][1] -= cantidad
                costoUni  = self.__inventario[nombre][0]
                print(f"\n<--  SALIDA\t\t:'{nombre}'\n\tCantidad\t: {cantidad}\n\tPrecio unitario\t: {round(costoUni,self.decimales)} {self.moneda}\n\tSubtotal\t: {round(cantidad*costoUni,self.decimales)} {self.moneda}")
            else:print(f"\nError, la cantidad del insummo '{nombre}' no es un número")
        else:print(f"\nError, el insummo '{nombre}' no existe")

    def informe(self, nombre):
        if nombre in self.__inventario.keys():
            cantidad          =  self.__inventario[nombre][1] 
            costoUni          =  self.__inventario[nombre][0]
            self.__sumaTotal  += cantidad*costoUni
            print(f"Resumen insumo\t\t:'{nombre}'\n\tCantidad\t: {cantidad}\n\tPrecio Unitario\t: {round(costoUni,self.decimales)} {self.moneda}\n\tSubtotal\t: {round(cantidad*costoUni,self.decimales)} {self.moneda}")
        else:print(f"   Error, el insummo '{nombre}' no existe")

    def informeTotal(self):
        linea=40*"-"
        self.__sumaTotal  = 0
        print('\n'+linea)
        print(  '  RESUMEN GENERAL DE ALMACEN   ')
        print( f'  Cantidad de insumos\t: {len(self.__inventario)}  ')
        print(linea)
        for x in self.__inventario.keys():
            self.informe(x)
            print(linea)
        print(  '  RESUMEN GENERAL DE ALMACEN   ')
        print( f'  Total valorizado\t: {round(self.__sumaTotal,self.decimales)} {self.moneda} ')
        print(linea)
 
# -------------------------------------------------------

var=almacen()

#var.moneda="USD"
#var.decimales=1


var.nuevoInsumo("saco azucar"   , 25.2233)
var.ingreso    ("saco azucar"   , 15     )
var.ingreso    ("saco azucar"   , 12     )
var.salida     ("saco azucar"   , 7      )

var.nuevoInsumo("saco harina"   , 50.7  )
var.ingreso    ("saco harina"   , 20    )
var.ingreso    ("saco harina"   , 12    )
var.salida     ("saco harina"   , 9     )

var.nuevoInsumo("caja de manzanas", 77.50  )
var.ingreso    ("caja de manzanas", 10  )
var.ingreso    ("caja de manzanas", 4   )
var.salida     ("caja de manzanas", 4   )



var.informeTotal()


