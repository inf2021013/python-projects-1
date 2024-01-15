import random
import time

import pygame              # Για τη δημιουργία του παιχνιδιού.
import os                  # Για να βρίσκει το path των φακέλων από το λογισμικό
from pygame import mixer   # Για τη χρήση μουσικής και ηχητικών εφέ
'''
    ΚΛΑΣΗ ΕΜΠΟΔΙΩΝ:
'''
class pipe(pygame.sprite.Sprite):
    def __init__(self,x,y,position):
        pipe_gap = random.randint(120,200)                          # Το κενό που υπάρχει ανάμεσα στο πάνω και στο κάτω μέρος του εμποδίου.
        pygame.sprite.Sprite.__init__(self)     # Αρχικοποίηση των sprites μέσα στην κλάση
        self.image = pygame.transform.scale(pygame.image.load('images/pipes.gif'),(89,286))  # Φόρτωση εμποδίων
        self.rect = self.image.get_rect()       # Δήλωση εμποδίων σε μορφή rectangle
        if position == 1:                       # Αν η παράμετρος position που έχουμε δώσει στην κλάση είναι 1
            self.image =pygame.transform.flip(self.image, False, True)  # τότε δηλώνεται το πάνω μέρος του εμποδίου
            self.rect.bottomleft = [x, y - int(pipe_gap/2)]             # και οι συντεταγμένες του
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
        self.x = x
        self.y = y
        # Βάζω σε μία λίστα από sprites τις εικόνες του διαστημοπλοίου για να μπορώ να τις αλλάζω πιο εύκολα:
        self.sprites = []
        self.sprites.append(pygame.transform.scale(pygame.image.load('images/Spaceship_1.gif').convert_alpha(), (64, 56)))
        self.sprites.append(pygame.transform.scale(pygame.image.load('images/Spaceship_1_power_up_ON.png').convert_alpha(), (64, 56)))
        self.sprites.append(pygame.transform.scale(pygame.image.load('images/Spaceship_2.gif').convert_alpha(), (64, 56)))
        self.sprites.append(pygame.transform.scale(pygame.image.load('images/Spaceship_2_power_up_ON.gif').convert_alpha(), (64, 56)))
        self.sprites.append(pygame.transform.scale(pygame.image.load('images/Spaceship_3.gif').convert_alpha(), (64, 56)))
        self.sprites.append(pygame.transform.scale(pygame.image.load('images/Spaceship_3_power_up_ON.gif').convert_alpha(), (64, 56)))
        self.sprites.append(pygame.transform.scale(pygame.image.load('images/Spaceship_4.gif').convert_alpha(), (64, 56)))
        self.sprites.append(pygame.transform.scale(pygame.image.load('images/Spaceship_4_power_up_ON.gif').convert_alpha(), (64, 56)))
        self.sprites.append(pygame.transform.scale(pygame.image.load('images/Spaceship_5.gif').convert_alpha(), (64, 56)))
        self.sprites.append(pygame.transform.scale(pygame.image.load('images/Spaceship_5_power_up_ON.gif').convert_alpha(), (64, 56)))
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]
        # Το διαστημόπλοιο ως rectangle και οι συντεταγμένες του
        self.rect = self.image.get_rect()
        self.rect.center = [self.x, self.y]
        self.acceleration = 0.3     # Αρχικοποίηση της επιτάχυνσης
        self.velocity = 0           # Αρχικοποίηση της ταχύτητας
        self.clicked = False        # Δηλώνει ότι δεν έχει κάνει κλικ ο χρήστης ακόμα στην οθόνη

    def update(self,GAME_OVER):
        # Ελέγχει αν έχει τελειώσει το παιχνίδι.
        if GAME_OVER == False:
            # gravity
            self.rect.y += self.velocity
            self.velocity += self.acceleration
            # control velocity:
            if self.velocity >= 11:
                self.velocity = 11
            # jump
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                self.velocity = -4
            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False
            # Δεν αφήνει το διαστημόπλοιο να ξεπεράσει τα όρια του παραθύρου :
            if self.rect.y <= 0:
                self.rect.y = 0
    # Όταν καλείται η συνάρτηση αυτή τότε το διαστημόπλοιο πέφτει μέχρι να ακουμπήσει το έδαφος.
    def fall(self):
        self.rect.y += 10
        if self.rect.y >= 450:
            self.rect.y = 450
    # Όταν καλείται τότε αλλάζει η εικόνα του διαστημοπλοίου.
    def change_sprite(self, current_sprite):
        self.current_sprite = current_sprite
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
'''
        MENU BUTTON:
'''
class play_button(pygame.sprite.Sprite):
    '''
        Αρχικόποίηση μεταβλητών όπως όλα τα sprites (Εικόνες) της κλάσης σε μια λίστα, το τρέχον sprite της λίστας,
        την μετατροπή τους σε rectangle, τη θέση τους, το ήχο του κουμπιού και την ένταση τους.
    '''
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        self.sprites.append(pygame.transform.scale(pygame.image.load('images/play_button.gif').convert_alpha(),(120*0.8,64*0.8)))
        self.sprites.append(pygame.transform.scale(pygame.image.load('images/play_button.gif').convert_alpha(),(120,64)))
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.clicked = False
        self.i = 0
        self.sound = mixer.Sound(os.path.join('sounds', 'button_sound.wav'))
        self.sound_check = True
        self.sound.set_volume(0.05)
    '''
        Η συνάρτηση αυτή, αρχικά ελέγχει αν ο χρήστης έχει το ποντίκι πάνω στο κουμπί και αν το έχει
        τότε η εικόνα του κουμπιού μεγαλώνει και ακουγέται ένας συγκεκριμένος ήχος.
        Όσο δεν το έχει πάνω στο κουμπί τότε η εικόνα του επιστρέφει στο αρχικό της μέγεθος.
        Επίσης, μόνο αν το έχει πάνω στο κουμπί και πατήσει κλικ τότε η συνάρτηση επιστρέφει true.
    '''
    def check_button_clicked(self):
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            self.current_sprite = 1
            self.image = self.sprites[self.current_sprite]
            if self.sound_check == True:
                self.sound.play(0)
                self.sound_check = False
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                time.sleep(0.1)
                return True
            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False
        else:
            self.current_sprite = 0
            self.image = self.sprites[self.current_sprite]
            self.sound_check = True
