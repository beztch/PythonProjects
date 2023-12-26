import pygame
from .colors import black


# Функции для вывода сообщения на экран
def message_to_screen(msg, color, x, y, size, game):
    """reflects message to screen.
    Args:
        msg (str): message text.
        color (colors): color of the text.
        x (int): x coordinate of the center.
        y (int): y coordinate of the center.
        size (int): size of the text.
        game (Game): parameters of the game.
    Returns:
        None.
    """
    font = pygame.font.SysFont(None, size)
    screen_text = font.render(msg, True, color)
    game.screen.blit(screen_text, [x, y])


def central_message_to_screen(msg, color, add_y, size, game):
    """reflects message to the center of the screen.
    Args:
        msg (str): message text.
        color (colors): color of the text.
        add_y (int): y coordinate of the center.
        size (int): size of the text.
        game (Game): parameters of the game.
    Returns:
        None.
    """
    font = pygame.font.SysFont(None, size)
    screen_text = font.render(msg, True, color)
    rect = screen_text.get_rect()
    rect.center = (game.width / 2, game.height / 2)
    game.screen.blit(screen_text, [rect.x, rect.y + add_y])


def DrawScores(snake_1, snake_2, game):
    """reflects actual scores of the players to screen.
    Args:
        snake_1 (Snake): first snake parameters.
        snake_2 (Snake): second snake parameters.
        game (Game): game parameters.
    Returns:
        None.
    """
    message_to_screen("snake 1: " + str(snake_1.score), black, 30 * game.k, 30 * game.k_h, int(20 * game.k) + 1, game)
    message_to_screen("snake 2: " + str(snake_2.score), black, game.width - 100 * game.k, 30 * game.k_h,
                      int(20 * game.k) + 1, game)
