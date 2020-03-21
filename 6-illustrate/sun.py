import pygame

class Sun:
    def __init__(self, size, color):
        self.size = size
        self.color = color
    
    def draw (self, surface):
        pygame.draw.circle(surface, self.color, (0,0), self.size)