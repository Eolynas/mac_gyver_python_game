# -*- coding: utf-8 -*-

import pygame
from pygame.locals import *

import MacGyver
import Display
import level as lvl
import Items
import endgame

# TODO: REQUIREMENT.txt


def main():
    '''
    principal function for the game.
    She will take care of all pygame event of the games
    :return: Game
    '''

    # Init lvl
    level_1 = lvl.Level("config/level_1.txt")

    # init mac gyver command line
    mac_gyver = MacGyver.MacGyver(level_1)

    # Init item
    items_1 = Items.Items(level_1, "aiguille")
    items_1.generate_object()

    items_2 = Items.Items(level_1, "ether")
    items_2.generate_object()

    items_3 = Items.Items(level_1, "tube")
    items_3.generate_object()

    # ####### WINDOW ####### #
    display_windows = Display.Display()
    display_windows.display(level_1, mac_gyver.objects)

    pygame.display.flip()

    while True:
        # Loop speed limit
        pygame.time.Clock().tick(30)

        event = pygame.event.wait()

        # Close the game if u press E
        # if event.type == QUIT or (event.type == KEYDOWN and event.key == K_e):
        #     break

        if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
            break

        elif event.type == KEYDOWN:
            # Move right
            if event.key == K_RIGHT:
                answer = mac_gyver.move("right")
                if answer == "W":
                    endgame.end_game("VOUS AVEZ GAGNE")
                    break
                if answer == "L":
                    endgame.end_game("VOUS AVEZ PERDU")
                    break

            # Move left
            elif event.key == K_LEFT:
                answer = mac_gyver.move("left")
                if answer == "W":
                    endgame.end_game("VOUS AVEZ GAGNE")
                    break
                if answer == "L":
                    endgame.end_game("VOUS AVEZ PERDU")
                    break
            # Move top
            elif event.key == K_UP:
                answer = mac_gyver.move("up")
                if answer == "W":
                    endgame.end_game("VOUS AVEZ GAGNE")
                    break
                if answer == "L":
                    endgame.end_game("VOUS AVEZ PERDU")
                    break
            # Move down
            elif event.key == K_DOWN:
                answer = mac_gyver.move("down")
                if answer == "W":
                    endgame.end_game("VOUS AVEZ GAGNE")
                    break
                if answer == "L":
                    endgame.end_game("VOUS AVEZ PERDU")
                    break

        # Re-display
        display_windows.display(level_1, mac_gyver.objects)

        # refresh
        pygame.display.flip()


if __name__ == '__main__':
    main()