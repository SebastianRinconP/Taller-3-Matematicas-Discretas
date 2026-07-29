# Ejercicio 5 - Medir el impacto de cerrar un punto de la red del campus.
from grafo_ponderado import GrafoPonderado
from ruta_minima import red_del_campus

SIN_CAMBIO = "SIN CAMBIO"
MAS_LARGO = "MAS LARGO"
DESCONECTADO = "DESCONECTADO"


def medir_impacto(g_original, g_sin_punto, pares):
    """Para cada par (origen, destino) compara la distancia antes y
    después de quitar un vértice, y clasifica el resultado en un
    diccionario con los datos de esa comparación."""
    resultados = []

    for origen, destino in pares:
        distancia_antes, _ = g_original.distancias_desde(origen)
        antes = distancia_antes[destino]

        if g_sin_punto.tiene_vertice(origen) and g_sin_punto.tiene_vertice(destino):
            distancia_despues, _ = g_sin_punto.distancias_desde(origen)
            despues = distancia_despues[destino]
        else:
            despues = float("inf")

        if despues == float("inf"):
            estado = DESCONECTADO
            diferencia = None
            despues_texto = "N/A"
        elif despues > antes:
            estado = MAS_LARGO
            diferencia = despues - antes
            despues_texto = despues
        else:
            estado = SIN_CAMBIO
            diferencia = 0
            despues_texto = despues

        resultados.append({
            "origen": origen,
            "destino": destino,
            "antes": antes,
            "despues": despues_texto,
            "diferencia": diferencia,
            "estado": estado,
        })

    return resultados


def mostrar_tabla(resultados, punto_cerrado):
    print(f"Punto cerrado: {punto_cerrado}\n")
    print(f"{'Origen':<14}{'Destino':<14}{'Antes':<8}{'Despues':<10}{'Diferencia':<12}{'Estado'}")
    for r in resultados:
        print(f"{r['origen']:<14}{r['destino']:<14}{r['antes']:<8}"
              f"{str(r['despues']):<10}{str(r['diferencia']):<12}{r['estado']}")


if __name__ == "__main__":
    campus = red_del_campus()
    punto_cerrado = "Cafeteria"
    campus_sin_punto = campus.quitar_vertice(punto_cerrado)

    pares = [
        ("Biblioteca", "Bloque6"),
        ("Biblioteca", "Coliseo"),
        ("Auditorio", "Coliseo"),
        ("Biblioteca", "Posgrados"),
        ("Auditorio", "Bloque6"),
    ]

    resultados = medir_impacto(campus, campus_sin_punto, pares)
    mostrar_tabla(resultados, punto_cerrado)
