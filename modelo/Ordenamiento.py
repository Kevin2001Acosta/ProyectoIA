import bisect


class Ordenado:
    def __init__(self, clave=lambda x: x):
        self.nodos = []
        self.clave = clave

    def insertar(self, nodo):
        bisect.insort_right(self.nodos, nodo, key=self.clave)  # Se inserta el valor

    def obtener_nodos(self):
        return self.nodos  # Se devuelve el valor

    def borrar_valor(self):
        return self.nodos.pop(0)