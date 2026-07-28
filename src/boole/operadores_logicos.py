"""
Generador de tablas de verdad para expresiones booleanas con A, B, C, D
usando los conectivos AND (and), OR (or), NOT (not) y XOR (!=).

En Python no existe un operador nativo "XOR" para booleanos, pero se puede
simular con el operador != (distinto), ya que:
    True != False  -> True   (equivalente a 1 XOR 0 = 1)
    True != True   -> False  (equivalente a 1 XOR 1 = 0)
"""

from itertools import product


# ---------------------------------------------------------
# 1. Definición de las expresiones booleanas
#    Cada expresión es una función que recibe A, B, C, D
#    y devuelve el resultado lógico (True/False).
# ---------------------------------------------------------

def expresion1(A, B, C, D):
    """(A AND B) OR (NOT C)"""
    return (A and B) or (not C)


def expresion2(A, B, C, D):
    """(A XOR B) AND C"""
    return (A != B) and C


def expresion3(A, B, C, D):
    """(A OR B) AND (NOT A OR C)"""
    return (A or B) and ((not A) or C)


# Diccionario con las expresiones a evaluar: nombre -> (función, variables usadas)
EXPRESIONES = {
    "(A AND B) OR (NOT C)": (expresion1, ["A", "B", "C"]),
    "(A XOR B) AND C": (expresion2, ["A", "B", "C"]),
    "(A OR B) AND (NOT A OR C)": (expresion3, ["A", "B", "C", "A"]),  # A y C repetido intencional, se limpia abajo
}

# Limpiamos duplicados manteniendo el orden
for nombre in EXPRESIONES:
    func, vars_ = EXPRESIONES[nombre]
    vars_unicas = list(dict.fromkeys(vars_))
    EXPRESIONES[nombre] = (func, vars_unicas)


# ---------------------------------------------------------
# 2. Generar e imprimir la tabla de verdad de una expresión
# ---------------------------------------------------------

def generar_tabla(nombre, func, variables):
    print(f"\nTabla de verdad para: {nombre}")
    encabezado = "  ".join(variables) + " | Resultado"
    print(encabezado)
    print("-" * len(encabezado))

    combinaciones = list(product([False, True], repeat=len(variables)))
    for combo in combinaciones:
        valores = dict(zip(variables, combo))
        # Rellenamos con False las variables no usadas por la expresión
        A = valores.get("A", False)
        B = valores.get("B", False)
        C = valores.get("C", False)
        D = valores.get("D", False)
        resultado = func(A, B, C, D)

        fila = "  ".join(str(int(valores[v])) for v in variables)
        print(f"{fila}  |    {int(resultado)}")


# ---------------------------------------------------------
# 3. Evaluar una expresión con una entrada concreta
# ---------------------------------------------------------

def evaluar_entrada(func, A, B, C, D):
    return func(A, B, C, D)


# ---------------------------------------------------------
# 4. Programa principal
# ---------------------------------------------------------

if __name__ == "__main__":
    # Generar todas las tablas de verdad
    for nombre, (func, variables) in EXPRESIONES.items():
        generar_tabla(nombre, func, variables)

    # Ejemplo de evaluación en una entrada concreta
    print("\n--- Evaluación en una entrada concreta ---")
    A, B, C, D = True, False, True, False
    print(f"Entrada: A={int(A)}, B={int(B)}, C={int(C)}, D={int(D)}")
    for nombre, (func, _) in EXPRESIONES.items():
        resultado = evaluar_entrada(func, A, B, C, D)
        print(f"{nombre} = {int(resultado)}")