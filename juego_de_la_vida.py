"""
Juego de la Vida de Conway
Implementación orientada a objetos con NumPy y SciPy.
"""

import numpy as np
from scipy.ndimage import convolve


class GameOfLife:

    KERNEL = np.array([
        [1, 1, 1],
        [1, 0, 1],
        [1, 1, 1]
    ], dtype=np.uint8)

    def __init__(self, rows: int, cols: int, initial_state=None):
        self.rows = rows
        self.cols = cols
        self.generation = 0

        if initial_state is not None:
            assert initial_state.shape == (rows, cols)
            self.board = initial_state.astype(np.uint8)
        else:
            self.board = np.random.choice(
                [0, 1], size=(rows, cols), p=[0.7, 0.3]
            ).astype(np.uint8)

    def step(self):
        neighbors = convolve(self.board, self.KERNEL, mode='wrap')

        new_board = (
            (self.board == 1) & ((neighbors == 2) | (neighbors == 3)) |
            (self.board == 0) & (neighbors == 3)
        ).astype(np.uint8)

        self.board = new_board
        self.generation += 1
        return self.board

    def run(self, steps: int):
        history = []
        for _ in range(steps):
            history.append(self.step().copy())
        return history

    def get_state(self):
        return self.board.copy()

    def reset(self, initial_state=None):
        self.generation = 0
        if initial_state is not None:
            self.board = initial_state.astype(np.uint8)
        else:
            self.board = np.random.choice(
                [0, 1], size=(self.rows, self.cols), p=[0.7, 0.3]
            ).astype(np.uint8)

    def count_alive(self):
        return int(self.board.sum())

    def __repr__(self):
        return (
            f"GameOfLife(rows={self.rows}, cols={self.cols}, "
            f"generation={self.generation}, alive={self.count_alive()})"
        )


def make_glider(rows, cols, offset_r=1, offset_c=1):
    board = np.zeros((rows, cols), dtype=np.uint8)
    glider = np.array([
        [0, 1, 0],
        [0, 0, 1],
        [1, 1, 1]
    ], dtype=np.uint8)
    board[offset_r:offset_r+3, offset_c:offset_c+3] = glider
    return board


def make_blinker(rows, cols):
    board = np.zeros((rows, cols), dtype=np.uint8)
    cr, cc = rows // 2, cols // 2
    board[cr, cc-1:cc+2] = 1
    return board


def make_toad(rows, cols):
    board = np.zeros((rows, cols), dtype=np.uint8)
    cr, cc = rows // 2, cols // 2
    board[cr,   cc:cc+3]   = 1
    board[cr+1, cc-1:cc+2] = 1
    return board


def make_block(rows, cols):
    board = np.zeros((rows, cols), dtype=np.uint8)
    cr, cc = rows // 2, cols // 2
    board[cr:cr+2, cc:cc+2] = 1
    return board