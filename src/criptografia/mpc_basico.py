# Ejercicio 3 - Suma segura entre 3 servidores (MPC básico).
import random

MODULO = 1000003  # número primo sugerido en el enunciado
NOTA_MIN = 0
NOTA_MAX = 50


def repartir_valor(valor, modulo=MODULO):
    """Reparte 'valor' en 3 partes aleatorias módulo 'modulo'.
    Se eligen s1 y s2 al azar, y s3 se calcula para que las tres partes,
    sumadas módulo 'modulo', den de vuelta el valor original."""
    if valor < NOTA_MIN or valor > NOTA_MAX:
        raise ValueError(f"El valor debe estar entre {NOTA_MIN} y {NOTA_MAX}.")

    s1 = random.randint(0, modulo - 1)
    s2 = random.randint(0, modulo - 1)
    s3 = (valor - s1 - s2) % modulo
    return s1, s2, s3


def repartir_notas(notas, modulo=MODULO):
    """Aplica repartir_valor a cada nota y agrupa las partes por servidor."""
    partes_servidor1 = []
    partes_servidor2 = []
    partes_servidor3 = []

    for nota in notas:
        s1, s2, s3 = repartir_valor(nota, modulo)
        partes_servidor1.append(s1)
        partes_servidor2.append(s2)
        partes_servidor3.append(s3)

    return partes_servidor1, partes_servidor2, partes_servidor3


def suma_servidor(partes, modulo=MODULO):
    """Cada servidor solo suma las partes que le tocaron."""
    total = 0
    for parte in partes:
        total = total + parte
    return total % modulo


def reconstruir_suma(suma1, suma2, suma3, modulo=MODULO):
    """Combina las sumas parciales de los 3 servidores en la suma real."""
    return (suma1 + suma2 + suma3) % modulo


def calcular_promedio(suma_total, cantidad_notas):
    if cantidad_notas <= 0:
        raise ValueError("No hay notas para calcular el promedio.")
    return suma_total / cantidad_notas


def simular_protocolo(notas, modulo=MODULO):
    """Corre el protocolo completo y devuelve un diccionario con todos
    los resultados."""
    if len(notas) == 0:
        raise ValueError("La lista de notas no puede estar vacía.")

    partes1, partes2, partes3 = repartir_notas(notas, modulo)
    suma1 = suma_servidor(partes1, modulo)
    suma2 = suma_servidor(partes2, modulo)
    suma3 = suma_servidor(partes3, modulo)
    suma_total = reconstruir_suma(suma1, suma2, suma3, modulo)
    promedio = calcular_promedio(suma_total, len(notas))

    return {
        "partes_servidor1": partes1,
        "partes_servidor2": partes2,
        "partes_servidor3": partes3,
        "suma_total": suma_total,
        "promedio": promedio,
    }


def menu():
    while True:
        print("\n=== Suma segura entre 3 servidores ===")
        print("1. Simular protocolo")
        print("2. Salir")
        opcion = input("Elige una opción: ").strip()

        if opcion == "1":
            texto = input("Notas separadas por coma (0 a 50, ej: 40,35,50,25): ")
            try:
                notas = []
                for parte in texto.split(","):
                    notas.append(int(parte.strip()))
                resultado = simular_protocolo(notas)
            except ValueError as error:
                print("Entrada inválida:", error)
                continue

            print("Partes servidor 1:", resultado["partes_servidor1"])
            print("Partes servidor 2:", resultado["partes_servidor2"])
            print("Partes servidor 3:", resultado["partes_servidor3"])
            print("Suma total:", resultado["suma_total"])
            print("Promedio:", resultado["promedio"])

        elif opcion == "2":
            print("Fin del programa.")
            break

        else:
            print("Opción no reconocida.")


if __name__ == "__main__":
    menu()
