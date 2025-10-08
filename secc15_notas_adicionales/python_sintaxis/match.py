
# match se introdujo a partir de Python 3.10
# PEP 634

x = 5

match x:
    case 1:
        print("El valor es 1")
    case 2:
        print("El valor es 2")
    case 3 | 4:
        print("El valor es 3 o 4")
    case _:
        print("El valor no es 1, 2, 3 ni 4")
# ----------------------------------

if x == 1:
    print("El valor es 1")
elif x == 2:
    print("El valor es 2")
elif x == 3 or x == 4:
    print("El valor es 3 o 4")
else:
    print("El valor no es 1, 2, 3 ni 4")
