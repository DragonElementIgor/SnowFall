import pygame
from random import randrange, randint
pygame.init()


bg = pygame.image.load("bg.png")
width = 1600
height = 1000
sc = pygame.display.set_mode((width, height))
pygame.display.set_caption("New Year!")
inWindow = True
clock = pygame.time.Clock()
fps = 14



snows = []

class Snow:
    def __init__(self, width):
        super().__init__()
        self.snowSize = randint(32, 40)
        self.y = 0 - randint(self.snowSize, self.snowSize+20)
        self.image = pygame.transform.scale(pygame.image.load("snow.png").convert_alpha(), (self.snowSize, self.snowSize))
        self.x = randrange(0, width - self.snowSize, 13)
        self.speed = randint(10, 18)
        self.tochedToGround = False
        self.timeCount = 0

    def draw(self, sc):
        sc.blit(self.image, (self.x, self.y))
    def move(self, height, width, snows, fps):
        xchanche = randint(-3, 3)
        self.timeCount += 1
        self.x += xchanche
        if self.timeCount >= fps * 6 and self.tochedToGround:
            self.y += self.speed
        elif self.y > height:
            snows.remove(self)
        else:
            if self.y > (height - self.snowSize):
                self.y -= 4
                if not self.tochedToGround:
                    for i in range(2):
                        snows.append(Snow(width))
                    self.tochedToGround = True
            else:
                self.y += self.speed
        return snows


for i in range(35):
    snows.append(Snow(width))


while inWindow:
    sc.fill((0, 0, 0))
    sc.blit(bg, (0, 0))
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            inWindow = False
    for snow in snows:
        snows = snow.move(height, width, snows, fps)
        snow.draw(sc)


    pygame.display.flip()
    clock.tick(fps)
