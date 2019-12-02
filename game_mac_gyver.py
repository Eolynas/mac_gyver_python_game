# -*- coding: utf-8 -*-

import pygame
from pygame.locals import *

import MacGyver
import display
import level as lvl
import items

# Initialisation lvl
level_1 = lvl.Level("config/level_1.txt")

# ########################################### #
"""
Initialisation de pygame
"""
# ####### FENETRE ####### #
display.display(level_1)
# ##################### #

# ####### MAC GYVER ####### #

# Mac Gyver icon
# init mac gyver en ligne de commande
mac_gyver = MacGyver.MacGyver(level_1.structure)
mac_gyver.display_mac_gyver()

# ###################### #

# # ####### ITEMS ####### #
# # Initialisation de l'items
items_1 = items.Items(level_1.structure, "aiguille")
items_1.generate_object()
items_1.display_aiguille()

items_2 = items.Items(level_1.structure, "ether")
items_2.generate_object()
items_2.display_ether()

items_3 = items.Items(level_1.structure, "tube")
items_3.generate_object()
items_3.display_ether()

# items_aiguille = items.Items(level_1.structure, "aiguille")
# # Génération de l'item 1
# items_aiguille.generate_object()
# # #### PYGAME #### #
# # items_1_icon = pygame.image.load(constances.img_aiguille).convert_alpha()
# # position_items_1 = (2, 0)
# # window.blit(items_1_icon, position_items_1)

# ##################### #
# TODO: Test display all
# display.test_display_all()
# display.display(level_1)
# Rafraichissement de la fenetre
pygame.display.flip()

# ########################################### #

continuer = 1
while continuer:
    # ########################################### #
    """
    Gestion de la boucle / event avec pygame
    """
    # Limitation de vitesse de la boucle
    pygame.time.Clock().tick(30)

    # On parcours tous les events
    for event in pygame.event.get():  # On parcours la liste de tous les événements reçus
        # Fermeture du jeux si on appui sur la croix ou E
        if event.type == QUIT or (
                event.type == KEYDOWN and event.key == K_e):  # Si un de ces événements est de type QUIT
            continuer = 0  # On arrête la boucle

        elif event.type == KEYDOWN:
            # Deplacement vers la droite
            if event.key == K_RIGHT:
                mac_gyver.move("right")

            # Deplacement vers la gauche
            if event.key == K_LEFT:
                mac_gyver.move("left")

            # Deplacement vers le haut
            if event.key == K_UP:
                mac_gyver.move("up")

            # Deplacement vers le bas
            if event.key == K_DOWN:
                mac_gyver.move("down")
    # Re-collage
    display.display(level_1)
    mac_gyver.display_mac_gyver()

    items_1.display_aiguille()
    items_2.display_ether()
    items_3.display_tube()


    # Rafraichissement
    pygame.display.flip()
