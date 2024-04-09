

class Nodo:
    def __init__(self, matriz, x, y, recorrido, marcados, heuristica, costo, pos_shuriken):
        self.matriz = matriz
        self.x = x
        self.y = y
        self.recorrido = recorrido
        self.marcados = marcados
        self.heuristica = heuristica
        self.costo = costo
        self.f = self.heuristica + self.costo
        self.pos_shuriken = pos_shuriken

    def verificar_ganar(self):
        return self.matriz[self.x, self.y] == 6

    def generar_hijos(self):
        hijos = []
        lista_marcados = self.marcados.copy()
        valorNodo = self.matriz[self.x, self.y]

        def crear_hijo(hijox, hijoy):
            print(hijox, hijoy)
            tupla = (self.x, self.y)
            lista_marcados.append(tupla)
            if not (hijox, hijoy) in lista_marcados:
                hijo = Nodo(self.matriz, hijox, hijoy, self.recorrido + [(hijox, hijoy)], lista_marcados,
                            abs(hijox - self.pos_shuriken[0]) + abs(hijoy - self.pos_shuriken[1]), self.costo + 1,
                            self.pos_shuriken)
                hijos.append(hijo)

        # hijos de arriba
        x = self.x - 1
        y = self.y
        if 0 <= x < self.matriz.shape[1] and 0 <= y < self.matriz.shape[0] and valorNodo != 5:
            if not (self.matriz[x][y] == 0 or self.matriz[x][y] == 4):
                print('hijo de arriba de: ', self.x, self.y, (x, y))
                crear_hijo(x, y)

        # hijos de la derecha
        x = self.x
        y = self.y + 1
        if 0 <= x < self.matriz.shape[1] and 0 <= y < self.matriz.shape[0] and valorNodo != 2:
            if not (self.matriz[x][y] == 0 or self.matriz[x][y] == 3):
                print('hijo de derecha de: ', self.x, self.y, (x, y))
                crear_hijo(x, y)

        # hijos de abajo
        x = self.x + 1
        y = self.y
        if 0 <= x < self.matriz.shape[1] and 0 <= y < self.matriz.shape[0] and valorNodo != 4:
            if not (self.matriz[x][y] == 0 or self.matriz[x][y] == 5):
                print('hijo de abajo de: ', self.x, self.y, (x, y))
                crear_hijo(x, y)

        # hijos de la izquierda
        x = self.x
        y = self.y - 1
        if 0 <= x < self.matriz.shape[1] and 0 <= y < self.matriz.shape[0] and valorNodo != 3:
            if not (self.matriz[x][y] == 0 or self.matriz[x][y] == 2):
                print('hijo de izquierda de: ', self.x, self.y, (x, y))
                crear_hijo(x, y)
        return hijos

