"""
Visualización del Juego de la Vida de Conway
Animaciones y gráficas estáticas usando matplotlib.
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

from juego_de_la_vida import (
    GameOfLife,
    make_glider,
    make_blinker,
    make_toad,
    make_block
)


def show_grid(board, title="Juego de la Vida", generation=0):
    """
    Muestra una imagen estática del tablero en su estado actual.

    Args:
        board (np.ndarray): Matriz 2D del tablero.
        title (str): Título de la imagen.
        generation (int): Número de generación actual.
    """
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.imshow(board, cmap="binary", interpolation="nearest")
    ax.set_title(f"{title} — Generación {generation}")
    ax.axis("off")
    plt.tight_layout()
    plt.show()


def animate_pattern(game, steps=50, interval=150, title="Juego de la Vida"):
    """
    Crea y muestra una animación de la evolución del juego.

    Args:
        game (GameOfLife): Instancia del juego ya inicializada.
        steps (int): Número de generaciones a animar.
        interval (int): Milisegundos entre cada frame.
        title (str): Título de la ventana.
    """
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.axis("off")

    # Estado inicial: generación 0
    img = ax.imshow(game.get_state(), cmap="binary", interpolation="nearest")
    titulo = ax.set_title(f"{title} — Generación 0/{steps}")

    def init():
        """
        Inicializa la animación sin avanzar generaciones.
        """
        img.set_data(game.get_state())
        titulo.set_text(f"{title} — Generación 0/{steps}")
        return [img, titulo]

    def update(frame):
        """
        Avanza exactamente una generación por frame.
        """
        game.step()
        img.set_data(game.get_state())

        # Usamos frame, no game.generation, para que nunca pase de steps
        titulo.set_text(f"{title} — Generación {frame}/{steps}")

        return [img, titulo]

    anim = animation.FuncAnimation(
        fig,
        update,
        frames=range(1, steps + 1),
        init_func=init,
        interval=interval,
        blit=False,
        repeat=False
    )

    plt.tight_layout()
    plt.show()

    return anim


def comparar_patrones(rows=32, cols=32, steps=10):
    """
    Muestra los 4 patrones clásicos lado a lado en una grilla 2x2.
    Útil para capturas de pantalla de patrones distintos.

    Args:
        rows (int): Filas del tablero.
        cols (int): Columnas del tablero.
        steps (int): Generaciones a simular antes de mostrar.
    """
    patrones = {
        "Glider": make_glider(rows, cols),
        "Blinker": make_blinker(rows, cols),
        "Toad": make_toad(rows, cols),
        "Block": make_block(rows, cols),
    }

    fig, axes = plt.subplots(2, 2, figsize=(10, 10))
    axes = axes.flatten()

    for ax, (nombre, estado_inicial) in zip(axes, patrones.items()):
        game = GameOfLife(rows, cols, initial_state=estado_inicial)
        game.run(steps)

        ax.imshow(game.get_state(), cmap="binary", interpolation="nearest")
        ax.set_title(f"{nombre} — Gen {steps}")
        ax.axis("off")

    plt.suptitle(f"Patrones clásicos ({rows}x{cols})", fontsize=14)
    plt.tight_layout()
    plt.show()


# ── Para probar directamente este archivo ──
if __name__ == "__main__":

    print("=== Mostrando comparación de patrones clásicos ===")
    comparar_patrones(rows=32, cols=32, steps=10)

    print("=== Animando el Glider en grilla 32x32 ===")
    game_glider = GameOfLife(32, 32, initial_state=make_glider(32, 32))
    animate_pattern(game_glider, steps=60, title="Glider")

    print("=== Animando el Blinker en grilla 32x32 ===")
    game_blinker = GameOfLife(32, 32, initial_state=make_blinker(32, 32))
    animate_pattern(game_blinker, steps=20, title="Blinker")