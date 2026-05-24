"""
Juego de la Vida de Conway — Punto de entrada principal.
Ejecuta visualizaciones y benchmark desde un solo archivo.
"""

from juego_de_la_vida import (
    GameOfLife,
    make_glider,
    make_blinker,
    make_toad,
    make_block
)
from visualize import animate_pattern, comparar_patrones, show_grid
from benchmark import correr_benchmark, graficar_resultados


def menu():
    print("\n╔══════════════════════════════════════╗")
    print("║    Juego de la Vida de Conway        ║")
    print("╠══════════════════════════════════════╣")
    print("║  1. Ver patrones clásicos (32x32)    ║")
    print("║  2. Ver patrones clásicos (128x128)  ║")
    print("║  3. Animar Glider                    ║")
    print("║  4. Animar Blinker                   ║")
    print("║  5. Animar Toad                      ║")
    print("║  6. Simulación aleatoria             ║")
    print("║  7. Correr benchmark de rendimiento  ║")
    print("║  0. Salir                            ║")
    print("╚══════════════════════════════════════╝")
    return input("Elegí una opción: ").strip()


def main():
    while True:
        opcion = menu()

        if opcion == "1":
            print("Mostrando patrones clásicos en 32x32...")
            comparar_patrones(rows=32, cols=32, steps=10)

        elif opcion == "2":
            print("Mostrando patrones clásicos en 128x128...")
            comparar_patrones(rows=128, cols=128, steps=10)

        elif opcion == "3":
            print("Animando Glider en 32x32...")
            game = GameOfLife(32, 32, initial_state=make_glider(32, 32))
            animate_pattern(game, steps=80, title="Glider")

        elif opcion == "4":
            print("Animando Blinker en 32x32...")
            game = GameOfLife(32, 32, initial_state=make_blinker(32, 32))
            animate_pattern(game, steps=20, title="Blinker")

        elif opcion == "5":
            print("Animando Toad en 32x32...")
            game = GameOfLife(32, 32, initial_state=make_toad(32, 32))
            animate_pattern(game, steps=20, title="Toad")

        elif opcion == "6":
            try:
                lado = int(input("Ingresá el tamaño de la grilla (ej: 64): "))
                pasos = int(input("¿Cuántas generaciones animar?: "))
                game = GameOfLife(lado, lado)
                print(f"Estado inicial: {game}")
                animate_pattern(game, steps=pasos, title=f"Aleatorio {lado}x{lado}")
            except ValueError:
                print("Error: ingresá números válidos.")

        elif opcion == "7":
            print("\nCorriendo benchmark (puede tardar unos segundos)...\n")
            tamanhos, tiempos = correr_benchmark()
            graficar_resultados(tamanhos, tiempos)

        elif opcion == "0":
            print("¡Hasta luego!")
            break

        else:
            print("Opción no válida, intentá de nuevo.")


if __name__ == "__main__":
    main()