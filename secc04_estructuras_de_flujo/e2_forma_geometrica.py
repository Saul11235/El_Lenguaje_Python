#
# FORMA GEOMETRICA
#
# Hacer un programa que lea una dimensión 
# y que luego pregunte si es el radio de una esfera, 
# el lado de un cubo ó un triángulo equilátero 
#

l=float(input("\nIngrese la dimensión: "))

print("\n¿Que figura calcular?")
print("( 1 ) para esfera")
print("( 2 ) para cubo")
print("( 3 ) para triángulo equilatero")
fig=input(" > ")

if fig=="1":
    pi=3.1415
    print("\nESFERA")
    print("radio =",l,"m")
    print("area =",4*pi*l**2,"m2")
    print("volumen =",4/3*pi*l**3,"m3")
elif fig=="2":
    print("\nCUBO")
    print("arista =",l,"m")
    print("area =",6*l**2,"m2")
    print("volumen =",l**3,"m3")
elif fig=="3":
    print("\nTRIANGULO EQUILATERO")
    print("lado =",l,"m")
    print("area =",(3**0.5/4)*l**2,"m2")
else:
    print("\nimagen no reconocida")

input()

