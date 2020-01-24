import math
import random
import pygame
import tkinter as tk
from tkinter import messagebox


class cube(object):
    rows = 20
    w = 500

    def __init__(self, start, dirnx=1, dirny=0, color=(255, 0, 0)):
        self.pos = start  # è una tupla contenente coord x,y
        self.dirnx = dirnx
        self.dirny = dirny
        self.color = color

    def move_cube(self, dirnx, dirny):
        self.dirnx = dirnx
        self.dirny = dirny
        # move cube
        self.pos = (self.pos[0] + self.dirnx, self.pos[1] + self.dirny)

    def draw_cube(self, surface, eyes=False):
        dist = self.w // self.rows
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


class snake(object):
    body_list = []  # lista di cube
    # Si tratta di un dizionario i cui elementi sono creati
    # nel momento in cui vi è una rotazione
    turns = {}

    def __init__(self, color, pos):  # pos: head position
        self.color = color
        self.head = cube(pos)
        self.body_list.append(self.head)  # We will add head (which is a cube object)
        # inizialmente snake va in basso
        self.dirnx = 0  # assume valori 0,-1,1 (se !=0, altro=0)
        self.dirny = 1  # assume valori 0,-1,1 (se !=0, altro=0)

    def move(self):
        # Gestore di eventi: intercetto eventi tastiera
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            keys = pygame.key.get_pressed()
            for key in keys:
                if keys[pygame.K_LEFT]:
                    self.dirnx = -1
                    self.dirny = 0
                elif keys[pygame.K_RIGHT]:
                    self.dirnx = 1
                    self.dirny = 0
                elif keys[pygame.K_UP]:
                    self.dirnx = 0
                    self.dirny = -1
                elif keys[pygame.K_DOWN]:
                    self.dirnx = 0
                    self.dirny = 1
                # All'atto della rotazione devo memorizzare la direzione
                # Come chiave la posizione della testa
                # come valore metto la direzione
                self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]

        # Implemento il movimento del serpente
        for index, cub in enumerate(self.body_list):  # body è una lista di cube
            # per ciascun blocchetto del body prendo la tupla della posizione (x,y)
            p = cub.pos[:]
            # se la posizione del blocchetto coincide con quella in cui
            # è avvenuta la rotazione della testa
            if p in self.turns:
                turn = self.turns[p]  # prendo la posizione di rotaz dal dizion
                # per ogni blocchetto del body chiamo il metodo move()
                cub.move_cube(turn[0], turn[1])  # turn[0]=direzX, turn[1]=direzY
                # se è l'ultimo cubo lo rimuovo
                if index == len(self.body_list) - 1:
                    self.turns.pop(p)
            else:
                # se la direz è sx e la pos_x<0 => riporto la x all'estremo dx
                if cub.dirnx == -1 and cub.pos[0] <= 0:
                    cub.pos = (cub.rows - 1, cub.pos[1])
                # se la direz è dx e la pos_x è al termine => riporto la x allo 0
                elif cub.dirnx == 1 and cub.pos[0] >= cub.rows - 1:
                    cub.pos = (0, cub.pos[1])
                # se la direz y è down e la pos_y è al termine => riporto la y allo 0
                elif cub.dirny == 1 and cub.pos[1] >= cub.rows - 1:
                    cub.pos = (cub.pos[0], 0)
                # se la direz y è up e la pos_y è al termine => riporto la y al termine
                elif cub.dirny == -1 and cub.pos[1] <= 0:
                    cub.pos = (cub.pos[0], cub.rows - 1)
                else:  # If we haven't reached the edge just move in our current direction
                    cub.move_cube(cub.dirnx, cub.dirny)

    def reset(self, pos):
        self.head = cube(pos)
        self.body_list = []
        self.body_list.append(self.head)
        self.turns = {}  # lista delle rotazioni
        self.dirnx = 0
        self.dirny = 1

    def addCube(self):
        tail = self.body_list[-1]
        dx, dy = tail.dirnx, tail.dirny

        # We need to know which side of the snake to add the cube to.
        # So we check what direction we are currently moving in to determine if we
        # need to add the cube to the left, right, above or below.
        if dx == 1 and dy == 0:  # going right (x-1, same y)
            self.body_list.append(cube((tail.pos[0] - 1, tail.pos[1])))
        elif dx == -1 and dy == 0:  # going left (x+1, same y)
            self.body_list.append(cube((tail.pos[0] + 1, tail.pos[1])))
        elif dx == 0 and dy == 1:  # going down (same x, y-1)
            self.body_list.append(cube((tail.pos[0], tail.pos[1] - 1)))
        elif dx == 0 and dy == -1:  # going up (same x, y+1)
            self.body_list.append(cube((tail.pos[0], tail.pos[1] + 1)))

        # We then set the cubes direction to the direction of the snake.
        self.body_list[-1].dirnx = dx
        self.body_list[-1].dirny = dy

    # Draw every cube of the body
    def draw(self, surface):
        for index, cub in enumerate(self.body_list):
            if index == 0:  # this is head, we need to draw eyes
                cub.draw_cube(surface, True)
            else:
                cub.draw_cube(surface)


