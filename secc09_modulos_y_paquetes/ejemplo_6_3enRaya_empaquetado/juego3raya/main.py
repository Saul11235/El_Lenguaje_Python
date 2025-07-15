# Juego 3 en raya
try:    from .juego3enRaya import juego3enRaya
except: from juego3enRaya  import juego3enRaya

def lanzar():
    # funcion que lanza el juego para 2 jugadores
    obj=juego3enRaya()
    obj.lanzar2jugadores()

def lanzar_vs_CPU():
    # funcion que lanza el juego para 1 jugador
    obj=juego3enRaya()
    obj.lanzar1jugador()



#  Lanzar función lanzar si se ejcuta

if __name__ =="__main__":
    lanzar_vs_CPU()

