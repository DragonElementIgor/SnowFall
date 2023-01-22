from snowFall import *
from win32api import GetSystemMetrics

width = GetSystemMetrics(0)
height = GetSystemMetrics(1)
bg = pygame.transform.scale(pygame.image.load("bg.png"), (width, height))
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

pygame.mixer.music.load('bgMusic.mp3')
pygame.mixer.music.set_volume(0.2)
pygame.mixer.music.play(-1)


snows = snowFallInit(width)