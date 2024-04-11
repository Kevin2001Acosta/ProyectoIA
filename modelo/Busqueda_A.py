import numpy as np
from modelo.Nodo_A import Nodo
from modelo.Ordenamiento import Ordenado

def busqueda_A(matriz):

    ninja_posx = 0
    ninja_posy = 0

    shuriken_posx = 0
    shuriken_posy = 0

    for fila in range(0, matriz.shape[0]):
        for columna in range(0, matriz.shape[1]):
            if matriz[fila][columna] == 7:
                ninja_posx = fila
                ninja_posy = columna
                matriz[fila][columna] = 1
            elif matriz[fila][columna] == 6:
                shuriken_posx = fila
                shuriken_posy = columna
    lista = []
    raiz = Nodo(
        matriz, ninja_posx, ninja_posy,
        [(ninja_posx, ninja_posy)],
        lista,
        abs(ninja_posx - shuriken_posx) + abs(ninja_posy - shuriken_posy),
        0,
        (shuriken_posx, shuriken_posy)
    )
    cola = Ordenado(clave=lambda nodo: nodo.f)
    cola.insertar(raiz)
    nodos_expandidos = 0
    nodos_creados = 1
    while True:
        if len(cola.obtener_nodos()) == 0:
            return [None, nodos_expandidos, nodos_creados]
        
        nodo_cola = cola.borrar_valor()
        nodos_expandidos += 1

        if nodo_cola.verificar_ganar():
            print('busqueda A*', nodos_expandidos, nodos_creados)
            return nodo_cola.recorrido, nodos_expandidos, nodos_creados

        hijos = nodo_cola.generar_hijos()
        for h in hijos:
            cola.insertar(h)
            nodos_creados += 1