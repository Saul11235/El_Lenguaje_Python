"""
Modulo de ejemplo, este ha sido documentado
"""


def doble(numero: int | float) -> int | float:
    """
    Calcula el doble de un número.
    >>> doble(4)
    8
    >>> doble(1.2)
    2.4
    """
    return numero * 2


def triple(numero: int | float) -> int | float:
    """
    Calcula el triple de un número.
    >>> triple(9) 
    27
    """
    return numero * 3


class Repetir:
    """
    Una clase para repetir un texto una cantidad de veces.
    """
    def doble(self, texto: str) -> str:
        """
        Repite un texto dos veces.
        >>> obj=Repetir()
        >>> obj.doble('texto')
        'textotexto'
        """
        return texto * 2

    def triple(self, texto: str) -> str:
        """
        Repite un texto tres veces.
        >>> obj=Repetir()
        >>> obj.triple('texto')
        'textotextotexto'
        """
        return texto * 3
    

if __name__=='__main__':
    import doctest
    doctest.testmod()

