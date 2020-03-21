import pygame
import mountain

class Land:
    
    def __init__(self, width, height, color):
        self.width = width
        self.height = height
        self.color = color

    def draw(self, surface):

        # Mountain
        m1 = mountain.Mountain((61, 97, 59), [(0, 600), (150, 250), (300, 600)])
        m1.draw(surface)
        
        m2 = mountain.Mountain((61, 97, 59), [(-200, 600), (50, 300), (100, 600)])
        m2.draw(surface)

        # Base land
        land = pygame.Rect(0, 500, self.width, self.height)
        pygame.draw.rect(surface, self.color, land)