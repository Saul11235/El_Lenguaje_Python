"""
Modulo de ejemplo, este ha sido documentado
"""


def doble(numero: int | float) -> int | float:
    """
    Calcula el doble de un número.
    """
    return numero * 2


def triple(numero: int | float) -> int | float:
    """
    Calcula el triple de un número.
    """
    return numero * 3


class Repetir:
    """
    Una clase para repetir un texto una cantidad de veces.
    """
    def doble(self, texto: str) -> str:
        """
        Repite un texto dos veces.
        """
        return texto * 2

    def triple(self, texto: str) -> str:
        """
        Repite un texto tres veces.
        """
        return texto * 3
    


if __name__=='__main__':
    var  = 5
    var2 = 10
    var3 = 15
    assert doble(var)  == var2
    assert triple(var) == var3
    assert Repetir().doble("a")  == 'aa'
    assert Repetir().triple("b") == 'bbb'


