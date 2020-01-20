# -*- coding: utf-8 -*-
import pygame

import constances


class Level:
    """
    level creation
    """

    def __init__(self, file):
        """
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
        level creation
        :return: structure level
        """
        # Open file for create lvl
        with open(self.file, "r") as file:
            level_structure = []
            for line in file:
                line_structure = []
                for sprite in line:
                    if sprite != '\n':
                        line_structure.append(sprite)
                level_structure.append(line_structure)
            self.structure = level_structure

