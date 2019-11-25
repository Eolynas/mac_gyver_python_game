# -*- coding: utf-8 -*-
import random
import level

class ObjectsPickUp:
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
        # IMG
        self.image = ""
        # Name
        self.name = name
        # Structure
        self.structure = structure
        self.name_object = ""


    def generate_object(self):
        """
        Function for generate position for the objects at pick up
        :return:
        """
        while True:
            self.case_x = random.randint(0, 6)
            self.case_y = random.randint(0, 6)
            if self.structure[self.case_x][self.case_y] == "0":
                print("Création de l'objet", self.name, " à l'emplacement x:", self.case_x, " y:", self.case_y)
                self.name_object = self.name[0].upper()
                return self.name_object, self.case_x, self.case_y









