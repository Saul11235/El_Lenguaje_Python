
def duplicar(x):
    """
    Duplica el valor recibido.

    >>> duplicar(2)
    4
    >>> duplicar(-1)
    -2
    """
    return x * 2

# Ejecutar pruebas
if __name__ == "__main__":
    import doctest
    doctest.testmod()
