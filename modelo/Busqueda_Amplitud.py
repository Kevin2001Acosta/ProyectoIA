from Nodo import nodo
import numpy as np


def busqueda_amplitud(matriz):
    
    ninja_posx = 0
    ninja_posy = 0
    
    for i in range(0, matriz.shape[0]):
        for j in range(0, matriz.shape[1]):
            if matriz[i, j] == 7:
                ninja_posx = i
                ninja_posy = j
                matriz[i, j] = 1
                break            
                
    raiz = nodo
    (
        matriz,
        ninja_posx,
        ninja_posy,
        np.append(np.array([]),(ninja_posx,ninja_posy)),
        np.array([]),
    )
    
    cola = [raiz]
    
    while True:
        nodo_cola = cola.pop(0)
        
        if nodo_cola.verificar_ganar():
            return nodo_cola.recorrido
        
        if len(cola) == 0:
            return None 
        
        hijos = nodo_cola.generar_hijos()
        for h in hijos:
            cola.append(h)