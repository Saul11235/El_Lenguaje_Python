#
# JUEGO 3 EN RAYA
#
# implemente el juego de 3 en raya para 2 jugadores
# utilizando el paradigma orientao a objetos, utilizando impresiones
# en consola y lecturas de la terminal
#

# ------------------------------------------

class tablero:
    'clase tablero, abstrae un tablero del 3 en raya'

    def __init__(self):
        'crea objeto tablero'
        self.win1             = 0    # atributos
        self.win2             = 0
        self.hayJugadas       = None
        self.hayGanador       = None
        self.hayTablas        = None
        self.turnoJug1        = None
        self.turnoJug2        = None
        self.__primeraJugada  = False # atributos privados
        self.__configuraTablero()     # configura el tablero

    def __configuraTablero(self):
        'metodo privado, alterna y configura tablero'
        self.__tablero        = [0]*9
        self.hayJugadas       = True
        self.hayGanador       = False
        self.hayTablas        = False
        if self.__primeraJugada:
            self.__primeraJugada = False
            self.turnoJug1       = True
            self.turnoJug2       = False
        else:
            self.__primeraJugada = True
            self.turnoJug1       = False
            self.turnoJug2       = True

    def juegoNuevo(self):
        'actualiza contadores y configura un nuevo juego'
        if   self.hayGanador and self.turnoJug1: self.win1+=1
        elif self.hayGanador and self.turnoJug2: self.win2+=1
        self.__configuraTablero()

    def getJugadasPosibles(self):
        'devuelve lista con las jugadas posibles'
        if not self.hayJugadas: return []
        listaJugadas = []
        contador     = 0
        for x in self.__tablero:
            contador += 1
            if x==0 : listaJugadas.append(contador)
        return listaJugadas

    def get(self):
        return self.__tablero[:]

    def __evaluaTablero(self):
        'metodo privado, evalua el tablero y modifica atributos'
        condiciones=[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[6,4,2]]
        def evaluaLinea(condicion):
            casilla1 = self.__tablero[condicion[0]]
            casilla2 = self.__tablero[condicion[1]]
            casilla3 = self.__tablero[condicion[2]]
            if casilla1 == casilla2 == casilla3:
                  return casilla1
            else: return 0
        lineas = [ evaluaLinea(x) for x in condiciones ]
        if not 0 in self.__tablero:
            self.hayJugadas = False
        if not self.hayJugadas and not(any(lineas)):
            self.hayTablas = True
            self.hayGanador= False
            pass
        if 1 in lineas or 2 in lineas:
            self.hayGanador=True

    def jugar(self,jugada):
        'metodo que coloca la siguiente jugada, True si fue una jugada correcta'
        if not self.hayJugadas: return False
        if type(jugada)!=int  : return False
        if not jugada in self.getJugadasPosibles(): return False
        ficha= 1 if self.turnoJug1 else 2
        self.__tablero[jugada-1]=ficha
        self.turnoJug1=not(self.turnoJug1)
        self.turnoJug2=not(self.turnoJug2)
        self.__evaluaTablero()
        return True


# ------------------------------------------

class juego3enRaya:

    def __init__(self):
        self.tablero=tablero() #creacion de atributo 

    def printTablero(self):
        'Metodo que imprime el tablero en pantalla'
        t=[(" " if x==0 else "O" if x==1 else "X") for x in self.tablero.get()]
        print('\n'+f' {t[0]} | {t[1]} | {t[2]}\n---+---+---')
        print(     f' {t[3]} | {t[4]} | {t[5]}\n---+---+---')
        print(     f' {t[6]} | {t[7]} | {t[8]}\n')
 
    def printMarcador(self):
        'Metodo que imprime el marcador en pantalla'
        print(f'\n victorias X: {self.tablero.win1}   victorias O: {self.tablero.win2}')

    def inputJugada(self):
        'Metodo que detiene el programa y recibe una instruccion de teclado'
        if not self.tablero.hayJugadas: return False
        jugador= "O" if self.tablero.turnoJug1 else "X"
        numero=int(input(f' turno jugador {jugador} : '))
        return self.tablero.jugar(numero)

    def lanzar2jugadores(self):
        self.printMarcador()
        self.printTablero()    
        repetir = True
        while repetir:
            repetir = not self.inputJugada()
        if not self.tablero.hayJugadas or self.tablero.hayGanador:
            self.printTablero()
            if self.tablero.hayTablas:
                input("\ntablas:\n")
            elif self.tablero.hayGanador and self.tablero.turnoJug1:
                input(f"\nvictoria del jugador X:\n")
            elif self.tablero.hayGanador and self.tablero.turnoJug2:
                input(f"\nvictoria del jugador O:\n")
            self.tablero.juegoNuevo()
        self.lanzar2jugadores()        # repetir


# --------------------------
#  Ejecutamos un input, luego crear un objeto de clase
#  juego3enRaya y ejecutar su metodo lanzar2jugadores

input('''
 TRES EN RAYA: por Edwin Saul
 implementación sencilla y en paradigma orientado a objetos
 del juego del tres en raya para 2 jugadores

''')
obj=juego3enRaya()
obj.lanzar2jugadores()

