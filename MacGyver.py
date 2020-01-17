# -*- coding: utf-8 -*-
import pygame
from pygame.locals import *
import constances
import level
import Display
import Items


class MacGyver:
    """
    Mac Gyver move
    """

    def __init__(self, my_level: level.Level):
        # self.structure = my_level.structure
        self.instance_level = my_level
        # Line horizontal
        self.case_x = 0
        # Line vertical
        self.case_y = 0
        self.x = 0
        self.y = 0
        self.name = "MG"
        self.objects = []

    # def display_mac_gyver(self, my_dysplay):
    #     my_dysplay.display_caractere(self.y, self.x)

    def move(self, move):
        structure = self.instance_level.get_structure()
        new_position = ''
        if move == "right":
            # if self.case_x < (constances.number_sprite - 1):
            #     new_position = structure[self.case_y][self.case_x + 1]
            #     if new_position == "0":
            #         structure[self.case_y][self.case_x] = "0"
            #         self.case_x += 1
            #         structure[self.case_y][self.case_x] = "MG"
            #         # TODO: Setter pour modif la structure
            #         self.instance_level.setter_structure(structure)
            #
            #     # Condition for items
            #     elif new_position == "T" or new_position == "A" or new_position == "E":
            #         # print(new_position)
            #         structure[self.case_y][self.case_x] = "0"
            #         self.case_x += 1
            #         structure[self.case_y][self.case_x] = "MG"
            #         self.instance_level.setter_structure(structure)
            #
            #         # On ajoute l'objet ramasé à la liste
            #         self.objects.append(Items.Items.pick_up_object(new_position))
            #         # return True

                    #####
                if self.case_x < (constances.number_sprite - 1):
                    new_position = structure[self.case_y][self.case_x + 1]
                    if new_position != 'm':
                        structure[self.case_y][self.case_x] = "0"
                        self.case_x += 1
                        structure[self.case_y][self.case_x] = "MG"
                        self.instance_level.setter_structure(structure)

                    self.calculate_position(new_position)

        elif move == "left":
            if self.case_x > 0:
                new_position = structure[self.case_y][self.case_x - 1]
                if new_position == "0":
                    structure[self.case_y][self.case_x] = "0"
                    self.case_x -= 1
                    structure[self.case_y][self.case_x] = "MG"

                    # TODO: Setter pour modif la structure
                    self.instance_level.setter_structure(structure)
                    self.x = self.case_x * constances.size_sprite
                    # return True

                elif new_position == "T" or new_position == "A" or new_position == "E":
                    structure[self.case_y][self.case_x] = "0"
                    self.case_x -= 1
                    structure[self.case_y][self.case_x] = "MG"
                    self.instance_level.setter_structure(structure)

                    # We add the objet at the list
                    self.objects.append(Items.Items.pick_up_object(new_position))
                    # return True

        elif move == "down":
            if self.case_y < (constances.number_sprite - 1):
                new_position = structure[self.case_y + 1][self.case_x]
                if new_position != 'm':
                    structure[self.case_y][self.case_x] = "0"
                    self.case_y += 1
                    structure[self.case_y][self.case_x] = "MG"
                    self.instance_level.setter_structure(structure)

                self.calculate_position(new_position)

                # if new_position == "0":
                #     self.y = self.case_y * constances.size_sprite
                #     # return True
                # elif new_position == "T" or new_position == "A" or new_position == "E":
                #     # We add the objet at the list
                #     self.objects.append(Items.Items.pick_up_object(new_position))
                #     # return True


        elif move == "up":
            if self.case_y > 0:
                new_position = structure[self.case_y - 1][self.case_x]
                if new_position == "0":
                    structure[self.case_y][self.case_x] = "0"
                    self.case_y -= 1
                    structure[self.case_y][self.case_x] = "MG"

                    # TODO: Setter pour modif la structure
                    self.instance_level.setter_structure(structure)
                    self.y = self.case_y * constances.size_sprite
                    # print(self.x)
                    return True

                elif new_position == "T" or new_position == "A" or new_position == "E":
                    structure[self.case_y][self.case_x] = "0"
                    self.case_y -= 1
                    structure[self.case_y][self.case_x] = "MG"
                    self.instance_level.setter_structure(structure)

                    # We add the objet at the list
                    self.objects.append(Items.Items.pick_up_object(new_position))
                    return True

        if new_position == "a":
            if len(self.objects) != 3:
                print("GAME OVER")
                return "L"
            else:
                print("FELICITATION VOUS AVEZ GAGNE")
                return "W"

        if move == "objects":
            print("Liste des objets que Mac Gyver à ramasé")
            for object in self.objects:
                print(object)

    def calculate_position(self, position):
        if position == "0":
            self.y = self.case_y * constances.size_sprite
            # return True
        elif position == "T" or position == "A" or position == "E":
            # We add the objet at the list
            self.objects.append(Items.Items.pick_up_object(position))
            # return True

