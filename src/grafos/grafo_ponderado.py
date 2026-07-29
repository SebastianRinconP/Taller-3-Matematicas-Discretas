# Estructura de grafo y algoritmo de ruta más corta (usado en los puntos 4 y 5).
#   vecinos = {"A": {"B": 4, "C": 2}, "B": {"A": 4}, ...}


class GrafoPonderado:

    def __init__(self):
        self.vecinos = {}

    def agregar_vertice(self, nombre):
        if nombre not in self.vecinos:
            self.vecinos[nombre] = {}

    def agregar_arista(self, origen, destino, peso):
        self.agregar_vertice(origen)
        self.agregar_vertice(destino)
        self.vecinos[origen][destino] = peso
        self.vecinos[destino][origen] = peso

    def quitar_vertice(self, nombre):
        """Devuelve un grafo nuevo, sin 'nombre' y sin las aristas que lo
        conectaban con otros vértices."""
        nuevo = GrafoPonderado()
        for vertice in self.vecinos:
            if vertice == nombre:
                continue
            for destino in self.vecinos[vertice]:
                if destino != nombre:
                    peso = self.vecinos[vertice][destino]
                    nuevo.agregar_arista(vertice, destino, peso)
        return nuevo

    def lista_de_vertices(self):
        return list(self.vecinos.keys())

    def tiene_vertice(self, nombre):
        return nombre in self.vecinos

    def distancias_desde(self, origen):
        """Algoritmo de Dijkstra escrito de forma directa: en cada paso se
        busca, con un ciclo for, el vértice no confirmado con menor
        distancia, y se actualizan sus vecinos."""
        distancia = {}
        anterior = {}
        for vertice in self.vecinos:
            distancia[vertice] = float("inf")
            anterior[vertice] = None
        distancia[origen] = 0

        confirmados = []

        while len(confirmados) < len(self.vecinos):
            # Buscar el vértice no confirmado con menor distancia
            actual = None
            menor_distancia = float("inf")
            for vertice in self.vecinos:
                if vertice not in confirmados and distancia[vertice] < menor_distancia:
                    menor_distancia = distancia[vertice]
                    actual = vertice

            if actual is None:
                break  # ya no quedan vértices alcanzables

            confirmados.append(actual)

            for vecino in self.vecinos[actual]:
                peso = self.vecinos[actual][vecino]
                nueva_distancia = distancia[actual] + peso
                if nueva_distancia < distancia[vecino]:
                    distancia[vecino] = nueva_distancia
                    anterior[vecino] = actual

        return distancia, anterior


def camino_hacia(anterior, origen, destino):
    """Arma la lista de vértices del camino más corto, recorriendo el
    diccionario 'anterior' hacia atrás desde el destino."""
    if destino not in anterior:
        return None

    camino = [destino]
    actual = destino
    while actual != origen:
        actual = anterior[actual]
        if actual is None:
            return None
        camino.append(actual)

    camino.reverse()
    return camino
