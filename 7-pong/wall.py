import pygame

class Wall:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    
    def getX(self):
        return self.x

    
    def getY(self):
        return self.y
        
    
    def getWidth(self):
        return self.width
        
    
    def getHeight(self):
        return self.height
        
    
    def getRightX(self):
        return self.width + self.x
        
    
    def getBottomY(self):
        return self.height + self.y
        
    
    def draw(self, surface):
        r = pygame.Rect(self.x, self.y, self.width, self.height)
        pygame.draw.rect(surface, (255,255,255), r)
