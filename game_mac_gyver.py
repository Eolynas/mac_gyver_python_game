# -*- coding: utf-8 -*-

import pygame
from pygame.locals import *

import MacGyver
import display
import level as lvl
import items
import Endgame


def main():

    # Initialisation lvl
    level_1 = lvl.Level("config/level_1.txt")

    # init mac gyver en ligne de commande
    mac_gyver = MacGyver.MacGyver(level_1)

    # Initialisation de l'items
    items_1 = items.Items(level_1, "aiguille")
    items_1.generate_object()

    items_2 = items.Items(level_1, "ether")
    items_2.generate_object()

    items_3 = items.Items(level_1, "tube")
    items_3.generate_object()

    # ####### FENETRE ####### #
    display_windows = display.Display()
    display_windows.display(level_1, mac_gyver.objects)

    pygame.display.flip()

    while True:
        """
        Gestion de la boucle / event avec pygame
        """
        # Limitation de vitesse de la boucle
        pygame.time.Clock().tick(30)

        event = pygame.event.wait()

        # Fermeture du jeux si on appui sur la croix ou E
        if event.type == QUIT or (
                event.type == KEYDOWN and event.key == K_e):  # Si un de ces événements est de type QUIT
            break # On arrête la boucle

        elif event.type == KEYDOWN:
            # Deplacement vers la droite
            if event.key == K_RIGHT:
                answer = mac_gyver.move("right")
                if answer == "W":
                    Endgame.end_game("VOUS AVEZ GAGNE")
                    break
                if answer == "L":
                    Endgame.end_game("VOUS AVEZ PERDU")
                    break

            # Deplacement vers la gauche
            elif event.key == K_LEFT:
                answer = mac_gyver.move("left")
                if answer == "W":
                    Endgame.end_game("VOUS AVEZ GAGNE")
                    break
                if answer == "L":
                    Endgame.end_game("VOUS AVEZ PERDU")
                    break
            # Deplacement vers le haut
            elif event.key == K_UP:
                answer = mac_gyver.move("up")
                if answer == "W":
                    Endgame.end_game("VOUS AVEZ GAGNE")
                    break
                if answer == "L":
                    Endgame.end_game("VOUS AVEZ PERDU")
                    break
            # Deplacement vers le bas
            elif event.key == K_DOWN:
                answer = mac_gyver.move("down")
                if answer == "W":
                    Endgame.end_game("VOUS AVEZ GAGNE")
                    break
                if answer == "L":
                    Endgame.end_game("VOUS AVEZ PERDU")
                    break

            elif event.key == K_o:
                mac_gyver.move("objects")

        # Re-collage
        display_windows.display(level_1, mac_gyver.objects)

        # Rafraichissement
        pygame.display.flip()


if __name__ == '__main__':
    main()