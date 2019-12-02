# -*- coding: utf-8 -*-

import pygame

import constances


class Display:
    # # ####### FENETRE ####### #



    def __init__(self):

        # Init pygame
        pygame.init()
        # Display windows
        self.window = pygame.display.set_mode((constances.cote_fenetre, constances.cote_fenetre))

        self.mg_icon = pygame.image.load(constances.mg_icon).convert_alpha()
        self.aiguille_icon = pygame.image.load(constances.img_aiguille).convert_alpha()
        self.ether_icon = pygame.image.load(constances.img_ether).convert_alpha()
        self.tube_icon = pygame.image.load(constances.img_tube).convert_alpha()

    def display(self, lvl):
        """

        :param lvl:
        :param mac_gyver:
        :param items:
        :param window:
        :return:
        """
        # ####### FENETRE ####### #
        # Display background
        background = pygame.image.load(constances.background_game).convert()
        self.window.blit(background, (0, 0))
        # Title
        pygame.display.set_caption(constances.title_game)
        # AFFICHAGE DES MURS
        wall = pygame.image.load(constances.img_wall)

        num_line = 0
        # On parcours les list de la structure (ligne horizontal)
        for line in lvl.structure:
            # On parcours les caracteres de la ligne (ligne vertical)
            num_case = 0
            for sprite in line:
                # On calcule la position en px
                x = num_case * constances.size_sprite
                y = num_line * constances.size_sprite
                if sprite == "m":
                    self.window.blit(wall, (x, y))
                num_case += 1
            num_line += 1

    def display_caractere(self, y, x):
        # AFFICHAGE DE MAC GYVER

        # position_mg = mg_icon.get_rect()
        # position_mg.move(x, y)
        position_mg = (x, y)
        self.window.blit(self.mg_icon, position_mg)

    def display_aiguille(self, y, x):
        # AFFICHAGE DE ITEM_1
        # item_icon = pygame.image.load(constances.img_aiguille).convert_alpha()
        position_item = (x, y)
        self.window.blit(self.aiguille_icon, position_item)

    def display_ether(self, y, x):
        # AFFICHAGE DE ITEM_2
        # item_icon = pygame.image.load(constances.img_ether).convert_alpha()
        position_item = (x, y)
        self.window.blit(self.ether_icon, position_item)

    def display_tube(self, y, x):
        # AFFICHAGE DE ITEM_2
        # item_icon = pygame.image.load(constances.img_tube).convert_alpha()
        position_item = (x, y)
        self.window.blit(self.tube_icon, position_item)
