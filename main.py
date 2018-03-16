#Dies ist das Projekt von Valerio und Timo
#Projektziel:   1. Mastermind (Spiel) auf pygame installieren
#               (2. Netzwerk für Multiplayer aufbauen)

import pygame
from pygame.constants import *

#              R    G    B
BACKGROUND = (110, 193, 150)
BLACK      = (  0,   0,   0)
BLUE       = (  0,   0, 255)
GRAY       = (100, 100, 100)
GREEN      = (  0, 255,   0)
ORANGE     = (255, 165,   0)
PINK       = (255,   8, 127)
PURPLE     = (255,   0, 255)
RED        = (255,   0,   0)
WHITE      = (255, 255, 255)
YELLOW     = (255, 255,   0)

FARBE = [WHITE, GRAY, BLACK, BLUE, PURPLE, PINK, RED, ORANGE, YELLOW, GREEN]


class Kreis:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius
        self.is_active = False
        self.farbe = None


class Gameboard:
    def __init__(self, screen, window_length, window_height, gameboard_width, gameboard_height, max_anz_versuche, player=1, kreisnummer=1):
        self.screen = screen
        self.window_length = window_length
        self.window_height = window_height
        self.gameboard_width = gameboard_width
        self.gameboard_height = gameboard_height
        self.anz_versuche = max_anz_versuche
        self.ebene = 0
        self.player = player
        self.kreisnummer = kreisnummer
        self.kasten_length = self.gameboard_width
        self.kasten_height = self.gameboard_height / (self.anz_versuche + 3)

        radius = self.kasten_height / 4
        self.steckplatz = [[0 for i in range(4)] for j in range(max_anz_versuche)]

        x_koordinate = self.window_length / 3
        y_koordinate = self.window_height - (1/2)*self.kasten_height

        # for i in range(len(self.steckplatz)):
        #
        #     for j in range(len(self.steckplatz[i])):
        #
        #         self.steckplatz[i][j] = Kreis()

    def zeichne_gameboard(self):
        x_koordinate = self.window_length / 3
        y_koordinate = self.window_height - (1/2)*self.kasten_height

        for i in range(self.anz_versuche):
            #Koordinaten für die Kreise
            x_kreis = x_koordinate + self.kasten_height + (1/2) * ((self.kasten_length - self.kasten_height) / 4)
            y_kreis = y_koordinate

            #Kasten erstellen
            pygame.draw.rect(self.screen, BLACK, (x_koordinate, y_koordinate, self.kasten_length, - self.kasten_height), 1)
            #Rückmeldungsbereich erstellen (als Quadrat)
            pygame.draw.rect(self.screen, BLACK, (x_koordinate, y_koordinate, self.kasten_height, - self.kasten_height), 1)

            #leere Kreise erstellen
            # for i in range(4):
            #     radius_kreis = self.kasten_height / 2
            #     pygame.draw.circle(self.screen, BLACK, (x_kreis, y_kreis), radius_kreis, 1)
            #     x_kreis += (kasten_length - self.kasten_height) / 4

            y_koordinate -= self.kasten_height


        y_koordinate -= self.kasten_height
        pygame.draw.rect(self.screen, BLACK, (x_koordinate, y_koordinate, self.kasten_length, - self.kasten_height), 1)


class Button:
    def __init__(self, length, height, text, farbe_text, farbe_box, x_kord, y_kord):
        self.length = length
        self.heigth = height
        self.text = text
        self.farbe_text = farbe_text
        self.farbe_box = farbe_box
        self.x_kord = x_kord
        self.y_kord = y_kord

    def zeichne_button(self):
        pass

#Main Programm
def main():
    pygame.init()

    # Fenstergroesse
    window_length = 900
    window_height = 700

    # Das Fenster erstellen
    screen = pygame.display.set_mode((window_length, window_height), 0, 32)
    pygame.display.set_caption('Mastermind')
    screen.fill(BACKGROUND)


    # game informationen
    gameboard_width = window_length / 3
    gameboard_height = window_height

    max_anz_versuche = 12
    ebene = 0
    player = 1

    FPS = 10
    fps_clock = pygame.time.Clock()
    gameboard_width = window_length / 3
    gameboard_height = window_height

    end_turn = False

###-------------------------------------------------------------------------###
    my_game = Gameboard(screen, window_length, window_height, gameboard_width, gameboard_height, max_anz_versuche, ebene, player)

    is_running = True
    while is_running:  # main game loop
        screen.fill(BACKGROUND)

        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                is_running = False

        my_game.zeichne_gameboard()
        pygame.display.update()



if __name__ == '__main__':
    main()
    print("Programm beendet.")