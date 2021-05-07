import math
import turtle

if __name__ == '__main__':

    zoom_factor: float = 8.6
    iteration_quantity: int = 1

    iteration_quantity = int(input('Insira o número de interações (deve ser > 1): '))

    while iteration_quantity < 1:
        iteration_quantity = int(input('Insira o número de interações (deve ser > 1): '))