'''
        Retry button:
'''

class retry_button(pygame.sprite.Sprite):
    '''
        Αρχικόποίηση μεταβλητών όπως όλα τα sprites (Εικόνες) της κλάσης σε μια λίστα, το τρέχον sprite της λίστας,
        την μετατροπή τους σε rectangle, τη θέση τους, το ήχο του κουμπιού και την ένταση τους.
    '''
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        self.sprites.append(pygame.transform.scale(pygame.image.load('images/retry_button.gif').convert_alpha(),(120*0.9,44*0.9)))
        self.sprites.append(pygame.transform.scale(pygame.image.load('images/retry_button.gif').convert_alpha(),(120,44)))
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.clicked = False
        self.sound = mixer.Sound(os.path.join('sounds', 'button_sound.wav'))
        self.sound_check = True
        self.sound.set_volume(0.05)

    '''
           Η συνάρτηση αυτή, αρχικά ελέγχει αν ο χρήστης έχει το ποντίκι πάνω στο κουμπί και αν το έχει
           τότε η εικόνα του κουμπιού μεγαλώνει και ακουγέται ένας συγκεκριμένος ήχος.
           Όσο δεν το έχει πάνω στο κουμπί τότε η εικόνα του επιστρέφει στο αρχικό της μέγεθος.
           Επίσης, μόνο αν το έχει πάνω στο κουμπί και πατήσει κλικ τότε η συνάρτηση επιστρέφει true.
    '''
    def check_retry_button_clicked(self):
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            self.current_sprite = 1
            if self.sound_check == True:
                self.sound.play(0)
                self.sound_check = False
            self.image = self.sprites[self.current_sprite]
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                time.sleep(0.1)
                return True
            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False
        else:
            self.current_sprite = 0
            self.image = self.sprites[self.current_sprite]
            self.sound_check = True
