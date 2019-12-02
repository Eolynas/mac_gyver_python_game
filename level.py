# -*- coding: utf-8 -*-
import pygame

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

    def display_structure(self):
        for line in self.structure:
            print(line)
            # pass

    def place_caractere(self, name, case_y, case_x):
        self.structure[case_y][case_x] = name
        Level.display_structure(self)

    def place_item(self, name_item, case_y, case_x):
        # case_x = items.case_x
        # case_y = items.case_y
        # name_object = items.name_object
        print("y: ", case_y)
        print("x: ", case_x)
        self.structure[case_x][case_y] = name_item
        Level.display_structure(self)

    # TODO: Recup valeur laby
    # TODO: Modifier la grille
