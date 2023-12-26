import random
from .colors import black
import pygame


class Blocks:
    pos = []
    amount = 0
    game = 0

    def __init__(self, game):
        """generates needed amount of blocks.
        Args:
            self (Blocks): an instance of the class.
            game (Game): game parameters.
        Returns:
            None.
        """
        self.pos = []
        self.game = game
        self.amount = game.level * 5 - 5
        for i in range(self.amount):
            x = round(random.randrange(0, game.width - game.block_size) / game.block_size) * game.block_size
            y = round(random.randrange(0, game.height - game.block_size) / game.block_size) * game.block_size
            while [x, y] in self.pos or [x, y] == [round((game.width / 2) / game.block_size) * game.block_size,
                                                   round((game.height / 2) / game.block_size) * game.block_size]:
                x = random.randint(0, self.game.width)
                y = random.randint(0, self.game.height)
            self.pos.append([x, y])

    # Рисование препятствия
    def Appear(self):
        """reflects the blocks on the screen.
        Args:
            game (Game): game parameters.
        Returns:
            None.
        """
        for rec in self.pos:
            pygame.draw.rect(self.game.screen, black,
                             [rec[0] + 0.1 * self.game.block_size, rec[1] + 0.1 * self.game.block_size,
                              self.game.block_size * 0.8, self.game.block_size * 0.8])
