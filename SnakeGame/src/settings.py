from .message import central_message_to_screen
from .button import Button
import pygame
from .colors import black, white, blue, fuksia

# Выбор режима игры
def ChooseSIngleOrTwo(game):
    """selection between the single- and multi- player games.
    Args:
        game (Game): game parameters.
    Returns:
        None.
    """
    button_pressed = False
    game.screen.fill(game.background_colour)
    central_message_to_screen("Сколько будет игроков?", black, -game.height * 0.3, 40, game)
    button_one = Button(pygame.image.load('./images/one_snake.png'), [game.width / 4, game.height / 2],
                        [game.width * 0.45, game.width * 0.45], game, "picture")
    button_two = Button(pygame.image.load('./images/two_snakes.png'), [game.width * 3 / 4, game.height / 2],
                        [game.width * 0.45, game.width * 0.45], game, "picture")
    button_one.Appear("picture")
    button_two.Appear("picture")
    pygame.display.update()
    while not button_pressed:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_one.Contain(event.pos):
                    game.amount_of_players = 1
                    button_pressed = True
                if button_two.Contain(event.pos):
                    game.amount_of_players = 2
                    button_pressed = True


# Выбор цвета
def ChooseColor(game):
    """selection of the snake's colors.
    Args:
        game (Game): game parameters.
    Returns:
        None.
    """
    button_pressed = False
    button_white = Button(white, [game.width / 4, game.height / 4], [game.width / 8, game.height / 8], game, "colour")
    button_blue = Button(blue, [game.width * 3 / 4, game.height / 4], [game.width / 8, game.height / 8], game,
                          "colour")
    button_black = Button(black, [game.width / 4, game.height * 3 / 4], [game.width / 8, game.height / 8], game,
                          "colour")
    button_fuksia = Button(fuksia, [game.width * 3 / 4, game.height * 3 / 4], [game.width / 8, game.height / 8], game,
                           "colour")
    game.screen.fill(game.background_colour)
    button_white.Appear("colour")
    button_black.Appear("colour")
    button_blue.Appear("colour")
    button_fuksia.Appear("colour")
    if (game.amount_of_players == 1):
        central_message_to_screen("Выберите цвет змеи", black, 0, int(30 * game.k) + 1, game)
    else:
        central_message_to_screen("Выберите цвет первой змеи", black, 0, int(30 * game.k) + 1, game)
    pygame.display.update()
    while not button_pressed:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_white.Contain(event.pos):
                    game.snake_colour_1 = white
                    button_pressed = True
                elif button_blue.Contain(event.pos):
                    game.snake_colour_1 = blue
                    button_pressed = True
                elif button_black.Contain(event.pos):
                    game.snake_colour_1 = black
                    button_pressed = True
                elif button_fuksia.Contain(event.pos):
                    game.snake_colour_1 = fuksia
                    button_pressed = True
    button_pressed = False
    game.screen.fill(game.background_colour)
    button_white.Appear("colour")
    button_black.Appear("colour")
    button_blue.Appear("colour")
    button_fuksia.Appear("colour")
    if (game.amount_of_players == 2):
        central_message_to_screen("Выберите цвет второй змеи", black, 0, int(30 * game.k) + 1, game)
        pygame.display.update()
        while not button_pressed:
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if button_white.Contain(event.pos):
                        game.snake_colour_2 = white
                        button_pressed = True
                    elif button_blue.Contain(event.pos):
                        game.snake_colour_2 = blue
                        button_pressed = True
                    elif button_black.Contain(event.pos):
                        game.snake_colour_2 = black
                        button_pressed = True
                    elif button_fuksia.Contain(event.pos):
                        game.snake_colour_2 = fuksia
                        button_pressed = True

# Выбор еды
def ChooseMeal(game):
    """selection of the meal.
    Args:
        game (Game): game parameters.
    Returns:
        None.
    """
    button_pressed = False
    # Создаем картинки
    game.screen.fill(game.background_colour)
    cheese_pic = pygame.transform.scale(pygame.image.load('./images/cheese.jpeg').convert_alpha(),
                                        (game.block_size, game.block_size))
    cheese_pic.set_colorkey((255, 255, 255))
    coffee_pic = pygame.transform.scale(pygame.image.load('./images/coffee.jpeg').convert_alpha(),
                                        (game.block_size, game.block_size))
    coffee_pic.set_colorkey((255, 255, 255))
    # Создаем кнопки
    button_cheese = Button(pygame.image.load('./images/cheese.jpeg'), [game.width / 3, game.height / 2],
                           [game.width / 3, game.height / 3], game, "picture")
    button_coffee = Button(pygame.image.load('./images/coffee.jpeg'), [game.width * 2 / 3, game.height / 2],
                           [game.width / 3, game.height / 3], game, "picture")
    button_cheese.Appear("picture")
    button_coffee.Appear("picture")
    # Надпись на экране
    central_message_to_screen("Выберите еду", black, -game.height / 4, int(30 * game.k) + 1, game)
    pygame.display.update()
    while not button_pressed:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_cheese.Contain(event.pos):
                    game.meal_pic = cheese_pic
                    button_pressed = True
                elif button_coffee.Contain(event.pos):
                    game.meal_pic = coffee_pic
                    button_pressed = True


# Выбор режима игры
def ChooseMode(game):
    """selection of the score needed to win.
    Args:
        game (Game): game parameters.
    Returns:
        None.
    """
    button_pressed = False
    game.screen.fill(game.background_colour)
    button_15 = Button(pygame.image.load('./images/15.png'), [game.width / 2, game.height * 2 / 6],
                       [game.width * 2 / 3, 50 * game.k], game, "picture")
    button_30 = Button(pygame.image.load('./images/30.png'), [game.width / 2, game.height * 3 / 6],
                       [game.width * 2 / 3, 50 * game.k], game, "picture")
    button_60 = Button(pygame.image.load('./images/60.png'), [game.width / 2, game.height * 4 / 6],
                       [game.width * 2 / 3, 50 * game.k], game, "picture")
    button_endless = Button(pygame.image.load('./images/endless.png'), [game.width / 2, game.height * 5 / 6],
                            [game.width * 7 / 8, 40 * game.k], game, "picture")
    central_message_to_screen("Выберите режим игры", black, -game.height * 2 / 6, int(50 * game.k), game)
    button_15.Appear("picture")
    button_30.Appear("picture")
    button_60.Appear("picture")
    button_endless.Appear("picture")
    pygame.display.update()
    while not button_pressed:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_15.Contain(event.pos):
                    game.win_score = 15
                    button_pressed = True
                elif button_30.Contain(event.pos):
                    game.win_score = 30
                    button_pressed = True
                elif button_60.Contain(event.pos):
                    game.win_score = 60
                    button_pressed = True
                elif button_endless.Contain(event.pos):
                    game.win_score = 10000
                    button_pressed = True
