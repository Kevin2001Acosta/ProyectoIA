# leer matriz de un txt
import numpy as np
import pygame
import sys
from pygame.locals import *
from modelo import Busqueda_Amplitud
from modelo import Busqueda_A


# Leer el archivo de texto y convertirlo en una matriz

matriz = np.loadtxt('./matrices/matriz1.txt', dtype=int)
matriz_2 = np.loadtxt('./matrices/matriz2.txt', dtype=int)
#matriz = matriz_2
matriz2 = matriz.copy()
matriz3 = matriz.copy()
matriz_original = matriz.copy()


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
COLOR = (210, 180, 140)
COLOR2 = (154, 122, 83)


# Configurar la PANTALLA
ANCHO = 900
ALTO = 600
PANTALLA = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption('Buscando el Shuringan por BFS y A*')

fuente = pygame.font.SysFont("Century Gothic", 18, bold=True)
text = fuente.render("BÚSQUEDA POR AMPLITUD", True, NEGRO)
text3 = fuente.render("BÚSQUEDA POR A*", True, NEGRO)
text4 = fuente.render("CREADOS:", True, NEGRO)
text5 = fuente.render("EXPANDIDOS:", True, NEGRO)


ninja_icon = pygame.transform.scale(pygame.image.load('./imagenes/ninja-icon.png'), (60, 60))
# icono del juego
pygame.display.set_icon(ninja_icon)


#ninja

caminaDerecha = [pygame.transform.scale(pygame.image.load('./imagenes/ninjas-right1.png'), (60, 60)),
                 pygame.transform.scale(pygame.image.load('./imagenes/ninjas-right2.png'), (60, 60)),
                 pygame.transform.scale(pygame.image.load('./imagenes/ninjas-right3.png'), (60, 60))]

caminaIzquierda = [pygame.transform.scale(pygame.image.load('./imagenes/ninjas-left1.png'), (60, 60)),
                   pygame.transform.scale(pygame.image.load('./imagenes/ninjas-left2.png'), (60, 60)),
                   pygame.transform.scale(pygame.image.load('./imagenes/ninjas-left3.png'), (60, 60))]

ninja_stop = pygame.transform.scale(pygame.image.load('./imagenes/ninja-stop.png'), (60, 60))
ninja_salto = pygame.transform.scale(pygame.image.load('./imagenes/ninja-salto.png'), (60, 60))
camina_arriba_abajo = [pygame.transform.scale(pygame.image.load('./imagenes/ninja-salto.png'), (60, 60)),
                       pygame.transform.scale(pygame.image.load('./imagenes/ninja-salto.png'), (60, 60)),
                       pygame.transform.scale(pygame.image.load('./imagenes/ninja-salto.png'), (60, 60))]


shuriken = pygame.transform.scale(pygame.image.load('./imagenes/shuriken.png'), (60, 60))

paisaje = pygame.transform.scale(pygame.image.load('./imagenes/paisajeNinja.png'), (600, 600)).convert()

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

imagen_boton = pygame.transform.scale(pygame.image.load("./imagenes/boton.png"), (90, 60))
imagen_boton2 = pygame.transform.scale(pygame.image.load("./imagenes/boton.png"), (90, 60))


# Obtener el rectángulo de la imagen del botón
rectangulo_boton1 = imagen_boton.get_rect()
rectangulo_boton1.center = (740, 75)

rectangulo_boton2 = imagen_boton2.get_rect()
rectangulo_boton2.center = (740, 155)

texto = ["","",""]
lista_recorrido = []

def pos_ninja():
    for fila in range(0, matriz.shape[0]):
        for columna in range(0, matriz.shape[1]):
            if matriz[fila][columna] == 7:
                return fila, columna


cuenta_pasos = 0
# Convertir la lista de recorridos en un iterador
recorridos_iter = iter(lista_recorrido)

