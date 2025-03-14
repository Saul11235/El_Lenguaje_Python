#
# MENU HOTELERO
#
# Un hotel, desea variar las combinaciones 
# entres su oferta de desayunos, almuerzos y 
# cenas, por lo que requiere un programa 
# que intercambie recursivamente 3 arrays 
# de las opciones disponibles, el usuario 
# debe indicar el número de días que desea generar.
#
 
desayuno=["americano","continental","mediterráneo"]
almuerzo=["vegetariano","marino","ejecutivo","buffet","light"]
cena=["ligera","vegetariana","italiana","asiática"]

dias=int(input('\n nro dias? > '))

for dia in range(dias):
    print("\nDIA Nro",dia+1)
    print('\tdesayuno :',desayuno[dia%3])
    print('\talmuerzo :',almuerzo[dia%5])
    print('\tcena     :',cena[dia%4])

input()

