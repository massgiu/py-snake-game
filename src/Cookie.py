from src.Cube import Cube
from src.Utils import Utils
from src.Constants import Constants
import pygame


class Cookie():

    def __init__(self, snake):
        self.cookie = Cube(Utils.random_cookie(snake), Constants.COOKIE_COLOR)
        self.pos = self.cookie.pos

    def draw_cube(self, surface):
        dist = Constants.WIDTH // Constants.ROWS
        # coloro il blocchetto
        pygame.draw.rect(surface, Constants.COOKIE_COLOR,
                         (self.pos[0], self.pos[1], Constants.SIZE_CUBE, Constants.SIZE_CUBE))
