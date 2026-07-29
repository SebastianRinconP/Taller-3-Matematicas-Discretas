import unittest
import sys
import os
import math

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../src/cuantica'))
from shannon import (
    frecuencia_texto,
    entropia_shanon,
)

class TestFrecuenciaTexto(unittest.TestCase):

    def test_cuenta_repeticiones_correctamente(self):
        resultado = frecuencia_texto("AAAB")
        esperado = {"A": 3, "B": 1}
        self.assertEqual(resultado, esperado)

    def test_no_devuelve_none(self):
        resultado = frecuencia_texto("HOLA")
        self.assertIsNotNone(resultado)
        self.assertIsInstance(resultado, dict)


class TestEntropiaShanon(unittest.TestCase):

    def test_calculo_manual_dos_simbolos(self):
        texto = "AABB"
        frecuencia = frecuencia_texto(texto)
        entropia = entropia_shanon(texto, frecuencia)
        self.assertAlmostEqual(entropia, 1.0, places=6)

    def test_texto_uniforme_tiene_entropia_maxima(self):
        texto = "ABCD"
        frecuencia = frecuencia_texto(texto)
        entropia = entropia_shanon(texto, frecuencia)
        self.assertAlmostEqual(entropia, 2.0, places=6)


class TestConTextosDesdeArchivo(unittest.TestCase):
    def setUp(self):
        self.texto_repetitivo = "AAAAAAAAAAAAA"
        self.texto_variado = "No soy gay pero soy peruano y tengo una fantasia donde peru invade chile" #Voy a suponer que no importa que tengan tamaños distintos
    def test_texto_repetitivo_tiene_entropia_cero(self):
        frecuencia = frecuencia_texto(self.texto_repetitivo)
        entropia = entropia_shanon(self.texto_repetitivo, frecuencia)
        self.assertAlmostEqual(entropia, 0.0, places=6)

    def test_texto_variado_tiene_entropia_mayor_que_cero(self):
        frecuencia = frecuencia_texto(self.texto_variado)
        entropia = entropia_shanon(self.texto_variado, frecuencia)
        self.assertGreater(entropia, 0.0)

    def test_texto_repetitivo_vs_variado(self):
        f1 = frecuencia_texto(self.texto_repetitivo)
        f2 = frecuencia_texto(self.texto_variado)

        h1 = entropia_shanon(self.texto_repetitivo, f1)
        h2 = entropia_shanon(self.texto_variado, f2)

        self.assertLess(h1, h2)


class TestPropiedadesGeneralesDeLaEntropia(unittest.TestCase):
    def test_entropia_no_negativa_y_acotada(self):
        textos = [
            "AAAAAA",
            "AABBCC",
            "MISSISSIPPI",
            "PROGRAMACION",
            "ABCDEFGH",
        ]
        for texto in textos:
            with self.subTest(texto=texto):
                frecuencia = frecuencia_texto(texto)
                entropia = entropia_shanon(texto, frecuencia)
                n_simbolos = len(frecuencia)
                cota_superior = math.log2(n_simbolos)

                self.assertGreaterEqual(entropia, 0.0)
                self.assertLessEqual(entropia, cota_superior + 1e-9)


if __name__ == '__main__':
    unittest.main()