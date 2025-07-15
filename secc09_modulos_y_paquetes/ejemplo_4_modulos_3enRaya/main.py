# Juego 3 en raya

try:    from .juego3enRaya import juego3enRaya
except: from juego3enRaya  import juego3enRaya

def lanzar():
    # funcion que lanza el juego
    obj=juego3enRaya()
    obj.lanzar2jugadores()


#  Lanzar función lanzar si se ejcuta

if __name__ =="__main__":
    lanzar()

