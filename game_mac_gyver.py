# -*- coding: utf-8 -*-

import pygame
from pygame.locals import *

import MacGyver
import display
import level as lvl
import items


def main():

    # Initialisation lvl
    level_1 = lvl.Level("config/level_1.txt")
    # level_1.display_structure()
    # ########################################### #
    """
    Initialisation de pygame
    """

    # ####### MAC GYVER ####### #

    # Mac Gyver icon
    # init mac gyver en ligne de commande
    mac_gyver = MacGyver.MacGyver(level_1)

    # ###################### #

    # # ####### ITEMS ####### #
    # # Initialisation de l'items
    # TODO: Passer l'objet level pour faire la modif sur la structure
    items_1 = items.Items(level_1, "aiguille")
    items_1.generate_object()

    items_2 = items.Items(level_1, "ether")
    items_2.generate_object()

    items_3 = items.Items(level_1, "tube")
    items_3.generate_object()

    # ####### FENETRE ####### #
    display_windows = display.Display()
    display_windows.display(level_1, mac_gyver.objects)
    # ##################### #

    # ##################### #
    # TODO: Test display all
    # display.test_display_all()
    # display.display(level_1)
    # Rafraichissement de la fenetre
    pygame.display.flip()

    # ########################################### #

    # continuer = 1
    while True:
        # ########################################### #
        """
        Gestion de la boucle / event avec pygame
        """
        # Limitation de vitesse de la boucle
        pygame.time.Clock().tick(30)

        # On parcours tous les events
        # for event in pygame.event.get():  # On parcours la liste de tous les événements reçus
        #
        #     # Fermeture du jeux si on appui sur la croix ou E
        #     if event.type == QUIT or (
        #             event.type == KEYDOWN and event.key == K_e):  # Si un de ces événements est de type QUIT
        #         # display_windows.end_game()
        #         break # On arrête la boucle
        #
        #     elif event.type == KEYDOWN:
        #         # Deplacement vers la droite
        #         if event.key == K_RIGHT:
        #             answer = mac_gyver.move("right")
        #             # level_1.display_structure()
        #             # print(answer)
        #             if not answer:
        #                 break
        #
        #         # Deplacement vers la gauche
        #         elif event.key == K_LEFT:
        #             answer = mac_gyver.move("left")
        #             # level_1.display_structure()
        #             # print(answer)
        #             if not answer:
        #                 break
        #
        #         # Deplacement vers le haut
        #         elif event.key == K_UP:
        #             answer = mac_gyver.move("up")
        #             # level_1.display_structure()
        #             # print(answer)
        #             if not answer:
        #                 return False
        #
        #         # Deplacement vers le bas
        #         elif event.key == K_DOWN:
        #             answer = mac_gyver.move("down")
        #             # level_1.display_structure()
        #             # print("DOWN")
        #             # print(answer)
        #             if not answer:
        #                 return False
        #
        #         elif event.key == K_o:
        #             mac_gyver.move("objects")

        event = pygame.event.wait()

        # Fermeture du jeux si on appui sur la croix ou E
        if event.type == QUIT or (
                event.type == KEYDOWN and event.key == K_e):  # Si un de ces événements est de type QUIT
            # display_windows.end_game()
            break # On arrête la boucle

        elif event.type == KEYDOWN:
            # Deplacement vers la droite
            if event.key == K_RIGHT:
                answer = mac_gyver.move("right")
                # level_1.display_structure()
                # print(answer)
                if not answer:
                    break
            # Deplacement vers la gauche
            elif event.key == K_LEFT:
                answer = mac_gyver.move("left")
                # level_1.display_structure()
                # print(answer)
                if not answer:
                    break

            # Deplacement vers le haut
            elif event.key == K_UP:
                answer = mac_gyver.move("up")
                # level_1.display_structure()
                # print(answer)
                if not answer:
                    break

            # Deplacement vers le bas
            elif event.key == K_DOWN:
                answer = mac_gyver.move("down")
                # level_1.display_structure()
                # print("DOWN")
                # print(answer)
                if not answer:
                    break

            elif event.key == K_o:
                mac_gyver.move("objects")

        # Re-collage
        display_windows.display(level_1, mac_gyver.objects)

        # Rafraichissement
        pygame.display.flip()


    display_windows.end_game()


if __name__ == '__main__':
    main()