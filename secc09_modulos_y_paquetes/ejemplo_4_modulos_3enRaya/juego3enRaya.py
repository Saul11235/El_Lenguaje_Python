#
# JUEGO 3 EN RAYA
#
try:    from .tablero import tablero
except: from tablero import tablero


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
        strinput=input(f' turno jugador {jugador} : ')
        if strinput=='q':
            quit()
        try:
            numero=int(strinput)
            return self.tablero.jugar(numero)
        except:
            return self.inputJugada() #repetir

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

if __name__=="__main__":
    obj=juego3enRaya()
    print(obj)
    print(obj.tablero)

