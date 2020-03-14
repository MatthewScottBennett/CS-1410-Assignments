import pygame
from froggerlib import frog, stage, road, race_car

class Frogger:
    def __init__(self, screen_width, screen_height, cell_size, rows, cols):
        self.width = screen_width
        self.height = screen_height
        self.frog_dead = False
        self.cell_size = cell_size
        self.rows = rows
        self.cols = cols
        self.num_roads = (self.rows - 3) // 2

        x = (self.cols // 2)*self.cell_size
        y = (self.rows - 1)*self.cell_size
        w = self.cell_size
        h = self.cell_size
        self.frog = frog.Frog(x, y, w, h, x, y, 10, w, h)

        self.roads = []
        for i in range(self.num_roads):    
            x = 0
            y = (self.rows - 2 - i)*self.cell_size
            w = self.width
            h = self.cell_size
            self.roads.append(road.Road(x, y, w, h))
        x = 0
        y = (self.rows - 1)*self.cell_size
        w = self.width
        h = self.cell_size
        self.stage1 = stage.Stage(x, y, w, h)

        self.racecars = []
        gap = 0.1 * self.cell_size
        for i in range(self.num_roads):
            w = self.cell_size+2*gap
            h = self.cell_size-2*gap
            if i % 2 ==0:
                x = -w
                dx = self.width + w
            else:
                x = self.width
                dx = -w
            y = (self.rows - 2 - i) * self.cell_size + gap
            dy = y
            mins = 5
            maxs = 10
            self.racecars.append(race_car.RaceCar(x, y, w, h, dx, dy, mins, maxs))

    
    def evolve(self, dt):
        for i in range(len(self.racecars)):
            car = self.racecars[i]
            car.move()
            if car.atDesiredLocation():
                if i % 2 == 0:
                    car.setX(-car.getWidth())
                else:
                    car.setX(self.width)
            if car.hits(self.frog):
                self.frog_dead = True
        if not self.frog_dead:
            self.frog.move()
        if self.frog.outOfBounds(self.width, self.height):
            self.frog_dead = True

    
    def up(self):
        self.frog.up()

    
    def down(self):
        self.frog.down()


    def right(self):
        self.frog.right()


    def left(self):
        self.frog.left()


    def draw(self, surface):
        # Background
        r = pygame.Rect(0, 0, self.width, self.height)
        pygame.draw.rect(surface, (255,255,255), r)

        # Stage
        rectangle(surface, self.stage1, (0, 0, 255))

        # Road
        for road in self.roads:
            rectangle(surface, road, (0, 0, 0))

        # Car
        for car in self.racecars:
            rectangle(surface, car, (0, 255, 0))

        # Frog
        rectangle(surface, self.frog, (255, 0, 0))

def rectangle(surface, obj, color):
    r = pygame.Rect(obj.getX(), obj.getY(), obj.getWidth(), obj.getHeight())
    pygame.draw.rect(surface, color, r)