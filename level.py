# -*- coding: utf-8 -*-
import pygame
from pygame.locals import *
import constances


class Level:

    """
    level creation
    """

    def __init__(self, file):
        """

        :param file: file for create level
        :type file: .txt
        """
        self.file = file
        self.structure = []
        self.create_level()

    def create_level(self):
        """

        :return:
        """
        # Open file for create lvl
        with open(self.file, "r") as file:
            level_structure = []
            for line in file:
                line_structure = []
                for sprite in line:
                    # TODO: Expliquation sur le '\n'
                    if sprite != '\n':
                        line_structure.append(sprite)
                # print(line_structure)
                level_structure.append(line_structure)
            self.structure = level_structure
            # print(self.structure)

    def display(self, windows):
        wall = pygame.image.load(constances.img_wall)

        num_line = 0
        # On parcours les list de la structure (ligne horizontal)
        for line in self.structure:
            # On parcours les caracteres de la ligne (ligne vertical)
            num_case = 0
            for sprite in line:
                # On calcule la position en px
                x = num_case * constances.size_sprite
                y = num_line * constances.size_sprite
                if sprite == "m":
                    windows.blit(wall, (x, y))
                num_case += 1
            num_line += 1

    def place_object(self, items):
        case_x = items.case_x
        case_y = items.case_y
        name_object = items.name_object
        self.structure[case_x][case_y] = name_object

    #TODO: Recup valeur laby
    #TODO: Modifier la grille
