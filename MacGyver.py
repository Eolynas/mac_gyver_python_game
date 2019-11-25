# -*- coding: utf-8 -*-


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
        self.objects = []
        # init mac gyver at position 0 0
        self.mac_gyver = self.structure[0][0] = "MG"
        MacGyver.display_structure(self)

    def display_structure(self):
        for line in self.structure:
            print(line)

    def move(self, move):
        # On recois la direction du move
        # On envoie la direction à la function condition_for_move pour savoir si on peux deplacer
        # SI condition_for_move == True

        if move == "right":
            condition = self.structure[self.case_x][self.case_y + 1]
            if condition == "0":
                self.structure[self.case_x][self.case_y] = "0"
                self.case_y = self.case_y + 1
                self.structure[self.case_x][self.case_y] = "MG"
                print("deplacement à droite")
                # print(self.structure)
                MacGyver.display_structure(self)
            if condition == "T" or condition == "A" or condition == "E":
                self.structure[self.case_x][self.case_y] = "0"
                self.case_y = self.case_y + 1
                self.structure[self.case_x][self.case_y] = "MG"
                print("Mac_Gyver viens de ramasser un object")
                self.objects.append("Tube")
                MacGyver.display_structure(self)
            elif condition == "m":
                print("deplacement impossible")

        if move == "left":
            condition = self.structure[self.case_x][self.case_y - 1]
            if condition == "0":
                self.structure[self.case_x][self.case_y] = "0"
                self.case_y = self.case_y - 1
                self.structure[self.case_x][self.case_y] = "MG"
                print("deplacement à droite")
                # print(self.structure)
                MacGyver.display_structure(self)
            if condition == "T":
                self.structure[self.case_x][self.case_y] = "0"
                self.case_y = self.case_y - 1
                self.structure[self.case_x][self.case_y] = "MG"
                print("Mac_Gyver viens de ramasser un TUBE")
                self.objects.append("Tube")
                MacGyver.display_structure(self)
            elif condition == "m":
                print("deplacement impossible")

        if move == "down":
            condition = self.structure[self.case_x + 1][self.case_y]
            if condition == "0":
                self.structure[self.case_x][self.case_y] = "0"
                self.case_x = self.case_x + 1
                self.structure[self.case_x][self.case_y] = "MG"
                print("deplacement en bas")
                MacGyver.display_structure(self)
            if condition == "T":
                self.structure[self.case_x][self.case_y] = "0"
                self.case_x = self.case_x + 1
                self.structure[self.case_x][self.case_y] = "MG"
                print("Mac_Gyver viens de ramasser un TUBE")
                self.objects.append("Tube")
                MacGyver.display_structure(self)
            elif condition == "m":
                print("deplacement impossible")

        if move == "up":
            condition = self.structure[self.case_x - 1][self.case_y]
            if condition == "0":
                self.structure[self.case_x][self.case_y] = "0"
                self.case_x = self.case_x - 1
                self.structure[self.case_x][self.case_y] = "MG"
                MacGyver.display_structure(self)
            if condition == "T":
                self.structure[self.case_x][self.case_y] = "0"
                self.case_x = self.case_x - 1
                self.structure[self.case_x][self.case_y] = "MG"
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

    def condition_for_move(self, direction):
        """
        function for the condition to move Mac Gyver
        :param direction: direction  MG has to move
        :type direction: str
        :return: True or False
        """
        # On recois en parametre la direction du move
        # On regarde si la direction es possible
        ############ ON lui envoie les nouvelles coordonnée (ou on fait ca sur une autre function ????)
        condition = self.structure[self.case_x][self.case_y + 1]
        if condition == '0':
            # Si la destination n'est pas un mur alors on peux deplacer MG
            return True
        else:
            # On emet un message d'erreur
            return False

        pass


