#
# NUMEROS ROMANOS
#
#  Plantee una clase romano que incorpore los métodos 
#  __add__, __sub__, __mul__, __truediv___ y para 
#  sumas y restas, multiplicaciones y divisiones, así
#  cómo el método __str__ para representarlos como string
#

# -------------------------------------------------------
# definiendo clase
class romano:

    def __init__(self,valor=0):
        self.valor=int(valor)

    def __add__(self,otro):
        return romano(self.valor+otro.valor)

    def __sub__(self,otro):
        return romano(self.valor-otro.valor)

    def __mul__(self,otro):
        return romano(self.valor*otro.valor)

    def __truediv__(self,otro):
        return romano(self.valor/otro.valor)

    def __str__(self):
        valor=abs(self.valor)
        respuesta=""
        if self.valor<0:respuesta+='-'
        simbolos={1:"I",4:"IV",5:"V",9:"IX",10:"X",40:"XL",50:"L",90:"XC",100:"C",400:"CD",500:"D",900:"CM",1000:"M"}
        for numero in sorted(simbolos.keys(),reverse=True):
            while valor>=numero:
                valor-=numero
                respuesta+=simbolos[numero]
        return respuesta

# -------------------------------------------------------

if __name__ =="__main__":

    print("ejemplos de uso")

    v1=romano(12)
    v2=romano(13)

    print("valor 1:",v1)
    print("valor 2:",v2)
    print(v1+v2)
    print('multiplicacion',v1*v2)

    for x in range(-100,100): 
        print(x,"=",romano(x))



