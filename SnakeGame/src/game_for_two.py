import pygame
from .snake import Snake
from .colors import white, black, red, light_pink
from .message import central_message_to_screen, DrawScores
from .meal import Meal

# Игра для двоих
def GameForTwo(game):
    """starts the multi-player game.
    Args:
        game (Game): game parameters.
    Returns:
        None.
    """
    gameExit = False
    gameOver = False
    # Слон
    elephant = pygame.transform.scale(pygame.image.load('./images/image.jpeg').convert_alpha(), (game.width, game.height))

    # Создаю еду
    meal = Meal(game.meal_pic, game)

    # Змеи
    snake_1 = Snake(game, game.snake_colour_1)
    snake_2 = Snake(game, game.snake_colour_2)
    snake_1.Draw()
    snake_2.Draw()
    move_1 = snake_1.Stay
    move_2 = snake_2.Stay
    loser = ""

    while not gameExit:

        while gameOver == True:
            game.screen.blit(elephant, (0, 0))
            central_message_to_screen(loser, red, -95 * game.k, int(70 * game.k) + 1, game)
            central_message_to_screen("is a loser", white, -65 * game.k, int(30 * game.k) + 1, game)
            central_message_to_screen("press C to play again, S for settings or Q to quit", white, -45 * game.k,
                                      int(20 * game.k) + 1, game)
            pygame.display.update()

            # Обработка событий
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameExit = True
                        gameOver = False
                    if event.key == pygame.K_c:
                        from .game import gameLoop
                        gameLoop(game)
                    elif event.key == pygame.K_s:
                        from .game import gameLoop
                        gameLoop(0)

        # Обработка событий
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    if not (move_2 == snake_2.Right and snake_2.length > 1):
                        move_2 = snake_2.Left
                elif event.key == pygame.K_RIGHT:
                    if not (move_2 == snake_2.Left and snake_2.length > 1):
                        move_2 = snake_2.Right
                elif event.key == pygame.K_UP:
                    if not (move_2 == snake_2.Down and snake_2.length > 1):
                        move_2 = snake_2.Up
                elif event.key == pygame.K_DOWN:
                    if not (move_2 == snake_2.Up and snake_2.length > 1):
                        move_2 = snake_2.Down
                if event.key == pygame.K_a:
                    if not (move_1 == snake_1.Right and snake_1.length > 1):
                        move_1 = snake_1.Left
                elif event.key == pygame.K_d:
                    if not (move_1 == snake_1.Left and snake_1.length > 1):
                        move_1 = snake_1.Right
                elif event.key == pygame.K_w:
                    if not (move_1 == snake_1.Down and snake_1.length > 1):
                        move_1 = snake_1.Up
                elif event.key == pygame.K_s:
                    if not (move_1 == snake_1.Up and snake_1.length > 1):
                        move_1 = snake_1.Down

        # Проверка на выход за границы окна
        if snake_1.lead_x >= game.width or snake_1.lead_x < 0 or snake_1.lead_y >= game.height or snake_1.lead_y < 0:
            gameOver = True
            loser += " first"
        if snake_2.lead_x >= game.width or snake_2.lead_x < 0 or snake_2.lead_y >= game.height or snake_2.lead_y < 0:
            gameOver = True
            loser += " second"

        game.screen.fill(game.background_colour)

        move_1()
        move_2()

        # Рисование сыра
        meal.Draw()

        # Рисование змеи
        snake_1.Draw()
        snake_2.Draw()

        # Вывод счета
        DrawScores(snake_1, snake_2, game)

        # Обновление экрана
        pygame.display.update()

        # Проверка на съедание еды
        eat_1 = snake_1.IsEat(meal)
        eat_2 = snake_2.IsEat(meal)
        if eat_1 or eat_2:
            meal = Meal(game.meal_pic, game)

        # Проверка на победителя
        if snake_1.score == game.win_score:
            loser += " second"
            gameOver = True
        if snake_2.score == game.win_score:
            loser += " first"
            gameOver = True

        # Проверка на самопересечение
        if snake_1.IsIntercept():
            loser += " first"
            gameOver = True
        if snake_2.IsIntercept():
            loser += " second"
            gameOver = True

        # Частота обновления экрана
        pygame.time.Clock().tick(game.time)

    # Закрытие Pygame
    pygame.quit()