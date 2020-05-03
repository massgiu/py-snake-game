import pygame

class Cube(object):
    ROWS = 20
    WIDTH = 500


    def __init__(self, initial_pos, dirnx=1, dirny=0, color=(255, 0, 0)):
        self.pos = initial_pos  # è una tupla contenente coord x,y
        self.dirnx = dirnx
        self.dirny = dirny
        self.color = color

    def move_cube(self, dirnx, dirny):
        self.dirnx = dirnx
        self.dirny = dirny
        # move cube
        self.pos = (self.pos[0] + self.dirnx, self.pos[1] + self.dirny)

    def draw_cube(self, surface, eyes=False):
        dist = self.WIDTH // self.ROWS
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