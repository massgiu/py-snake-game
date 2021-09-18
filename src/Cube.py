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
            dy = -1
        if direction == "DOWN":
            dy = 1
        if direction == "RIGHT":
            dx = 1
        if direction == "LEFT":
            dx = -1
        self.pos = (self.pos[0]+dx, self.pos[1]+dy)

    def draw_cube(self, surface, eyes=False):
        dist = Constants.WIDTH // Constants.ROWS
        x = self.pos[0]  # x-coord cube
        y = self.pos[1]  # y-coord cube
        # coloro il blocchetto
        pygame.draw.rect(surface, self.color, (x * dist + 1, y * dist + 1, dist - 2, dist - 2))
        if eyes:
            centre = dist // 2
            radius = 3
            circleMiddle = (x * dist + centre - radius, y * dist + 8)
            circleMiddle2 = (x * dist + dist - radius * 2, y * dist + 8)
            pygame.draw.circle(surface, (0, 0, 0), circleMiddle, radius)
            pygame.draw.circle(surface, (0, 0, 0), circleMiddle2, radius)