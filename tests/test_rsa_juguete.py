import unittest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
from criptografia.rsa_juguete import mcd_extendido, calcular_inverso, crear_llaves, cifrar, descifrar


class TestRSAJuguete(unittest.TestCase):

    def test_caso_obligatorio_del_enunciado(self):
        llaves = crear_llaves(p=61, q=53, e=17)
        self.assertEqual(llaves["n"], 3233)
        self.assertEqual(llaves["phi"], 3120)
        self.assertEqual(llaves["d"], 2753)

        c = cifrar(65, llaves)
        self.assertEqual(c, 2790)
        self.assertEqual(descifrar(c, llaves), 65)

    def test_identidad_de_bezout(self):
        a, b = 240, 46
        g, x, y = mcd_extendido(a, b)
        self.assertEqual(g, 2)
        self.assertEqual(a * x + b * y, g)

    def test_exponente_no_coprimo_lanza_error(self):
        with self.assertRaises(ValueError):
            crear_llaves(p=61, q=53, e=6)

    def test_p_o_q_no_primos_lanza_error(self):
        with self.assertRaises(ValueError):
            crear_llaves(p=9, q=53, e=17)

    def test_p_igual_a_q_lanza_error(self):
        with self.assertRaises(ValueError):
            crear_llaves(p=13, q=13, e=7)

    def test_mensaje_fuera_de_rango_lanza_error(self):
        llaves = crear_llaves(p=61, q=53, e=17)
        with self.assertRaises(ValueError):
            cifrar(llaves["n"], llaves)

    def test_ciclo_completo_con_otras_llaves(self):
        llaves = crear_llaves(p=17, q=11, e=7)
        for mensaje in [0, 5, 42, 100]:
            self.assertEqual(descifrar(cifrar(mensaje, llaves), llaves), mensaje)


if __name__ == "__main__":
    unittest.main()
