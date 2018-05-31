#Dies ist das Projekt von Valerio und Timo
#Projektziel:   1. Mastermind (Spiel) auf pygame installieren
#               (2. Netzwerk für Multiplayer aufbauen)

import pygame
from pygame.constants import *
import random

#              R    G    B
BACKGROUND = (110, 193, 150)
BOARDCOLOR = (168, 101,   9)
KREISCOLOR = (128,  61,   9)
BLACK      = (  0,   0,   0)
BLUE       = (  0, 100, 255)
GRAY       = (100, 100, 100)
GREEN      = (  0, 255,   0)
ORANGE     = (255, 165,   0)
PINK       = (255,   0, 255)
PURPLE     = (121,  54, 152)
RED        = (255,   0,   0)
WHITE      = (255, 255, 255)
YELLOW     = (255, 255,   0)
CLICKCOLOR = (168, 172, 173)

FARBE = [RED, ORANGE, YELLOW, GREEN, BLUE, PURPLE, PINK, GRAY, BLACK, WHITE]
VORLAGE_FARBE = [RED, ORANGE, YELLOW, GREEN, BLUE, PURPLE, PINK, GRAY, BLACK, WHITE]

#hallo du coole typ


class Kreis:        #Farbe???
    def __init__(self, x, y, radius):
        self.x = int(x)
        self.y = int(y)
        self.radius = int(radius)
        self.is_active = False
        self.farbe = KREISCOLOR

