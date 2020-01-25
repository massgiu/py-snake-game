import pygame

from src.snake import Snake
from src.cube import Cube
from src.utils import Utils

def main():
    width = 500  # Width of our screen
    rows = 20  # Amount of rows
    win = pygame.display.set_mode((width, width))

    snake_color = (255, 0, 0)
    snake_pos = (10, 10)
    snk = Snake(snake_color, snake_pos)
    utils = Utils()
    cookie = Cube(utils.randomSnack(rows, snk), color=(0, 255, 0))
    flag = True
    clock = pygame.time.Clock()  # create an object to help track time
    while flag:
        # pause the program for an amount of time
        pygame.time.delay(50)  # se diminuisce, va più veloce
        clock.tick(10)  # se diminuisce, va più lento
        snk.move()
        if utils.checkCrossing(snk): break
        if snk.body_list[0].pos == cookie.pos:  # Checks if the head collides with the cookie
            snk.addCube()  # Adds a new cube to the snake
            cookie = Cube(utils.randomSnack(rows, snk), color=(0, 255, 0))  # creates a new cube object
        utils.redrawWindow(win, rows, width, snk, cookie)

main()
