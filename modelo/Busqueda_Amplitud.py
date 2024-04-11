import numpy as np
from modelo.Nodo_Amplitud import nodo


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
    nodos_expandidos = 0
    nodos_creados = 1
    while True:
        print(len(cola))
        if len(cola) == 0:
            return [None, nodos_expandidos, nodos_creados]

        nodo_cola = cola.pop(0)
        nodos_expandidos += 1
        # print(nodo_cola.x, nodo_cola.y)
        if nodo_cola.verificar_ganar():
            print('Busqueda Amplitud', nodos_expandidos, nodos_creados)
            return nodo_cola.recorrido, nodos_expandidos, nodos_creados

        hijos = nodo_cola.generar_hijos()
        for h in hijos:
            cola.append(h)
            nodos_creados += 1