# -*- coding: utf-8 -*-


class Level:

    """
    level creation
    """
    variable = 0
    def __init__(self, file):
        """

        :param file: file for create level
        :type file: .txt
        """
        self.file = file
        self.structure = 0
        self.create_level()

    def create_level(self):
        """

        :return:
        """
        # Open file for create lvl
        with open(self.file, "r") as file:
            level_structure = []
            for line in file:
                line_structure = []
                for sprite in line:
                    # TODO: Expliquation sur le '\n'
                    if sprite != '\n':
                        line_structure.append(sprite)
                # print(line_structure)
                level_structure.append(line_structure)
            self.structure = level_structure
            # print(self.structure)



    #TODO: Recup valeur laby
    #TODO: Modifier la grille
