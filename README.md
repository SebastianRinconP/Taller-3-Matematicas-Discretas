# Taller 3 — Matemáticas Discretas I

**Universidad Nacional de Colombia**

Estudiantes: Sebastian Polo Alvarez - Juan Sebastian Rincon Pinzon

Docente: Jhoan Sebastian Tenjo García

---

## Descripción general

En este repositorio se presentan las soluciones implementadas en Python para los 10 ejercicios del **Taller 3** de la asignatura **Matemáticas Discretas I**. El proyecto abarca desarrollos prácticos organizados en tres bloques principales: criptografía, teoría de grafos, álgebra booleana, teoría de información de Shannon y computación cuántica básica. Cada ejercicio cuenta con su respectiva estructura modular, pruebas unitarias y código verificado.

---

## Requisitos

Necesitas **Python 3.11** o superior. utiliza librerías estándar de Python como: (`os`, `sys`, etc.). y tambien (`pytest`) que se instala escribiendo (`pip install pytest`) en la terminal.

---

## Estructura del Repositorio

```text
Taller-3-Matematicas-Discretas/
│
├── src/
│   ├── criptografia/      # Ejercicios 1, 2 y 3 (Cifrado César, RSA, MPC básico)
│   ├── grafos/            # Ejercicios 4, 5 y 6 (Dijkstra, Impacto de cierres, Coloreo)
│   ├── boole/             # Ejercicios 7 y 8 (Tablas de verdad, Simplificación booleana)
│   └── cuantica/          # Ejercicios 9 y 10 (Entropía de Shannon, Simulador cuántico)
│
└── tests/                 # Pruebas generales o unitarias automatizadas (pytest) 

```

---

## Cómo ejecutar las pruebas unitarias

Todas las funcionalidades cuentan con una suite de pruebas unitarias robustas. Para ejecutar todas las pruebas de forma automática desde la raíz del proyecto, corre:

```bash
python -m pytest tests/ -v

```

También puedes ejecutar pruebas de módulos específicos de manera independiente, por ejemplo:

```bash
python -m pytest tests/test_ruta_minima.py tests/test_impacto_cierre.py -v
```

---

## Bloques y Ejercicios Desarrollados

### 5.1. Bloque A. Criptografía (`src/criptografia/`)

1. **Cifrado César (`cifrado_desplazamiento.py`):** Permite cifrar y descifrar textos mediante el clásico cifrado por desplazamiento, preservando la integridad de espacios, números y símbolos especiales. Incluye un método de ataque por fuerza bruta que evalúa automáticamente los 26 desplazamientos posibles.


2. **RSA de Juguete (`rsa_juguete.py`):** Simula el ciclo completo de un criptosistema de llave pública RSA a escala educativa. Recibe dos primos $p$ y $q$, calcula $n = pq$, $\varphi(n) = (p-1)(q-1)$, el inverso modular $d$ mediante el algoritmo de Euclides extendido, y realiza el cifrado y descifrado por exponenciación modular.


3. **MPC Básico (`mpc_basico.py`):** Simula un protocolo de Computación Multipartita Segura donde las notas de los estudiantes (entre 0 y 50) se dividen en tres partes aleatorias módulo $M = 1000003$ distribuidas en tres servidores, permitiendo calcular la suma total y el promedio global sin revelar los datos individuales.



### 5.2. Bloque B. Grafos (`src/grafos/`)

4. **Ruta más corta (`ruta_minima.py` y `grafo_ponderado.py`):** Implementa el algoritmo de Dijkstra sobre un grafo ponderado de al menos 8 vértices y 12 aristas para encontrar la ruta de menor costo en una red de transporte.


5. **Cierre de una estación (`impacto_cierre.py`):** Mide el impacto estructural en una red de transporte ante la eliminación de un vértice o arista clave, generando una tabla comparativa de distancias y reportando los pares afectados o desconectados.


6. **Coloreo de Grafos (`coloreo_grafos.py`):** Asigna colores a los vértices de un grafo de conflictos de mínimo 10 nodos usando un algoritmo voraz, verificando que no existan vértices adyacentes con el mismo color.



### 5.3. Bloque C. Álgebra de Boole, Shannon y Computación Cuántica (`src/boole/` y `src/cuantica/`)

7. **Tablas de verdad y circuitos lógicos (`operadores_logicos.py`):** Genera tablas de verdad y evalúa expresiones booleanas con variables $A, B, C, D$ usando operadores AND, OR, NOT y XOR.


8. **Simplificación booleana (`simplificacion_booleana.py`):** Recibe funciones booleanas por sus minitérminos y genera una expresión simplificada en suma de productos, comprobando la equivalencia de tablas de verdad.


9. **Shannon (`shannon.py`):** Calcula las frecuencias, probabilidades y la entropía de Shannon ($H = -\sum p_i \log_2 p_i$) de mensajes escritos, comparando las fuentes de información.


10. **Simulador cuántico (`simulador_cuantico.py`):** Modela qubits como vectores de estado de dos entradas y simula la aplicación de compuertas cuánticas $X$, $Z$ y $H$, calculando probabilidades y simulando 1000 mediciones estadísticas.



---

## Nota sobre el uso de inteligencia artificial

Declaración de uso de IA
En el desarrollo de este taller se utilizó inteligencia artificial (IA) como herramienta de apoyo, de la siguiente manera:

 - README: este documento fue redactado casi en su totalidad con ayuda de IA, a partir de la información real del repositorio.
 - Código de cada punto: primero se implementó la lógica y el algoritmo de cada punto por cuenta propia; después, ese código se pasó por una IA para darle formato y organizarlo mejor.
 - Documentación de cada punto: se siguió el mismo proceso: las explicaciones matemáticas y conceptuales se redactaron primero por nuestra parte, y luego se usó IA como apoyo para mejorar la gramática y la redacción.
 - Pruebas (tests/): se usó IA como apoyo principal para escribir los archivos de test, ya que no contábamos con experiencia previa usando frameworks de pruebas como pytest.
