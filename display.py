# -*- coding: utf-8 -*-

import pygame
import time
import constances


class Display:
    # # ####### FENETRE ####### #

    def __init__(self):

        # Init pygame
        pygame.init()
        # Display windows
        self.window = pygame.display.set_mode((constances.cote_fenetre, (constances.cote_fenetre + constances.size_info)))

        self.mg_icon = pygame.image.load(constances.mg_icon).convert_alpha()
        self.aiguille_icon = pygame.image.load(constances.img_aiguille).convert_alpha()
        self.aiguille_icon_none = pygame.image.load(constances.img_aiguille_none).convert_alpha()

        self.ether_icon = pygame.image.load(constances.img_ether).convert_alpha()
        self.tube_icon = pygame.image.load(constances.img_tube).convert_alpha()
        self.guardian = pygame.image.load(constances.img_guardian).convert_alpha()

        self.background = pygame.image.load(constances.background_game).convert()
        # AFFICHAGE DES MURS
        self.wall = pygame.image.load(constances.img_wall)

    def display(self, lvl, items_pu):
        """

        :param lvl:
        :param items_pu:
        :return:
        """
        # ####### FENETRE ####### #
        # Display background
        # if items_pu is None:
        #     items_pu = []

        self.window.blit(self.background, (0, 0))
        # Title
        pygame.display.set_caption(constances.title_game)

        # On parcours les list de la structure (ligne horizontal)
        for num_line, line in enumerate(lvl.structure):
            # On parcours les caracteres de la ligne (ligne vertical)
            mapping = {"m": self.wall, "d": self.mg_icon, "MG": self.mg_icon, "A": self.aiguille_icon,
                       "E": self.ether_icon, "T": self.tube_icon, "a": self.guardian }

            for num_case, sprite in enumerate(line):
                # On calcule la position en px
                x = num_case * constances.size_sprite
                y = num_line * constances.size_sprite
                try:
                    self.window.blit(mapping[sprite], (x, y))
                except KeyError:
                    pass
        self.display_object_pu(items_pu)

    def display_object_pu(self, items):
        red = (125, 13, 43)
        font = pygame.font.SysFont("comicsansms", 30)
        text = font.render("Liste des objets: ", True, red)
        textRect = text.get_rect()
        textRect.center = (90, constances.cote_fenetre + 70)
        self.window.blit(text, textRect)
        if "Aiguille" in items:
            self.window.blit(self.aiguille_icon, (170, 645))
        else:
            self.window.blit(self.aiguille_icon_none, (170, 645))
        if "Tube" in items:
            self.window.blit(self.tube_icon, (230, 645))
        else:
            self.window.blit(self.tube_icon, (230, 645))
        if "Ether" in items:
            self.window.blit(self.ether_icon, (200, 645))
        else:
            self.window.blit(self.ether_icon, (200, 645))

    # def end_game(self):
    #     # activate the pygame library
    #     # initiate pygame and give permission
    #     # to use pygame's functionality.
    #     pygame.init()
    #
    #     # define the RGB value for white,
    #     #  green, blue colour .
    #     white = (255, 255, 255)
    #     green = (0, 255, 0)
    #     blue = (0, 0, 128)
    #
    #     # assigning values to X and Y variable
    #     X = 400
    #     Y = 400
    #
    #     # create the display surface object
    #     # of specific dimension..e(X, Y).
    #     display_surface = pygame.display.set_mode((X, Y))
    #
    #     # set the pygame window name
    #     pygame.display.set_caption('Show Text')
    #
    #     # create a font object.
    #     # 1st parameter is the font file
    #     # which is present in pygame.
    #     # 2nd parameter is size of the font
    #     font = pygame.font.Font('freesansbold.ttf', 32)
    #
    #     # create a text suface object,
    #     # on which text is drawn on it.
    #     text = font.render('VOUS AVEZ GAGNE', True, green, blue)
    #
    #     # create a rectangular object for the
    #     # text surface object
    #     textRect = text.get_rect()
    #
    #     # set the center of the rectangular object.
    #     textRect.center = (X // 2, Y // 2)
    #
    #     # infinite loop
    #     while True:
    #
    #         # completely fill the surface object
    #         # with white color
    #         display_surface.fill(white)
    #
    #         # copying the text surface object
    #         # to the display surface object
    #         # at the center coordinate.
    #         display_surface.blit(text, textRect)
    #
    #         # iterate over the list of Event objects
    #         # that was returned by pygame.event.get() method.
    #         for event in pygame.event.get():
    #
    #             # if event object type is QUIT
    #             # then quitting the pygame
    #             # and program both.
    #             if event.type == pygame.QUIT:
    #                 # deactivates the pygame library
    #                 pygame.quit()
    #
    #                 # quit the program.
    #                 quit()
    #
    #                 # Draws the surface object to the screen.
    #             pygame.display.update()
    #
    #     # time.sleep(5)
    #
    #         return False


