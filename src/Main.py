import pygame
from src.Cookie import Cookie
from src.Snake import Snake
from src.Utils import Utils
from src.Constants import Constants


def main():
    win = pygame.display.set_mode((Constants.WIDTH, Constants.WIDTH))
    pygame.display.set_caption("Snake Game")

    snake = Snake(Constants.SNAKE_COLOR)
    cookie = Cookie(snake)
    flag = True
    clock = pygame.time.Clock()  # create an object to help track time
    while flag:
        # pause the program for an amount of time
        pygame.time.delay(90)
        # clock.tick(60) # Now your game will be capped at FPS fps
        snake.move()
        Utils.check_crossing(snake, cookie)
        Utils.redrawWindow(win, Constants.ROWS, Constants.WIDTH, snake, cookie)


if __name__ == '__main__':
    main()
