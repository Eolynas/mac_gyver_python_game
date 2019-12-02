# -*- coding: utf-8 -*-

import pygame

import constances

# # ####### FENETRE ####### #
# # Init pygame
# pygame.init()
# # Display windows
# window = pygame.display.set_mode((constances.cote_fenetre, constances.cote_fenetre))
# # Display background
# background = pygame.image.load(constances.background_game).convert()
# window.blit(background, (0, 0))
# # Title
# pygame.display.set_caption(constances.title_game)
# # Title
# pygame.display.set_caption(constances.title_game)

# Init pygame
pygame.init()
# Display windows
window = pygame.display.set_mode((constances.cote_fenetre, constances.cote_fenetre))


def display(lvl):
    """

    :param lvl:
    :param mac_gyver:
    :param items:
    :param window:
    :return:
    """
    # ####### FENETRE ####### #
    # Display background
    background = pygame.image.load(constances.background_game).convert()
    window.blit(background, (0, 0))
    # Title
    pygame.display.set_caption(constances.title_game)
    # AFFICHAGE DES MURS
    wall = pygame.image.load(constances.img_wall)

    num_line = 0
    # On parcours les list de la structure (ligne horizontal)
    for line in lvl.structure:
        # On parcours les caracteres de la ligne (ligne vertical)
        num_case = 0
        for sprite in line:
            # On calcule la position en px
            x = num_case * constances.size_sprite
            y = num_line * constances.size_sprite
            if sprite == "m":
                window.blit(wall, (x, y))
            num_case += 1
        num_line += 1


def display_caractere(y, x):
    # AFFICHAGE DE MAC GYVER
    mg_icon = pygame.image.load(constances.mg_icon).convert_alpha()
    position_mg = (x, y)
    window.blit(mg_icon, position_mg)


def display_aiguille(y, x):
    # AFFICHAGE DE ITEM_1
    item_icon = pygame.image.load(constances.img_aiguille).convert_alpha()
    position_item = (x, y)
    window.blit(item_icon, position_item)

def display_ether(y, x):
    # AFFICHAGE DE ITEM_2
    item_icon = pygame.image.load(constances.img_ether).convert_alpha()
    position_item = (x, y)
    window.blit(item_icon, position_item)

def display_tube(y, x):
    # AFFICHAGE DE ITEM_2
    item_icon = pygame.image.load(constances.img_tube).convert_alpha()
    position_item = (x, y)
    window.blit(item_icon, position_item)


