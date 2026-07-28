from itertools import product

def num_a_binario(n, num_vars):
    return format(n, f"0{num_vars}b")


def se_combinan(term1, term2):
    diferencias = 0
    resultado = []
    for b1, b2 in zip(term1, term2):
        if b1 != b2:
            diferencias += 1
            resultado.append("-")
        else:
            resultado.append(b1)
    if diferencias == 1:
        return "".join(resultado)
    return None


# ---------------------------------------------------------
# 2. Algoritmo de Quine-McCluskey
# ---------------------------------------------------------

def encontrar_implicantes_primos(minterminos, num_vars):
    # grupo inicial: (termino_binario, {minterminos que representa})
    grupo_actual = {num_a_binario(m, num_vars): {m} for m in minterminos}

    implicantes_primos = {}  # termino -> set de minterminos que cubre
    while grupo_actual:
        combinados = {}
        usados = set()
        terminos = list(grupo_actual.keys())

        for i in range(len(terminos)):
            for j in range(i + 1, len(terminos)):
                nuevo = se_combinan(terminos[i], terminos[j])
                if nuevo is not None:
                    usados.add(terminos[i])
                    usados.add(terminos[j])
                    cubiertos = grupo_actual[terminos[i]] | grupo_actual[terminos[j]]
                    combinados[nuevo] = combinados.get(nuevo, set()) | cubiertos

        for termino in terminos:
            if termino not in usados:
                implicantes_primos[termino] = grupo_actual[termino]

        grupo_actual = combinados

    return implicantes_primos


def elegir_implicantes_esenciales(implicantes_primos, minterminos):
    pendientes = set(minterminos)
    seleccionados = []

    # Paso 1: implicantes esenciales
    for m in list(pendientes):
        cubridores = [t for t, cubiertos in implicantes_primos.items() if m in cubiertos]
        if len(cubridores) == 1 and cubridores[0] not in seleccionados:
            seleccionados.append(cubridores[0])

    for t in seleccionados:
        pendientes -= implicantes_primos[t]

    while pendientes:
        mejor = max(
            implicantes_primos,
            key=lambda t: len(implicantes_primos[t] & pendientes)
        )
        if len(implicantes_primos[mejor] & pendientes) == 0:
            break
        if mejor not in seleccionados:
            seleccionados.append(mejor)
        pendientes -= implicantes_primos[mejor]

    return seleccionados


def termino_a_expresion(termino, nombres_variables):
    literales = []
    for bit, var in zip(termino, nombres_variables):
        if bit == "1":
            literales.append(var)
        elif bit == "0":
            literales.append(f"NOT {var}")
    if not literales:
        return "1"  # la funcion es siempre verdadera
    return " AND ".join(literales)


def simplificar(minterminos, num_vars, nombres_variables=None):

    if nombres_variables is None:
        nombres_variables = ["A", "B", "C", "D"][:num_vars]

    if not minterminos:
        return [], "0"  # funcion siempre falsa

    implicantes_primos = encontrar_implicantes_primos(minterminos, num_vars)
    elegidos = elegir_implicantes_esenciales(implicantes_primos, minterminos)

    productos = [termino_a_expresion(t, nombres_variables) for t in elegidos]
    expresion = " OR ".join(f"({p})" for p in productos)
    return elegidos, expresion


# ---------------------------------------------------------
# 3. Verificacion: comparar tabla de verdad original vs simplificada
# ---------------------------------------------------------

def tabla_desde_minterminos(minterminos, num_vars):
    """Genera la tabla de verdad (dict: tupla_de_bits -> 0/1) a partir de los minterminos."""
    tabla = {}
    for combo in product([0, 1], repeat=num_vars):
        n = int("".join(map(str, combo)), 2)
        tabla[combo] = 1 if n in minterminos else 0
    return tabla


def evaluar_termino(termino, combo):
    """Evalua un termino binario con '-' contra una combinacion concreta de bits."""
    for bit, valor in zip(termino, combo):
        if bit == "0" and valor != 0:
            return False
        if bit == "1" and valor != 1:
            return False
    return True


def tabla_desde_terminos(terminos, num_vars):
    """Genera la tabla de verdad de la expresion simplificada (OR de los terminos)."""
    tabla = {}
    for combo in product([0, 1], repeat=num_vars):
        tabla[combo] = 1 if any(evaluar_termino(t, combo) for t in terminos) else 0
    return tabla


def verificar_equivalencia(minterminos, terminos, num_vars):
    """Devuelve True si la tabla de verdad original y la simplificada coinciden en todas las filas."""
    original = tabla_desde_minterminos(minterminos, num_vars)
    simplificada = tabla_desde_terminos(terminos, num_vars)
    return original == simplificada, original, simplificada


# ---------------------------------------------------------
# 4. Programa principal / caso de prueba
# ---------------------------------------------------------

def mostrar_caso(minterminos, num_vars, nombres_variables=None):
    if nombres_variables is None:
        nombres_variables = ["A", "B", "C", "D"][:num_vars]

    print(f"\nMinterminos: {sorted(minterminos)}  (variables: {', '.join(nombres_variables)})")
    elegidos, expresion = simplificar(minterminos, num_vars, nombres_variables)
    print(f"Expresion simplificada: {expresion}")

    ok, original, simplificada = verificar_equivalencia(minterminos, elegidos, num_vars)
    print(f"Verificacion: la tabla original y la simplificada son {'IGUALES' if ok else 'DIFERENTES'}")

    print(f"{'  '.join(nombres_variables)} | Original | Simplificada")
    for combo in sorted(original):
        fila = "  ".join(str(b) for b in combo)
        print(f"{fila}  |    {original[combo]}     |     {simplificada[combo]}")


if __name__ == "__main__":
    # --- Caso de prueba sugerido: 3 variables, minterminos {1, 3, 5, 7} ---
    # Con orden de variables A, B, C, el resultado esperado es equivalente a "C"
    mostrar_caso(minterminos={1, 3, 5, 7}, num_vars=3, nombres_variables=["A", "B", "C"])

    # --- Otro caso con 3 variables ---
    mostrar_caso(minterminos={0, 2, 4, 6}, num_vars=3, nombres_variables=["A", "B", "C"])

    # --- Caso con 4 variables ---
    mostrar_caso(minterminos={0, 1, 2, 3, 8, 9, 10, 11}, num_vars=4, nombres_variables=["A", "B", "C", "D"])