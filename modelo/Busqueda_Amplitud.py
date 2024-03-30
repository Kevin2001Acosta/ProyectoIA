import numpy as np
from modelo.Nodo import nodo


def busqueda_amplitud(matriz):

    ninja_posx = 0
    ninja_posy = 0

    for fila in range(0, matriz.shape[0]):
        for columna in range(0, matriz.shape[1]):
            if matriz[fila][columna] == 7:
                print(fila, columna)
                ninja_posx = fila
                ninja_posy = columna
                matriz[fila][columna] = 1
                break
    lista = []
    raiz = nodo(
        matriz,
        ninja_posx,
        ninja_posy,
        [(ninja_posx, ninja_posy)],
        lista
    )
    cola = [raiz]

    while True:
        print(len(cola))
        if len(cola) == 0:
            return None

        nodo_cola = cola.pop(0)
        # print(nodo_cola.x, nodo_cola.y)
        if nodo_cola.verificar_ganar():
            return nodo_cola.recorrido

        hijos = nodo_cola.generar_hijos()
        for h in hijos:
            cola.append(h)


# matriz1 = np.loadtxt('../matrices/matriz1.txt', dtype=int)

# valores = busqueda_amplitud(matriz1)
# print(valores)