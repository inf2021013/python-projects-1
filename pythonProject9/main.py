import pygame
import time
wn = pygame.display.set_mode((800,600))
pygame.init()
def window():
    wn.fill((0,0,0))
    pygame.display.update()
start_ticks = pygame.time.get_ticks()
run = True
while run:
    seconds = (pygame.time.get_ticks() - start_ticks)
    window()

    print(seconds)
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            run = False

pygame.quit()