"""
Generador de tablas de verdad para expresiones booleanas con A, B, C, D
usando los conectivos AND (and), OR (or), NOT (not) y XOR (!=).

En Python no existe un operador nativo "XOR" para booleanos, pero se puede
simular con el operador != (distinto), ya que:
    True != False  -> True   (equivalente a 1 XOR 0 = 1)
    True != True   -> False  (equivalente a 1 XOR 1 = 0)
"""

from itertools import product


def expresion1(A, B, C, D):
    return (A and B) or (not C)


def expresion2(A, B, C, D):
    return (A != B) and C


def expresion3(A, B, C, D):
    return (A or B) and ((not A) or C)


# Diccionario con las expresiones a evaluar: nombre -> (función, variables usadas)
EXPRESIONES = {
    "(A AND B) OR (NOT C)": (expresion1, ["A", "B", "C"]),
    "(A XOR B) AND C": (expresion2, ["A", "B", "C"]),
    "(A OR B) AND (NOT A OR C)": (expresion3, ["A", "B", "C", "A"]),  # A y C repetido intencional, se limpia abajo
}
# EXPRESIONES es un diccionario que guarda, para cada fórmula su función y la lista de variables 
# que realmente usa (así la tabla no muestra columnas de más si una expresión no usa D, por ejemplo)

for nombre in EXPRESIONES:
    func, vars_ = EXPRESIONES[nombre]
    vars_unicas = list(dict.fromkeys(vars_))
    EXPRESIONES[nombre] = (func, vars_unicas)


def generar_tabla(nombre, func, variables):
    print(f"\nTabla de verdad para: {nombre}")
    encabezado = "  ".join(variables) + " | Resultado"
    print(encabezado)
    print("-" * len(encabezado))

    combinaciones = list(product([False, True], repeat=len(variables)))
    for combo in combinaciones:
        valores = dict(zip(variables, combo))
        A = valores.get("A", False)
        B = valores.get("B", False)
        C = valores.get("C", False)
        D = valores.get("D", False)
        resultado = func(A, B, C, D)

        fila = "  ".join(str(int(valores[v])) for v in variables)
        print(f"{fila}  |    {int(resultado)}")

#generar_tabla usa itertools.product([False, True], repeat=n) para generar automáticamente todas las combinaciones posibles de 0 y 1 
# según el número de variables. Por cada combinación evalúa la función y la imprime en formato de tabla.

def evaluar_entrada(func, A, B, C, D):
    return func(A, B, C, D)

if __name__ == "__main__":
    for nombre, (func, variables) in EXPRESIONES.items():
        generar_tabla(nombre, func, variables)

    print("\n--- Evaluación en una entrada concreta ---")
    A, B, C, D = True, False, True, False #EJEMPLO CON ENTRADA COMPLETA
    print(f"Entrada: A={int(A)}, B={int(B)}, C={int(C)}, D={int(D)}")
    for nombre, (func, _) in EXPRESIONES.items():
        resultado = evaluar_entrada(func, A, B, C, D)
        print(f"{nombre} = {int(resultado)}")

    print("INGRESADO MANUAL (True or False)")
    A = bool(input("Ingrese su valor A: ").lower().capitalize())
    B = bool(input("Ingrese su valor B: ").lower().capitalize())
    C = bool(input("Ingrese su valor C: ").lower().capitalize())
    D = bool(input("Ingrese su valor D: ").lower().capitalize())

    for nombre, (func, _) in EXPRESIONES.items():
        resultado = evaluar_entrada(func, A, B, C, D)
        print(f"{nombre} = {int(resultado)}")
""""
    Un circuito lógico es un sistema electrónico o matemático que procesa 
    información usando señales de encendido y apagado. Sus componentes principales son las compuertas lógicas, 
    las entradas binarias y las salidas de datos, las tablas de verdad se relacionan con los circuitos logicos 
    ya que modelan todos los posibles resultados de un circuito logico, dependiendo de sus valores de entrada
"""