# -*- coding: utf-8 -*-
import Items
import constances
import level


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

    def move(self, move):
        """
        Condition for move MacGyver
        :param move: move direction
        :return: New position if condition true
        """
        structure = self.instance_level.get_structure()
        new_position = ''
        if move == "right":
            if self.case_x < (constances.NUMBER_SPRITE - 1):
                new_position = structure[self.case_y][self.case_x + 1]
                if new_position != 'm' and self.case_x + 1 >= 0:
                    structure[self.case_y][self.case_x] = "0"
                    self.case_x += 1
                    structure[self.case_y][self.case_x] = "MG"
                    self.instance_level.setter_structure(structure)

                self.calculate_position(new_position)

        elif move == "left":
            if self.case_x < (constances.NUMBER_SPRITE - 1):
                new_position = structure[self.case_y][self.case_x - 1]
                if new_position != 'm' and self.case_x - 1 >= 0:
                    structure[self.case_y][self.case_x] = "0"
                    self.case_x -= 1
                    structure[self.case_y][self.case_x] = "MG"
                    self.instance_level.setter_structure(structure)

                self.calculate_position(new_position)

        elif move == "down":
            if self.case_y < (constances.NUMBER_SPRITE - 1):
                new_position = structure[self.case_y + 1][self.case_x]
                if new_position != 'm' and self.case_y + 1 >= 0:
                    structure[self.case_y][self.case_x] = "0"
                    self.case_y += 1
                    structure[self.case_y][self.case_x] = "MG"
                    self.instance_level.setter_structure(structure)

                self.calculate_position(new_position)

        elif move == "up":
            if self.case_y < (constances.NUMBER_SPRITE - 1):
                new_position = structure[self.case_y - 1][self.case_x]
                if new_position != 'm' and self.case_y - 1 >= 0:
                    structure[self.case_y][self.case_x] = "0"
                    self.case_y -= 1
                    structure[self.case_y][self.case_x] = "MG"
                    self.instance_level.setter_structure(structure)

                self.calculate_position(new_position)

        if new_position == "a":
            if len(self.objects) != 3:
                print("GAME OVER")
                return "L"
            else:
                print("FELICITATION VOUS AVEZ GAGNE")
                return "W"

    def calculate_position(self, position):
        """
        Calculate position for move function
        :param position:
        :return: new calculate position
        """
        if position == "0":
            self.y = self.case_y * constances.SIZE_SPRITE
        elif position == "T" or position == "A" or position == "E":
            # We add the objet at the list
            self.objects.append(Items.Items.pick_up_object(position))