'''
        ANIMATION 2:
'''
class animation_2(pygame.sprite.Sprite):
    def __init__(self,x,y,limit,name):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        # Βάζω σε μία λίστα από sprites το διαστημοπλοίο που έχει κάθε φορά διαφορετική εικόνα στο πρώτο animation:
        self.sprites.append(pygame.transform.scale(pygame.image.load(name).convert_alpha(), (30, 26)))
        self.current_sprite = 0      # αρχικοποιήση του τρέχον sprite
        self.image = self.sprites[self.current_sprite] # η εικόνα του διαστημοπλοίου ανάλογα ποιο είναι το τρέχον sprite
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]       # η θέση του κάθε διαστημοπλοίου.
        self.acceleration = 0.3         # Αρχικοποίηση της επιτάχυνσης.
        self.velocity = 0               # Αρχικοποίηση της ταχύτητας.
        self.limit = limit              # το όριο το οποίο δεν μπορεί να ξεπεράσει κάθε διαστημόπλοιο.
        self.ended = False              # δηλώνει οτι δεν έχει τελειώσει το δεύτερο animation

    '''
        Αυτή η συνάρτηση καλείται όσο ο μετρητής των πόσων animations έχουν ολοκληρωθεί είναι μονός αριθμός.
        Όταν επιτρέπεται να καλεστεί τότε εμφανίζει ταυτόχρονα και τα πέντε skins των διαστημόπλοίων, 
        το ένα κάτω από το άλλο να χοροπηδάνε και να κινούνται προς τα δεξιά συνεχώς μέχρι να βρεθούνε εκτός οθόνης
        ώσπου αυξάνεται ο μετρητής των animations που έχουν ολοκληρωθεί κατά 1.
    '''
    def update(self,width,allow_animation_2,animation_count):
        self.animation_count = animation_count
        if self.animation_count % 2 == 1:
            self.ended = False
        if allow_animation_2 == True:
            self.rect.y += self.velocity
            self.velocity += self.acceleration
            if self.velocity > 5:
                self.velocity = -5
            self.rect.x += 3
            if self.rect.y <= self.limit:
                self.rect.y = self.limit
            if self.rect.x >= width + 18:
                self.ended = True
                self.rect.x = - 40
                self.animation_count+=1
            time.sleep(0.0018)
    # Επιστρέφει το μέγεθος του μετρητή των animations που έχουν ολοκληρωθεί στο κύριο πρόγραμμα.
    def Animation_count(self):
        return self.animation_count
    # Ελέχγει αν έχει τελείωσει το συγκεκριμένο animation ώστε να ξανα-ξεκινήσει το άλλο.
    def check(self):
        if self.ended == True:
            return True
        else:
            return False
'''
        ANIMATION 1:
'''
class animation_1(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        # Βάζω σε μία λίστα από sprites τις εικόνες του διαστημοπλοίου για να μπορώ να τις αλλάζω πιο εύκολα:
        self.sprites.append(pygame.transform.scale(pygame.image.load('images/Spaceship_1.gif').convert_alpha(), (30, 26)))
        self.sprites.append(pygame.transform.scale(pygame.image.load('images/Spaceship_2.gif').convert_alpha(), (30, 26)))
        self.sprites.append(pygame.transform.scale(pygame.image.load('images/Spaceship_3.gif').convert_alpha(), (30, 26)))
        self.sprites.append(pygame.transform.scale(pygame.image.load('images/Spaceship_4.gif').convert_alpha(), (30, 26)))
        self.sprites.append(pygame.transform.scale(pygame.image.load('images/Spaceship_5.gif').convert_alpha(), (30, 26)))
        self.current_sprite = 0         # αρχικοποιήση του τρέχον sprite
        self.image = self.sprites[self.current_sprite] # η εικόνα του διαστημοπλοίου ανάλογα ποιο είναι το τρέχον sprite
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]       # η θέση του κάθε διαστημοπλοίου.
        self.acceleration = 0.3         # Αρχικοποίηση της επιτάχυνσης
        self.velocity = 0               # Αρχικοποίηση της ταχύτητας
        self.limit = 70                 # το όριο το οποίο δεν μπορεί να ξεπεράσει κάθε διαστημόπλοιο.
        self.ended = False

    '''
            Αυτή η συνάρτηση καλείται όσο ο μετρητής των πόσων animations έχουν ολοκληρωθεί είναι ζυγός αριθμός.
            Όταν επιτρέπεται να καλεστεί τότε εμφανίζεται το κάθε skin του διαστημοπλοίου, 
            το ένα μετά από το άλλο, να χοροπηδαεί και να κινείται προς τα δεξιά συνεχώς μέχρι να βρεθεί εκτός οθόνης
            ώσπου όταν και τα 5 εμφανιστούν, τότε αυξάνεται ο μετρητής των animations που έχουν ολοκληρωθεί κατά 1.
    '''
    def update(self,width,allow_animation_1,animation_count):
        self.animation_count = animation_count
        if self.animation_count % 2 == 0:
            self.ended = False
        if allow_animation_1 == True:
            self.rect.y += self.velocity
            self.velocity += self.acceleration
            if self.velocity > 5:
                self.velocity = -5
            self.rect.x += 3
            if self.rect.y <= self.limit:
                self.rect.y = self.limit
            if self.rect.x >= width + 18:
                self.rect.x = -40
                self.current_sprite += 1
                self.limit += 100
                self.rect.y += 100
                if self.current_sprite > 4:
                    self.limit = 70
                    self.rect.y = 100
                    self.ended = True
                    self.animation_count += 1
                    self.current_sprite = 0
            self.image = self.sprites[self.current_sprite]
            time.sleep(0.01)

    # Επιστρέφει το μέγεθος του μετρητή των animations που έχουν ολοκληρωθεί στο κύριο πρόγραμμα.
    def Animation_count(self):
        return self.animation_count

    # Ελέχγει αν έχει τελείωσει το συγκεκριμένο animation ώστε να ξανα-ξεκινήσει το άλλο.
    def check(self):
        if self.ended == True:
            return True
        else:
            return False
