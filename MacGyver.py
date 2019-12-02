# -*- coding: utf-8 -*-
import pygame
from pygame.locals import *
import constances
import level
import display


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
        self.name = "MG"
        self.objects = []
        # init mac gyver at position 0 0
        # self.mac_gyver = self.structure[0][0] = "MG"
        # MacGyver.display_structure(self)

    # def display_structure(self):
    #     for line in self.structure:
    #         print(line)
    #         # pass

    def display_mac_gyver(self):
        # level.Level.place_caractere(self, self.name, self.case_y, self.case_x)
        display.display_caractere(self.y, self.x)

    def move(self, move):
        # On recois la direction du move
        # On envoie la direction à la function condition_for_move pour savoir si on peux deplacer

        if move == "right":
            if self.case_x < (constances.number_sprite - 1):

                condition = self.structure[self.case_y][self.case_x + 1]
                if condition == "0":
                    self.structure[self.case_y][self.case_x] = "0"
                    self.case_x += 1
                    self.structure[self.case_y][self.case_x] = "MG"
                    # print("deplacement à droite")
                    # print(self.structure)
                    self.x = self.case_x * constances.size_sprite
                    # TODO: Affichage de MG en LDC (pourquoi mettre le SELF ??????)

                    # TODO: On fait appel à display pour gerer l'affichage de pygame

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
            if self.case_x > 0:
                condition = self.structure[self.case_y][self.case_x - 1]
                if condition == "0":
                    self.structure[self.case_y][self.case_x] = "0"
                    self.case_x -= 1
                    self.structure[self.case_y][self.case_x] = "MG"
                    # print("deplacement à droite")
                    # print(self.structure)
                    self.x = self.case_x * constances.size_sprite
                    print(self.x)
                    # MacGyver.display_structure(self)

        if move == "down":
            if self.case_y < (constances.number_sprite - 1):
                condition = self.structure[self.case_y + 1][self.case_x]
                if condition == "0":
                    self.structure[self.case_y][self.case_x] = "0"
                    self.case_y += 1
                    self.structure[self.case_y][self.case_x] = "MG"
                    # print("deplacement à droite")
                    # print(self.structure)
                    self.y = self.case_y * constances.size_sprite
                    print(self.x)
                    # MacGyver.display_structure(self)

        if move == "up":
            if self.case_y > 0:
                condition = self.structure[self.case_y - 1][self.case_x]
                if condition == "0":
                    self.structure[self.case_y][self.case_x] = "0"
                    self.case_y -= 1
                    self.structure[self.case_y][self.case_x] = "MG"
                    # print("deplacement à droite")
                    # print(self.structure)
                    self.y = self.case_y * constances.size_sprite
                    print(self.x)
                    # MacGyver.display_structure(self)


        if move == "objects":
            print("Mac gyver à les objets suivant: ", self.objects)
            # MacGyver.display_structure(self)

        print(str("Mac Gyver est à la possition x:{} et y:{}").format(self.case_x, self.case_y))


