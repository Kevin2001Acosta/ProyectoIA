import numpy as np


class nodo:
    def __init__(self, matriz, x, y, recorrido, marcados):
        self.matriz = matriz
        self.x = x
        self.y = y
        self.recorrido = recorrido
        self.marcados = marcados

    def verificar_ganar(self):
        return self.matriz[self.x, self.y] == 6

    def generar_hijos(self):

        hijos = []
        lista_marcados = self.marcados.copy()
        valor = self.matriz[self.x, self.y]

        def crear_hijo(hijox, hijoy):
            # print(hijox, hijoy)
            tupla = (self.x, self.y)
            lista_marcados.append(tupla)
            if not (hijox, hijoy) in lista_marcados:
                hijo = nodo(
                    self.matriz,
                    hijox,
                    hijoy,
                    self.recorrido + [(hijox, hijoy)],
                    lista_marcados
                )
                hijos.append(hijo)

        # hijos de arriba
        x = self.x - 1
        y = self.y
        if 0 <= x < self.matriz.shape[1] and 0 <= y < self.matriz.shape[0] and valor != 5:
            if not (self.matriz[x][y] == 0 or self.matriz[x][y] == 4):
                print('hijo de arriba de: ', self.x, self.y, (x, y))
                crear_hijo(x, y)

        # hijos de la derecha
        x = self.x
        y = self.y + 1
        if 0 <= x < self.matriz.shape[1] and 0 <= y < self.matriz.shape[0] and valor != 2:
            if not (self.matriz[x][y] == 0 or self.matriz[x][y] == 3):
                print('hijo de derecha de: ', self.x, self.y, (x, y))
                crear_hijo(x, y)

        # hijos de abajo
        x = self.x + 1
        y = self.y
        if 0 <= x < self.matriz.shape[1] and 0 <= y < self.matriz.shape[0] and valor != 4:
            if not (self.matriz[x][y] == 0 or self.matriz[x][y] == 5):
                print('hijo de abajo de: ', self.x, self.y, (x, y))
                crear_hijo(x, y)

        # hijos de la izquierda
        x = self.x
        y = self.y - 1
        if 0 <= x < self.matriz.shape[1] and 0 <= y < self.matriz.shape[0] and valor != 3:
            if not (self.matriz[x][y] == 0 or self.matriz[x][y] == 2):
                print('hijo de izquierda de: ', self.x, self.y, (x, y))
                crear_hijo(x, y)

        return hijos
