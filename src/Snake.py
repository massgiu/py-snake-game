import pygame, sys
from src.Cube import Cube
from src.Constants import  Constants

class Snake(object):
    body_list = []  # lista di cube
    # Dictionary that stores tuple about point of rotations
    turns = {}

    def __init__(self, color, pos):  # pos: head position
        self.color = color
        self.head = Cube(pos)
        self.body_list.append(self.head)  # We will add head (which is a cube object)
        # inizialmente snake va in basso
        self.direction = "DOWN"

    def move(self):
        # Gestore di eventi: intercetto eventi tastiera
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            keys = pygame.key.get_pressed()
            for key in keys:
                #se premo a sinis and la direz non è destra e la lunghez >1 oppure se premo a sx e la lunghezza è 1
                if (keys[pygame.K_LEFT] and self.direction != "RIGHT" and len(self.body_list) > 1) or (
                        keys[pygame.K_LEFT] and len(self.body_list) == 1):
                    self.direction = "LEFT"
                elif (keys[pygame.K_RIGHT] and self.direction != "LEFT" and len(self.body_list) > 1) or (
                                keys[pygame.K_RIGHT] and len(self.body_list) == 1):
                    self.direction = "RIGHT"
                elif (keys[pygame.K_UP] and self.direction != "DOWN" and len(self.body_list) > 1) or (
                                keys[pygame.K_UP] and len(self.body_list) == 1):
                    self.direction = "UP"
                elif (keys[pygame.K_DOWN] and self.direction != "UP" and len(self.body_list) > 1) or (
                                keys[pygame.K_DOWN] and len(self.body_list) == 1):
                    self.direction = "DOWN"
                # All'atto della rotazione devo memorizzare la direzione
                # Come chiave la posizione della testa
                # come valore metto la direzione
                self.turns[self.head.pos[:]] = self.direction

        # Implemento il movimento del serpente
        for index, cub in enumerate(self.body_list):  # body_list è una lista di cube
            # per ciascun blocchetto del body prendo la tupla della posizione (x,y)
            p = cub.pos[:]
            # se la posizione del blocchetto coincide con quella in cui
            # è avvenuta la rotazione della testa
            if p in self.turns:
                direction = self.turns[p]  # prendo la direzione di rotaz dal dizion
                # per ogni blocchetto del body chiamo il metodo move()
                cub.move_cube(direction)  # turn[0]=direzX, turn[1]=direzY
                # se è l'ultimo cubo lo rimuovo
                if index == len(self.body_list) - 1:
                    self.turns.pop(p)
            else:
                # se la direz è sx e la pos_x<0 => riporto la x all'estremo dx
                if cub.direction == "LEFT" and cub.pos[0] <= 0:
                    cub.pos = (Constants.ROWS - 1, cub.pos[1])
                # se la direz è dx e la pos_x è al termine => riporto la x allo 0
                elif cub.direction == "RIGHT" and cub.pos[0] >= Constants.ROWS - 1:
                    cub.pos = (0, cub.pos[1])
                # se la direz y è down e la pos_y è al termine => riporto la y allo 0
                elif cub.direction == "DOWN" and cub.pos[1] >= Constants.ROWS - 1:
                    cub.pos = (cub.pos[0], 0)
                # se la direz y è up e la pos_y è al termine => riporto la y al termine
                elif cub.direction == "UP" and cub.pos[1] <= 0:
                    cub.pos = (cub.pos[0], Constants.ROWS - 1)
                else:  # If we haven't reached the edge just move in our current direction
                    cub.move_cube(cub.direction)

    def reset(self, pos):
        self.head = Cube(pos)
        self.body_list = []
        self.body_list.append(self.head)
        self.turns = {}  # lista delle rotazioni
        self.direction = "DOWN"

    def addCube(self):
        tail = self.body_list[-1]
        direction = tail.direction

        # We need to know which side of the snake to add the cube to.
        # So we check what direction we are currently moving in to determine if we
        # need to add the cube to the left, right, above or below.
        if direction == "RIGHT":  # going right (x-1, same y)
            self.body_list.append(Cube((tail.pos[0] - 1, tail.pos[1])))
        elif direction == "LEFT":  # going left (x+1, same y)
            self.body_list.append(Cube((tail.pos[0] + 1, tail.pos[1])))
        elif direction == "DOWN":  # going down (same x, y-1)
            self.body_list.append(Cube((tail.pos[0], tail.pos[1] - 1)))
        elif direction == "UP":  # going up (same x, y+1)
            self.body_list.append(Cube((tail.pos[0], tail.pos[1] + 1)))

        # We then set the new cube direction to the direction of the snake.
        self.body_list[-1].direction = direction

    # Draw every cube of the body
    def draw(self, surface):
        for index, cub in enumerate(self.body_list):
            if index == 0:  # this is head, we need to draw eyes
                cub.draw_cube(surface, True)
            else:
                cub.draw_cube(surface)