class menu_button(pygame.sprite.Sprite):
    '''
        Αρχικόποίηση μεταβλητών όπως όλα τα sprites (Εικόνες) της κλάσης σε μια λίστα, το τρέχον sprite της λίστας,
        την μετατροπή τους σε rectangle, τη θέση τους, το ήχο του κουμπιού και την ένταση τους.
    '''
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        self.sprites.append(pygame.transform.scale(pygame.image.load('images/menu_button.gif').convert_alpha(), (150 * 0.6, 64 * 0.6)))
        self.sprites.append(pygame.transform.scale(pygame.image.load('images/menu_button.gif').convert_alpha(), (150 * 0.8, 64 * 0.8)))
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.clicked = False
        self.i = 0
        self.sound = mixer.Sound(os.path.join('sounds', 'button_sound.wav'))
        self.sound_check = True
        self.sound.set_volume(0.05)
    '''
               Η συνάρτηση αυτή, αρχικά ελέγχει αν ο χρήστης έχει το ποντίκι πάνω στο κουμπί και αν το έχει
               τότε η εικόνα του κουμπιού μεγαλώνει και ακουγέται ένας συγκεκριμένος ήχος.
               Όσο δεν το έχει πάνω στο κουμπί τότε η εικόνα του επιστρέφει στο αρχικό της μέγεθος.
               Επίσης, μόνο αν το έχει πάνω στο κουμπί και πατήσει κλικ τότε η συνάρτηση επιστρέφει true.
    '''
    def check_menu_button_clicked(self):
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            self.current_sprite = 1
            if self.sound_check == True:
                self.sound.play(0)
                self.sound_check = False
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                time.sleep(0.1)
                return True
            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False
        else:
            self.current_sprite = 0
            self.sound_check = True
        self.image = self.sprites[self.current_sprite]
'''
        EXIT BUTTON:
'''
class exit_button(pygame.sprite.Sprite):
    '''
            Αρχικόποίηση μεταβλητών όπως όλα τα sprites (Εικόνες) της κλάσης σε μια λίστα, το τρέχον sprite της λίστας,
            την μετατροπή τους σε rectangle, τη θέση τους, το ήχο του κουμπιού και την ένταση τους.
    '''
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        self.sprites.append(pygame.transform.scale(pygame.image.load('images/exit_button.gif').convert_alpha(), (110 * 0.7, 39 * 0.7)))
        self.sprites.append(pygame.transform.scale(pygame.image.load('images/exit_button.gif').convert_alpha(), (110 * 0.9, 39 * 0.9)))
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.clicked = False
        self.sound = mixer.Sound(os.path.join('sounds', 'button_sound.wav'))
        self.sound_check = True
        self.sound.set_volume(0.05)
    '''
               Η συνάρτηση αυτή, αρχικά ελέγχει αν ο χρήστης έχει το ποντίκι πάνω στο κουμπί και αν το έχει
               τότε η εικόνα του κουμπιού μεγαλώνει και ακουγέται ένας συγκεκριμένος ήχος.
               Όσο δεν το έχει πάνω στο κουμπί τότε η εικόνα του επιστρέφει στο αρχικό της μέγεθος.
               Επίσης, μόνο αν το έχει πάνω στο κουμπί και πατήσει κλικ τότε η συνάρτηση επιστρέφει true.
    '''
    def check_button_clicked(self):
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            self.current_sprite = 1
            if self.sound_check == True:
                self.sound.play(0)
                self.sound_check = False
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                time.sleep(0.1)
                return True
            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False
        else:
            self.current_sprite = 0
            self.sound_check = True
        self.image = self.sprites[self.current_sprite]

