GRAFO = { #Esta vaina es un diccionario, muestra que clase se relaciona con que
    "Quimica" : ["Mecanica", "Fluidos"],
    "Mecanica": ["Calculo Diferencial","Quimica"],
    "Algebra" : ["Calculo Diferencial", "Programacion", "Discretas"],
    "Calculo Diferencial": ["Mecanica","Algebra"],
    "Programacion" : ["Algebra","Discretas", "Estructuras"],
    "Estadistica": ["Fluidos", "Bases"],
    "Discretas" : ["Algebra","Programacion","Estructuras"],
    "Fluidos" : ["Quimica","Estadistica"],
    "Estructuras": ["Discretas","Programacion","Bases"],
    "Bases": ["Estructuras","Estadistica"]
}

def coloreado(grafo: dict) -> dict: #Tiene de entrada un diccionario y lo devuelve a otro diccionario, asi se podra operar despues
    colores = {}
    for vertice in grafo: #Un vertice seria una clase
        colores_vecinos = {colores[vecino] for vecino in grafo[vertice] if vecino in colores}
        color = 0
        while color in colores_vecinos:
            color += 1 #Suma si ya esta ese color como vecino
        colores[vertice] = color 
    return colores

def validacion (grafo: dict, colores: dict) -> bool: #Verifica que se haya pasado bien la informacion 
    #y que cada grafo coloreado corresponda con el grafo propio
    for vertice, vecinos in grafo.items():
        for vecino in vecinos:
            if colores[vertice] == colores[vecino]:
                return False
    return True

def resumen_(colores: dict) -> dict:
    resumen = {}
    for vertice, color in colores.items():
        resumen.setdefault(color, []).append(vertice)
    return resumen


def main():
    while True:
        print(" |=== COLOREO DE GRAFOS ===| \n")
        print("1. Colorear Grafo")
        print("2. Salir del programa 😔")
        opcion = int(input("Elige una opcion (1-2): "))

        if opcion == 1:
            coloreo = coloreado(GRAFO)
            valido = validacion(GRAFO,coloreo)
            resumen = resumen_(coloreo)

            print(f"¿El coloreo es válido? {valido}")
            print(f"Colores usados: {len(resumen)}")
            for color, vertices in sorted(resumen.items()):
                print(f"  Color {color}: {vertices}")

            print("Diccionario original: ")
            for vertice in GRAFO:
                print(vertice,"------",GRAFO[vertice])

        elif opcion == 2:
            print("Adios 😔")
            break   
        else:
            print("Opcion no valida")


if __name__ == "__main__":
    main()