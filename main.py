from settings import *

while inWindow:
    sc.fill((0, 0, 0))
    sc.blit(bg, (0, 0))
    if len(snows) >= 290:
        bigSnows = True
    if bigSnows:
        if len(snows) < 160:
            bigSnows = False
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            inWindow = False
    for snow in snows:
        snows = snow.move(height, width, snows, fps, bigSnows)
        snow.draw(sc)

    pygame.display.flip()
    clock.tick(fps)