class Gameboard:
    def __init__(self, screen, window_length, window_height, gameboard_width, gameboard_height, max_anz_versuche):
        self.screen = screen
        self.window_length = window_length
        self.window_height = window_height
        self.gameboard_width = gameboard_width
        self.gameboard_height = gameboard_height
        self.anz_versuche = max_anz_versuche
        self.kasten_length = self.gameboard_width
        self.kasten_height = self.gameboard_height / (self.anz_versuche + 3)
        #######
        self.stiftkasten_length = self.kasten_height

        #Kreise definieren
        kreis_radius = self.kasten_height / 4

        #Matrix für Kreise in Steckplatz erstellen
        self.steckplatz = [[0 for i in range(4)] for j in range(max_anz_versuche)]

        kreis_abstand = (self.kasten_length - self.kasten_height) / 4
        y_koordinate = self.window_height

        for i in range(len(self.steckplatz)):
            y_koordinate -= self.kasten_height
            x_koordinate = self.window_length / 3 + self.kasten_height + kreis_abstand / 2
            for j in range(len(self.steckplatz[i])):
                self.steckplatz[i][j] = Kreis(x_koordinate, y_koordinate, kreis_radius)
                x_koordinate += kreis_abstand

        #Liste für Kreise in Vorlagekasten erstellen
        self.vorlagekasten = [0 for i in range(4)]
        kreis_abstand = (self.kasten_length) / 4
        y_koordinate = y_koordinate - 2 * self.kasten_height
        x_koordinate = self.window_length / 3 + kreis_abstand / 2
        for i in range(len(self.vorlagekasten)):
            self.vorlagekasten[i] = Kreis(x_koordinate, y_koordinate, kreis_radius)
            x_koordinate += kreis_abstand

        #Stifte definieren
        stift_radius = self.stiftkasten_length / 4 / 2

        #Matrix für Stifte
        self.stifte = [[0 for i in range(4)] for j in range(max_anz_versuche)]
        stift_abstand = self.kasten_height / 3
        y_stift = self.window_height - 1.5 * self.kasten_height + stift_abstand
        x_stift = self.window_length / 3 + stift_abstand

        for i in range(len(self.stifte)):       #von 0-11 (range(12))
            self.stifte[i][0] = Kreis(x_stift, y_stift, stift_radius)   #links oben
            x_stift += stift_abstand
            self.stifte[i][1] = Kreis(x_stift, y_stift, stift_radius)   #rechts oben
            y_stift += stift_abstand
            x_stift -= stift_abstand
            self.stifte[i][2] = Kreis(x_stift, y_stift, stift_radius)   #links unten
            x_stift += stift_abstand
            self.stifte[i][3] = Kreis(x_stift, y_stift, stift_radius)   #rechts unten
            y_stift -= stift_abstand
            x_stift -= stift_abstand
            y_stift -= self.kasten_height

        #Liste für Farbauswahl
        self.farbauswahl = [0 for i in range(len(FARBE))]
        #Farbauswahl erstellen
        farbauswahlx = 2/3 * self.window_length + self.kasten_height
        farbauswahl_height = 10 * self.kasten_height
        farbauswahly = 1/4 * window_height

        for i in range(len(FARBE)):
            self.farbauswahl[i] = Button(self.screen, self.kasten_height, self.kasten_height, FARBE[i], BLACK, farbauswahlx, farbauswahly)
            farbauswahly += self.kasten_height - 2

    def vorlage_farben_erstellen(self):
        vorlage_farbe = []
        for i in range(len(self.vorlagekasten)):
            index = random.randint(0, len(VORLAGE_FARBE) - 1)
            farbe_neu = VORLAGE_FARBE.pop(index)
            self.vorlagekasten[i].farbe = farbe_neu
            vorlage_farbe.append(farbe_neu)
        return vorlage_farbe

    def zeichne_gameboard(self):
        x_koordinate = self.window_length / 3
        y_koordinate = self.window_height - (1/2)*self.kasten_height

        for i in range(self.anz_versuche):
            #Koordinaten für die Kreise
            x_kreis = x_koordinate + self.kasten_height + (1/2) * ((self.kasten_length - self.kasten_height) / 4)
            y_kreis = y_koordinate

            #Kasten erstellen
            pygame.draw.rect(self.screen, BOARDCOLOR, (x_koordinate, y_koordinate, self.kasten_length, - self.kasten_height), 0)
            pygame.draw.rect(self.screen, BLACK, (x_koordinate, y_koordinate, self.kasten_length, - self.kasten_height), 2)

            #Rückmeldungsbereich erstellen (als Quadrat)
            pygame.draw.rect(self.screen, BLACK, (x_koordinate, y_koordinate, self.kasten_height, - self.kasten_height), 2)

            y_koordinate -= self.kasten_height

        #leere Kreise im Gameboard zeichnen
        for i in range(len(self.steckplatz)):
            for j in range(len(self.steckplatz[i])):
                pygame.draw.circle(self.screen, self.steckplatz[i][j].farbe,
                                   (self.steckplatz[i][j].x, self.steckplatz[i][j].y), self.steckplatz[i][j].radius, 0)
                pygame.draw.circle(self.screen, BLACK,
                                   (self.steckplatz[i][j].x, self.steckplatz[i][j].y), self.steckplatz[i][j].radius, 2)
                if self.steckplatz[i][j].is_active:
                    # aktiver Kreis mit Rot umkreisen
                    pygame.draw.circle(self.screen, RED,
                                       (self.steckplatz[i][j].x, self.steckplatz[i][j].y),
                                       self.steckplatz[i][j].radius, 2)

        #leere Stifte im Gameboard zeichnen
        for i in range(len(self.stifte)):
            for j in range(len(self.stifte[i])):
                pygame.draw.circle(self.screen, self.stifte[i][j].farbe,
                                   (self.stifte[i][j].x, self.stifte[i][j].y), self.stifte[i][j].radius, 0)
                pygame.draw.circle(self.screen, BLACK,
                                   (self.stifte[i][j].x, self.stifte[i][j].y), self.stifte[i][j].radius, 2)


        #Vorlagekasten zeichnen
        y_koordinate -= self.kasten_height
        pygame.draw.rect(self.screen, BOARDCOLOR, (x_koordinate, y_koordinate, self.kasten_length, - self.kasten_height), 0)
        pygame.draw.rect(self.screen, BLACK, (x_koordinate, y_koordinate, self.kasten_length, - self.kasten_height), 2)

        # leere Kreise im Vorlagekasten zeichnen
        for i in range(len(self.vorlagekasten)):
            pygame.draw.circle(self.screen, self.vorlagekasten[i].farbe,
                               (self.vorlagekasten[i].x, self.vorlagekasten[i].y), self.vorlagekasten[i].radius, 0)
            pygame.draw.circle(self.screen, BLACK,
                               (self.vorlagekasten[i].x, self.vorlagekasten[i].y), self.vorlagekasten[i].radius, 2)


    def kreis_farbe_aendern(self, zeile, spalte, neue_farbe):
        self.steckplatz[zeile][spalte].farbe = neue_farbe

    def stift_farbe_aendern(self, zeile, spalte, neue_farbe):
        self.stifte[zeile][spalte].farbe = neue_farbe

    def vorlage_kreis_farbe_aendern(self, index, neue_farbe):
        self.vorlagekasten[index].farbe = neue_farbe

    def farben_abgleichen(self, vorlage_farbe, EBENE):
        #Abfrage: richtige Farbe an richtigem Platz -> BLACK
        game_over = True
        liste_richtige = []
        for i in range(len(self.steckplatz[EBENE])):
            if self.steckplatz[EBENE][i].farbe == vorlage_farbe[i]:
                liste_richtige.append(True)
            else:
                liste_richtige.append(False)
                game_over = False                   #sobald eine Farbe falsch ist, wird die boolean auf False gewechselt

        #Abfrage: richtige Farbe an falschem Platz -> WHITE
        counter_white = 0
        for i in range(len(liste_richtige)):        #für i = 0:3
            if not liste_richtige[i]:
                for j in range(len(liste_richtige)):
                    if i != j and self.steckplatz[EBENE][i] == vorlage_farbe[j]:     #für alle j != i: wenn steckplatzfarbe bei i == vorlagefarbe bei j:
                        counter_white += 1

        #Ausgabe erstellen:
        ausgabe = []
        #überprüfen, wie viele am richtigen Ort (schwarz) sind
        counter_black = 0
        for i in range(len(liste_richtige)):
            if liste_richtige[i]:
                counter_black += 1
        #Ausgabe ergänzen           ------>>> BLACK
        for i in range(counter_black):
            ausgabe.append(BLACK)

        #Ausgabe ergänzen           ------>>> WHITE
        for i in range(counter_white):
            ausgabe.append(WHITE)

        #Endausgabe
        if game_over == True:
            return game_over            #Wenn alle Farben richtig sind, wird True zurückgegeben
        else:
            return ausgabe


    def end_of_game(self):
        pass

    def zeichne_abdeckung(self):
        abdeckung_x = 1/3 * self.window_length + 2
        abdeckung_y = 1/2 * self.kasten_height + 1/5 * self.kasten_height
        abdeckung_height = self.kasten_height - 2/5 * self.kasten_height
        pygame.draw.rect(self.screen, GRAY, (abdeckung_x, abdeckung_y, self.kasten_length - 3, abdeckung_height), 0)
        pygame.draw.rect(self.screen, BLACK, (abdeckung_x, abdeckung_y, self.kasten_length - 3, abdeckung_height), 2)

