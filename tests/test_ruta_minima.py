import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "..", "src", "redes"))

from grafo_ponderado import GrafoPonderado, camino_hacia
from ruta_minima import red_del_campus, encontrar_ruta


def test_red_del_campus_tiene_8_vertices_y_12_aristas():
    g = red_del_campus()
    total_aristas = 0
    for vertice in g.vecinos:
        total_aristas = total_aristas + len(g.vecinos[vertice])
    total_aristas = total_aristas // 2

    assert len(g.lista_de_vertices()) == 8
    assert total_aristas == 12


def test_ruta_biblioteca_a_bloque6():
    g = red_del_campus()
    minutos, recorrido = encontrar_ruta(g, "Biblioteca", "Bloque6")
    assert minutos == 15
    assert recorrido == ["Biblioteca", "Cafeteria", "Bloque6"]


def test_ruta_auditorio_a_posgrados():
    g = red_del_campus()
    minutos, recorrido = encontrar_ruta(g, "Auditorio", "Posgrados")
    assert minutos == 19
    assert recorrido == ["Auditorio", "Laboratorio", "Posgrados"]


def test_distancia_de_un_vertice_a_si_mismo_es_cero():
    g = red_del_campus()
    distancia, _ = g.distancias_desde("Coliseo")
    assert distancia["Coliseo"] == 0


def test_vertice_aislado_queda_inalcanzable():
    g = GrafoPonderado()
    g.agregar_arista("X", "Y", 1)
    g.agregar_vertice("Z")  # Z no tiene ninguna arista
    distancia, anterior = g.distancias_desde("X")
    assert distancia["Z"] == float("inf")
    assert camino_hacia(anterior, "X", "Z") is None
