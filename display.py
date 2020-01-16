# -*- coding: utf-8 -*-

import pygame
import time
import constances


class Display:
    # # ####### WINDOW ####### #

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
        # Display wall
        self.wall = pygame.image.load(constances.img_wall)

    def display(self, lvl, items_pu):
        """

        :param lvl: lvl to display
        :param items_pu: object pickup
        :return: Display pygame
        """

        self.window.blit(self.background, (0, 0))
        # Title
        pygame.display.set_caption(constances.title_game)

        # We browse the list of the structure (horizontal line)
        for num_line, line in enumerate(lvl.structure):
            # We browse the caracters of the line (vertical line)
            mapping = {"m": self.wall, "d": self.mg_icon, "MG": self.mg_icon, "A": self.aiguille_icon,
                       "E": self.ether_icon, "T": self.tube_icon, "a": self.guardian }

            for num_case, sprite in enumerate(line):
                # We calcultate the position in px
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



