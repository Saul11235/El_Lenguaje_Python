# ejemplo programa division, edwinsaul.com

class ErrorDenominador(Exception): pass

try:
    input("\n PROGRAMA DIVISON \n")
    var1 = float(input("Numerador  : "))
    var2 = float(input("Denominador: "))
    if var2<=0:
        raise ErrorDenominador
    print("\n Resultado :", var1/var2)

except ValueError:
    print("No se pudo convertir a numeros")
    
except ZeroDivisionError:
    print("Error, division entre cero")
     
except ErrorDenominador:
    print("Error, denominador no positivo")

else:
    print("No hubo ningun error :) ")

finally:
    print("\n esta linea se ejecuta siempre")

input()
