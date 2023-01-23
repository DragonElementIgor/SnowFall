from settings import *


while inWindow:
    sc.fill((0, 0, 0))
    sc.blit(bg, (0, 0))
    if len(snows) >= 240:
        bigSnows = True
    if snowLayer >= maxSnowLayer:
        timeHotSnow = True
    if bigSnows:
        if len(snows) < 160:
            bigSnows = False
    if timeHotSnow:
        if snowLayer < minSnowLayer:
            timeHotSnow = False
            maxSnowLayer = randint(height / 2 - 140, height / 2 + 30)
            minSnowLayer = randint(135, 200)
        snowLayer -= 6
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            inWindow = False
        key_ESC = pygame.key.get_pressed()[pygame.K_ESCAPE]
        if key_ESC:
            inWindow = False
    if timeHotSnow:
        drawSun(sunColor, 90, sc, width)
    for snow in snows:
        snows, snowLayer = snow.move(height, width, snows, fps, bigSnows, snowLayer)
        snow.draw(sc)
    drawSnowLayer(snowLayer, width, sc, height)

    pygame.display.flip()
    clock.tick(fps)
