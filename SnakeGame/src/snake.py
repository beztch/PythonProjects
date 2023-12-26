import pygame


class Snake:
    score = 1
    length = 1
    lead_x = 0
    lead_y = 0
    game = 0
    colour = 0
    pos = [[lead_x, lead_y]]

   # Конструктор
    def __init__(self, game, colour):
        """sets the initial parameters of the snake.
        Args:
            self (Snake): an instance of the class.
            game (Game): game parameters.
            colour (colors): color of the snake.
        Returns:
            None.
        """
        self.game = game
        self.score = 1
        self.length = 1
        self.lead_x = round((game.width / 2) / game.block_size) * game.block_size
        self.lead_y = round((game.height / 2) / game.block_size) * game.block_size
        self.colour = colour
        self.pos = [[self.lead_x, self.lead_y]]

    def Stay(self):
        """leaves the snake on the place.
        Args:
            self (Snake): an instance of the class.
        Returns:
            None.
        """
        pass

    # Движение змейки
    def Left(self):
        """moves the snake to the left.
        Args:
            self (Snake): an instance of the class.
        Returns:
            None.
        """
        self.lead_x -= self.game.block_size
        self.pos.append([self.lead_x, self.lead_y])
        self.pos.pop(0)

    def Right(self):
        """moves the snake to the right.
        Args:
            self (Snake): an instance of the class.
        Returns:
            None.
        """
        self.lead_x += self.game.block_size
        self.pos.append([self.lead_x, self.lead_y])
        self.pos.pop(0)

    def Up(self):
        """moves the snake up.
        Args:
            self (Snake): an instance of the class.
        Returns:
            None.
        """
        self.lead_y -= self.game.block_size
        self.pos.append([self.lead_x, self.lead_y])
        self.pos.pop(0)

    def Down(self):
        """moves the snake down.
        Args:
            self (Snake): an instance of the class.
        Returns:
            None.
        """
        self.lead_y += self.game.block_size
        self.pos.append([self.lead_x, self.lead_y])
        self.pos.pop(0)

    # Рисование змейки
    def Draw(self):
        """reflects the meal on the screen.
        Args:
            self (Snake): an instance of the class.
        Returns:
            None.
        """
        for rec in self.pos:
            pygame.draw.rect(self.game.screen, self.colour,
                             [rec[0] + 0.1 * self.game.block_size, rec[1] + 0.1 * self.game.block_size,
                              self.game.block_size * 0.8, self.game.block_size * 0.8])

    # Проверка на съедение змейкой лакомств
    def IsEat(self, meal):
        """checks if the meal is eaten.
        Args:
            self (Snake): an instance of the class.
            meal (Meal): parameters of the current meal.
        Returns:
            bool: True, if meal is eaten. False, otherwise.
        """
        if self.lead_x == meal.x and self.lead_y == meal.y:
            self.score += 1
            pygame.display.update()
            self.length += 1
            self.pos.insert(0, [0, 0])
            return True
        return False

    # Проверка на врезание в препятствие
    def IsBlock(self, blocks):
        """checks if the snake has met the block.
        Args:
            self (Snake): an instance of the class.
            blocks (Blocks): parameters of the current position of the blocks.
        Returns:
            bool: True, if snake has met the blocks. False, otherwise.
        """
        if [self.lead_x, self.lead_y] in blocks.pos:
            return True
        return False

    # Проверка на самопересечение
    def IsIntercept(self):
        """checks if the snake has met itself.
        Args:
            self (Snake): an instance of the class.
        Returns:
            bool: True, if snake has met itself. False, otherwise.
        """
        tale = self.pos.copy()
        tale.pop()
        if [self.lead_x, self.lead_y] in tale:
            return True
        return False
