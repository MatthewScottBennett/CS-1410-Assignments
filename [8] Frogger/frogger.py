import pygame
from froggerlib import frog

class Frogger:
    def __init__(self, screen_width, screen_height):
        self.width = screen_width
        self.height = screen_height
        self.frog = frog.Frog(0, 0, 50, 50, 0, 0, 10, 50, 50)
        self.frog_dead = False

    
    def evolve(self, dt):
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

        # Frog
        frog = pygame.Rect(self.frog.getX(), self.frog.getY(), self.frog.getWidth(), self.frog.getHeight())
        pygame.draw.rect(surface, (0, 255, 0), frog)
