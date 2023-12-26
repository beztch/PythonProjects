import pygame


class Button:
    center = [0, 0]
    size = [0, 0]
    game = 0
    colour = 0

    def __init__(self, filling, center, size, game, button_type):
        """generates button.
        Args:
            self (Button): an instance of the class.
            filling (colors): color of the button.
            center (list): center of the button.
            size (list): width and height of the buttton.
            game (Game): game parameters.
            button_type (str): type of button.
        Returns:
            None.
        """
        if button_type == "colour":
            self.colour = filling
            self.center = center
            self.size = size
            self.game = game
        elif button_type == "picture":
            self.image_scaled = pygame.transform.scale(filling, (size[0], size[1]))
            self.center = center
            self.size = size
            self.game = game

    # Рисование кнопки
    def Appear(self, button_type):
        """reflects the button on the screen.
        Args:
            self (Button): an instance of the class.
            button_type (str): type of button.
        Returns:
            None.
        """
        if button_type == "colour":
            pygame.draw.rect(self.game.screen, self.colour,
                             [self.center[0] - self.size[0] / 2, self.center[1] - self.size[1] / 2, self.size[0],
                              self.size[1]])
        elif button_type == "picture":
            self.game.screen.blit(self.image_scaled,
                                  (self.center[0] - self.size[0] / 2, self.center[1] - self.size[1] / 2))

    # Проверка на нажатие
    def Contain(self, pos):
        """checks if the button is pressed.
        Args:
            self (Button): an instance of the class.
            pos (tuple): position of mouse.
        Returns:
            bool: True, if button is pressed. False, otherwise.
        """
        return (abs(pos[0] - self.center[0]) < self.size[0] / 2) and (abs(pos[1] - self.center[1]) < self.size[1] / 2)
