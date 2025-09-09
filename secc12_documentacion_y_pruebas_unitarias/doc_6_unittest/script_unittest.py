
def sumar(a, b):
    """Suma dos números y devuelve el resultado."""
    return a + b


#----------------------------------------------------


import unittest

class TestCalculadora(unittest.TestCase):
    """Clase para agrupar todas las pruebas."""

    def test_suma_numeros_enteros(self): 
        self.assertEqual(sumar(2, 3), 5)

    def test_suma_numeros_negativos(self): 
        self.assertEqual(sumar(-1, -1), -2)
        
    def test_suma_cero(self): 
        self.assertEqual(sumar(5, 0), 5)

# --- Bloque de ejecución principal ---
if __name__ == "__main__":
    print("Ejecutando pruebas unitarias con unittest...")
    unittest.main()
