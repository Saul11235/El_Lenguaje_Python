# CONJETURA COLLATZ
#
# la conjetura de collatz es un problema matemático que dice
# sea todo número entero positivo, y si se opera recursivamente
#
# SI n ES IMPAR:  devolver   3n+1
# SI n ES PAR  :  devolver  n/2
#
# la conjetura establece que recursivamente siempre terminaremos
# en el bucle 4 2 1
#


print('\n CONJETURA DE COLLATZ \n')

num=int(input(" ingrese un numero > "))

def collatz(n):
    if n%2==1: return int(3*n+1)
    else:      return int(n/2)

repetir=True

while repetir:
    print(num)
    if num==0 or num==1:
        repetir=False
    num=collatz(num)

input()
