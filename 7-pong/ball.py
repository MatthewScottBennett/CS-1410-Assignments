# http://cit.dixie.edu/cs/1410/labs/pong.php

import pygame

class Ball:
    def __init__(self, size, min_x, max_x, min_y, max_y, left_paddle_x, right_paddle_x):
        self.x = min_x
        self.y = min_y
        self.size = size
        self.dx = 0
        self.dy = 0
        self.min_x = min_x
        self.max_x = max_x
        self.min_y = min_y
        self.max_y = max_y
        self.left_paddle_x = left_paddle_x
        self.left_paddle_min_y = min_y
        self.left_paddle_max_y = max_y
        self.right_paddle_x = right_paddle_x
        self.right_paddle_min_y = min_y
        self.right_paddle_max_y = max_y

    
    def getX(self):
        return self.x

    
    def getY(self):
        return self.y


    def getSize(self):
        return self.size


    def getDX(self):
        return self.dx


    def getDY(self):
        return self.dy


    def getMinX(self):
        return self.min_x

    
    def getMaxX(self):
        return self.max_x


    def getMinY(self):
        return self.min_y


    def getMaxY(self):
        return self.max_y


    def getLeftPaddleX(self):
        return self.left_paddle_x


    def getLeftPaddleMinY(self):
        return self.left_paddle_min_y


    def getLeftPaddleMaxY(self):
        return self.left_paddle_max_y


    def getRightPaddleX(self):
        return self.right_paddle_x


    def getRightPaddleMinY(self):
        return self.right_paddle_min_y


    def getRightPaddleMaxY(self):
        return self.right_paddle_max_y


    def setPosition(self, x, y):
        if (x >= self.min_x) and (x+self.size <= self.max_x) and (y >= self.min_y) and (y+self.size <= self.max_y): 
           self.x = x
           self.y = y
           return True
        return False

    def setSpeed(self, dx, dy):
        self.dx = dx
        self.dy = dy


    def setLeftPaddleY(self, paddle_min_y, paddle_max_y):
        if (paddle_min_y >= self.min_y) and (paddle_max_y <= self.max_y) and (paddle_min_y < paddle_max_y):
            self.left_paddle_min_y = paddle_min_y
            self.left_paddle_max_y = paddle_max_y
            return True
        return False


    def setRightPaddleY(self, paddle_min_y, paddle_max_y):
        if (paddle_min_y >= self.min_y) and (paddle_max_y <= self.max_y) and (paddle_min_y < paddle_max_y):
            self.right_paddle_min_y = paddle_min_y
            self.right_paddle_max_y = paddle_max_y
            return True
        return False


    def checkTop(self, new_y):
        if new_y < self.min_y:
            self.dy = -self.dy
            new_y = self.min_y - (new_y - self.min_y)
        return new_y


    def checkBottom(self, new_y):
        bottom = self.max_y - self.size
        if new_y > bottom:
            self.dy = -self.dy
            new_y = bottom - (new_y - bottom)
        return new_y


    def checkLeft(self, new_x):
        if new_x < self.min_x:
            new_x = self.min_x
            self.dx = 0
            self.dy = 0
        return new_x


    def checkRight(self, new_x):
        right = self.max_x - self.size
        if new_x > right:
            new_x = self.max_x - self.size
            self.dx = 0
            self.dy = 0
        return new_x


    def checkLeftPaddle(self, new_x, new_y):
        mid_y = (new_y + self.y)/2
        if mid_y >= self.left_paddle_min_y and mid_y <= self.left_paddle_max_y and new_x <= self.left_paddle_x and self.x >= self.left_paddle_x:
            self.dx = -self.dx
            new_x = self.left_paddle_x + (self.left_paddle_x - new_x)
        return new_x


    def checkRightPaddle(self, new_x, new_y):
        right = self.right_paddle_x - self.size
        mid_y = (new_y + self.y)/2
        if mid_y >= self.right_paddle_min_y and mid_y <= self.right_paddle_max_y and new_x >= right and self.x <= right:
            self.dx = -self.dx
            new_x = right + (right - new_x)
        return new_x


    def move(self, dt):
        return


    def serveLeft(self, x, min_y, max_y, min_dx, max_dx, min_dy, max_dy):
        return

    
    def serveRight(self, x, min_y, max_y, min_dx, max_dx, min_dy, max_dy):
        return


    def draw(self, surface):
        r = pygame.Rect(self.x, self.y, self.size, self.size)
        pygame.draw.rect(surface, (0,0,0), r)