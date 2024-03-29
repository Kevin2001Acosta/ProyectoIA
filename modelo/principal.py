# leer matriz de un txt
import numpy as np
import pygame
import sys
from pygame.locals import *

# Leer el archivo de texto y convertirlo en una matriz
matriz = np.loadtxt('./matrices/matriz1.txt', dtype=int)

#  print(matriz[0][0])


#  Inicializar Pygame
pygame.init()

# paleta de colores

BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
AZUL = (0, 0, 255)
VERDE = (0, 255, 0)
ROJO = (255, 0, 0)
AZULCLARO = (41, 197, 255)
PURPURA = (186, 2, 255)
AMARILLO = (255, 234, 56)
GRIS = (155, 155, 155)

# Configurar la PANTALLA
ANCHO = 1000
ALTO = 700
PANTALLA = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption('El Ninja')

ninja_stop = pygame.transform.scale(pygame.image.load('./imagenes/ninja-stop.jpg'), (60, 60))
# icono del juego
pygame.display.set_icon(ninja_stop)

caminaDerecha = [pygame.transform.scale(pygame.image.load('./imagenes/ninjas-right1.jpg'), (60, 60)),
                 pygame.transform.scale(pygame.image.load('./imagenes/ninjas-right2.jpg'), (60, 60)),
                 pygame.transform.scale(pygame.image.load('./imagenes/ninjas-right3.jpg'), (60, 60))]

caminaIzquierda = [pygame.transform.scale(pygame.image.load('./imagenes/ninjas-left1.jpg'), (60, 60)),
                   pygame.transform.scale(pygame.image.load('./imagenes/ninjas-left2.jpg'), (60, 60)),
                   pygame.transform.scale(pygame.image.load('./imagenes/ninjas-left3.jpg'), (60, 60))]

shuriken = pygame.transform.scale(pygame.image.load('./imagenes/shuriken.png'), (60, 60))

paisaje = pygame.transform.scale(pygame.image.load('./imagenes/paisajeNinja.jpg'), (600, 600))

muro2 = pygame.transform.scale(pygame.image.load('./imagenes/muro2.jpg'), (60, 60))
espacioVacioBottom = pygame.transform.scale(pygame.image.load('./imagenes/espacio-vacio-bottom.png'), (60, 60))
espacioVacioTop = pygame.transform.scale(pygame.image.load('./imagenes/espacio-vacio-top.png'), (60, 60))
espacioVacioLeft = pygame.transform.scale(pygame.image.load('./imagenes/espacio-vacio-left.png'), (60, 60))
espacioVacioRight = pygame.transform.scale(pygame.image.load('./imagenes/espacio-vacio-right.png'), (60, 60))
espacioVacioLeft.set_colorkey(BLANCO)
espacioVacioRight.set_colorkey(BLANCO)
espacioVacioTop.set_colorkey(BLANCO)
espacioVacioBottom.set_colorkey(BLANCO)

espacioVacio2 = pygame.transform.scale(pygame.image.load('./imagenes/espacio-vacio.png'), (60, 60))
espacioVacio2.set_colorkey(BLANCO)

imagenes = {0: muro2,1: espacioVacio2,
            2: espacioVacioRight, 3: espacioVacioLeft,
            4: espacioVacioBottom, 5: espacioVacioTop,
            6: shuriken}
#  Inicializar el reloj
reloj = pygame.time.Clock()


def recarga_pantalla():
    PANTALLA.fill(GRIS)
    PANTALLA.blit(paisaje, (0, 0))
    for (fila, columna), valor in np.ndenumerate(matriz):
        PANTALLA.blit(imagenes[valor], (columna * 60, fila * 60))
    PANTALLA.blit(ninja_stop, (9 * 60, 8 * 60))
    pygame.display.update()


ejecuta = True
# bucle del juego
while ejecuta:
    for evento in pygame.event.get():
        if evento.type == QUIT:
            ejecuta = False
    recarga_pantalla()
    reloj.tick(60)

pygame.quit()
sys.exit()
