import pygame
wn = pygame.display.set_mode((800,600))
button_width = 89
button_height = 20
button_rect = pygame.Rect(400,100,button_width,button_height)
'''
CLASSES

'''
class Button(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        self.sprites.append(pygame.transform.scale(pygame.image.load('o.gif').convert_alpha(),(89,20)))
        self.sprites.append(pygame.transform.scale(pygame.image.load('o1.gif').convert_alpha(),(100,20)))
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.clicked = False
        self.i = 0
    def check_button_clicked(self):
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                return True

            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False


    def change_sprite(self,i):
        self.current_sprite = i
        self.image = self.sprites[self.current_sprite]
button_group = pygame.sprite.Group()
button = Button(button_rect.x,button_rect.y)

button_group.add(button)

i=0
'''
menu
'''
def draw_menu(wn):
    wn.fill((255,255,255))
    button_group.draw(wn)
    button.change_sprite(0)
    pygame.display.update()
run_menu = True
run_game = True
'''            
main game
'''
def MAIN_GAME(wn):
    wn.fill((0, 0, 0))
    button_group.draw(wn)
    button.change_sprite(1)
    pygame.display.update()
run = True
while run:


    while run_menu:
        draw_menu(wn)

        keys = pygame.key.get_pressed()

        if button.check_button_clicked() == True:
            run_menu = False
            run_game = True
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run_menu = False
                run = False
                run_game = False


    while run_game:
        MAIN_GAME(wn)
        keys = pygame.key.get_pressed()
        if button.check_button_clicked() == True:
            run_game = False
            run_menu = True
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run_game = False
                run = False

pygame.quit()