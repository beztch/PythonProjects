import pygame
from .snake import Snake
from .blocks import Blocks
from .colors import white, black, red, light_pink
from .message import message_to_screen, central_message_to_screen
from .meal import Meal

# Одиночный режим
def GameForOne(game):
    """starts the single-player game.
    Args:
        game (Game): game parameters.
    Returns:
        None.
    """
    gameExit = False
    gameOver = False
    LevelUp = False
    # Слон
    elephant = pygame.transform.scale(pygame.image.load('./images/image.jpeg').convert_alpha(), (game.width, game.height))

    # Создаю еду
    meal = Meal(game.meal_pic, game)

    # Создаю препятствия
    blocks = Blocks(game)

    # Змея
    snake = Snake(game, game.snake_colour_1)
    snake.Draw()
    move = snake.Stay
    while not gameExit:

        while gameOver == True:

            if LevelUp == False:
                game.screen.blit(elephant, (0, 0))
                central_message_to_screen("Игра окончена", red, -95 * game.k, int(70 * game.k) + 1, game)
                central_message_to_screen("итоговый счет: " + str(snake.score), white, -65 * game.k,
                                          int(30 * game.k) + 1,
                                          game)
                central_message_to_screen("press C to play again, S for settings or Q to quit", white, -45 * game.k,
                                          int(20 * game.k) + 1, game)
                central_message_to_screen("таблица рекордов", white, 30, 30, game)
                central_message_to_screen(
                    str(game.scores_table[0]) + " " + str(game.scores_table[1]) + " " + str(game.scores_table[2]),
                    white,
                    50, 30, game)
                pygame.display.update()

            elif LevelUp == True:
                game.screen.blit(elephant, (0, 0))
                central_message_to_screen("Следующий уровень!", red, -95 * game.k, int(60 * game.k) + 1, game)
                central_message_to_screen("Этап: " + str(game.level), white, -65 * game.k,
                                          int(30 * game.k) + 1,
                                          game)
                central_message_to_screen("press C to play, S for settings or Q to quit", white, -45 * game.k,
                                          int(20 * game.k) + 1, game)
                pygame.display.update()

            # Обработка событий
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game.level = 1
                        gameExit = True
                        gameOver = False
                    if event.key == pygame.K_c:
                        if LevelUp == False:
                            if game.level > 1:
                                game.scores_table = [0, 0, 0]
                            game.level = 1
                        from .game import gameLoop
                        gameLoop(game)
                    elif event.key == pygame.K_s:
                        game.level = 1
                        from .game import gameLoop
                        gameLoop(0)

        # Обработка событий
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    if not (move == snake.Right and snake.length > 1):
                        move = snake.Left
                elif event.key == pygame.K_RIGHT:
                    if not (move == snake.Left and snake.length > 1):
                        move = snake.Right
                elif event.key == pygame.K_UP:
                    if not (move == snake.Down and snake.length > 1):
                        move = snake.Up
                elif event.key == pygame.K_DOWN:
                    if not (move == snake.Up and snake.length > 1):
                        move = snake.Down
                elif event.key == pygame.K_a:
                    if not (move == snake.Right and snake.length > 1):
                        move = snake.Left
                elif event.key == pygame.K_d:
                    if not (move == snake.Left and snake.length > 1):
                        move = snake.Right
                elif event.key == pygame.K_w:
                    if not (move == snake.Down and snake.length > 1):
                        move = snake.Up
                elif event.key == pygame.K_s:
                    if not (move == snake.Up and snake.length > 1):
                        move = snake.Down
                elif event.key == pygame.K_SPACE:
                    game.pause = True

        while game.pause:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        game.pause = False
                    if event.key == pygame.K_ESCAPE:
                        gameExit = True
        move()

        # Проверка на выход за границы окна
        if snake.lead_x >= game.width or snake.lead_x < 0 or snake.lead_y >= game.height or snake.lead_y < 0:
            if game.win_score < 61:
                game.scores_table.append(game.level)
            else:
                game.scores_table.append(snake.score)
            game.scores_table.sort(reverse=True)
            game.level = 1
            LevelUp = False
            gameOver = True

        game.screen.fill(game.background_colour)

        # Рисование препятствий
        blocks.Appear()

        # Рисование сыра
        meal.Draw()

        # Рисование змеи
        snake.Draw()

        # Вывод счета
        message_to_screen("score: " + str(snake.score), black, 30 * game.k, 30 * game.k_h, int(20 * game.k) + 1, game)

        # Обновление экрана
        pygame.display.update()

        # Проверка на самопересечение
        if snake.IsIntercept():
            if game.win_score < 61:
                game.scores_table.append(game.level)
            else:
                game.scores_table.append(snake.score)
            game.scores_table.sort(reverse=True)
            game.level = 1
            LevelUp = False
            gameOver = True

        # Проверка на препятствие
        if snake.IsBlock(blocks):
            if game.win_score < 61:
                game.scores_table.append(game.level)
            else:
                game.scores_table.append(snake.score)
            game.scores_table.sort(reverse=True)
            game.level = 1
            LevelUp = False
            gameOver = True

        # Проверка на съедание еды
        eat = snake.IsEat(meal)
        if eat:
            meal = Meal(game.meal_pic, game)
            while [meal.x, meal.y] in blocks.pos:
                meal = Meal(game.meal_pic, game)

        # Проверка на победителя
        if snake.score == game.win_score:
            if game.win_score > 61:
                game.scores_table.append(snake.score)
            game.scores_table.sort(reverse=True)
            LevelUp = True
            game.level += 1
            gameOver = True

        # Частота обновления экрана
        pygame.time.Clock().tick(game.time)

    # Закрытие Pygame
    pygame.quit()
