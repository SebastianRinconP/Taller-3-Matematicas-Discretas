import math
def frecuencia_texto(texto):
    frecuencia= {}
    for letra in texto:
        if letra in frecuencia:
            frecuencia[letra] +=1 #Aumenta la cantidad de veces que aparece la letra
        else:
            frecuencia[letra] =1
    return frecuencia

def entropia_shanon(texto, frecuencia):
    suma = 0
    for letra in frecuencia:
        probabilidad = frecuencia[letra]/len(texto) #La probabilidad de la letra en la longitud de texto
        suma += probabilidad * math.log2(probabilidad) #Esta es la sumatoria de los numeros 
    return -suma 

def main():
    while True:
        print("SHANON: medir informacion de un mensaje")
        print("1. Comparar la entropia de Shanon")
        print("2. Medir la entropia individual")
        print("3. Salir")
        opcion=int(input("Ingrese su opcion (1/2/3): "))        
        if opcion == 1:

            texto1 = input("Ingrese el texto 1: ").upper()
            texto2 = input("Ingrese el texto 2: ").upper()

            f1 =frecuencia_texto(texto1)
            f2=frecuencia_texto(texto2)
            en1 = entropia_shanon(texto1,f1)
            en2 = entropia_shanon(texto2,f2)
            print(f"Entropia del texto 1: {en1}")
            print(f"Entropia del texto 2: {en2}")
            if en1>en2:
                print("La entropia del texto 1 es mayor")
            elif en2>en1:
                print("La entropia del texto 2 es mayor")
            else:
                print("La entropia de ambos textos es igual")
        elif opcion ==2:
            texto1 = input("Ingrese el texto: ").upper()
            f1 =frecuencia_texto(texto1)
            en1 = entropia_shanon(texto1,f1)
            print(f"La entropia del texto es: {en1}")
        elif opcion == 3:
            print("Adios 😔")
            break   
        else:
            print("opcion no valida")

if __name__ == "__main__":
    main()