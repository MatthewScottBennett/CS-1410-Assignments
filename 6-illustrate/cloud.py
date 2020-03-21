import pygame

class Cloud:
    def __init__(self, width, height, color, start):
        self.width = width
        self.height = height
        self.color = color 
        self.start = start
    
    def draw(self, surface):
        cloud = pygame.Rect(self.start[0], self.start[1], self.width, self.height)
        pygame.draw.ellipse(surface, self.color, cloud)