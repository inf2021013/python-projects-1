import pygame              # Για τη δημιουργία του παιχνιδιού.
import os                  # Για να βρίσκει το path των φακέλων από το λογισμικό

'''
    ΚΛΑΣΗ ΕΜΠΟΔΙΩΝ:
'''
class pipe(pygame.sprite.Sprite):
    def __init__(self,x,y,position):
        pipe_gap = 200                          # Το κενό που υπάρχει ανάμεσα στο πάνω και στο κάτω μέρος του εμποδίου.
        pygame.sprite.Sprite.__init__(self)     # Αρχικοποίηση των sprites μέσα στην κλάση
        self.image = pygame.transform.scale(pygame.image.load('images/pipes.gif'),(89,286))  # Φόρτωση εμποδίων
        self.rect = self.image.get_rect()       # Δήλωση εμποδίων σε μορφή rectangle
        if position == 1:                       # Αν η παράμετρος position που έχουμε δώσει στην κλάση είναι 1
            self.image =pygame.transform.flip(self.image, False, True)  # τότε δηλώνεται το πάνω μέρος του εμποδίου
            self.rect.bottomleft = [x, y - int(pipe_gap/2)]             # και συντεταγμένες του
        if position == -1:                      # Αν η παράμετρος position που έχουμε δώσει στην κλάση είναι -1
            '''
                Τότε δηλώνεται το κάτω μέρος του εμποδίου,
                καθώς και οι συντεταγμένες του:
            '''
            self.rect.topleft = [x, y + int(pipe_gap/2)]

    # ΌΣΟ καλείται η συνάρτηση update τότε το κάθε εμπόδιο προχωράει προς τα αριστερά μέχρι να βγει εκτός παραθύρου
    def update(self):
        self.rect.x -= 4
        if self.rect.right < 0:
            self.kill()

'''
    ΚΛΑΣΗ ΤΟΥ ΥΠΟΛΟΙΠΟΥ ΤΩΝ ΕΜΠΟΔΙΩΝ:
'''
class restpipe(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        # Φόρτωση της εικόνας του υπολοίπου του εμποδίου και ως rectangle
        self.image = pygame.transform.scale(pygame.image.load(os.path.join('images','missing_pipe.gif')),(89,20))
        self.rect = self.image.get_rect()
        self.rect.topleft = [x, y]  # βρίσκεται στη βάση του κάθε Εμποδίου

# ΌΣΟ καλείται η συνάρτηση update τότε το κάθε υπόλοιπο εμπόδιο προχωράει προς τα αριστερά μέχρι να βγει εκτός παραθύρου
    def update(self):
        self.rect.x -= 4
        if self.rect.right < 0:
            self.kill()

'''
    ΚΛΑΣΗ ΔΙΑΣΤΗΜΟΠΛΟΙΟΥ:
'''
class spaceship(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        # Βάζω σε μία λίστα από sprites τις εικόνες του διαστημοπλοίου για να μπορώ να τις αλλάζω πιο εύκολα:
        self.sprites = []
        self.sprites.append(pygame.transform.scale(pygame.image.load('images/spaceship.gif').convert_alpha(), (64, 56)))
        self.sprites.append(pygame.transform.scale(pygame.image.load('images/spaceship_power_up_ON.png').convert_alpha(), (64, 56)))
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]
        # Το διαστημόπλοιο ως rectangle και οι συντεταγμένες του
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.acceleration = 0.3     # Αρχικοποίηση της επιτάχυνσης
        self.velocity = 0           # Αρχικοποίηση της ταχύτητας
        self.clicked = False        # Δηλώνει ότι δεν έχει κάνει κλικ ο χρήστης ακόμα στην οθόνη
        self.GAMEOVER = False       # Δηλώνει ότι δεν έχει χάσει ο παίκτης ακόμα
        self.STOP_GAME = False      # Δηλώνει ότι δεν έχει τελειώσει το παιχνίδι ακόμα
    def update(self):
        # Ελέγχει αν έχει τελειώσει το παιχνίδι.
        if self.STOP_GAME == False:
            # gravity
            self.rect.y += self.velocity
            self.velocity += self.acceleration
            # jump
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                self.velocity = -4
            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False
            # Δεν αφήνει το διαστημόπλοιο να ξεπεράσει τα όρια του παραθύρου :
            if self.rect.y <= 0:
                self.rect.y = 0
            # CHECK FOR GAME OVER:
            if self.rect.y >= 450:
                self.GAMEΟVER = True
            if self.GAMEOVER == True :
                self.STOP_GAME = True
    # Επιστρέφει στο κύριο παιχνίδι αν έχει χάσει ο παίκτης.
    def game_over(self):
        if self.GAMEOVER == True:
            return True
    # Όταν καλείται η συνάρτηση αυτή τότε το διαστημόπλοιο πέφτει μέχρι να ακουμπήσει το έδαφος.
    def fall(self):
        self.rect.y += 10
        if self.rect.y >= 450:
            self.rect.y = 450
    # Όταν καλείται τότε αλλάζει η εικόνα του διαστημοπλοίου.
    def change_sprite(self, i):
        self.current_sprite = i
        self.image = self.sprites[self.current_sprite]

'''
    ΚΛΑΣΗ ΕΞΩΓΗΙΝΩΝ:
'''
class Alien(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        # Φόρτωση της εικόνας του κάθε εξωγήινου και ως rectangle καθώς και οι συντεταγμένες του.
        self.image = pygame.transform.scale(pygame.image.load(os.path.join('images','alien.gif')), (40, 40)).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = [x,y]

# ΌΣΟ καλείται η συνάρτηση update τότε ο κάθε εξωγήινος προχωράει προς τα αριστερά μέχρι να βγει εκτός παραθύρου.
    def update(self):
        self.rect.x -= 4
        if self.rect.right < 0:
            self.kill()

'''
    ΚΛΑΣΗ ΠΥΡΑΥΛΩΝ:
'''
class rocket(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        # Φόρτωση της εικόνας του πυραύλου και ως rectangle καθώς και οι συντεταγμένες του.
        self.image = pygame.transform.scale(pygame.image.load(os.path.join('images','rocket.gif')), (84, 46)).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]

# ΌΣΟ καλείται η συνάρτηση update τότε ο κάθε πύραυλος προχωράει προς τα αριστερά μέχρι να βγει εκτός παραθύρου.
    def update(self):
        self.rect.x -= 15
        if self.rect.right < 0:
            self.kill()

'''
    ΚΛΑΣΗ POWER_UPS:
'''
class PowerUp(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        # Φόρτωση της εικόνας των power_ups και ως rectangle καθώς και οι συντεταγμένες τους.
        self.image = pygame.transform.scale(pygame.image.load(os.path.join('images','power_up.gif')).convert_alpha(), (40, 40))
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]

# ΌΣΟ καλείται η συνάρτηση update τότε το κάθε power_up προχωράει προς τα δεξιά μέχρι να βγει εκτός παραθύρου.
    def update(self):
        self.rect.x -= 4
        if self.rect.right < 0:
            self.kill()