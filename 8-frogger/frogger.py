import pygame
from froggerlib import frog, stage, road, race_car, dozer, truck, car, water, log, turtle, home, grass
import random

class Frogger:

    def __init__(self, screen_width, screen_height, cell_size, rows, cols):
        self.width = screen_width
        self.height = screen_height
        self.frog_dead = False
        self.frog_win = False
        self.cell_size = cell_size
        self.rows = rows
        self.cols = cols
        self.num_roads = (self.rows - 3) // 2
        self.num_waters = self.rows - 3 - self.num_roads

        # Frog
        padding = .1 * self.cell_size
        x = (self.cols // 2) * self.cell_size + padding
        y = (self.rows - 1) * self.cell_size + padding
        w = self.cell_size - 2*padding
        h = self.cell_size - 2*padding
        dx = x
        dy = y
        s = 10
        hg = self.cell_size
        vg = self.cell_size
        self.frog = frog.Frog(x, y, w, h, dx, dy, s, hg, vg)

        # First stage
        x = 0
        y = (self.rows - 1) * self.cell_size
        w = self.width
        h = self.cell_size
        self.stage1 = stage.Stage(x, y, w, h)

        # Roads
        self.roads = []
        for i in range(self.num_roads):
            x = 0
            y = (self.rows - 2 - i) * self.cell_size
            w = self.width
            h = self.cell_size
            self.roads.append(road.Road(x, y, w, h))

        # Cars

        # Race Cars
        self.racecars = []
        gap = .1 * self.cell_size
        for i in range(self.num_roads):
            w = self.cell_size + 2*gap
            h = self.cell_size - 2*gap
            x = random.randrange(self.width)
            if i % 2 == 0:
                dx = self.width + w
            else:
                dx = -w
            y = (self.rows - 2 - i) * self.cell_size + gap
            dy = y
            mins = 5
            maxs = 10
            self.racecars.append(race_car.RaceCar(x,y,w,h,dx,dy,mins,maxs))

        # Bulldozer
        self.dozers = []
        gap = .1 * self.cell_size
        for i in range(self.num_roads):
            w = self.cell_size + 2*gap
            h = self.cell_size - 2*gap
            x = random.randrange(self.width)
            if i % 2 == 0:
                dx = self.width + w
            else:
                dx = -w
            y = (self.rows - 2 - i) * self.cell_size + gap
            dy = y
            speed = 3
            self.dozers.append(dozer.Dozer(x,y,w,h,dx,dy,speed))

        # Truck
        self.trucks = []
        gap = .1 * self.cell_size
        for i in range(self.num_roads):
            w = self.cell_size + 2*gap
            h = self.cell_size - 2*gap
            x = random.randrange(self.width)
            if i % 2 == 0:
                dx = self.width + w
            else:
                dx = -w
            y = (self.rows - 2 - i) * self.cell_size + gap
            dy = y
            speed = 4
            self.trucks.append(truck.Truck(x,y,w,h,dx,dy,speed))

        # Car
        self.cars = []
        gap = .1 * self.cell_size
        for i in range(self.num_roads):
            w = self.cell_size + 2*gap
            h = self.cell_size - 2*gap
            x = random.randrange(self.width)
            if i % 2 == 0:
                dx = self.width + w
            else:
                dx = -w
            y = (self.rows - 2 - i) * self.cell_size + gap
            dy = y
            speed = 5
            self.cars.append(car.Car(x,y,w,h,dx,dy,speed))

        # Second Stage
        x = 0
        y = (self.rows - 2 - self.num_roads) * self.cell_size
        w = self.width
        h = self.cell_size
        self.stage2 = stage.Stage(x,y,w,h)

        # Water
        self.waters = []
        for i in range(self.num_waters):
            x = 1
            y = (self.rows - 2 - self.num_roads - 1 - i) * self.cell_size
            w = self.width
            h = self.cell_size
            self.waters.append(water.Water(x,y,w,h))

        # Logs
        self.logs = []
        for i in range(self.num_waters):
            w = self.cell_size
            h = self.cell_size
            x = random.randrange(self.width)
            y = (self.rows - 2 - self.num_roads - 1 - i) * self.cell_size
            if i % 2 == 0:
                dx = self.width + w
            else:
                dx = -w
            dy = y
            s = 3
            self.logs.append(log.Log(x, y, w, h, dx, dy, s))

        # Turtles
        self.turtles = []
        for i in range(self.num_waters):
            w = self.cell_size
            h = self.cell_size
            x = random.randrange(self.width)
            y = (self.rows - 2 - self.num_roads - 2 - i) * self.cell_size
            if i % 2 == 0:
                dx = self.width + w
            else:
                dx = -w
            dy = y
            s = 3
            self.turtles.append(turtle.Turtle(x, y, w, h, dx, dy, s))

        # Home
        self.homes = []
        self.homesx = []
        for i in range(3):
            x = random.randrange(self.width)
            y = 0
            w = self.cell_size
            h = self.cell_size
            self.homesx.append(x)
            self.homes.append(home.Home(x,y,w,h))

        # Grass
            x = 9
            y = 0
            w = self.width
            h = self.cell_size
            self.grass = grass.Grass(x,y,w,h)


    def up(self):
        self.frog.up()

    def down(self):
        self.frog.down()

    def left(self):
        self.frog.left()

    def right(self):
        self.frog.right()

    def evolve(self, dt):
        if not self.frog_dead:
            # Cars

            # Racecars
            for i in range(len(self.racecars)):
                car = self.racecars[i]
                car.move()
                if car.atDesiredLocation():
                    if i % 2 == 0:
                        car.setX(-car.getWidth())
                    else:
                        car.setX(self.width)
                # detect collisions with frog
                if car.hits(self.frog):
                    self.frog_dead = True
            
            # Dozers
            for i in range(len(self.dozers)):
                car = self.dozers[i]
                car.move()
                if car.atDesiredLocation():
                    if i % 2 == 0:
                        car.setX(-car.getWidth())
                    else:
                        car.setX(self.width)
                # detect collisions with frog
                if car.hits(self.frog):
                    self.frog_dead = True

            # Trucks
            for i in range(len(self.trucks)):
                car = self.trucks[i]
                car.move()
                if car.atDesiredLocation():
                    if i % 2 == 0:
                        car.setX(-car.getWidth())
                    else:
                        car.setX(self.width)
                # detect collisions with frog
                if car.hits(self.frog):
                    self.frog_dead = True

            # Cars
            for i in range(len(self.cars)):
                car = self.cars[i]
                car.move()
                if car.atDesiredLocation():
                    if i % 2 == 0:
                        car.setX(-car.getWidth())
                    else:
                        car.setX(self.width)
                # detect collisions with frog
                if car.hits(self.frog):
                    self.frog_dead = True
            # Frog
            self.frog.move()
            if self.frog.outOfBounds(self.width, self.height):
                self.frog_dead = True

            # Water
            for water in self.waters:
                if water.hits(self.frog):
                    self.frog_dead = True

            # Logs
            for i in range(len(self.logs)):
                log = self.logs[i]
                log.move()
                if log.atDesiredLocation():
                    if i % 2 == 0:
                        log.setX(-log.getWidth())
                    else:
                        log.setX(self.width)
                # detect collisions with frog
                log.supports(self.frog)

            # Turtles
            for i in range(len(self.turtles)):
                turtle = self.turtles[i]
                turtle.move()
                if turtle.atDesiredLocation():
                    if i % 2 == 0:
                        turtle.setX(-turtle.getWidth())
                    else:
                        turtle.setX(self.width)
                turtle.supports(self.frog)

            # Check if frog lands on grass
            if self.grass.hits(self.frog):
                self.frog_dead = True

            # Check if frog lands on home
            for i in range(len(self.homes)):
                home = self.homes[i]
                if home.hits(self.frog):
                    self.frog_win = True

    def draw(self, surface):
        # draw background
        r = pygame.Rect(0, 0, self.width, self.height)
        pygame.draw.rect(surface, (255, 255, 255), r)

        rectangle(surface, self.stage1, (200, 10, 200))
        for road in self.roads:
            rectangle(surface, road, (0, 0, 0))
        for racecar in self.racecars:
            rectangle(surface, racecar, (255, 0, 0))
        for truck in self.trucks:
            rectangle(surface, truck, (26, 32, 115))
        for dozer in self.dozers:
            rectangle(surface, dozer, (82, 115, 26))
        for car in self.cars:
            rectangle(surface, car, (115, 72, 26))
        rectangle(surface, self.stage2, (200,55,244))
        for water in self.waters:
            rectangle(surface, water, (0,0,240))
        for log in self.logs:
            rectangle(surface, log, (200,200,0))
        for turtle in self.turtles:
            rectangle(surface, turtle, (0,155,0))
        rectangle(surface, self.grass, (0,200,0)) 
        for home in self.homes:
            rectangle(surface, home, (10,55,100))
        if self.frog_win:
            rectangle(surface, self.frog, (random.randrange(255),random.randrange(255),random.randrange(255)))
        else:
            rectangle(surface, self.frog, (0,255,0))

def rectangle(surface, obj, color):
    # Draws a locatable object
    r = pygame.Rect(obj.getX(), obj.getY(), obj.getWidth(), obj.getHeight())
    pygame.draw.rect(surface, color, r)
