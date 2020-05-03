import pygame

from src.Snake import Snake
from src.Cube import Cube
from src.Utils import Utils

def main():
    # width = 500  # Width of our screen
    # rows = 20  # Amount of rows
    win = pygame.display.set_mode((Cube.WIDTH, Cube.WIDTH))

    snake_color = (255, 0, 0)
    snake_pos = (10, 10)
    snk = Snake(snake_color, snake_pos)
    utils = Utils()
    cookie = Cube(utils.randomSnack(Cube.ROWS, snk), color=(0, 255, 0))
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
            cookie = Cube(utils.randomSnack(Cube.ROWS, snk), color=(0, 255, 0))  # creates a new cube object
        utils.redrawWindow(win, Cube.ROWS, Cube.WIDTH, snk, cookie)

main()
