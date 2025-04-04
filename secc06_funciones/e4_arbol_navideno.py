# ARBOL NAVIDEÑO
#
# se desea hacer una funcion que en base a funciones recursivas
# dibuje un arbol navideño usando caracteres ascci
#

def line(space=5,size=2,char="X"):
    print(" "*int(space)+char*int(size))

#line()
#line(5,4,"A")

def lineCenter(chars=2,center=10,char="X"):
    line(space=center-chars,size=2*chars,char=char)

#lineCenter()
#lineCenter(4,8,"E")

def cuerpo(inicio=4,fin=10,lineas=5,centro=10,char="X"):
    contador=0
    for x in range(lineas):
        contenido=inicio+contador/lineas*(fin-inicio)
        lineCenter(chars=contenido,center=centro,char=char)
        contador+=1

#cuerpo()
#cuerpo(2,8,4)

def arbol(altura=20,ancho=12,elementos=3,char="X"):
    lineas=int(altura/elementos)
    contador=0
    anchoContador=ancho/(elementos-1)
    for x in range(elementos-1):
        inicioCuerpo = (contador/2)*anchoContador
        finCuerpo    = (contador+1)*anchoContador
        cuerpo(inicioCuerpo,finCuerpo,lineas,ancho,char)
        contador+=1
    cuerpo(1,1,lineas,ancho,char)

#arbol()
#arbol(18,12,3,"*")
#arbol(15,20,4,"f")

