# -*- coding: utf-8 -*-

import pygame
import constances


class Display:
    # # ####### WINDOW ####### #

    def __init__(self):

        # Init pygame
        pygame.init()
        # Display windows
        self.window = pygame.display.set_mode((constances.SIZE_WINDOW, (constances.SIZE_WINDOW + constances.SIZE_INFO)))

        self.mg_icon = pygame.image.load(constances.MG_ICON).convert_alpha()
        self.aiguille_icon = pygame.image.load(constances.IMG_AIGUILLE).convert_alpha()
        self.aiguille_icon_none = pygame.image.load(constances.IMG_AIGUILLE_NONE).convert_alpha()

        self.ether_icon = pygame.image.load(constances.IMG_ETHER).convert_alpha()

        self.tube_icon = pygame.image.load(constances.IMG_TUBE).convert_alpha()

        self.guardian = pygame.image.load(constances.IMG_GUARDIAN).convert_alpha()

        self.background = pygame.image.load(constances.BACKGROUND_GAME).convert()
        # Display wall
        self.wall = pygame.image.load(constances.IMG_WALL)

    def display(self, lvl, items_pu):
        """

        :param lvl: lvl to display
        :param items_pu: object pickup
        :return: Display pygame
        """

        self.window.blit(self.background, (0, 0))
        # Title
        pygame.display.set_caption(constances.TITLE_GAME)

        # We browse the list of the structure (horizontal line)
        for num_line, line in enumerate(lvl.structure):
            # We browse the caracters of the line (vertical line)
            mapping = {"m": self.wall, "d": self.mg_icon, "MG": self.mg_icon, "A": self.aiguille_icon,
                       "E": self.ether_icon, "T": self.tube_icon, "a": self.guardian }

            for num_case, sprite in enumerate(line):
                # We calcultate the position in px
                x = num_case * constances.SIZE_SPRITE
                y = num_line * constances.SIZE_SPRITE
                try:
                    self.window.blit(mapping[sprite], (x, y))
                except KeyError:
                    pass
        self.display_object_pu(items_pu)

    def display_object_pu(self, items):
        '''

        :param items:
        :return:
        '''
        red = (125, 13, 43)
        font = pygame.font.SysFont("comicsansms", 30)
        text = font.render("Liste des objets: ", True, red)
        textRect = text.get_rect()
        textRect.center = (90, constances.SIZE_WINDOW + 70)
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



