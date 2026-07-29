import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "..", "src", "redes"))

from grafo_ponderado import GrafoPonderado
from ruta_minima import red_del_campus
from impacto_cierre import medir_impacto, SIN_CAMBIO, MAS_LARGO, DESCONECTADO


def test_cierre_cafeteria_afecta_varias_rutas():
    g = red_del_campus()
    g_sin_cafeteria = g.quitar_vertice("Cafeteria")

    pares = [
        ("Biblioteca", "Bloque6"),
        ("Biblioteca", "Coliseo"),
        ("Auditorio", "Coliseo"),
        ("Biblioteca", "Posgrados"),
        ("Auditorio", "Bloque6"),
    ]
    resultados = medir_impacto(g, g_sin_cafeteria, pares)

    assert resultados[0]["diferencia"] == 11
    assert resultados[1]["diferencia"] == 7
    assert resultados[2]["estado"] == SIN_CAMBIO
    assert resultados[3]["diferencia"] == 7
    assert resultados[4]["diferencia"] == 4


def test_cierre_de_un_extremo_no_afecta_rutas_que_no_lo_usan():
    g = red_del_campus()
    g_sin_posgrados = g.quitar_vertice("Posgrados")

    pares = [("Biblioteca", "Coliseo"), ("Auditorio", "Cafeteria")]
    resultados = medir_impacto(g, g_sin_posgrados, pares)

    for r in resultados:
        assert r["estado"] == SIN_CAMBIO


def test_cierre_provoca_desconexion():
    # Grafo lineal simple, solo para mostrar el caso de desconexión.
    g = GrafoPonderado()
    g.agregar_arista("Punto1", "Punto2", 2)
    g.agregar_arista("Punto2", "Punto3", 3)
    g.agregar_arista("Punto3", "Punto4", 4)
    g.agregar_arista("Punto4", "Punto5", 1)

    g_sin_punto3 = g.quitar_vertice("Punto3")
    pares = [("Punto1", "Punto5"), ("Punto2", "Punto4"), ("Punto1", "Punto2")]
    resultados = medir_impacto(g, g_sin_punto3, pares)

    assert resultados[0]["estado"] == DESCONECTADO
    assert resultados[1]["estado"] == DESCONECTADO
    assert resultados[2]["estado"] == SIN_CAMBIO
