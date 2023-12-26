import pygame
from .colors import white, black, red, light_pink
from .settings import ChooseMode, ChooseColor, ChooseMeal, ChooseSIngleOrTwo
from .game_for_two import GameForTwo
from .game_for_one import GameForOne


class Game:
    def __init__(self, width, height, block_size, win_score, time, snake_colour_1, snake_colour_2, background_colour,
                 meal_pic, amount_of_players, scores_table, level):
        """sets the initial position of game parameters.
        Args:
            self (Game): an instance of the class.
            width (int): width of the screen.
            height (int): height of the screen.
            block_size (int): block size.
            win_score (int): amount of points needed to win..
            time (int): regulates game speed.
            snake_colour_1 (colors): color of the first snake.
            snake_colour_1 (colors): color of the first snake.
            background_colour (colors): color of the background.
            meal_pic (str): picture of selected meal.
            amount_of_players (int): amount of players.
            scores_table (list): scores table.
            level (int): current level.
        Returns:
            None.
        """
        # Размеры окна
        self.width = width
        self.height = height
        # Размер блока
        self.block_size = block_size
        # Очки на победу
        self.win_score = win_score
        # Создание окнаы
        self.screen = pygame.display.set_mode((width, height))
        # Заголовок окна
        pygame.display.set_caption("Snake Game")
        # Скорость
        self.time = time
        # Цвет змеек
        self.snake_colour_1 = snake_colour_1
        self.snake_colour_2 = snake_colour_2
        # Цвет фона
        self.background_colour = background_colour
        # Коэффициенты для шрифтов
        self.k = width / 500
        self.k_h = height / 500
        # Картинка для еды
        self.meal_pic = meal_pic
        # Количество игроков
        self.amount_of_players = amount_of_players
        # Таблица рекордов
        self.scores_table = scores_table
        # уровень в одиночном режиме
        self.level = level
        # Пауза
        self.pause = False


# Инициализация Pygame
pygame.init()


# Основной цикл игры
def gameLoop(flag):
    """starts the game.
    Args:
        flag (bool): True, if new game started. False, otherwise.
    Returns:
        None.
    """
    if flag == 0:
        # Создаем игру

        # ширина экрана, высота экрана, размер блоков, очки для победы, скорость, змея 1, змея 2, фон, еда, количество игроков, таблица рекордов, пауза
        game = Game(750, 750, 30, 60, 11, black, black, light_pink, 0, 2, [0, 0, 0], 1)
        game.screen.fill(game.background_colour)

        # Кнопки
        ChooseSIngleOrTwo(game)
        ChooseColor(game)
        ChooseMeal(game)
        ChooseMode(game)

    else:
        game = flag

    if game.amount_of_players == 2:
        GameForTwo(game)
    elif game.amount_of_players == 1:
        GameForOne(game)
