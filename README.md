# Juego de la Vida de Conway

## Descripción del proyecto

Este proyecto implementa el **Juego de la Vida de Conway** en Python utilizando programación orientada a objetos, NumPy, SciPy y Matplotlib.

El Juego de la Vida es un autómata celular propuesto por John Horton Conway en 1970. Consiste en una rejilla bidimensional donde cada celda puede estar viva o muerta. A partir de reglas simples, el sistema evoluciona generación tras generación y puede producir comportamientos complejos como osciladores, estructuras estáticas y patrones móviles.

---

## Objetivo

El objetivo de este proyecto es implementar una simulación del Juego de la Vida de Conway que permita:

- Aplicar programación orientada a objetos.
- Simular la evolución de un tablero bidimensional.
- Visualizar patrones clásicos del juego.
- Generar animaciones con Matplotlib.
- Medir el rendimiento empírico del algoritmo.
- Comparar el tiempo de ejecución con curvas teóricas de complejidad.

---

## Estructura del proyecto

La estructura principal del repositorio es la siguiente:

```text
TAREA_computacion_paralela/
├── benchmark.py
├── benchmark_resultados.png
├── juego_de_la_vida.py
├── main.py
├── requirements.txt
├── visualize.py
└── README.md
```

---

## Archivos principales

| Archivo | Descripción |
|---|---|
| `juego_de_la_vida.py` | Contiene la clase principal `GameOfLife` y las funciones para crear patrones clásicos. |
| `visualize.py` | Contiene las funciones para mostrar tableros, animaciones y comparación de patrones. |
| `benchmark.py` | Realiza las pruebas de rendimiento para diferentes tamaños de grilla. |
| `main.py` | Archivo principal con un menú interactivo para ejecutar el proyecto. |
| `benchmark_resultados.png` | Gráfica generada por el benchmark de rendimiento. |
| `requirements.txt` | Lista de dependencias necesarias para ejecutar el proyecto. |

---

## Requisitos

Para ejecutar el proyecto se necesita tener instalado **Python 3**.

Las librerías utilizadas son:

- NumPy
- SciPy
- Matplotlib

Se pueden instalar con:

```bash
pip install -r requirements.txt
```

En caso de instalar manualmente las dependencias:

```bash
pip install numpy scipy matplotlib
```

---

## Cómo ejecutar el proyecto

Para iniciar el programa principal, se debe ejecutar:

```bash
python main.py
```

Al ejecutar el archivo principal, aparece un menú interactivo:

```text
╔══════════════════════════════════════╗
║    Juego de la Vida de Conway        ║
╠══════════════════════════════════════╣
║  1. Ver patrones clásicos (32x32)    ║
║  2. Ver patrones clásicos (128x128)  ║
║  3. Animar Glider                    ║
║  4. Animar Blinker                   ║
║  5. Animar Toad                      ║
║  6. Simulación aleatoria             ║
║  7. Correr benchmark de rendimiento  ║
║  0. Salir                            ║
╚══════════════════════════════════════╝
```

Desde este menú se pueden visualizar patrones clásicos, ejecutar simulaciones aleatorias y correr las pruebas de rendimiento.

---

## Implementación orientada a objetos

La lógica principal del juego está implementada en la clase `GameOfLife`.

Esta clase representa el estado completo de la simulación mediante los siguientes atributos:

| Atributo | Descripción |
|---|---|
| `rows` | Cantidad de filas del tablero. |
| `cols` | Cantidad de columnas del tablero. |
| `board` | Matriz que representa el estado actual del tablero. |
| `generation` | Número de generación actual. |

La clase contiene los siguientes métodos principales:

| Método | Descripción |
|---|---|
| `__init__(self, rows, cols, initial_state=None)` | Inicializa el tablero con un estado aleatorio o uno definido manualmente. |
| `step(self)` | Avanza el juego una generación aplicando las reglas de Conway. |
| `run(self, steps)` | Ejecuta múltiples generaciones. |
| `get_state(self)` | Devuelve una copia del estado actual del tablero. |
| `reset(self, initial_state=None)` | Reinicia el tablero. |
| `count_alive(self)` | Cuenta la cantidad de celdas vivas. |

Ejemplo básico:

```python
from juego_de_la_vida import GameOfLife

game = GameOfLife(32, 32)
game.step()

print(game.get_state())
```

---

## Reglas del Juego de la Vida

Cada celda tiene ocho vecinas: horizontales, verticales y diagonales. En cada generación, el estado de las celdas se actualiza simultáneamente según las siguientes reglas:

1. Una celda viva con menos de dos vecinos vivos muere por soledad.
2. Una celda viva con dos o tres vecinos vivos sobrevive.
3. Una celda viva con más de tres vecinos vivos muere por superpoblación.
4. Una celda muerta con exactamente tres vecinos vivos se convierte en celda viva.

