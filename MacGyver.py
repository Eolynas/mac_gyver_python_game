# -*- coding: utf-8 -*-
import pygame
from pygame.locals import *
import constances


class MacGyver:
    """
    Mac Gyver move
    """

    def __init__(self, structure):
        self.structure = structure
        # Line horizontal
        self.case_x = 0
        # Line vertical
        self.case_y = 0
        self.x = 0
        self.y = 0
        self.objects = []
        # init mac gyver at position 0 0
        self.mac_gyver = self.structure[0][0] = "MG"
        MacGyver.display_structure(self)

    def display_structure(self):
        for line in self.structure:
            print(line)
            # pass

    def move(self, move):
        # On recois la direction du move
        # On envoie la direction à la function condition_for_move pour savoir si on peux deplacer

        if move == "right":
            condition = self.structure[self.case_y][self.case_x + 1]
            if self.case_x < (constances.number_sprite - 1):

                if condition == "0":
                    self.structure[self.case_y][self.case_x] = "0"
                    self.case_x += 1
                    print("41: case_x: ", self.case_x)
                    print("42: case_y: ", self.case_y)
                    self.structure[self.case_y][self.case_x] = "MG"
                    # print("deplacement à droite")
                    # print(self.structure)
                    self.x = self.case_x * constances.size_sprite
                    print(self.x)
                    MacGyver.display_structure(self)
                    # return True

                # if condition == "T" or condition == "A" or condition == "E":
                #     self.structure[self.case_y][self.case_x] = "0"
                #     self.case_y = self.case_y + 1
                #     self.structure[self.case_y][self.case_x] = "MG"
                #     print("Mac_Gyver viens de ramasser un object")
                #     self.objects.append("Tube")
                #     MacGyver.display_structure(self)
                # elif condition == "m":
                #     print("deplacement impossible")

        if move == "left":
            condition = self.structure[self.case_y][self.case_x - 1]
            if self.case_x > 0:
                if condition == "0":
                    self.structure[self.case_y][self.case_x] = "0"
                    self.case_x -= 1
                    self.structure[self.case_y][self.case_x] = "MG"
                    # print("deplacement à droite")
                    # print(self.structure)
                    self.x = self.case_x * constances.size_sprite
                    print(self.x)
                    MacGyver.display_structure(self)

        if move == "down":
            condition = self.structure[self.case_y + 1][self.case_x]
            if self.case_y < (constances.number_sprite - 1):
                if condition == "0":
                    self.structure[self.case_y][self.case_x] = "0"
                    self.case_y += 1
                    self.structure[self.case_y][self.case_x] = "MG"
                    # print("deplacement à droite")
                    # print(self.structure)
                    self.y = self.case_y * constances.size_sprite
                    print(self.x)
                    MacGyver.display_structure(self)

        if move == "up":
            condition = self.structure[self.case_y - 1][self.case_x]
            if self.case_y > 0:
                if condition == "0":
                    self.structure[self.case_y][self.case_x] = "0"
                    self.case_y -= 1
                    self.structure[self.case_y][self.case_x] = "MG"
                    # print("deplacement à droite")
                    # print(self.structure)
                    self.y = self.case_y * constances.size_sprite
                    print(self.x)
                    MacGyver.display_structure(self)

        if move == "up":
            condition = self.structure[self.case_x - 1][self.case_y]
            if condition == "0":
                self.structure[self.case_y][self.case_x] = "0"
                self.case_x = self.case_x - 1
                self.structure[self.case_y][self.case_x] = "MG"
                MacGyver.display_structure(self)
            if condition == "T":
                self.structure[self.case_y][self.case_x] = "0"
                self.case_x = self.case_x - 1
                self.structure[self.case_y][self.case_x] = "MG"
                MacGyver.display_structure(self)
                print("Mac_Gyver viens de ramasser un TUBE")
                self.objects.append("Tube")
                MacGyver.display_structure(self)
            elif condition == "m":
                print("deplacement impossible")
        if move == "objects":
            print("Mac gyver à les objets suivant: ", self.objects)
            MacGyver.display_structure(self)

        print(str("Mac Gyver est à la possition x:{} et y:{}").format(self.case_x, self.case_y))


