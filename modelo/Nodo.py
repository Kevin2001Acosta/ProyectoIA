
import numpy as np

class nodo:
    def __init__(self, matriz, x, y, recorrido, marcados):
        self.matriz = matriz
        self.x = x
        self.y = y
        self.recorrido = recorrido
        self.marcados = marcados
        self.hijos = []
        

    def verificar_ganar(self):
        return self.matriz[self.x,self.y]  == 6
    
    
    
    def generar_hijos(self):
        
        hijos =[]
        def crear_hijo(hijox, hijoy):
        
            if hijoy >= 0 and hijox >= 0 and hijoy < self.matriz.shape[0] and hijox < self.matriz.shape[1] and not ((hijox,hijoy) in self.marcados):
                hijo = nodo
                (
                    self.matriz,
                    hijox,
                    hijoy,
                    np.append(self.recorrido, (hijox,hijoy)),
                    np.append(self.marcados,(self.x, self.y))
                )
                hijos.append(hijo)
                
                
        #hijos de arriba        
        x = self.x
        y = self.y - 1
        if self.matriz[x][y] == 0 and self.matriz[x][y] == 4:
            crear_hijo(x, y)
        
        #hijos de la derecha
        x = self.x + 1
        y = self.y 
        if self.matriz[x][y] == 0 and self.matriz[x][y] == 3:
            crear_hijo(x, y)

        #hijos de abajo
        x = self.x
        y = self.y + 1
        if self.matriz[x][y] == 0 and self.matriz[x][y] == 5:
            crear_hijo(x, y)
        
        #hijos de la izquierda
        x = self.x - 1
        y = self.y
        if self.matriz[x][y] == 0 and self.matriz[x][y] == 2:
            crear_hijo(x, y)
        
        
        
        return hijos
    
    
    
            