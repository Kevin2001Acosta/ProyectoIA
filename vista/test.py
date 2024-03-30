import math

def manhattan(origen, destino):
    return abs(origen[0] - destino[0]) + abs(origen[1] - destino[1])

valor = manhattan((9,7), (0, 0))
print(valor)

