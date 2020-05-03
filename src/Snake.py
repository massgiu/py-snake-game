import pygame
from src.Cube import Cube

class Snake(object):
    body_list = []  # lista di cube
    # Dictionary that stores tuple about point of rotations
    turns = {}

    def __init__(self, color, pos):  # pos: head position
        self.color = color
        self.head = Cube(pos)
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
                if (keys[pygame.K_LEFT] and self.dirnx !=1 and len(self.body_list)>1) or (keys[pygame.K_LEFT] and len(self.body_list)==1):
                    self.dirnx = -1
                    self.dirny = 0
                elif (keys[pygame.K_RIGHT] and self.dirnx !=-1 and len(self.body_list)>1) or (keys[pygame.K_RIGHT] and len(self.body_list)==1):
                    self.dirnx = 1
                    self.dirny = 0
                elif (keys[pygame.K_UP] and self.dirny !=1 and len(self.body_list)>1) or (keys[pygame.K_UP] and len(self.body_list)==1):
                    self.dirnx = 0
                    self.dirny = -1
                elif (keys[pygame.K_DOWN] and self.dirny !=-1 and len(self.body_list)>1) or (keys[pygame.K_DOWN] and len(self.body_list)==1):
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
                turn = self.turns[p]  # prendo la direzione di rotaz dal dizion
                # per ogni blocchetto del body chiamo il metodo move()
                cub.move_cube(turn[0], turn[1])  # turn[0]=direzX, turn[1]=direzY
                # se è l'ultimo cubo lo rimuovo
                if index == len(self.body_list) - 1:
                    self.turns.pop(p)
            else:
                # se la direz è sx e la pos_x<0 => riporto la x all'estremo dx
                if cub.dirnx == -1 and cub.pos[0] <= 0:
                    cub.pos = (cub.ROWS - 1, cub.pos[1])
                # se la direz è dx e la pos_x è al termine => riporto la x allo 0
                elif cub.dirnx == 1 and cub.pos[0] >= cub.ROWS - 1:
                    cub.pos = (0, cub.pos[1])
                # se la direz y è down e la pos_y è al termine => riporto la y allo 0
                elif cub.dirny == 1 and cub.pos[1] >= cub.ROWS - 1:
                    cub.pos = (cub.pos[0], 0)
                # se la direz y è up e la pos_y è al termine => riporto la y al termine
                elif cub.dirny == -1 and cub.pos[1] <= 0:
                    cub.pos = (cub.pos[0], cub.ROWS - 1)
                else:  # If we haven't reached the edge just move in our current direction
                    cub.move_cube(cub.dirnx, cub.dirny)

    def reset(self, pos):
        self.head = Cube(pos)
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
            self.body_list.append(Cube((tail.pos[0] - 1, tail.pos[1])))
        elif dx == -1 and dy == 0:  # going left (x+1, same y)
            self.body_list.append(Cube((tail.pos[0] + 1, tail.pos[1])))
        elif dx == 0 and dy == 1:  # going down (same x, y-1)
            self.body_list.append(Cube((tail.pos[0], tail.pos[1] - 1)))
        elif dx == 0 and dy == -1:  # going up (same x, y+1)
            self.body_list.append(Cube((tail.pos[0], tail.pos[1] + 1)))

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