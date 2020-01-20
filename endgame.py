import pygame
import time


def end_game(message):
    """
    display the endgame message
    :param message: str: message end game
    :return: pygame (close after 5s)
    """
    pygame.init()

    white = (255, 255, 255)
    green = (0, 255, 0)
    red = (255, 0, 0)

    # assigning values to X and Y variable
    X = 400
    Y = 400

    # create the display surface object
    display_surface = pygame.display.set_mode((X, Y))

    # set the pygame window name
    pygame.display.set_caption('Fin de partie')

    # create a font object.
    font = pygame.font.Font('freesansbold.ttf', 32)

    # Condition for the message endgame
    if message == "VOUS AVEZ GAGNE":
        text = font.render(message, True, green)
    else:
        text = font.render(message, True, red)
    # create a rectangular object for the
    # text surface object
    textRect = text.get_rect()

    # set the center of the rectangular object.
    textRect.center = (X // 2, Y // 2)

    # infinite loop
    while True:

        display_surface.fill(white)
        display_surface.blit(text, textRect)
        pygame.display.update()

        time.sleep(5)

        break
