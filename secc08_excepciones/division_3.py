# ejemplo programa division, edwinsaul.com

try:
    input("\n PROGRAMA DIVISON \n")

    var1 = float(input("Numerador  : "))
    var2 = float(input("Denominador: ")) 

    print("\n Resultado :", var1/var2)

except ValueError:
    print("No se pudo convertir a numeros")

except ZeroDivisionError:
    print("Error, division entre cero")

except:
    print("Este es un error comun")

input() 
