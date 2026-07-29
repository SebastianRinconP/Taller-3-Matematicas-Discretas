import unittest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
from criptografia.mpc_basico import (
    repartir_valor,
    repartir_notas,
    suma_servidor,
    reconstruir_suma,
    calcular_promedio,
    simular_protocolo,
)


class TestSumaSegura(unittest.TestCase):

    def test_partes_suman_el_valor_original(self):
        s1, s2, s3 = repartir_valor(37)
        self.assertEqual((s1 + s2 + s3) % 1000003, 37)

    def test_ejemplo_del_enunciado(self):
        resultado = simular_protocolo([40, 35, 50, 25])
        self.assertEqual(resultado["suma_total"], 150)
        self.assertEqual(resultado["promedio"], 37.5)

    def test_ninguna_parte_individual_revela_el_valor(self):
        s1, s2, s3 = repartir_valor(45)
        self.assertTrue(s1 != 45 or s2 != 45 or s3 != 45)

    def test_valor_fuera_de_rango_lanza_error(self):
        with self.assertRaises(ValueError):
            repartir_valor(51)
        with self.assertRaises(ValueError):
            repartir_valor(-1)

    def test_lista_vacia_lanza_error(self):
        with self.assertRaises(ValueError):
            simular_protocolo([])

    def test_promedio_sin_valores_lanza_error(self):
        with self.assertRaises(ValueError):
            calcular_promedio(suma_total=0, cantidad_notas=0)

    def test_repartir_y_reconstruir_con_una_sola_nota(self):
        partes1, partes2, partes3 = repartir_notas([20])
        suma1 = suma_servidor(partes1)
        suma2 = suma_servidor(partes2)
        suma3 = suma_servidor(partes3)
        self.assertEqual(reconstruir_suma(suma1, suma2, suma3), 20)


if __name__ == "__main__":
    unittest.main()
