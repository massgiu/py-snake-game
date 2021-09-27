import pygame
import random
import tkinter as tk
from tkinter import messagebox

from src.Constants import Constants


class Utils(object):

    @staticmethod
    def draw_grid(width, rows, surface):
        color_line = (128, 128, 128)
        x = 0
        y = 0
        for l in range(rows):
            x = x + Constants.SIZE_CUBE
            y = y + Constants.SIZE_CUBE
            # Vertical line
            pygame.draw.line(surface, color_line, (x, 0), (x, width))
            # Horizontal line
            pygame.draw.line(surface, color_line, (0, y), (width, y))

    # Update display
    @staticmethod
    def redraw_window(surface, snk, cookie):
        surface.fill((0, 0, 0))  # Fills the screen with black
        snk.draw(surface)
        cookie.draw_cube(surface)
        Utils.draw_grid(Constants.WIDTH, Constants.ROWS, surface)  # Will draw our grid lines
        pygame.display.update()  # Updates the screen

    # This function generates the coordinates x,y for a random cube to eat
    @staticmethod
    def random_cookie(snk):
        while True:  # Keep generating random positions until we get a valid one
            x = random.randrange(Constants.ROWS) * Constants.SIZE_CUBE
            y = random.randrange(Constants.ROWS) * Constants.SIZE_CUBE
            # get a list with all position of snake's cube
            position_list = list(map(lambda z: z.pos, snk.body_list))
            if (x, y) in position_list:  # This wll check if the position we generated is occupied by the snake
                continue
            else:
                break

        return x, y

    @staticmethod
    def message_box(subject, content):
        root = tk.Tk()
        root.attributes("-topmost", True)
        root.withdraw()
        messagebox.showinfo(subject, content)
        try:
            root.destroy()
        except:
            pass

    @staticmethod
    def check_crossing(snake, cookie):
        for x in range(len(snake.body_list)):
            # Check if snake head overlaps with its body
            if snake.body_list[0].pos in list(map(lambda z: z.pos, snake.body_list[1:])):
                Utils.you_lost(snake)
            #eat cookie
            if snake.body_list[0].pos == cookie.pos:  # Checks if the head collides with cookie
                snake.addCube()  # Adds a new cube to the snake
                cookie.__init__(snake)# creates a new cube object


    @staticmethod
    def you_lost(snake):
        print('Your score is: ', len(snake.body_list))
        Utils.message_box('You Lost!', 'Play again...')
        snake.__init__(Constants.SNAKE_COLOR)
        pygame.display.update()