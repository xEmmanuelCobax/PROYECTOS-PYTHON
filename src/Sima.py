import pygame
import numpy as np
import time
import sys

# Iniciar
pygame.init()

width, height = 700, 700
bg = 25, 25, 25
screen = pygame.display.set_mode((height, width))
screen.fill(bg)

# Tamaño de nuestra matriz
nxC, nyC = 25, 25

# Estado de las celdas. Viva = 1 / Muerta = 0
gameState = np.zeros((nxC, nyC))

# dimensiones de cada celda individual
dimCW = width / nxC
dimCH = height / nyC

# probabilidades
probabilidad_propagacion = float(input("Ingrese la probabilidad de propagación (0-1): "))
probabilidad_cura = float(input("Ingrese la probabilidad de cura (0-1): "))

pauseExect = True

# Variable para mantener el bucle en ejecución
running = True

# Bucle de ejecución
while running:
    # Copiamos la matriz del estado anterior
    # para representar la matriz en el nuevo estado
    newGameState = np.copy(gameState)

    # Ralentizamos la ejecución a 0.1 segundos
    time.sleep(0.1)

    # Limpiamos la pantalla
    screen.fill(bg)

    # Registramos eventos de teclado y ratón.
    ev = pygame.event.get()

    # Cada vez que identificamos un evento lo procesamos
    for event in ev:
        # Detectamos si se presiona una tecla.
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                pauseExect = not pauseExect
            elif event.key == pygame.K_r:
                pauseExect = True
                gameState = np.zeros((nxC, nyC))

        # Detectamos si se presiona el ratón.
        if pygame.mouse.get_pressed()[0]:
            posX, posY = pygame.mouse.get_pos()
            celX, celY = int(np.floor(posX / dimCW)), int(np.floor(posY / dimCH))
            newGameState[celX, celY] = 1

        if event.type == pygame.QUIT:
            running = False

    for y in range(0, nxC):
        for x in range(0, nyC):
            if not pauseExect:
                # Calculamos el número de vecinos cercanos. en total son 12 vecinos, las 8 + 4 extras
                n_neigh = gameState[(x - 1) % nxC, (y - 1) % nyC] + \
                        gameState[(x) % nxC, (y - 1) % nyC] + \
                        gameState[(x + 1) % nxC, (y - 1) % nyC] + \
                        gameState[(x - 1) % nxC, (y) % nyC] + \
                        gameState[(x + 1) % nxC, (y) % nyC] + \
                        gameState[(x - 1) % nxC, (y + 1) % nyC] + \
                        gameState[(x) % nxC, (y + 1) % nyC] + \
                        gameState[(x + 1) % nxC, (y + 1) % nyC] + \
                        gameState[(x - 2) % nxC, (y) % nyC] + \
                        gameState[(x + 2) % nxC, (y) % nyC] + \
                        gameState[(x) % nxC, (y - 2) % nyC] + \
                        gameState[(x) % nxC, (y + 2) % nyC]
                # Regla #1 : Una celda enferma se cura con cierta probabilidad.
                if gameState[x, y] == 1 and np.random.rand() < probabilidad_cura:
                    newGameState[x, y] = 0

                # Regla #2: Una celda sana con dos o más vecinas enfermas se enferma con cierta probabilidad.
                elif gameState[x, y] == 0 and n_neigh >= 3 and np.random.rand() < probabilidad_propagacion:
                    newGameState[x, y] = 1

                # Regla #3: Una celda enferma con menos de dos vecinas enfermas se cura (simulando que el aislamiento ayuda a la recuperación).
                elif gameState[x, y] == 1 and n_neigh < 2:
                    newGameState[x, y] = 0

                # Regla #4: Una celda sana con menos de dos vecinas enfermas permanece sana.
                elif gameState[x, y] == 0 and n_neigh < 2:
                    newGameState[x, y] = 0
                

            # Calculamos el polígono que forma la celda.
            poly = [((x) * dimCW, y * dimCH),
                    ((x + 1) * dimCW, y * dimCH),
                    ((x + 1) * dimCW, (y + 1) * dimCH),
                    ((x) * dimCW, (y + 1) * dimCH)]

            # Si la celda está "enferma" pintamos un recuadro con borde gris
            if newGameState[x, y] == 0:
                pygame.draw.polygon(screen, (0, 255, 0), poly, 0)
            # Si la celda está "Sana" pintamos un recuadro relleno de color
            else:
                pygame.draw.polygon(screen, (255, 0, 0), poly, 0)

    # Actualizamos el estado del juego.
    gameState = np.copy(newGameState)

    # Mostramos el resultado
    pygame.display.flip()

# Salir del juego
pygame.quit()
sys.exit()
