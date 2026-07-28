# Ejercicio 1 - Cifrado por desplazamiento (César).
# Versión simple: se recorre el texto letra por letra con un ciclo for.

ALFABETO_MAYUS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
ALFABETO_MINUS = "abcdefghijklmnopqrstuvwxyz"


def cifrar(texto, desplazamiento):
    """Cifra el texto moviendo cada letra 'desplazamiento' posiciones.
    Los espacios, números y signos de puntuación se dejan igual."""
    desplazamiento = desplazamiento % 26
    resultado = ""

    for letra in texto:
        if letra in ALFABETO_MAYUS:
            posicion = ALFABETO_MAYUS.index(letra)
            nueva_posicion = (posicion + desplazamiento) % 26
            resultado = resultado + ALFABETO_MAYUS[nueva_posicion]
        elif letra in ALFABETO_MINUS:
            posicion = ALFABETO_MINUS.index(letra)
            nueva_posicion = (posicion + desplazamiento) % 26
            resultado = resultado + ALFABETO_MINUS[nueva_posicion]
        else:
            resultado = resultado + letra

    return resultado


def descifrar(texto, desplazamiento):
    """Descifrar es cifrar con el desplazamiento contrario."""
    return cifrar(texto, -desplazamiento)


def romper_por_fuerza_bruta(texto_cifrado):
    """Prueba los 26 desplazamientos posibles y devuelve un diccionario
    con el resultado de cada uno, para que se pueda revisar cuál tiene
    sentido."""
    resultados = {}
    for k in range(26):
        resultados[k] = descifrar(texto_cifrado, k)
    return resultados


def menu():
    while True:
        print("\n=== Cifrado por desplazamiento (César) ===")
        print("1. Cifrar")
        print("2. Descifrar")
        print("3. Fuerza bruta")
        print("4. Salir")
        opcion = input("Elige una opción: ").strip()

        if opcion == "1":
            texto = input("Texto a cifrar: ")
            k = int(input("Desplazamiento: "))
            print("Resultado:", cifrar(texto, k))
        elif opcion == "2":
            texto = input("Texto a descifrar: ")
            k = int(input("Desplazamiento: "))
            print("Resultado:", descifrar(texto, k))
        elif opcion == "3":
            texto = input("Texto cifrado: ")
            resultados = romper_por_fuerza_bruta(texto)
            for k in resultados:
                print(f"  k={k}: {resultados[k]}")
        elif opcion == "4":
            print("Fin del programa.")
            break
        else:
            print("Opción no reconocida.")


if __name__ == "__main__":
    menu()
