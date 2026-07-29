import unittest
import sys
import os
import math

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../src/cuantica'))
from simulador_cuantico import (
    ESTADO_0,
    ESTADO_1,
    X,
    Z,
    H,
    aplicar_compuerta,
    calcular_probabilidades,
    simular_mediciones,
)


class TestAplicarCompuerta(unittest.TestCase):

    def test_x_sobre_estado_0_da_estado_1(self):
        resultado = aplicar_compuerta(X, ESTADO_0)
        self.assertAlmostEqual(resultado[0].real, ESTADO_1[0].real, places=6)
        self.assertAlmostEqual(resultado[1].real, ESTADO_1[1].real, places=6)

    def test_x_sobre_estado_1_da_estado_0(self):
        resultado = aplicar_compuerta(X, ESTADO_1)
        self.assertAlmostEqual(resultado[0].real, ESTADO_0[0].real, places=6)
        self.assertAlmostEqual(resultado[1].real, ESTADO_0[1].real, places=6)

    def test_z_no_cambia_estado_0(self):
        resultado = aplicar_compuerta(Z, ESTADO_0)
        self.assertAlmostEqual(resultado[0].real, 1.0, places=6)
        self.assertAlmostEqual(resultado[1].real, 0.0, places=6)

    def test_hh_sobre_estado_0_devuelve_estado_0(self):
        primero = aplicar_compuerta(H, ESTADO_0)
        segundo = aplicar_compuerta(H, primero)
        self.assertAlmostEqual(segundo[0].real, 1.0, places=6)
        self.assertAlmostEqual(segundo[1].real, 0.0, places=6)


class TestCalcularProbabilidades(unittest.TestCase):

    def test_probabilidades_estado_0(self):
        p0, p1 = calcular_probabilidades(ESTADO_0)
        self.assertAlmostEqual(p0, 1.0, places=6)
        self.assertAlmostEqual(p1, 0.0, places=6)

    def test_probabilidades_estado_1(self):
        p0, p1 = calcular_probabilidades(ESTADO_1)
        self.assertAlmostEqual(p0, 0.0, places=6)
        self.assertAlmostEqual(p1, 1.0, places=6)

    def test_h_sobre_estado_0_da_probabilidades_50_50(self):
        estado_h = aplicar_compuerta(H, ESTADO_0)
        p0, p1 = calcular_probabilidades(estado_h)
        self.assertAlmostEqual(p0, 0.5, places=6)
        self.assertAlmostEqual(p1, 0.5, places=6)


class TestPropiedadesGenerales(unittest.TestCase):
    def test_probabilidades_suman_uno(self):
        estados = [
            ESTADO_0,
            ESTADO_1,
            aplicar_compuerta(X, ESTADO_0),
            aplicar_compuerta(H, ESTADO_0),
            aplicar_compuerta(Z, ESTADO_0),
            aplicar_compuerta(H, aplicar_compuerta(H, ESTADO_0)),
        ]
        for estado in estados:
            with self.subTest(estado=estado):
                p0, p1 = calcular_probabilidades(estado)
                self.assertAlmostEqual(p0 + p1, 1.0, places=6)


class TestSimularMediciones(unittest.TestCase):
    def test_estado_0_siempre_mide_0(self):
        f0, f1 = simular_mediciones(ESTADO_0, n_mediciones=1000)
        self.assertAlmostEqual(f0, 1.0, places=6)
        self.assertAlmostEqual(f1, 0.0, places=6)

    def test_frecuencias_suman_uno(self):
        estado_h = aplicar_compuerta(H, ESTADO_0)
        f0, f1 = simular_mediciones(estado_h, n_mediciones=1000)
        self.assertAlmostEqual(f0 + f1, 1.0, places=6)

    def test_h_da_frecuencias_cercanas_a_50_50(self):
        estado_h = aplicar_compuerta(H, ESTADO_0)
        f0, f1 = simular_mediciones(estado_h, n_mediciones=1000)
        self.assertGreater(f0, 0.4)
        self.assertLess(f0, 0.6)
        self.assertGreater(f1, 0.4)
        self.assertLess(f1, 0.6)


if __name__ == '__main__':
    unittest.main()