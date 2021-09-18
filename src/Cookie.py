from src.Cube import Cube
from src.Utils import Utils
from src.Constants import Constants
import pygame

class Cookie():

    def __init__(self, snake):
        self.color = (0, 255, 0)
        self.cookie = Cube(Utils.randomSnack(Constants.ROWS, snake), self.color)
        self.pos = self.cookie.pos


    def draw_cube(self, surface):
        dist = Constants.WIDTH // Constants.ROWS
        i = self.pos[0]  # x-coord cube
        j = self.pos[1]  # y-coord cube
        # coloro il blocchetto
        pygame.draw.rect(surface, self.color, (i * dist + 1, j * dist + 1, dist - 2, dist - 2))
