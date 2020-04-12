import pygame

class Paddle:
    def __init__(self, x, y, width, height, speed, min_y, max_y):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = speed
        self.min_y = min_y
        self.max_y = max_y

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
        
    
    def getSpeed(self):
        return self.speed
        
    
    def getMinY(self):
        return self.min_y
        
    
    def getMaxY(self):
        return self.max_y
        
    
    def setPosition(self, y):
        if y+self.height > self.max_y or y < self.min_y:
            return
        self.y = y
        
    
    def moveUp(self, dt):
        new_y = self.y - (dt * self.speed)
        if new_y < self.min_y:
            self.y = self.min_y
        else:
            self.y = new_y
        
    
    def moveDown(self, dt):
        new_y = self.y + (dt * self.speed)
        if new_y > self.max_y-self.height:
            self.y = self.max_y-self.height
        else:
            self.y = new_y
        
    
    def draw(self, surface):
        r = pygame.Rect(self.x, self.y, self.width, self.height)
        pygame.draw.rect(surface, (255,255,255), r)

        