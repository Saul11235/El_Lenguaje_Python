# ejemplo programa division, edwinsaul.com

class Error(Exception): 
    def __init__(self,mensaje,objeto):
        super().__init__(mensaje)
        self.mensaje = mensaje
        self.objeto  = objeto

try:
    input("\n PROGRAMA DIVISON \n")
    var1 = float(input("Numerador  : "))
    var2 = float(input("Denominador: "))
    if var2<=0:
        raise Error("mensaje de error",{'objeto':'error'})
    print("\n Resultado :", var1/var2)

except Error as e:
    print( "Error, detectado")
    print(f"El error es del tipo: {type(e)}")
    print(f'Mensaje: {e.mensaje}')
    print(f'Objeto:  {e.objeto}')

except:
    print('ha ocurrido un error')

input()
