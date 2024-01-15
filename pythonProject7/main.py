import pygame
pygame.init()
run = True
wn3 = pygame.display.set_mode((800,500))
wn4 =pygame.display.set_mode((400,600))
def wn():
    wn3.fill((255,255,255))
    pygame.display.update
def wn2():
    wn4.fill((255,0,0))
    pygame.display.update()
while run:
    wn()
    wn2()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
pygame.quit()