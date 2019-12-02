# -*- coding: utf-8 -*-
import random
import level
import pygame
from pygame.locals import *
import constances
import display


class Items:
    """
    creating objects to pick up
    """
    def __init__(self, structure, name):
        """

        """
        # Line horizontal
        self.case_x = ""
        # Line vertical
        self.case_y = ""
        self.x = 0
        self.y = 0
        # IMG
        name_image = str("constances.images/img_" + name + ".png")
        print(name_image)
        self.image = name_image
        # Name
        self.name = name
        # Structure
        self.structure = structure
        self.name_object = ""
        # Placement de l'objet sur la structure
        # self.generate_object()
        # self.items = self.structure[self.y][self.x]

    def generate_object(self):
        """
        Function for generate position for the objects at pick up
        :return:
        """
        while True:
            self.case_x = random.randint(0, 14)
            self.case_y = random.randint(0, 14)
            if self.structure[self.case_y][self.case_x] == "0":
                print("Création de l'objet", self.name, " à l'emplacement x:", self.case_x, " y:", self.case_y)
                self.name_object = self.name[0].upper()
                # self.structure[self.case_y][self.case_x] = self.name_object
                # print(self.structure)
                self.x = self.case_x * constances.size_sprite
                self.y = self.case_y * constances.size_sprite
                # TODO: On envoie les coordonnées à la class level qui gere l'affichage en ligne de commande
                # level.Level.place_item(self, self.name_object, self.case_y, self.case_x)

                # break
                # display.display_items(self.x, self.y)
                return self.name_object, self.image, self.case_y, self.case_x

    def display_aiguille(self, my_dysplay: display.Display):
        my_dysplay.display_aiguille(self.y, self.x)

    def display_ether(self, my_dysplay: display.Display):
        my_dysplay.display_ether(self.y, self.x)

    def display_tube(self, my_dysplay: display.Display):
        my_dysplay.display_tube(self.y, self.x)







