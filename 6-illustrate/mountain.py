import pygame

class Mountain:
    def __init__(self, color, points):
        self.points = points
        self.color = color
    
    def draw(self, surface):
        pygame.draw.polygon(surface, self.color, self.points)