#Dies ist das Projekt von Valerio und Timo
#Projektziel:   1. Mastermind (Spiel) auf pygame installieren
#               2. Netzwerk für Multiplayer aufbauen

import pygame
from pygame.constants import *

#             R    G    B
BLACK     = (  0,   0,   0)
BLUE      = (  0,   0, 255)
GRAY      = (100, 100, 100)
GREEN     = (  0, 255,   0)
ORANGE    = (255, 165,   0)
PINK      = (255,   8, 127)
PURPLE    = (255,   0, 255)
RED       = (255,   0,   0)
WHITE     = (255, 255, 255)
YELLOW    = (255, 255,   0)



class Spiel:
    def __init__(self, screen, window_length, window_height, gameboard_width, gameboard_height, ebene, player, anz_versuche):
        self.screen = screen
        self.window_length = window_length
        self.window_height = window_height
        self.gameboard_width = gameboard_width
        self.gameboard_height = gameboard_height
        self.ebene = ebene
        self.player = player
        self.anz_versuche = anz_versuche

    def zeichne_gameboard(self):
        kasten_length = self.gameboard_width
        kasten_height = self.gameboard_height / (self.anz_versuche + 2)

        x_koordinate = self.window_length / 4
        y_koordinate = self.window_height

        for i in range(anz_versuche):
            pygame.draw.rect(screen, BLACK, (x_koordinate, y_koordinate, kasten_length, kasten_height), 1)
            y_koordinate -= kasten_height

        y_koordinate -= kasten_height
        pygame.draw.rect(screen, BLACK, (x_koordinate, y_koordinate, kasten_length, kasten_height), 1)




#Main Programm
def main():
    pygame.init()

    # Fenstergroesse
    window_length = 900
    window_height = 700

    # Das Fenster erstellen
    screen = pygame.display.set_mode((window_length, window_height), 0, 32)
    pygame.display.set_caption('Mastermind')

    # game informationen
    gameboard_width = window_length / 2
    gameboard_height = window_height

    anz_versuche = 12


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