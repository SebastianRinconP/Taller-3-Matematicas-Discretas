# Taller-3-Matematicas-Discretas

Juan Sebastian Rincon
Sebastian Polo Alvarez

# Lenguaje Usado:
Python

# Cómo ejecutar

1. Clonar/descargar el repositorio y ubicarse en la carpeta raíz del taller:
   cd Taller-3-Matematicas-Discretas

2. Ejecutar un ejercicio individual:
   python src/boole/operadores_logicos.py
   python src/boole/simplificacion_booleana.py
   python src/grafos/coloreo_grafos.py

3. Ejecutar todas las pruebas automáticas:
   python -m unittest discover tests

4. Las Bibliotecas del boole utilizan la siguiente :
 itertools,
 math,
 random

## Ejercicio 6: Coloreo de Grafos
En el ejercicio 6, se trabaja un coloreo de grafos, donde ningun grafo puede chocar con un grafo del mismo color, en este caso no se usa ninguna biblioteca, y se usa un diccionario para ver los grafos y con que chocan
## EJercicio 7:
Se simulan las salidas de los circuitos logicos con todas las posibles opciones, van variando los valores asi se pueden generar todas las salidas posibles, en esta se utiliza la libreria de itertools, pero es una interna

## Ejercicio 8:
En este ejercicio se trata de simplificar textos booleanos muy largos y como se relacionan entre ellos

## Ejercicio 9: Entropia de Shanon
En el ejercicio 9, se trabaja la entropia de shanon donde mide la repetitividad de los textos, se utiliza la biblioteca math para desarrollar el ejercicio

# Ejercicio 10: SImulador cuantico
En el ejercicio 10, se trabaja un simulador cuantico donde usa diferentes compuertas en forma de matrices, se ve la probabilidad de medir 0 y 1 y se simulan las 1000 mediciones, utiliza la libreria math y random