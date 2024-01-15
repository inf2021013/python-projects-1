import pygame
from pygame import mixer
pygame.init()
pygame.mixer.pre_init(44100, -16, 2, 2048)
pygame.mixer.init()
# CLASS:
class Object(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(pygame.image.load('object.gif'),(40,20))
        self.rect = self.image.get_rect()
        self.rect.center = [x,y]
    def update(self):
        pos = pygame.mouse.get_pos()
        x,y = pos
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0]:
                self.rect.x = x-27.5
                if self.rect.x < 50:
                    self.rect.x = 50
                if self.rect.x > 469:
                    self.rect.x = 469
class Song_button(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.spites= [
            pygame.transform.scale(pygame.image.load('OFF_button.gif'), (120, 60)),
            pygame.transform.scale(pygame.image.load('ON_button.gif'), (120, 60)),
        ]
        self.current_sprite = 0
        self.image = self.spites[self.current_sprite]
        self.rect = self.image.get_rect()
        mixer.music.load('space_music.wav')
        self.rect.center = [x, y]
        self.clicked = False
        self.clicked_counter = 0
    def update(self):
        if self.clicked_counter % 2 == 0:
            self.current_sprite = 0
            self.image = self.spites[self.current_sprite]
            mixer.music.stop()
            self.played_music = True
        if self.clicked_counter % 2 == 1:
            self.current_sprite = 1
            if self.played_music == True:
                mixer.music.play(-1)
                self.played_music = False
            self.image = self.spites[self.current_sprite]
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] and not self.clicked:
                self.clicked = True
                self.clicked_counter+=1
            if not pygame.mouse.get_pressed()[0]:
                self.clicked = False
class Line(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(pygame.image.load('line.gif'), (500, 5))
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
class Small_line(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(pygame.image.load('small_line.gif'), (5, 40))
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]

# MUSIC:
mixer.music.load('space_music.wav')
# GROUPS:
object_group = pygame.sprite.Group()
object = Object(150,200)
object_group.add(object)
line_group = pygame.sprite.Group()
line = Line(300,203)
line_group.add(line)
x=50
small_line_group = pygame.sprite.Group()
small_line=[]
for i in range(11):
    small_line.append(Small_line(x,203))
    x+=50
small_line_group.add(small_line)
# song_button
song_button_group = pygame.sprite.Group()
song_button = Song_button(200,400)
song_button_group.add(song_button)

vol = []
for i in range(11):
    if pygame.sprite.spritecollideany(small_line[i], object_group):
        vol.append(i*0.1)


# FUNCTIONS:
def draw_window():
    wn.fill((255, 255, 255))
    song_button_group.draw(wn)
    line_group.draw(wn)
    small_line_group.draw(wn)
    object_group.draw(wn)
    pygame.display.update()
run = True
wn = pygame.display.set_mode((800,600))
while run:
    draw_window()
    song_button_group.update()
    object_group.update()
    mixer.music.set_volume()
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            run = False

pygame.quit()