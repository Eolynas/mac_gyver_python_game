# -*- coding: utf-8 -*-
import pygame
from pygame.locals import *
import constances
import level
import display
import items


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

    def display_mac_gyver(self, my_dysplay: display.Display):
        # level.Level.place_caractere(self, self.name, self.case_y, self.case_x)
        my_dysplay.display_caractere(self.y, self.x)
        # display.display_caractere(self.y, self.x)

    def move(self, move):
        # On recois la direction du move
        # On envoie la direction à la function condition_for_move pour savoir si on peux deplacer
        structure = self.instance_level.get_structure()
        if move == "right":
            if self.case_x < (constances.number_sprite - 1):
                # structure = self.instance_level.get_structure()
                new_position = structure[self.case_y][self.case_x + 1]
                if new_position == "0":
                    structure[self.case_y][self.case_x] = "0"
                    self.case_x += 1
                    structure[self.case_y][self.case_x] = "MG"
                    # TODO: Setter pour modif la structure
                    self.instance_level.setter_structure(structure)
                    return True

                # Condition for items
                elif new_position == "T" or new_position == "A" or new_position == "E":
                    print(new_position)
                    structure[self.case_y][self.case_x] = "0"
                    self.case_x += 1
                    structure[self.case_y][self.case_x] = "MG"
                    self.instance_level.setter_structure(structure)

                    # On ajoute l'objet ramasé à la liste
                    self.objects.append(items.Items.pick_up_object(new_position))
                    return True

                elif new_position == "a":
                    if len(self.objects) != 3:
                        print("GAME OVER")
                        return "L"
                    else:
                        print("FELICITATION VOUS AVEZ GAGNE")
                        return "W"
            return True

        if move == "left":
            if self.case_x > 0:
                new_position = structure[self.case_y][self.case_x - 1]
                if new_position == "0":
                    structure[self.case_y][self.case_x] = "0"
                    self.case_x -= 1
                    structure[self.case_y][self.case_x] = "MG"

                    # TODO: Setter pour modif la structure
                    self.instance_level.setter_structure(structure)
                    # print("deplacement à droite")
                    # print(self.structure)
                    self.x = self.case_x * constances.size_sprite
                    # print(self.x)
                    return True

                elif new_position == "T" or new_position == "A" or new_position == "E":
                    structure[self.case_y][self.case_x] = "0"
                    self.case_x -= 1
                    structure[self.case_y][self.case_x] = "MG"
                    self.instance_level.setter_structure(structure)

                    # On ajoute l'objet ramasé à la liste
                    self.objects.append(items.Items.pick_up_object(new_position))
                    return True

                elif new_position == "a":
                    if len(self.objects) != 3:
                        print("GAME OVER")
                        return False
                    else:
                        print("FELICITATION VOUS AVEZ GAGNEZ")
                        return False
            return True

        if move == "down":
            if self.case_y < (constances.number_sprite - 1):
                new_position = structure[self.case_y + 1][self.case_x]
                if new_position == "0":
                    structure[self.case_y][self.case_x] = "0"
                    self.case_y += 1
                    structure[self.case_y][self.case_x] = "MG"

                    # TODO: Setter pour modif la structure
                    self.instance_level.setter_structure(structure)
                    # print("deplacement à droite")
                    # print(self.structure)
                    self.y = self.case_y * constances.size_sprite
                    # print(self.x)
                    return True

                elif new_position == "T" or new_position == "A" or new_position == "E":
                    structure[self.case_y][self.case_x] = "0"
                    self.case_y += 1
                    structure[self.case_y][self.case_x] = "MG"
                    self.instance_level.setter_structure(structure)

                    # On ajoute l'objet ramasé à la liste
                    self.objects.append(items.Items.pick_up_object(new_position))
                    return True

                elif new_position == "a":
                    if len(self.objects) != 3:
                        print("GAME OVER")
                        return False
                    else:
                        print("FELICITATION VOUS AVEZ GAGNEZ")
                        return False
            return True

        if move == "up":
            if self.case_y > 0:
                new_position = structure[self.case_y - 1][self.case_x]
                if new_position == "0":
                    structure[self.case_y][self.case_x] = "0"
                    self.case_y -= 1
                    structure[self.case_y][self.case_x] = "MG"

                    # TODO: Setter pour modif la structure
                    self.instance_level.setter_structure(structure)
                    # print("deplacement à droite")
                    # print(self.structure)
                    self.y = self.case_y * constances.size_sprite
                    # print(self.x)
                    return True

                elif new_position == "T" or new_position == "A" or new_position == "E":
                    structure[self.case_y][self.case_x] = "0"
                    self.case_y -= 1
                    structure[self.case_y][self.case_x] = "MG"
                    self.instance_level.setter_structure(structure)

                    # On ajoute l'objet ramasé à la liste
                    self.objects.append(items.Items.pick_up_object(new_position))
                    return True

                elif new_position == "a":
                    if len(self.objects) != 3:
                        print("GAME OVER")
                        return False
                    else:
                        print("FELICITATION VOUS AVEZ GAGNER")
                        return False
            return True

        if move == "objects":
            print("Liste des objets que Mac Gyver à ramasé")
            for object in self.objects:
                print(object)

        # print(str("Mac Gyver est à la possition x:{} et y:{}").format(self.case_x, self.case_y))


