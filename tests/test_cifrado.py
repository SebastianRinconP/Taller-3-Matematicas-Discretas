import unittest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
from criptografia.cifrado_desplazamiento import cifrar, descifrar, romper_por_fuerza_bruta


class TestCifradoDesplazamiento(unittest.TestCase):

    def test_ejemplo_del_enunciado(self):
        self.assertEqual(cifrar("HOLA UNAL", 3), "KROD XQDO")

    def test_descifrar_deshace_el_cifrado(self):
        original = "Matematicas Discretas, grupo 4!"
        k = 9
        self.assertEqual(descifrar(cifrar(original, k), k), original)

    def test_no_altera_simbolos_no_alfabeticos(self):
        original = "Sala 305, bloque B - 8:15 am"
        k = 5
        resultado = cifrar(original, k)
        for i in range(len(original)):
            if not original[i].isalpha():
                self.assertEqual(original[i], resultado[i])

    def test_mayusculas_y_minusculas_no_se_mezclan(self):
        self.assertEqual(cifrar("aA", 1), "bB")

    def test_desplazamientos_equivalentes_dan_igual_resultado(self):
        texto = "PROGRAMACION"
        self.assertEqual(cifrar(texto, 4), cifrar(texto, 4 + 26))
        self.assertEqual(cifrar(texto, -3), cifrar(texto, 23))

    def test_fuerza_bruta_encuentra_el_desplazamiento_real(self):
        original = "MATEMATICAS DISCRETAS"
        k_real = 11
        cifrado = cifrar(original, k_real)
        candidatos = romper_por_fuerza_bruta(cifrado)
        self.assertEqual(len(candidatos), 26)
        self.assertEqual(candidatos[k_real], original)


if __name__ == "__main__":
    unittest.main()