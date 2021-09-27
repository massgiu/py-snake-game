import pygame
from src.Constants import Constants


class Cube(object):

    def __init__(self, initial_pos, direction="DOWN", color=(255, 0, 0)):
        self.pos = initial_pos  # è una tupla contenente coord x,y
        self.direction = direction
        self.color = color

    def move_cube(self, direction):
        self.direction = direction
        # move cube
        dx, dy = 0, 0
        if direction == "UP":
            dy = -Constants.SIZE_CUBE
        if direction == "DOWN":
            dy = Constants.SIZE_CUBE
        if direction == "RIGHT":
            dx = Constants.SIZE_CUBE
        if direction == "LEFT":
            dx = -Constants.SIZE_CUBE
        self.pos = (self.pos[0] + dx, self.pos[1] + dy)

    def draw_cube(self, surface, eyes=False):
        x = self.pos[0]  # x-coord cube
        y = self.pos[1]  # y-coord cube
        # coloro il blocchetto
        pygame.draw.rect(surface, self.color, (x, y, Constants.SIZE_CUBE, Constants.SIZE_CUBE))
        if eyes:
            centre = Constants.SIZE_CUBE // 2
            radius = 3
            circle_middle = (x + centre - radius, y + 8)
            circle_middle2 = (x + Constants.SIZE_CUBE - radius * 2, y + 8)
            pygame.draw.circle(surface, (0, 0, 0), circle_middle, radius)
            pygame.draw.circle(surface, (0, 0, 0), circle_middle2, radius)
