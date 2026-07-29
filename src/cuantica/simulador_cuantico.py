import math #math solo se utiliza para la raiz cuadrada y el valor absoluto y me niego a hacerlo de otra forma
import random

ESTADO_0 = [1 + 0j, 0 + 0j]   # |0>
ESTADO_1 = [0 + 0j, 1 + 0j]   # |1>

X = [[0, 1],
     [1, 0]]

Z = [[1, 0],
     [0, -1]]

raiz2 = math.sqrt(2)
H = [[1 / raiz2, 1 / raiz2],
     [1 / raiz2, -1 / raiz2]]


def aplicar_compuerta(matriz, estado):
    nuevo_estado = []
    for fila in matriz:
        entrada = sum(fila[j] * estado[j] for j in range(len(estado)))
        nuevo_estado.append(entrada)
    return nuevo_estado


def calcular_probabilidades(estado):
    p0 = abs(estado[0]) ** 2
    p1 = abs(estado[1]) ** 2
    return p0, p1


def medir_una_vez(probabilidades):
    p0, _ = probabilidades
    return 0 if random.random() < p0 else 1


def simular_mediciones(estado, n_mediciones=1000):

    probabilidades = calcular_probabilidades(estado)
    conteo = {0: 0, 1: 0}
    for _ in range(n_mediciones):
        resultado = medir_una_vez(probabilidades)
        conteo[resultado] += 1

    frecuencia_0 = conteo[0] / n_mediciones
    frecuencia_1 = conteo[1] / n_mediciones
    return frecuencia_0, frecuencia_1


def mostrar_estado(estado, etiqueta=""):
    print(f"{etiqueta}Estado: {estado}")
    p0, p1 = calcular_probabilidades(estado)
    print(f"{etiqueta}P(0) = {p0:.4f}, P(1) = {p1:.4f}")


def main():
    print("=== Simulador de un qubit ===\n")

    print("Estado inicial |0>:")
    mostrar_estado(ESTADO_0)

    print("\nAplicando X a |0> (deberia dar |1>):")
    estado_x = aplicar_compuerta(X, ESTADO_0)
    mostrar_estado(estado_x)

    print("\nAplicando H a |0> (deberia dar ~50%/50%):")
    estado_h = aplicar_compuerta(H, ESTADO_0)
    mostrar_estado(estado_h)
    f0, f1 = simular_mediciones(estado_h, 1000)
    print(f"Frecuencias observadas en 1000 mediciones: 0 -> {f0:.3f}, 1 -> {f1:.3f}")

    print("\nAplicando H dos veces a |0> (deberia volver a |0>):")
    estado_hh = aplicar_compuerta(H, aplicar_compuerta(H, ESTADO_0))
    mostrar_estado(estado_hh)

    print("\nAplicando Z a |0> (Z no deberia cambiar |0>, |0> es su propio autoestado):")
    estado_z = aplicar_compuerta(Z, ESTADO_0)
    mostrar_estado(estado_z)


if __name__ == "__main__":
    main()