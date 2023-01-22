from snowFall import *

bg = pygame.image.load("bg.png")
width = 1600
height = 1000
sc = pygame.display.set_mode((width, height))
pygame.display.set_caption("New Year!")
pygame.display.set_icon(pygame.image.load("snow.png"))
inWindow = True
clock = pygame.time.Clock()
fps = 14
bigSnows = False
snowLayer = 0
timeHotSnow = False
sunColor = "#FFD500"

snows = snowFallInit(width)