En esta implementación, el conteo de vecinos se realiza mediante una convolución usando un kernel de 3x3:

```python
KERNEL = np.array([
    [1, 1, 1],
    [1, 0, 1],
    [1, 1, 1]
], dtype=np.uint8)
```

El valor central es `0` para no contar la propia celda, sino únicamente sus ocho vecinas.

---

## Patrones clásicos incluidos

El proyecto incluye varios patrones clásicos del Juego de la Vida:

| Patrón | Tipo | Descripción |
|---|---|---|
| `Glider` | Nave espacial | Se desplaza por la grilla con el paso de las generaciones. |
| `Blinker` | Oscilador | Alterna entre dos estados. |
| `Toad` | Oscilador | Cambia periódicamente entre configuraciones. |
| `Block` | Estructura estática | Permanece estable con el paso del tiempo. |

Ejemplo de uso del patrón `Glider`:

```python
from juego_de_la_vida import GameOfLife, make_glider
from visualize import animate_pattern

game = GameOfLife(32, 32, initial_state=make_glider(32, 32))
animate_pattern(game, steps=60, title="Glider")
```

---

## Visualización

Las visualizaciones se encuentran en el archivo `visualize.py`.

Funciones principales:

| Función | Descripción |
|---|---|
| `show_grid()` | Muestra una imagen estática del tablero. |
| `animate_pattern()` | Genera una animación de la evolución del juego. |
| `comparar_patrones()` | Muestra varios patrones clásicos en una misma figura. |

Para ejecutar directamente las visualizaciones:

```bash
python visualize.py
```

Esto permite visualizar patrones clásicos como `Glider`, `Blinker`, `Toad` y `Block`.

---

## Benchmark de rendimiento

El archivo `benchmark.py` mide el rendimiento del algoritmo usando distintos tamaños de grilla:

```text
32x32
64x64
128x128
256x256
512x512
1024x1024
```

Para cada tamaño se calcula el tiempo promedio por iteración.

Para ejecutar el benchmark:

```bash
python benchmark.py
```

El programa genera una gráfica llamada:

```text
benchmark_resultados.png
```

Esta gráfica incluye:

- Tiempo de ejecución por iteración.
- Comparación con complejidad O(n).
- Comparación con complejidad O(n log n).
- Comparación con complejidad O(n²).
- Visualización en escala log-log.

---

## Análisis de complejidad

En esta implementación, el tablero se representa como una matriz bidimensional de NumPy. Cada celda puede tener valor `0` si está muerta o `1` si está viva.

En cada generación, se calcula el número de vecinos vivos de cada celda usando una operación de convolución. Luego se aplican las reglas de Conway a todas las celdas de forma vectorizada.

Si `n` representa el número total de celdas:

```text
n = filas × columnas
```

entonces la complejidad esperada por iteración se aproxima a:

```text
O(n)
```

Esto ocurre porque en cada generación todas las celdas deben ser evaluadas.

---

## Uso de memoria

El uso de memoria crece aproximadamente de forma lineal con el número de celdas:

```text
O(n)
```

Esto se debe a que el programa almacena:

- El tablero actual.
- La matriz con el conteo de vecinos.
- El nuevo tablero generado en cada iteración.
- El historial de generaciones cuando se utiliza el método `run()`.

En grillas grandes, como `512x512` o `1024x1024`, el consumo de memoria y el tiempo de procesamiento aumentan considerablemente.

---

## Resultados esperados

Al ejecutar el benchmark, se obtiene una gráfica de rendimiento llamada:

```text
benchmark_resultados.png
```

Esta gráfica permite observar cómo aumenta el tiempo de ejecución conforme crece el tamaño de la grilla. En general, se espera que el comportamiento se acerque a una tendencia lineal con respecto al número total de celdas, ya que todas las celdas deben evaluarse en cada generación.

---



## Posibles mejoras futuras

Algunas mejoras posibles son:

- Implementar una versión acelerada con Numba.


---

## Conclusiones

Este proyecto fue un gran inicio para repasar conceptos de paradigmas de programacion orientada a objetos y ademas, de como con pocas reglas se puede llegar a crear un comportamiento complejo, simulaciones, de celulas en este caso, pero si se logra, replicar la idea con reglas especificas de otros compuestos organicos, se podria replicar el experimento.
Los resultados del benchmark permiten observar que el tiempo de ejecución aumenta conforme crece el tamaño de la grilla. Esto confirma que el rendimiento del algoritmo depende directamente del número total de celdas que deben evaluarse en cada generación.

En general, el proyecto cumple con los objetivos de implementar el Juego de la Vida de Conway, visualizar su evolución y analizar empíricamente su rendimiento computacional.

---
