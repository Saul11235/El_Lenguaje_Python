# JUEGO 3 EN RAYA
#
# implemente el juego de 3 en raya para 2 jugadores
# utilizando el paradigma funcional, utilizando impresiones
# en consola y lecturas de la terminal
#

# --------------------------

# declaramos variables de consulta

# declararemos una lista con las jugadas
# 1 -> "O"
# 2 -> "X"
tablero=[0,0,0,0,0,0,0,0,0]

# contador de victorias de los jugs 1 y 2
win1=0
win2=0

# True si es turno del jug1
turno=True

#True si la primera jugada de la partida es de jug1
primeraJugada=True

# --------------------------

#declaramos funciones

def alistaTablero():
    'Funcion que alista las variables del tablero'
    global tablero, turno, primeraJugada
    tablero=[0,0,0,0,0,0,0,0,0]
    if primeraJugada: 
        primeraJugada=False
        turno=False
    else: 
        primeraJugada=True
        turno=True


def printTablero():
    'Funcion que imprime el tablero en pantalla'
    global tablero
    t=[(" " if x==0 else "O" if x==1 else "X") for x in tablero]
    print('\n'+f' {t[0]} | {t[1]} | {t[2]}\n---+---+---')
    print(     f' {t[3]} | {t[4]} | {t[5]}\n---+---+---')
    print(     f' {t[6]} | {t[7]} | {t[8]}\n')


def printMarcador():
    'Funcion que imprime el marcador en pantalla'
    global win1,win2
    print(f'\n victorias O: {win1}   victorias X: {win2}')


def evaluaTablero():
    '''Funcion que evalua el tablero, devuelve un booleano
    Bool es true en caso exista un ganador'''
    global tablero, win1, win2
    jugador = 0
    if   tablero[0]!=0 and tablero[0]==tablero[1]==tablero[2]:
        jugador = tablero[0]
    elif tablero[3]!=0 and tablero[3]==tablero[4]==tablero[5]:
        jugador = tablero[3]
    elif tablero[6]!=0 and tablero[6]==tablero[7]==tablero[8]:
        jugador = tablero[6]
    elif tablero[0]!=0 and tablero[0]==tablero[3]==tablero[6]:
        jugador = tablero[0]
    elif tablero[1]!=0 and tablero[1]==tablero[4]==tablero[7]:
        jugador = tablero[1]
    elif tablero[2]!=0 and tablero[2]==tablero[5]==tablero[8]:
        jugador = tablero[2]
    elif tablero[0]!=0 and tablero[0]==tablero[4]==tablero[8]:
        jugador = tablero[0]
    elif tablero[2]!=0 and tablero[2]==tablero[4]==tablero[6]:
        jugador = tablero[2]
    #-------
    if jugador==1: win1+=1
    if jugador==2: win2+=1
    #-------
    if jugador==0: return False
    else:          return True


def hayJugadasPosibles():
    'Funcion que evalua el tablero y avisa si hay jugadas posibles'
    global tablero
    for x in tablero:
        if x==0: return True
    return False


def inputJugada():
    'Funcion que detiene el programa y recibe una instruccion de teclado'
    global  turno, tablero
    jugador= "O" if turno else "X"
    numero=int(input(f' turno jugador {jugador} : '))-1
    if tablero[numero]==0:
        if turno:
            tablero[numero]=1
            turno=False
        else:
            tablero[numero]=2
            turno=True
    else: inputJugada()


def tresEnRaya():
    'Funcion que realiza el final de la jugada y la lógica del programa'
    global win1,win2,turno
    printMarcador()
    printTablero()
    inputJugada() 
    victoria=evaluaTablero()
    if victoria:
        printTablero()
        jugador= "X" if turno else "O"
        input(f"\nvictoria del jugador {jugador}:\n")
        alistaTablero()
    elif not victoria and not(hayJugadasPosibles()):
        input("\ntablas:\n")
        alistaTablero()
    tresEnRaya()

# --------------------------
#  Ejecutamos un input y ejecutar una función principal

input('''
 TRES EN RAYA: por Edwin Saul
 implementación sencilla y en paradigma funcional
 del juego del tres en raya para 2 jugadores

''')
tresEnRaya()

