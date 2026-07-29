# Ejercicio 4 - Ruta más corta entre dos puntos de un campus, modelado como grafo.
from grafo_ponderado import GrafoPonderado, camino_hacia


def red_del_campus():
    """Grafo de prueba con 8 vértices y 12 aristas. El peso de cada
    arista es el tiempo caminando en minutos entre dos puntos."""
    g = GrafoPonderado()
    g.agregar_arista("Biblioteca", "Auditorio", 6)
    g.agregar_arista("Biblioteca", "Cafeteria", 3)
    g.agregar_arista("Auditorio", "Cafeteria", 4)
    g.agregar_arista("Auditorio", "Laboratorio", 9)
    g.agregar_arista("Cafeteria", "Coliseo", 7)
    g.agregar_arista("Laboratorio", "Coliseo", 2)
    g.agregar_arista("Laboratorio", "Posgrados", 10)
    g.agregar_arista("Coliseo", "Bloque5", 5)
    g.agregar_arista("Posgrados", "Bloque5", 3)
    g.agregar_arista("Posgrados", "Bloque6", 8)
    g.agregar_arista("Bloque5", "Bloque6", 4)
    g.agregar_arista("Bloque6", "Cafeteria", 12)
    return g


def encontrar_ruta(g, origen, destino):
    """Devuelve el tiempo total y la lista de puntos del recorrido más
    corto entre origen y destino."""
    distancia, anterior = g.distancias_desde(origen)
    tiempo_total = distancia[destino]
    recorrido = camino_hacia(anterior, origen, destino)
    return tiempo_total, recorrido


if __name__ == "__main__":
    campus = red_del_campus()

    pares = [("Biblioteca", "Bloque6"), ("Auditorio", "Posgrados")]
    for origen, destino in pares:
        minutos, recorrido = encontrar_ruta(campus, origen, destino)
        print(f"{origen} -> {destino}: {minutos} min")
        print("Recorrido:", " -> ".join(recorrido))
        print()