'''
        GAME TITLE:
'''
class title(pygame.sprite.Sprite):
    '''
        Αρχικόποίηση μεταβλητών όπως όλα τα sprites (Εικόνες) της κλάσης σε μια λίστα, το τρέχον sprite
        και την μετατροπή τους σε rectangle.
    '''
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        self.sprites.append(pygame.transform.scale(pygame.image.load('images/title.gif').convert_alpha(), (400, 200)))
        self.sprites.append(pygame.transform.scale(pygame.image.load('images/title.gif').convert_alpha(), (400*1.05, 200*1.05)))
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]

    '''
        Η συνάρτηση update, αρχικά ελέγχει αν ο χρήστης έχει το ποντίκι πάνω στο τίτλο του παχνιδιού και αν το έχει
        τότε η εικόνα του τίτλου μεγαλώνει.
        Όσο δεν το έχει πάνω στον τίτλο τότε η εικόνα του επιστρέφει στο αρχικό της μέγεθος.          
    '''

    def update(self):
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            self.current_sprite = 1
        else:
            self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]
'''
        SKIN BUTTON:
'''
class skins_button(pygame.sprite.Sprite):
    '''
        Αρχικόποίηση μεταβλητών όπως όλα τα sprites (Εικόνες) της κλάσης σε μια λίστα, το τρέχον sprite της λίστας,
        την μετατροπή τους σε rectangle, τη θέση τους, το ήχο του κουμπιού και την ένταση τους.
    '''
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        self.sprites.append(pygame.transform.scale(pygame.image.load('images/skins_button.gif').convert_alpha(), (110 * 0.7, 39 * 0.7)))
        self.sprites.append(pygame.transform.scale(pygame.image.load('images/skins_button.gif').convert_alpha(), (110 * 0.9, 39 * 0.9)))
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.clicked = False
        self.sound = mixer.Sound(os.path.join('sounds', 'button_sound.wav'))
        self.sound_check = True
        self.sound.set_volume(0.05)
    '''
               Η συνάρτηση αυτή, αρχικά ελέγχει αν ο χρήστης έχει το ποντίκι πάνω στο κουμπί και αν το έχει
               τότε η εικόνα του κουμπιού μεγαλώνει και ακουγέται ένας συγκεκριμένος ήχος.
               Όσο δεν το έχει πάνω στο κουμπί τότε η εικόνα του επιστρέφει στο αρχικό της μέγεθος.
               Επίσης, μόνο αν το έχει πάνω στο κουμπί και πατήσει κλικ τότε η συνάρτηση επιστρέφει true.
    '''
    def check_button_clicked(self):
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            self.current_sprite = 1
            if self.sound_check == True:
                self.sound.play(0)
                self.sound_check = False
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                time.sleep(0.1)
                return True
            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False
        else:
            self.current_sprite = 0
            self.sound_check = True
        self.image = self.sprites[self.current_sprite]
