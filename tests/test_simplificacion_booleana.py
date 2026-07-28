import unittest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../src/boole'))
from simplificacion_booleana import (
    num_a_binario,
    se_combinan,
    simplificar,
    verificar_equivalencia,
)


class TestSimplificacionBooleana(unittest.TestCase):

    def test_num_a_binario(self):
        self.assertEqual(num_a_binario(5, 3), "101")
        self.assertEqual(num_a_binario(11, 4), "1011")

    def test_se_combinan_un_bit_de_diferencia(self):
        self.assertEqual(se_combinan("001", "101"), "-01")

    def test_se_combinan_mas_de_un_bit_no_combina(self):
        self.assertIsNone(se_combinan("001", "110"))

    def test_caso_sugerido_del_taller_minterminos_1_3_5_7(self):
        # Caso de prueba sugerido en el enunciado: con A,B,C la simplificacion
        # esperada es una expresion equivalente a C
        minterminos = {1, 3, 5, 7}
        elegidos, expresion = simplificar(minterminos, num_vars=3,
                                           nombres_variables=["A", "B", "C"])
        self.assertEqual(elegidos, ["--1"])  # unico termino, equivalente a "C"

    def test_original_y_simplificada_tienen_la_misma_tabla_de_verdad(self):
        # Condicion del taller: el programa debe comprobar que la expresion
        # original y la simplificada tienen la misma tabla de verdad
        minterminos = {1, 3, 5, 7}
        elegidos, _ = simplificar(minterminos, num_vars=3)
        ok, original, simplificada = verificar_equivalencia(minterminos, elegidos, 3)
        self.assertTrue(ok)
        self.assertEqual(original, simplificada)

    def test_funcion_siempre_falsa_sin_minterminos(self):
        elegidos, expresion = simplificar(set(), num_vars=3)
        self.assertEqual(expresion, "0")

    def test_funcion_siempre_verdadera_con_todos_los_minterminos(self):
        minterminos = set(range(8))  # 2**3 combinaciones, todas en 1
        elegidos, _ = simplificar(minterminos, num_vars=3)
        ok, original, simplificada = verificar_equivalencia(minterminos, elegidos, 3)
        self.assertTrue(ok)
        self.assertTrue(all(v == 1 for v in simplificada.values()))

    def test_equivalencia_para_varios_conjuntos_de_minterminos(self):
        # Prueba general con subTest: la simplificacion nunca debe cambiar
        # el comportamiento del circuito, para ningun conjunto de minterminos
        casos = [
            ({0, 2, 4, 6}, 3),
            ({1, 2, 3, 4, 5, 6, 7}, 3),
            ({0, 1, 2, 3, 8, 9, 10, 11}, 4),
            ({5, 7, 13, 15}, 4),
        ]
        for minterminos, num_vars in casos:
            with self.subTest(minterminos=minterminos, num_vars=num_vars):
                elegidos, _ = simplificar(minterminos, num_vars)
                ok, original, simplificada = verificar_equivalencia(minterminos, elegidos, num_vars)
                self.assertTrue(ok)


if __name__ == '__main__':
    unittest.main()