# LENGUAJE CIFRADO
#
# Hacer un programa que  codifique un texto,
# exprese todo en mayúsculas y cambie la A por un 4, 
# la E por un 3, la I por un 1, la O por un 0, 
# la U por un y los espacios por un punto
#
#    Un eucalipto    ->    7N.37C4L1PT0
#    El Arquitecto  ->    3L.4RQ71T3CT0
#

txt=input("\ningrese su texto: ")

txt2=txt.upper().replace("A","4").replace("E","3").replace("I","1").replace("O","0").replace("U","7").replace(" ",".")
print("\nTexto codificado:\n",txt2)
input()