'''
        SKIN 1:
'''
class skin_1(pygame.sprite.Sprite):
    '''
        Αρχικόποίηση μεταβλητών όπως όλα τα sprites (Εικόνες) της κλάσης σε μια λίστα, το τρέχον sprite της λίστας,
        την μετατροπή τους σε rectangle, τη θέση τους, το ήχο του κουμπιού και την ένταση τους.
    '''
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        self.sprites.append(pygame.transform.scale(pygame.image.load('images/skin_1.gif').convert_alpha(), (130 * 0.7, 109 * 0.7)))
        self.sprites.append(pygame.transform.scale(pygame.image.load('images/skin_1.gif').convert_alpha(), (130 * 0.9, 109 * 0.9)))
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.clicked = False
        self.sound = mixer.Sound(os.path.join('sounds', 'button_sound.wav'))
        self.sound_check = True
        self.sound.set_volume(0.05)

    '''
           Η συνάρτηση αυτή, αρχικά ελέγχει αν ο χρήστης έχει το ποντίκι πάνω στο κουμπί και αν το έχει
           τότε η εικόνα του κουμπιού μεγαλώνει και ακουγέται ένας συγκεκριμένος ήχος.
           Όσο δεν το έχει πάνω στο κουμπί τότε η εικόνα του επιστρέφει στο αρχικό της μέγεθος.
           Επίσης, μόνο αν το έχει πάνω στο κουμπί και πατήσει κλικ τότε η συνάρτηση επιστρέφει true.
    '''
    def check_button_clicked(self):
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            self.current_sprite = 1
            if self.sound_check == True:
                self.sound.play(0)
                self.sound_check = False
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                time.sleep(0.1)
                return True
            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False
        else:
            self.current_sprite = 0
            self.sound_check = True
        self.image = self.sprites[self.current_sprite]
'''
        SKIN 2:
'''
class skin_2(pygame.sprite.Sprite):
    '''
        Αρχικόποίηση μεταβλητών όπως όλα τα sprites (Εικόνες) της κλάσης σε μια λίστα, το τρέχον sprite της λίστας,
        την μετατροπή τους σε rectangle, τη θέση τους, το ήχο του κουμπιού και την ένταση τους.
    '''
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        self.sprites.append(pygame.transform.scale(pygame.image.load('images/skin_2.gif').convert_alpha(), (130 * 0.7, 109 * 0.7)))
        self.sprites.append(pygame.transform.scale(pygame.image.load('images/skin_2.gif').convert_alpha(), (130 * 0.9, 109 * 0.9)))
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.clicked = False
        self.sound = mixer.Sound(os.path.join('sounds', 'button_sound.wav'))
        self.sound_check = True
        self.sound.set_volume(0.05)

    '''
           Η συνάρτηση αυτή, αρχικά ελέγχει αν ο χρήστης έχει το ποντίκι πάνω στο κουμπί και αν το έχει
           τότε η εικόνα του κουμπιού μεγαλώνει και ακουγέται ένας συγκεκριμένος ήχος.
           Όσο δεν το έχει πάνω στο κουμπί τότε η εικόνα του επιστρέφει στο αρχικό της μέγεθος.
           Επίσης, μόνο αν το έχει πάνω στο κουμπί και πατήσει κλικ τότε η συνάρτηση επιστρέφει true.
    '''
    def check_button_clicked(self):
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            self.current_sprite = 1
            if self.sound_check == True:
                self.sound.play(0)
                self.sound_check = False
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                time.sleep(0.1)
                return True
            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False
        else:
            self.current_sprite = 0
            self.sound_check = True
        self.image = self.sprites[self.current_sprite]
'''
        SKIN 3:
'''
class skin_3(pygame.sprite.Sprite):
    '''
         Αρχικόποίηση μεταβλητών όπως όλα τα sprites (Εικόνες) της κλάσης σε μια λίστα, το τρέχον sprite της λίστας,
         την μετατροπή τους σε rectangle, τη θέση τους, το ήχο του κουμπιού και την ένταση τους.
    '''
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        self.sprites.append(pygame.transform.scale(pygame.image.load('images/skin_3.gif').convert_alpha(), (130 * 0.7, 109 * 0.7)))
        self.sprites.append(pygame.transform.scale(pygame.image.load('images/skin_3.gif').convert_alpha(), (130 * 0.9, 109 * 0.9)))
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.clicked = False
        self.sound = mixer.Sound(os.path.join('sounds', 'button_sound.wav'))
        self.sound_check = True
        self.sound.set_volume(0.05)

    '''
           Η συνάρτηση αυτή, αρχικά ελέγχει αν ο χρήστης έχει το ποντίκι πάνω στο κουμπί και αν το έχει
           τότε η εικόνα του κουμπιού μεγαλώνει και ακουγέται ένας συγκεκριμένος ήχος.
           Όσο δεν το έχει πάνω στο κουμπί τότε η εικόνα του επιστρέφει στο αρχικό της μέγεθος.
           Επίσης, μόνο αν το έχει πάνω στο κουμπί και πατήσει κλικ τότε η συνάρτηση επιστρέφει true.
    '''
    def check_button_clicked(self):
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            self.current_sprite = 1
            if self.sound_check == True:
                self.sound.play(0)
                self.sound_check = False
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                time.sleep(0.1)
                return True
            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False
        else:
            self.current_sprite = 0
            self.sound_check = True
        self.image = self.sprites[self.current_sprite]
