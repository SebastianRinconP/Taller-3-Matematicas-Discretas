import unittest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../src/boole'))
from operadores_logicos import expresion1, expresion2, expresion3, evaluar_entrada


class TestTablasVerdad(unittest.TestCase):

    def test_expresion1_caso_taller(self):
        # (A AND B) OR (NOT C): si C es falso, el resultado siempre es verdadero
        self.assertEqual(expresion1(False, False, False, False), True)

    def test_expresion1_caso_falso(self):
        # A=0, B=1, C=1 -> (0 AND 1)=False, NOT C=False -> resultado False
        self.assertEqual(expresion1(False, True, True, False), False)

    def test_expresion2_xor_y_C_verdaderos(self):
        # (A XOR B) AND C: A distinto de B, y C verdadero
        self.assertEqual(expresion2(True, False, True, False), True)

    def test_expresion2_xor_falso_por_A_igual_B(self):
        # A == B -> XOR es falso, sin importar C
        self.assertEqual(expresion2(True, True, True, False), False)

    def test_expresion3_caso_verdadero(self):
        # (A OR B) AND (NOT A OR C)
        self.assertEqual(expresion3(False, True, False, False), True)

    def test_expresion3_caso_falso_por_A_or_B(self):
        # A=0, B=0 -> (0 OR 0)=False -> resultado False sin importar C
        self.assertEqual(expresion3(False, False, True, False), False)

    def test_tabla_completa_expresion1_contra_definicion_manual(self):
        # Condicion del taller: la tabla debe cubrir TODAS las combinaciones posibles
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
        # Condicion del taller: el programa debe permitir evaluar la expresion
        # en una entrada concreta (no solo generar la tabla completa)
        resultado = evaluar_entrada(expresion2, True, False, True, False)
        self.assertEqual(resultado, True)


if __name__ == '__main__':
    unittest.main()