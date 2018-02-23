#Dies ist das Projekt von Valerio und Timo
#Projektziel:   1. Mastermind (Spiel) auf pygame installieren
#               2. Netzwerk für Multiplayer aufbauen

import pygame
from pygame.constants import *

#             R    G    B
BLACK     = (  0,   0,   0)
BLUE      = (  0,   0, 255)
CYAN      = (  0, 255, 255)
GRAY      = (100, 100, 100)
GREEN     = (  0, 255,   0)
ORANGE    = (255, 165,   0)
PINK      = (255,   8, 127)
PURPLE    = (255,   0, 255)
RED       = (255,   0,   0)
WHITE     = (255, 255, 255)
YELLOW    = (255, 255,   0)


pygame.init()

# Fenstergroesse
board_length = 900
board_height = 700

# Das Fenster erstellen
screen = pygame.display.set_mode((board_length, board_height), 0, 32)
pygame.display.set_caption('Mastermind')


#Main Programm
def main():
    screen.fill(WHITE)
    pygame.display.update()

    is_running = True
    while is_running:  # main game loop
        screen.fill(WHITE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                is_running = False


if __name__ == '__main__':
    main()
    print("Programm beendet.")