'''
        SKIN 4:
'''
class skin_4(pygame.sprite.Sprite):
    '''
        Αρχικόποίηση μεταβλητών όπως όλα τα sprites (Εικόνες) της κλάσης σε μια λίστα, το τρέχον sprite της λίστας,
        την μετατροπή τους σε rectangle, τη θέση τους, το ήχο του κουμπιού και την ένταση τους.
    '''
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        self.sprites.append(pygame.transform.scale(pygame.image.load('images/skin_4.gif').convert_alpha(), (130 * 0.7, 109 * 0.7)))
        self.sprites.append(pygame.transform.scale(pygame.image.load('images/skin_4.gif').convert_alpha(), (130 * 0.9, 109 * 0.9)))
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.clicked = False
        self.sound = mixer.Sound(os.path.join('sounds', 'button_sound.wav'))
        self.sound_check = True
        self.sound.set_volume(0.05)

    '''
           Η συνάρτηση αυτή, αρχικά ελέγχει αν ο χρήστης έχει το ποντίκι πάνω στο κουμπί και αν το έχει
           τότε η εικόνα του κουμπιού μεγαλώνει και ακουγέται ένας συγκεκριμένος ήχος.
           Όσο δεν το έχει πάνω στο κουμπί τότε η εικόνα του επιστρέφει στο αρχικό της μέγεθος.
           Επίσης, μόνο αν το έχει πάνω στο κουμπί και πατήσει κλικ τότε η συνάρτηση επιστρέφει true.
    '''
    def check_button_clicked(self):
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            self.current_sprite = 1
            if self.sound_check == True:
                self.sound.play(0)
                self.sound_check = False
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                time.sleep(0.1)
                return True
            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False
        else:
            self.current_sprite = 0
            self.sound_check = True
        self.image = self.sprites[self.current_sprite]
'''
        SKIN 5:
'''
class skin_5(pygame.sprite.Sprite):
    '''
        Αρχικόποίηση μεταβλητών όπως όλα τα sprites (Εικόνες) της κλάσης σε μια λίστα, το τρέχον sprite της λίστας,
        την μετατροπή τους σε rectangle, τη θέση τους, το ήχο του κουμπιού και την ένταση τους.
    '''
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        self.sprites.append(pygame.transform.scale(pygame.image.load('images/skin_5.gif').convert_alpha(), (130 * 0.7, 109 * 0.7)))
        self.sprites.append(pygame.transform.scale(pygame.image.load('images/skin_5.gif').convert_alpha(), (130 * 0.9, 109 * 0.9)))
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.clicked = False
        self.sound = mixer.Sound(os.path.join('sounds', 'button_sound.wav'))
        self.sound_check = True
        self.sound.set_volume(0.05)

    '''
           Η συνάρτηση αυτή, αρχικά ελέγχει αν ο χρήστης έχει το ποντίκι πάνω στο κουμπί και αν το έχει
           τότε η εικόνα του κουμπιού μεγαλώνει και ακουγέται ένας συγκεκριμένος ήχος.
           Όσο δεν το έχει πάνω στο κουμπί τότε η εικόνα του επιστρέφει στο αρχικό της μέγεθος.
           Επίσης, μόνο αν το έχει πάνω στο κουμπί και πατήσει κλικ τότε η συνάρτηση επιστρέφει true.
    '''
    def check_button_clicked(self):
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            self.current_sprite = 1
            if self.sound_check == True:
                self.sound.play(0)
                self.sound_check = False
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                time.sleep(0.1)
                return True
            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False
        else:
            self.current_sprite = 0
            self.sound_check = True
        self.image = self.sprites[self.current_sprite]
