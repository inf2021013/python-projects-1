import pygame

screen = pygame.display.set_mode((400,500))

back_ground_image = pygame.image.load('flappy bird BG.png')
back_ground = pygame.transform.scale(back_ground_image,(800,500))
screen_rect=pygame.Rect(0,0,0,0)
def draw_window():
    screen.blit(back_ground,(screen_rect.x,screen_rect.y))
    pygame.display.update()
run=True
while run:
    if screen_rect.x<-200:
        screen_rect.x=0
    else:
        screen_rect.x-= 1
    draw_window()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

pygame.quit()