import random

class Meal:
    x = 0
    y = 0
    game = 0
    meal_pic = 0

    # Конструктор
    def __init__(self, meal_pic, game):
        """generates button.
        Args:
            self (Meal): an instance of the class.
            meal_pic (str): picture of the meal.
            game (Game): game parameters.
        Returns:
            None.
        """
        self.game = game
        self.x = round(random.randrange(0, game.width - game.block_size) / game.block_size) * game.block_size
        self.y = round(random.randrange(0, game.height - game.block_size) / game.block_size) * game.block_size
        self.meal_pic = meal_pic

    # Рисование еды
    def Draw(self):
        """reflects the meal on the screen.
        Args:
            self (Meal): an instance of the class.
        Returns:
            None.
        """
        self.game.screen.blit(self.meal_pic, (self.x, self.y))