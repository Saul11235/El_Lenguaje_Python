 
import unittest

# hemos importado los objetos de los cuales haremos un test
from   codigo import *

class TestFunciones(unittest.TestCase):

    def test_doble(self):
        # Prueba para la función doble
        self.assertEqual(doble(4), 8)
        self.assertEqual(doble(0), 0)
        self.assertEqual(doble(-3), -6)
        self.assertEqual(doble(2.5), 5.0)

    def test_triple(self):
        # Prueba para la función triple
        self.assertEqual(triple(4), 12)
        self.assertEqual(triple(0), 0)
        self.assertEqual(triple(-3), -9)
        self.assertEqual(triple(2.5), 7.5)

class TestRepetir(unittest.TestCase):

    def setUp(self):
        # Inicializamos la clase Repetir antes de cada prueba
        self.repetir = Repetir()

    def test_doble_texto(self):
        # Prueba para la función doble de la clase Repetir
        self.assertEqual(self.repetir.doble("hola"), "holahola")
        self.assertEqual(self.repetir.doble(""), "")
        self.assertEqual(self.repetir.doble("abc"), "abcabc")

    def test_triple_texto(self):
        # Prueba para la función triple de la clase Repetir
        self.assertEqual(self.repetir.triple("hola"), "holaholahola")
        self.assertEqual(self.repetir.triple(""), "")
        self.assertEqual(self.repetir.triple("abc"), "abcabcabc")

if __name__ == "__main__":
    unittest.main()
