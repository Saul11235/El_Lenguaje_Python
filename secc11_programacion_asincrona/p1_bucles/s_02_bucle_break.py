#
#  EJEMPLOS DE BUCLES SENCILLOS EN PYTHON
#
# los bucles en python se realizan
# con las estructuras for o while
#
# break, termina con las 
#
# ----------------------------

for x in range(10):
    # -----------
    if x==5:
        print("Ejecutamos break \n")
        break
    # -----------
    print(f'bucle for x={x}')

# ----------------------------

x=0


while x<10:
    x+=1
    # -----------
    if x==5:
        print("Ejecutamos break \n")
        break
    # -----------
    print(f'bucle while x={x}')


# ----------------------------

