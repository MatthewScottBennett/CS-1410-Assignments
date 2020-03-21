import pygame
import sun
import bird
import cloud

class Sky:
    def __init__(self, width, height, color):
        self.width = width
        self.height = height
        self.color = color

    def draw(self, surface):
        sky = pygame.Rect(0, 0, self.width, self.height)
        pygame.draw.rect(surface, self.color, sky)

        # Sun
        sunpic = sun.Sun(150, (232, 196, 53))
        sunpic.draw(surface)

        #Clouds
        cloud1 = cloud.Cloud(200, 150, (255,255,255), (350, 150))
        cloud1.draw(surface)

        cloud2 = cloud.Cloud(200, 150, (207, 207, 207), (390, 190))
        cloud2.draw(surface)

        # Birds
        # Straight
        bird1 = bird.Bird((250, 70), 'straight', 4, (0,0,0))
        bird1.draw(surface)

        bird2 = bird.Bird((300, 90), 'straight', 4, (0,0,0))
        bird2.draw(surface)

        bird3 = bird.Bird((350, 50), 'straight', 4, (0,0,0))
        bird3.draw(surface)

        # Curved
        bird4 = bird.Bird((450, 70), 'curved', 4, (0,0,0))
        bird4.draw(surface)

        bird4 = bird.Bird((500, 90), 'curved', 4, (0,0,0))
        bird4.draw(surface)

        bird4 = bird.Bird((550, 70), 'curved', 4, (0,0,0))
        bird4.draw(surface)