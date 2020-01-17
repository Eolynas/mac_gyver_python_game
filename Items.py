# -*- coding: utf-8 -*-
import random

import constances


class Items:
    """
    creating objects to pick up
    """

    def __init__(self, level, name):
        """

        """
        # Instance level object
        self.instance_level = level
        # Line horizontal
        # self.case_x = ""
        # # Line vertical
        # self.case_y = ""
        self.x = 0
        self.y = 0
        # IMG
        name_image = str("constances.images/img_" + name + ".png")
        # print(name_image)
        self.image = name_image
        # Name
        self.name = name
        self.name_object = ""

    def generate_object(self):
        """
        Function for generate position for the objects at pick up
        :return:
        """
        # Getter pour recup la structure
        structure = self.instance_level.get_structure()
        while True:
            self.case_x = random.randint(0, 14)
            self.case_y = random.randint(0, 14)
            # If not wall
            if structure[self.case_y][self.case_x] == "0":
                print("Création de l'objet", self.name, " à l'emplacement x:", self.case_x, " y:", self.case_y)
                self.name_object = self.name[0].upper()
                structure[self.case_y][self.case_x] = self.name_object
                # print(self.structure)
                self.x = self.case_x * constances.size_sprite
                self.y = self.case_y * constances.size_sprite
                # TODO: On envoie les coordonnées à la class level qui gere l'affichage en ligne de commande
                self.instance_level.setter_structure(structure)

                break

    @staticmethod
    def pick_up_object(object_pu: str):

        if object_pu == "A":
            return "Aiguille"
        elif object_pu == "E":
            return "Ether"
        elif object_pu == "T":
            return "Tube"
