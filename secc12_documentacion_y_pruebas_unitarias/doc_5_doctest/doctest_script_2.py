# ejemplo 2

class Calculadora:
    """
    Una clase simple para realizar operaciones matemáticas.
    
    >>> calc = Calculadora()
    >>> calc.sumar(2, 3)
    5
    """
    def sumar(self, a, b):
        """
        Suma dos números.
        
        >>> calc = Calculadora()
        >>> calc.sumar(5, 5)
        10
        >>> calc.sumar(4, 5)
        2
        """
        return a + b  
# Ejecutar pruebas
if __name__ == "__main__":
    import doctest
    doctest.testmod()

