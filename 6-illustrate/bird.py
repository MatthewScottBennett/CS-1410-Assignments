import pygame
from math import pi

class Bird:
    def __init__(self, startpoint, birdtype, size, color):
        self.size = size
        self.color = color
        self.type = birdtype
        self.startpoint = startpoint

    def draw(self, surface):
        if self.type == 'straight':
            # wing1
            pygame.draw.line(surface, self.color, self.startpoint, (self.startpoint[0]+10, self.startpoint[1]-10), self.size)
            pygame.draw.line(surface, self.color, (self.startpoint[0]+10, self.startpoint[1]-10), (self.startpoint[0]+20, self.startpoint[1]), self.size)

            # wing2
            pygame.draw.line(surface, self.color, (self.startpoint[0]+20, self.startpoint[1]), (self.startpoint[0]+30, self.startpoint[1]-10), self.size)
            pygame.draw.line(surface, self.color, (self.startpoint[0]+30, self.startpoint[1]-10), (self.startpoint[0]+40, self.startpoint[1]), self.size)
        elif self.type == 'curved':
            cbird = pygame.Rect(self.startpoint[0], self.startpoint[1], 40, 40)
            pygame.draw.arc(surface, self.color, cbird, pi/4, pi/2+1, self.size)

            cbird1 = pygame.Rect(self.startpoint[0]+30, self.startpoint[1], 40, 40)
            pygame.draw.arc(surface, self.color, cbird1, pi/4, pi/2+1, self.size)
        else:
            return
