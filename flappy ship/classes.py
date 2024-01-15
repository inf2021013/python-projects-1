import pygame
import random
from pygame import mixer
import time
ship_scale = 0.6
background_scale = 1
pygame.init()
class Ship(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        # Βάζω σε μία λίστα από sprites τις εικόνες του διαστημοπλοίου για να μπορώ να τις αλλάζω πιο εύκολα:
        self.sprites = [
            pygame.transform.scale(pygame.image.load('images/ship.png'), (int(110 *ship_scale), int(109*ship_scale)))
        ]
        self.current_sprite = 0     # Αρχικοποίηση του τρέχον sprite.
        self.image = self.sprites[
            self.current_sprite     # Η εικόνα του διαστημοπλοίου ανάλογα ποιο είναι το τρέχον sprite.
        ]
        # Το διαστημόπλοιο ως rectangle και οι συντεταγμένες του
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.acceleration = 0.3  # Αρχικοποίηση της επιτάχυνσης
        self.velocity = 0  # Αρχικοποίηση της ταχύτητας
        self.clicked = False  # Δηλώνει ότι δεν έχει κάνει κλικ ο χρήστης ακόμα στην οθόνη
        self.sound = mixer.Sound('sounds/jump_sound.wav')  # Φορτώνει τον ήχο "jump" του διαστημόπλοιου.
        self.sound.set_volume(0.1)

    def update(self, GAME_OVER):
        # Ελέγχει αν έχει τελειώσει το παιχνίδι.
        if not GAME_OVER:
            # gravity
            self.rect.y += self.velocity
            self.velocity += self.acceleration
            # control velocity:
            if self.velocity >= 11:
                self.velocity = 11
            # jump
            if pygame.mouse.get_pressed()[0] == 1 and not self.clicked:
                # Αν ο χρήστης κάνει click και το STOP_GAME είναι False τότε το διαστημόπλοιο θα χοροπηδήσει:
                self.sound.play(0)
                self.clicked = True
                self.velocity = -4
            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False
            # Δεν αφήνει το διαστημόπλοιο να ξεπεράσει τα όρια του παραθύρου :
            if self.rect.y <= 0:
                self.rect.y = 0

    # Όταν καλείται η συνάρτηση αυτή τότε το διαστημόπλοιο πέφτει μέχρι να ακουμπήσει το έδαφος.
    def drown(self):
        self.rect.y += 2
        if self.rect.y >= 550:
            self.rect.y = 550
    def fall(self):
        self.rect.y += 5
        if self.rect.y >= 550:
            self.rect.y = 550

    # Όταν καλείται τότε αλλάζει η εικόνα του διαστημοπλοίου.
    def change_sprite(self, current_sprite):
        self.current_sprite = current_sprite
        self.image = self.sprites[self.current_sprite]

class Pipe(pygame.sprite.Sprite):
    def __init__(self, x, y, position):
        pipe_gap = random.randint(120, 200)  # Το κενό που υπάρχει ανάμεσα στο πάνω και στο κάτω μέρος του εμποδίου.
        pygame.sprite.Sprite.__init__(self)  # Αρχικοποίηση των sprites μέσα στην κλάση
        self.image = pygame.transform.scale(pygame.image.load('images/pipe.png'), (100, 1137))  # Φόρτωση εμποδίων
        self.rect = self.image.get_rect()  # Δήλωση εμποδίων σε μορφή rectangle
        if position == 1:  # Αν η παράμετρος position που έχουμε δώσει στην κλάση είναι 1
            self.image = pygame.transform.flip(self.image, False, True)  # τότε δηλώνεται το πάνω μέρος του εμποδίου
            self.rect.bottomleft = [x, y - int(pipe_gap / 2)]  # και οι συντεταγμένες του
        if position == -1:  # Αν η παράμετρος position που έχουμε δώσει στην κλάση είναι -1
            '''
                Τότε δηλώνεται το κάτω μέρος του εμποδίου,
                καθώς και οι συντεταγμένες του:
            '''
            self.rect.topleft = [x, y + int(pipe_gap / 2)]

    # ΌΣΟ καλείται η συνάρτηση update τότε το κάθε εμπόδιο προχωράει προς τα αριστερά μέχρι να βγει εκτός παραθύρου
    def update(self, speed):
        self.rect.x -= speed
        if self.rect.right < 0:
            self.kill()

