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

    def get_structure(self):
        return self.structure

    def setter_structure(self, structure):
        self.structure = structure

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
                level_structure.append(line_structure)
            self.structure = level_structure

    def display(self, windows):
        wall = pygame.image.load(constances.img_wall)

        num_line = 0
        # We browse the list of the structure (horizontal line)
        for line in self.structure:
            # We browse the caracters of the line (vertical line)
            num_case = 0
            for sprite in line:
                # We calculte the position in px
                x = num_case * constances.size_sprite
                y = num_line * constances.size_sprite
                if sprite == "m":
                    windows.blit(wall, (x, y))
                num_case += 1
            num_line += 1

    def display_structure(self):
        for line in self.structure:
            print(line)

    def place_caractere(self, name, case_y, case_x):
        self.structure[case_y][case_x] = name
        Level.display_structure(self)

    def place_item(self, name_item, case_y, case_x):
        self.structure[case_x][case_y] = name_item
        Level.display_structure(self)

    def update_structure(self, x, y):
        return self.structure[y][x]