en_movimiento = False
pos_actual_ninja = pos_ninja()
def ninja_movimiento():
    global cuenta_pasos, en_movimiento, pos_actual_ninja

    try:
        # Obtener el siguiente movimiento de la lista de recorridos
        i = next(recorridos_iter)
    except StopIteration:
        # Si ya no hay más movimientos, salir de la función
        en_movimiento = False
        return
    velocidad = 3
    # arriba
    if i[0] < pos_actual_ninja[0]:
        PANTALLA.blit(camina_arriba_abajo[cuenta_pasos//1], (pos_actual_ninja[1]*60, pos_actual_ninja[0]*60 - (20 * cuenta_pasos)))
        pygame.display.update()
        reloj.tick(velocidad)
        pos_actual_ninja = i
        cuenta_pasos += 1

    # abajo
    elif i[0] > pos_actual_ninja[0]:
        PANTALLA.blit(camina_arriba_abajo[cuenta_pasos//1], (pos_actual_ninja[1]*60, pos_actual_ninja[0]*60 + (20 * cuenta_pasos)))
        pygame.display.update()
        reloj.tick(velocidad)
        pos_actual_ninja = i
        cuenta_pasos += 1

    # derecha
    elif i[1] > pos_actual_ninja[1]:
        PANTALLA.blit(caminaDerecha[cuenta_pasos//1], (pos_actual_ninja[1]*60 + (20 * cuenta_pasos), pos_actual_ninja[0] * 60))
        pygame.display.update()
        reloj.tick(velocidad)
        pos_actual_ninja = i
        cuenta_pasos += 1

    # izquierda
    elif i[1] < pos_actual_ninja[1]:
        PANTALLA.blit(caminaIzquierda[cuenta_pasos//1], (pos_actual_ninja[1]*60 - (20 * cuenta_pasos), pos_actual_ninja[0]*60))
        pygame.display.update()
        reloj.tick(velocidad)
        pos_actual_ninja = i
        cuenta_pasos += 1

    if cuenta_pasos + 1 >= 3:
        cuenta_pasos = 0


# Función para verificar si se hizo clic en el botón
def verificar_clic(pos_mouse):
    global en_movimiento, lista_recorrido, recorridos_iter
    coordenadas = Busqueda_Amplitud.busqueda_amplitud(matriz2.copy())[0]
    creados = Busqueda_Amplitud.busqueda_amplitud(matriz2.copy())[2]
    expandidos = Busqueda_Amplitud.busqueda_amplitud(matriz2.copy())[1]
    
    if rectangulo_boton1.collidepoint(pos_mouse):
        if coordenadas is not None:
            lista_recorrido = []
            lista_recorrido.extend(coordenadas)
            recorridos_iter = iter(lista_recorrido)
            texto = ", ".join(map(str, coordenadas))
            en_movimiento = True
            return [texto, creados, expandidos]
        else:
            return ["No hay solución", creados, expandidos]
    
    coordenadas = Busqueda_A.busqueda_A(matriz3.copy())[0]
    creados = Busqueda_A.busqueda_A(matriz2.copy())[2]
    expandidos = Busqueda_A.busqueda_A(matriz2.copy())[1]
    if rectangulo_boton2.collidepoint(pos_mouse):
        if coordenadas is not None:
            lista_recorrido = []
            lista_recorrido.extend(coordenadas)
            recorridos_iter = iter(lista_recorrido)
            texto = ", ".join(map(str, coordenadas))
            en_movimiento = True
            return [texto, creados, expandidos]
        else:
            return ["No hay solución", creados, expandidos]
    
    else:
        return ""
    
 
def ajustar_texto(texto, fuente, max_width):
    lineas = []
    palabras = texto.split(' ')
    linea_actual = ''
    for palabra in palabras:
        test_linea = linea_actual + palabra + ' '
        if fuente.render(test_linea, True, (0, 0, 0)).get_rect().width < max_width -40:  # Resta 40 para dejar espacio a los lados
            linea_actual = test_linea
        else:
            lineas.append(linea_actual)
            linea_actual = palabra + ' '
    lineas.append(linea_actual)
    return '\n'.join(lineas)

def dividir_texto_en_lineas(texto, max_width):
    lineas = texto.split('\n')
    lineas_divididas = []
    for linea in lineas:
        palabras = linea.split(' ')
        linea_actual = ''
        for palabra in palabras:
            test_linea = linea_actual + palabra + ' '
            if fuente.render(test_linea, True, (0, 0, 0)).get_rect().width < max_width :
                linea_actual = test_linea
            else:
                lineas_divididas.append(linea_actual)
                linea_actual = palabra + ' '
        lineas_divididas.append(linea_actual)
    return lineas_divididas       


def mostrar_texto_y_rectangulo(texto):
    
    x, y, width, height = 632, 290, 240, 280
    
    tamano_fuente = 15
    fuente = pygame.font.SysFont("consolas", tamano_fuente)

    rectangulo = pygame.Rect(x, y, width, height)
    pygame.draw.rect(PANTALLA, BLANCO, rectangulo)
    pygame.draw.rect(PANTALLA, COLOR2, (x, y, width, height))

# Definir las dimensiones del rectángulo interior (para el borde)
    border_width = 3  # Ancho del borde
    inner_rect = pygame.Rect(x + border_width, y + border_width, width - 2 * border_width, height - 2 * border_width)

    # Dibujar el rectángulo interior (borde)
    pygame.draw.rect(PANTALLA, BLANCO, inner_rect)

    # Ajustar el tamaño del texto para que quepa dentro del rectángulo
    texto_renderizado = ajustar_texto(texto, fuente, rectangulo.width)

    # Calcular las líneas de texto para ajustarlo dentro del rectángulo
    lineas = dividir_texto_en_lineas(texto_renderizado, rectangulo.width)

    # Mostrar el texto dentro del rectángulo
    y = rectangulo.top

    for linea in lineas:
        # Renderizar la línea de texto con la fuente y el tamaño definidos
        texto = fuente.render(linea, True, NEGRO)
        
        # Obtener el rectángulo del texto y centrarlo horizontalmente en el rectángulo blanco
        texto_rect = texto.get_rect(topleft=(rectangulo.left + 25, y + 10))
        
        # Mostrar el texto en la pantalla
        PANTALLA.blit(texto, texto_rect)
        
        # Aumentar la posición y para la siguiente línea
        y += texto_rect.height  
        

def mostrar_nodos_y_rectangulo(nodosCreados, nodosExpandidos):
    
    x1, y1 = 750, 190 
    x2, y2 = 750, 230
    width, height = 100, 30
    tamano_fuente = 15
    fuente = pygame.font.SysFont("consolas", tamano_fuente)

    for (x, y), info in [((x1, y1), nodosCreados), ((x2, y2), nodosExpandidos)]:
        rectangulo = pygame.Rect(x, y, width, height)
        pygame.draw.rect(PANTALLA, BLANCO, rectangulo)
        pygame.draw.rect(PANTALLA, COLOR2, (x, y, width, height))
        
        border_width = 3  
        inner_rect = pygame.Rect(x + border_width, y + border_width, width - 2 * border_width, height - 2 * border_width)

        pygame.draw.rect(PANTALLA, BLANCO, inner_rect)

        texto = fuente.render(str(info), True, NEGRO)
        
        texto_rect = texto.get_rect(center=(x + width // 2, y + height // 2))

        PANTALLA.blit(texto, texto_rect)


imagenes = {0: muro2, 1: espacioVacio2,
            2: espacioVacioRight, 3: espacioVacioLeft,
            4: espacioVacioBottom, 5: espacioVacioTop,
            6: shuriken, 7: ninja_stop}
#  Inicializar el reloj
reloj = pygame.time.Clock()

cuenta_pasos = 0

def recarga_pantalla(informacion):
    PANTALLA.fill(COLOR)
    PANTALLA.blit(paisaje, (0, 0))
    
        
    for (fila, columna), valor in np.ndenumerate(matriz):
        if (fila, columna) == pos_actual_ninja:
            PANTALLA.blit(ninja_stop, (columna * 60, fila * 60))
        else:
            PANTALLA.blit(imagenes[valor], (columna * 60, fila * 60))
    for x in range(0, 650, 60):
        pygame.draw.line(PANTALLA, NEGRO, (x, 0), (x, ALTO))
    
    # Dibujar líneas horizontales
    for y in range(0, 600, 60):
        pygame.draw.line(PANTALLA, NEGRO, (0, y), (600, y))
    
    PANTALLA.blit(text, (640, 25))
    PANTALLA.blit(text3, (670, 105))
    PANTALLA.blit(text4, (620, 190))
    PANTALLA.blit(text5, (620, 235))
    
    pygame.draw.rect(PANTALLA, AZULCLARO, (0, 600, 200, 200))
    
    mostrar_texto_y_rectangulo(informacion[0])
    mostrar_nodos_y_rectangulo(informacion[1], informacion[2])

        
    PANTALLA.blit(imagen_boton, rectangulo_boton1)
    PANTALLA.blit(imagen_boton2, rectangulo_boton2)
        
    pygame.display.update()


ejecuta = True
# bucle del juego
while ejecuta:
    for evento in pygame.event.get():
        if evento.type == QUIT:
            ejecuta = False
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            if evento.button == 1:  # Verificar clic izquierdo del ratón
                mouse_pos = pygame.mouse.get_pos()
                texto = verificar_clic(mouse_pos)
    if en_movimiento:
        ninja_movimiento()
    recarga_pantalla(texto)
    reloj.tick(10)

pygame.quit()
sys.exit()
