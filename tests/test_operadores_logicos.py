import unittest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../src/boole'))
from operadores_logicos import expresion1, expresion2, expresion3, evaluar_entrada


class TestTablasVerdad(unittest.TestCase):

    def test_expresion1_caso_taller(self):
        self.assertEqual(expresion1(False, False, False, False), True)

    def test_expresion1_caso_falso(self):
        self.assertEqual(expresion1(False, True, True, False), False)

    def test_expresion2_xor_y_C_verdaderos(self):
        self.assertEqual(expresion2(True, False, True, False), True)

    def test_expresion2_xor_falso_por_A_igual_B(self):
        self.assertEqual(expresion2(True, True, True, False), False)

    def test_expresion3_caso_verdadero(self):
        self.assertEqual(expresion3(False, True, False, False), True)

    def test_expresion3_caso_falso_por_A_or_B(self):
        self.assertEqual(expresion3(False, False, True, False), False)

    def test_tabla_completa_expresion1_contra_definicion_manual(self):
        from itertools import product
        for A, B, C in product([False, True], repeat=3):
            esperado = (A and B) or (not C)
            self.assertEqual(expresion1(A, B, C, False), esperado)

    def test_tabla_completa_expresion2_contra_definicion_manual(self):
        from itertools import product
        for A, B, C in product([False, True], repeat=3):
            esperado = (A != B) and C
            self.assertEqual(expresion2(A, B, C, False), esperado)

    def test_evaluar_entrada_concreta(self):
        resultado = evaluar_entrada(expresion2, True, False, True, False)
        self.assertEqual(resultado, True)


if __name__ == '__main__':
    unittest.main()