class Button:
    def __init__(self, screen, button_length, button_height, farbe_box, farbe_rand, x_koord, y_koord,
                 button_text="", farbe_text=BLACK):
        self.screen = screen
        self.button_length = button_length
        self.button_height = button_height
        self.button_text = button_text
        self.farbe_text = farbe_text
        self.farbe_rand = farbe_rand
        self.farbe_box = farbe_box
        self.x_koord = x_koord
        self.y_koord = y_koord

    def zeichne_button(self, font_obj=None):
        box_rect = pygame.Rect(self.x_koord, self.y_koord, self.button_length, self.button_height)
        pygame.draw.rect(self.screen, self.farbe_box, box_rect, 0)
        pygame.draw.rect(self.screen, self.farbe_rand, box_rect, 2)
        # fehlt noch etwas beim einfügen (von game infos einfügen)
        text_obj = font_obj.render(self.button_text, True, self.farbe_text)
        rect_text = text_obj.get_rect()  # Position des Textes setzen
        rect_text.center = box_rect.center
        self.screen.blit(text_obj, rect_text)

    def changecolor_clicked_button(self):
        self.farbe_box = CLICKCOLOR

    def recolor_unclicked_button(self, color):
        self.farbe_box = color

# Main Programm
def main():
    pygame.init()

    # Fenstergroesse
    window_length = 1000
    window_height = 700

    # Das Fenster erstellen
    screen = pygame.display.set_mode((window_length, window_height), 0, 32)
    pygame.display.set_caption('Mastermind')
    screen.fill(BACKGROUND)

    # game informationen
    gameboard_width = window_length / 3
    gameboard_height = window_height
    max_anz_versuche = 12
    EBENE = 0
    KREISNUMMER = 0

    FPS = 10
    fps_clock = pygame.time.Clock()
    gameboard_width = window_length / 3
    gameboard_height = window_height

    # für text
    font_obj = pygame.font.Font('freesansbold.ttf', 35)

    # button_end_turn Informationen:
    b_end_turn_length = 200
    b_end_turn_height = 100
    b_end_turn_text = 'END TURN!'
    b_end_turn_t_color = BLACK
    b_end_turn_fill = GREEN
    b_end_turn_border = BLACK
    b_end_turn_x = (window_length * 1 / 3 - b_end_turn_length) / 2
    b_end_turn_y = (window_height - b_end_turn_height) / 2


    my_game = Gameboard(screen, window_length, window_height, gameboard_width, gameboard_height, max_anz_versuche)
    button_end_turn = Button(screen, b_end_turn_length, b_end_turn_height, b_end_turn_fill, b_end_turn_border,
                             b_end_turn_x, b_end_turn_y, b_end_turn_text, b_end_turn_t_color)

    vorlage_farbe = my_game.vorlage_farben_erstellen()          #zufällige Farben werden für den Vorlagekasten erstellt und eine Liste mit den Farben herausgegeben
    #print(vorlage_farbe)

    # farbauswahl koordinaten für klick abfragen
    farbauswahl_x = 2/3 * my_game.window_length + my_game.kasten_height
    y_koord_farbauswahl = 1/4 * my_game.window_height
    farbauswahl_y = []
    for i in range(len(FARBE)):
        farbauswahl_y.append(1/4 * my_game.window_height + i * my_game.kasten_height)


    end_turn = False

    ###-------------------------------------------------------------------------###

    is_running = True
    while is_running:  # main game loop
        screen.fill(BACKGROUND)

        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                is_running = False

            # Abfrage ob Button end turn geklickt:
            elif (event.type == pygame.MOUSEBUTTONDOWN) and (b_end_turn_x <= pygame.mouse.get_pos()[0]) and (
                    pygame.mouse.get_pos()[0] <= (b_end_turn_x + b_end_turn_length)) and (
                    b_end_turn_y <= pygame.mouse.get_pos()[1]) and (
                    pygame.mouse.get_pos()[1] <= (b_end_turn_y + b_end_turn_height)):
                button_end_turn.changecolor_clicked_button()

            elif (event.type == pygame.MOUSEBUTTONUP) and (b_end_turn_x <= pygame.mouse.get_pos()[0]) and (
                    pygame.mouse.get_pos()[0] <= (b_end_turn_x + b_end_turn_length)) and (
                    b_end_turn_y <= pygame.mouse.get_pos()[1]) and (
                    pygame.mouse.get_pos()[1] <= (b_end_turn_y + b_end_turn_height)):
                button_end_turn.recolor_unclicked_button(GREEN)


                if EBENE == max_anz_versuche:  # spiel ist fertig da spieler zuoberst ist und nicht errraten.
                    my_game.end_of_game()

                else:
                    not_kreiscolor = True
                    for i in range(4):
                        not_kreiscolor = not_kreiscolor and my_game.steckplatz[EBENE][i].farbe != KREISCOLOR
                    if not_kreiscolor:
                        EBENE += 1
                        KREISNUMMER = 0
                    else:
                        pass


            # Mit Pfeilen Kreisnummer wählen:
            elif event.type == pygame.KEYUP:
                if event.key == K_RIGHT:
                    KREISNUMMER += 1
                    if KREISNUMMER == 4:
                        KREISNUMMER = 0
                elif event.key == K_LEFT:
                    KREISNUMMER -= 1
                    if KREISNUMMER < 0:
                        KREISNUMMER = 3


            #Abfrage ob eine Farbe bei der Farbauswahl geklickt ist und dann den richtigen Kreis Färben.
            else:
                 for i in range(0, len(my_game.farbauswahl)):
                    if (event.type == pygame.MOUSEBUTTONDOWN) and (farbauswahl_x <= pygame.mouse.get_pos()[0]) and (
                            pygame.mouse.get_pos()[0] <= (farbauswahl_x + my_game.kasten_height)) and (
                            my_game.farbauswahl[i].y_koord <= pygame.mouse.get_pos()[1]) and (
                            pygame.mouse.get_pos()[1] <= (my_game.farbauswahl[i].y_koord + my_game.kasten_height)):

                        my_game.farbauswahl[i].changecolor_clicked_button()

                    elif (event.type == pygame.MOUSEBUTTONUP) and (farbauswahl_x <= pygame.mouse.get_pos()[0]) and (
                            pygame.mouse.get_pos()[0] <= (farbauswahl_x + my_game.kasten_height)) and (
                            my_game.farbauswahl[i].y_koord <= pygame.mouse.get_pos()[1]) and (
                            pygame.mouse.get_pos()[1] <= (my_game.farbauswahl[i].y_koord + my_game.kasten_height)):

                        my_game.farbauswahl[i].recolor_unclicked_button(FARBE[i])
                        my_game.kreis_farbe_aendern(EBENE, KREISNUMMER, FARBE[i])

                        not_kreiscolor1 = True
                        for i in range(4):
                            not_kreiscolor1 = not_kreiscolor1 and my_game.steckplatz[EBENE][i].farbe != KREISCOLOR
                        if not_kreiscolor1:
                            pass
                        else:
                            KREISNUMMER += 1


        for i in range(len(my_game.steckplatz)):
            for j in range(len(my_game.steckplatz[i])):
                if i == EBENE and j == KREISNUMMER:
                    my_game.steckplatz[i][j].is_active = True
                else:
                    my_game.steckplatz[i][j].is_active = False



        game_over = True            #Boolean, dass am



        my_game.zeichne_gameboard()
        #zeichne_farbauswahl
        for i in range(len(my_game.farbauswahl)):
            my_game.farbauswahl[i].zeichne_button(font_obj)
        button_end_turn.zeichne_button(font_obj)
        if not game_over:
            my_game.zeichne_abdeckung()
        pygame.display.update()

if __name__ == '__main__':
    main()
    print("Programm beendet.")