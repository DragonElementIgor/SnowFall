import pygame
from random import randrange, randint
pygame.init()


def snowFallInit(width):
    snowFall = []
    for i in range(85):
        snowFall.append(Snow(width))
    return snowFall

def drawSnowLayer(snowLayer, width, sc, height):
    pygame.draw.rect(sc, (255,255,255), rect=(0, height-snowLayer, width, snowLayer))

def drawSun(sunColor, radiusSun, sc, width):
    pygame.draw.circle(sc, sunColor, (width - radiusSun - 30, radiusSun + 50), radiusSun)
class Snow:
    def __init__(self, width):
        super().__init__()
        self.minSnowSize = 32
        self.snowSize = randint(self.minSnowSize, 46)
        self.y = 0 - randint(self.snowSize, self.snowSize+20)
        self.image = pygame.transform.scale(pygame.image.load("snow.png").convert_alpha(), (self.snowSize, self.snowSize))
        self.x = randrange(0, width - self.snowSize, 22)
        self.speed = randint(10, 18)
        self.tochedToGround = False
        self.timeCount = 0

    def draw(self, sc):
        sc.blit(self.image, (self.x, self.y))
    def move(self, height, width, snows, fps, bigSnows, snowLayer):
        xchanche = randint(-2, 2)
        self.timeCount += 1
        self.x += xchanche
        if self.timeCount >= fps * 7 and self.tochedToGround:
            self.y += self.speed
        if self.y >= height or self.x < 0 - self.snowSize or self.x > width:
            snows.remove(self)
            if self.snowSize == self.minSnowSize:
                snowLayer += 1
            else:
                snowLayer += (self.snowSize - self.minSnowSize) // 3
        else:
            if self.y > (height - self.snowSize):
                self.y -= 4
                if not self.tochedToGround:
                    if not bigSnows:
                        #for i in range(3):
                        snows.append(Snow(width))
                    self.tochedToGround = True
            else:
                self.y += self.speed
        return (snows, snowLayer)
