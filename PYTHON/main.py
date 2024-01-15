import pygame
import sys
pygame.font.init()
turquoise = (0, 200, 205)
pygame.joystick.init()
window = (width, height) = (800, 500)
wn = pygame.display.set_mode(window)
ob = pygame.image.load('spaceship.gif')
ob=pygame.transform.scale(ob,(90,80))
def draw_screen(ob_pos):
    wn.fill(turquoise)
    wn.blit(ob,(ob_pos.x,ob_pos.y))
    pygame.display.update()



run = True
while run:
    ob_pos=pygame.Rect(300, 200, 75, 100)
    controller_X = pygame.CONTROLLER_BUTTON_X
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == JOYBUTTONDOWN:
            ob_pos.x -= 3
    draw_screen(ob_pos)
pygame.quit()