def drawGrid(width, rows, surface):
    sizeBwn = width // rows

    x = 0
    y = 0
    for l in range(rows):
        x = x + sizeBwn
        y = y + sizeBwn
        # Vertical line
        pygame.draw.line(surface, (255, 255, 255), (x, 0), (x, width))
        # Horizontal line
        pygame.draw.line(surface, (255, 255, 255), (0, y), (width, y))


# Update display
def redrawWindow(surface, rows, width, snk, cookye):
    surface.fill((0, 0, 0))  # Fills the screen with black
    snk.draw(surface)
    cookye.draw_cube(surface)
    drawGrid(width, rows, surface)  # Will draw our grid lines
    pygame.display.update()  # Updates the screen


# This function generates the coordinates x,y for a random cube to eat
def randomSnack(rows, snk):
    while True:  # Keep generating random positions until we get a valid one
        x = random.randrange(rows)
        y = random.randrange(rows)
        position_list = list(map(lambda z: z.pos, snk.body_list))
        if (x,y) in position_list: # This wll check if the position we generated is occupied by the snake
            continue
        else:
            break

    return (x, y)


def message_box(subject, content):
    root = tk.Tk()
    root.attributes("-topmost", True)
    root.withdraw()
    messagebox.showinfo(subject, content)
    try:
        root.destroy()
    except:
        pass


def checkCrossing(snake):
    for x in range(len(snake.body_list)):
        # Check if snake head overlaps with its body
        if snake.body_list[0].pos in list(map(lambda z: z.pos, snake.body_list[1:])):
            print('Score: ', len(snake.body_list))
            message_box('You Lost!', 'Play again...')
            snake.reset((10, 10))
            True


def main():
    width = 500  # Width of our screen
    rows = 20  # Amount of rows
    win = pygame.display.set_mode((width, width))
    snake_color = (255, 0, 0)
    snake_pos = (10, 10)
    snk = snake(snake_color, snake_pos)
    cookie = cube(randomSnack(rows, snk), color=(0, 255, 0))
    flag = True
    clock = pygame.time.Clock()  # create an object to help track time
    while flag:
        # pause the program for an amount of time
        pygame.time.delay(50)  # se diminuisce, va più veloce
        clock.tick(10)  # se diminuisce, va più lento
        snk.move()
        if checkCrossing(snk): break
        if snk.body_list[0].pos == cookie.pos:  # Checks if the head collides with the cookie
            snk.addCube()  # Adds a new cube to the snake
            cookie = cube(randomSnack(rows, snk), color=(0, 255, 0))  # creates a new cube object
        redrawWindow(win, rows, width, snk, cookie)


main()
