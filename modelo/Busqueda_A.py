import numpy as np
from modelo.Nodo_A import Nodo
from modelo.Ordenamiento import Ordenado

def busqueda_A(matriz):

    ninja_posx = 0
    ninja_posy = 0

    for fila in range(0, matriz.shape[0]):
        for columna in range(0, matriz.shape[1]):
            if matriz[fila][columna] == 7:
                ninja_posx = fila
                ninja_posy = columna
                matriz[fila][columna] = 1
                break
    lista = []
    raiz = Nodo(
        matriz,
        ninja_posx,
        ninja_posy,
        [(ninja_posx, ninja_posy)],
        lista,
        abs(ninja_posx - 0) + abs(ninja_posy - 0),
        0
    )
    cola = Ordenado(clave=lambda nodo: nodo.f)
    cola.insertar(raiz)

    while True:
        if len(cola.obtener_nodos()) == 0:
            return None
        nodo_cola = cola.borrar_valor()
        if nodo_cola.verificar_ganar():
            return nodo_cola.recorrido

        hijos = nodo_cola.generar_hijos()
        for h in hijos:
            cola.insertar(h)

matriz1 = np.loadtxt('../matrices/matriz1.txt', dtype=int)
valores = busqueda_A(matriz1)
print(valores)