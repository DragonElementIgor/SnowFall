from settings import *

while inWindow:
    sc.fill((0, 0, 0))
    sc.blit(bg, (0, 0))
    if len(snows) >= 240:
        bigSnows = True
    if snowLayer >= height/2-140:
        timeHotSnow = True
    if bigSnows:
        if len(snows) < 160:
            bigSnows = False
    if timeHotSnow:
        if snowLayer < 135:
            timeHotSnow = False
        snowLayer -= 6
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            inWindow = False
    if timeHotSnow:
        drawSun(sunColor, 70, sc, width)
    for snow in snows:
        snows, snowLayer = snow.move(height, width, snows, fps, bigSnows, snowLayer)
        snow.draw(sc)
    drawSnowLayer(snowLayer, width, sc, height)

    pygame.display.flip()
    clock.tick(fps)
