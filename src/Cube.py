import pygame
from src.Constants import Constants

class Cube(object):

    def __init__(self, initial_pos, direction="DOWN", color=(255, 0, 0)):
        self.pos = initial_pos  # è una tupla contenente coord x,y
        #self.dirnx = dirnx
        #self.dirny = dirny
        self.direction = direction
        self.color = color

    def move_cube(self, direction):
        #self.dirnx = dirnx
        #self.dirny = dirny
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
        i = self.pos[0]  # x-coord cube
        j = self.pos[1]  # y-coord cube
        # coloro il blocchetto
        pygame.draw.rect(surface, self.color, (i * dist + 1, j * dist + 1, dist - 2, dist - 2))
        if eyes:
            centre = dist // 2
            radius = 3
            circleMiddle = (i * dist + centre - radius, j * dist + 8)
            circleMiddle2 = (i * dist + dist - radius * 2, j * dist + 8)
            pygame.draw.circle(surface, (0, 0, 0), circleMiddle, radius)
            pygame.draw.circle(surface, (0, 0, 0), circleMiddle2, radius)