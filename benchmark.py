"""
Medición de rendimiento y complejidad empírica
del Juego de la Vida de Conway.
"""

import time
import numpy as np
import matplotlib.pyplot as plt
from juego_de_la_vida import GameOfLife


def medir_tiempo(rows, cols, steps=10, repeticiones=5):
    """
    Mide el tiempo promedio por iteración para una grilla de tamaño rows x cols.

    Args:
        rows (int): Filas del tablero.
        cols (int): Columnas del tablero.
        steps (int): Iteraciones por medición.
        repeticiones (int): Cuántas veces repetir para promediar.

    Returns:
        float: Tiempo promedio en segundos por iteración.
    """
    tiempos = []

    for _ in range(repeticiones):
        game = GameOfLife(rows, cols)
        inicio = time.perf_counter()
        game.run(steps)
        fin = time.perf_counter()
        tiempo_por_iter = (fin - inicio) / steps
        tiempos.append(tiempo_por_iter)

    return np.mean(tiempos)


def correr_benchmark():
    """
    Corre el benchmark para distintos tamaños de grilla
    y devuelve los resultados.

    Returns:
        tuple: (tamaños, tiempos) donde tamaños es número de celdas.
    """
    # Tamaños de grilla a probar (de 32x32 hasta 1024x1024)
    lados = [32, 64, 128, 256, 512, 1024]
    tamanhos = [lado ** 2 for lado in lados]
    tiempos = []

    print(f"{'Grilla':<12} {'Celdas':<12} {'Tiempo/iter (s)'}")
    print("-" * 40)

    for lado in lados:
        t = medir_tiempo(lado, lado, steps=10, repeticiones=5)
        tiempos.append(t)
        print(f"{lado}x{lado:<8} {lado**2:<12} {t:.6f}")

    return tamanhos, tiempos


def graficar_resultados(tamanhos, tiempos):
    """
    Genera dos gráficas:
    1. Tiempo vs número de celdas (escala normal)
    2. Tiempo vs número de celdas (escala log-log con curvas teóricas)

    Args:
        tamanhos (list): Lista de tamaños (número de celdas).
        tiempos (list): Lista de tiempos promedio por iteración.
    """
    tamanhos = np.array(tamanhos)
    tiempos  = np.array(tiempos)

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

    # ── Gráfica 1: Escala normal ──────────────────────────────
    ax1.plot(tamanhos, tiempos, 'o-', color='steelblue',
             linewidth=2, markersize=7, label='Tiempo medido')
    ax1.set_xlabel("Número de celdas (n)")
    ax1.set_ylabel("Tiempo por iteración (s)")
    ax1.set_title("Rendimiento empírico — Escala normal")
    ax1.legend()
    ax1.grid(True, alpha=0.3)

    # ── Gráfica 2: Escala log-log con curvas teóricas ─────────
    # Curvas teóricas normalizadas al primer punto medido
    n = tamanhos
    factor = tiempos[0]

    on      = factor * (n / n[0])
    onlogn  = factor * (n * np.log(n)) / (n[0] * np.log(n[0]))
    on2     = factor * (n / n[0]) ** 2

    ax2.loglog(tamanhos, tiempos, 'o-', color='steelblue',
               linewidth=2, markersize=7, label='Tiempo medido')
    ax2.loglog(n, on,     '--', color='green',  alpha=0.7, label='O(n)')
    ax2.loglog(n, onlogn, '--', color='orange', alpha=0.7, label='O(n log n)')
    ax2.loglog(n, on2,    '--', color='red',    alpha=0.7, label='O(n²)')

    ax2.set_xlabel("Número de celdas (n)")
    ax2.set_ylabel("Tiempo por iteración (s)")
    ax2.set_title("Rendimiento empírico — Escala log-log")
    ax2.legend()
    ax2.grid(True, which='both', alpha=0.3)

    plt.suptitle("Análisis de complejidad empírica — Juego de la Vida", fontsize=13)
    plt.tight_layout()
    plt.savefig("benchmark_resultados.png", dpi=150)
    plt.show()
    print("\nGráfica guardada como 'benchmark_resultados.png'")


# ── Para correr directamente ──
if __name__ == "__main__":
    print("Corriendo benchmark...\n")
    tamanhos, tiempos = correr_benchmark()
    print("\nGenerando gráficas...")
    graficar_resultados(tamanhos, tiempos)