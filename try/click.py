import pygame
import time
pygame.init()
wn = pygame.display.set_mode((600,600))

button = [pygame.image.load(''),pygame.image.load('')]
def draw_window(i):
    wn.blit(button[i],(300,300))
    pygame.display.update()

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

