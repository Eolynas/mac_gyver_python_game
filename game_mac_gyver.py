import pygame
from pygame.locals import *

import MacGyver
import ObjectsPickUp
import constances
import level as lvl

# Initialisation lvl
level_1 = lvl.Level("config/level_1.txt")

# ########################################### #
"""
Initialisation de pygame
"""
# Init pygame
pygame.init()
# Display windows
windows = pygame.display.set_mode((constances.cote_fenetre, constances.cote_fenetre))
background = pygame.image.load(constances.background_game).convert()
windows.blit(background, (0, 0))
# Title
pygame.display.set_caption(constances.title_game)

# TODO: Test wall
level_1.display(windows)

# Mac Gyver icon
mg_icon = pygame.image.load(constances.mg_icon).convert_alpha()
position_mg = mg_icon.get_rect()
windows.blit(mg_icon, position_mg)

# Rafraichissement de la fenetre
pygame.display.flip()

# ########################################### #


# Initit object
# list_objects = ["aiguille", "tube", "ether"]
# object_1 = ObjectsPickUp.ObjectsPickUp(level_1.structure, "aiguille")
# object_1.generate_object()
# level_1.place_object(object_1)
#
# object_2 = ObjectsPickUp.ObjectsPickUp(level_1.structure, "tube")
# object_2.generate_object()
# level_1.place_object(object_2)
#
# object_3 = ObjectsPickUp.ObjectsPickUp(level_1.structure, "ether")
# object_3.generate_object()
# level_1.place_object(object_3)
# level_1.structure[position_x_object_1][position_y_object_1] = name_object_1
# print(level_1.structure)

# initit mac gyver
mac_gyver = MacGyver.MacGyver(level_1.structure)

# Boucle infinie
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
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_e):  # Si un de ces événements est de type QUIT
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
    windows.blit(background, (0, 0))
    windows.blit(mg_icon, (mac_gyver.x, mac_gyver.y))
    level_1.display(windows)
    # Rafraichissement
    pygame.display.flip()

    # ########################################### #




    # cmd = input('Utiliser ZQSD pour déplacer Mac_Gyver')
    #
    # if cmd == "z":
    #     # On fait monter MG
    #     mac_gyver.move("up")
    #     if mac_gyver.move("up"):
    #         print("GAGNE")
    #         break
    #
    # if cmd == "q":
    #     # On fait aller à droite MG
    #     mac_gyver.move("left")
    #
    # if cmd == "d":
    #     # On fait aller à gauche MG
    #     mac_gyver.move("right")
    #
    # if cmd == "s":
    #     # On fait descendre MG
    #     mac_gyver.move("down")
    #
    # if cmd == "o":
    #     mac_gyver.move("objects")
    # if cmd == "e":
    #     print("PARTIE TERMINEE")
    #     break

# #initit mac gyver
# mac_gyver = MacGyver.MacGyver(level_1.structure)
# mac_gyver.move("right")
# mac_gyver.move("right")
# mac_gyver.move("down")
# mac_gyver.move("right")
