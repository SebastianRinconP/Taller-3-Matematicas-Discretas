# Ejercicio 2 - RSA de juguete. Solo con fines educativos.


def mcd_extendido(a, b):
    """Algoritmo de Euclides extendido, escrito con un ciclo while.
    Devuelve (g, x, y) tales que a*x + b*y = g = mcd(a, b)."""
    x0, x1 = 1, 0
    y0, y1 = 0, 1

    while b != 0:
        cociente = a // b
        a, b = b, a - cociente * b
        x0, x1 = x1, x0 - cociente * x1
        y0, y1 = y1, y0 - cociente * y1

    return a, x0, y0


def calcular_inverso(numero, modulo):
    """Busca d tal que numero*d ≡ 1 (mod modulo)."""
    g, x, y = mcd_extendido(numero, modulo)
    if g != 1:
        raise ValueError(f"{numero} no tiene inverso módulo {modulo}.")
    return x % modulo


def es_primo(n):
    if n < 2:
        return False
    for divisor in range(2, int(n ** 0.5) + 1):
        if n % divisor == 0:
            return False
    return True


def crear_llaves(p, q, e):
    """Devuelve un diccionario con p, q, n, phi, e y d."""
    if not es_primo(p) or not es_primo(q):
        raise ValueError("p y q deben ser primos.")
    if p == q:
        raise ValueError("p y q deben ser distintos.")

    n = p * q
    phi = (p - 1) * (q - 1)
    d = calcular_inverso(e, phi)

    return {"p": p, "q": q, "n": n, "phi": phi, "e": e, "d": d}


def cifrar(mensaje, llaves):
    """C = M^e mod n."""
    if mensaje < 0 or mensaje >= llaves["n"]:
        raise ValueError("El mensaje debe cumplir 0 <= M < n.")
    return pow(mensaje, llaves["e"], llaves["n"])


def descifrar(cifrado, llaves):
    """M = C^d mod n."""
    return pow(cifrado, llaves["d"], llaves["n"])


def pedir_numero(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Debe ser un número entero.")


def menu():
    llaves = None
    while True:
        print("\n=== RSA de juguete ===")
        if llaves:
            print(f"Llaves actuales -> n={llaves['n']}, e={llaves['e']}, d={llaves['d']}")
        print("1. Crear llaves")
        print("2. Cifrar mensaje")
        print("3. Descifrar mensaje")
        print("4. Salir")
        opcion = input("Elige una opción: ").strip()

        if opcion == "1":
            p = pedir_numero("p: ")
            q = pedir_numero("q: ")
            e = pedir_numero("e: ")
            try:
                llaves = crear_llaves(p, q, e)
                print(f"n={llaves['n']}, phi(n)={llaves['phi']}, d={llaves['d']}")
            except ValueError as error:
                print("Error:", error)

        elif opcion == "2":
            if llaves is None:
                print("Primero crea las llaves.")
                continue
            m = pedir_numero("Mensaje M: ")
            try:
                print("Cifrado:", cifrar(m, llaves))
            except ValueError as error:
                print("Error:", error)

        elif opcion == "3":
            if llaves is None:
                print("Primero crea las llaves.")
                continue
            c = pedir_numero("Cifrado C: ")
            print("Mensaje:", descifrar(c, llaves))

        elif opcion == "4":
            print("Fin del programa.")
            break

        else:
            print("Opción no reconocida.")


if __name__ == "__main__":
    menu()
