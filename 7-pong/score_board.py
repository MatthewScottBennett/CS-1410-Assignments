import text

class ScoreBoard:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.left_score = 0
        self.right_score = 0
        self.serve_status = 1


    def getX(self):
        return self.x
        

    def getY(self):
        return self.y
        

    def getWidth(self):
        return self.width
        

    def getHeight(self):
        return self.height
        

    def getLeftScore(self):
        return self.left_score
        

    def getRightScore(self):
        return self.right_score
        

    def getServeStatus(self):
        return self.serve_status
        

    def isGameOver(self):
        if (self.serve_status == 3) or (self.serve_status == 4):
            return True
        else:
            return False
        

    def scoreLeft(self):
        if not self.isGameOver():
            self.left_score += 1
            if self.left_score == 9:
                self.serve_status = 3
        

    def scoreRight(self):
        if not self.isGameOver():
            self.right_score += 1
            if self.right_score == 9:
                self.serve_status = 4
        

    def swapServe(self):
        if not self.isGameOver():
            if self.serve_status == 1:
                self.serve_status = 2
            elif self.serve_status == 2:
                self.serve_status = 1


    def draw(self, surface):
        right_score = text.Text(str(self.right_score), self.x, self.y)
        right_score.setColor((255,255,255))
        right_score.draw(surface)

        left_score = text.Text(str(self.left_score), self.x+self.width, self.y)
        left_score.setColor((255,255,255))
        left_score.draw(surface)