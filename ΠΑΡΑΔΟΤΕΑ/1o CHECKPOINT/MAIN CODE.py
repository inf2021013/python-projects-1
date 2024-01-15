'''

       ΒΙΒΛΙΟΘΗΚΕΣ:

'''
import pygame              # Για τη δημιουργία του παιχνιδιού.
from pygame import mixer   # Για τη χρήση μουσικής και ηχητικών εφέ
#CLASSES:               # ΠΑΙΡΝΕΙ ΟΛΕΣ ΤΙΣ CLASSES ΠΟΥ ΧΡΕΙΑΣΤΟΥΜΕ, ΑΠΟ ΤΗΝ ΒΙΒΛΙΟΘΗΚΗ CLASSES1 ΠΟΥ ΕΧΟΥΜΕ ΔΗΜΙΟΥΡΓΗΣΕΙ
from CLASSES1 import spaceship  # Κάνει import το διαστημόπλοιο (κεντρικό χαρακτήρα)

#FUNCTIONS:      # ΠΑΙΡΝΕΙ ΟΛΕΣ ΤΙΣ ΣΥΝΑΡΤΗΣΕΙΣ ΠΟΥ ΧΡΕΙΑΣΤΟΥΜΕ, ΑΠΟ ΤΗΝ ΒΙΒΛΙΟΘΗΚΗ functions1 ΠΟΥ ΕΧΟΥΜΕ ΔΗΜΙΟΥΡΓΗΣΕΙ
from functions1 import draw_window      # Κάνει import τη συνάρτηση που δημιουργεί το παράθυρο

'''

       ΑΡΧΙΚΟΠΟΙΗΣΗ ΜΕΤΑΒΛΗΤΩΝ:

'''

pygame.init()   # Αρχικοποίηση του pygame

'''   

       ΔΗΛΩΣΗ ΑΡΧΙΚΩΝ ΜΕΤΑΒΛΗΤΩΝ: 

'''


width, height = 1000, 603      # Πλάτος και ύψος του παραθύρου.
clock = pygame.time.Clock()    # Δημιουργεί ένα αντικείμενο ρολογιού που μετρά την ώρα.
STOP_GAME = False              # Σταματάει το παιχνίδι αν γίνει True.

'''

    MUSIC AND SOUND EFFECTS:

'''

death_sound = True                                     # Δεν ξανά-επαναλαμβάνεται ο ήχος που κάνει όταν χάνει ο χρήστης
space_music = mixer.music.load('music/space_music.wav')              # Φορτώνει τη μουσική του παιχνιδιού.
#mixer.music.play(-1)                                                 # Το -1 είναι για να παίζει τη μουσική επ' άπειρον.
jump_sound_effect = mixer.Sound('sounds/jump_sound.wav')             # Φορτώνει τον ήχο "jump" του διαστημόπλοιου.
death_sound_effect = mixer.Sound('sounds/death_sound.wav')           # Φορτώνει τον ήχο που κάνει όταν χάνει.
jump_sound_effect.set_volume(0.1)                                    # Ορίζει τον ένταση του ηχητικού εφέ 'jump'.
death_sound_effect.set_volume(0.2)                                   # Ορίζει τον ένταση του ηχητικού εφέ 'jump'.

'''      

        BACKGROUND:       

'''
background_image = pygame.image.load('images/SPACE.jpg')  # Φορτώνει την εικόνα του background.

# Μετατρέπει το μέγεθος της εικόνας του background στο μέγεθος του παραθύρου:
background = pygame.transform.scale(background_image, (width, height))

# Οι αρχικές συντεταγμένες του background και το μέγεθος του ως Rectangle:
background_rect = pygame.Rect(0, 0, 0, 0)

# Φορτώνει την εικόνα του Εδάφους:
ground_image = pygame.image.load('images/ground.gif')

# Μετατρέπει το μέγεθος της εικόνας του Εδάφους στο μέγεθος του παραθύρου:
ground = pygame.transform.scale(ground_image, (width, height+33))

# Οι αρχικές συντεταγμένες του εδάφους και το μέγεθος του ως Rectangle.
ground_rect = pygame.Rect(0, -30, 0, 0)

'''      

         ΠΑΡΑΘΥΡΟ ΠΑΙΧΝΙΔΙΟΥ:

'''
wn = pygame.display.set_mode((width, height))            # Δημιουργία του παραθύρου.
pygame.display.set_caption("Flappy Spaceship")           # Τίτλος παραθύρου Flappy bird.
'''    
       
       ΚΕΝΤΡΙΚΟΣ ΧΑΡΑΚΤΗΡΑΣ:
          
'''
spaceship_rect = pygame.Rect(100, 80, 70, 50)               # Δημιουργεί rectangle για το διαστημόπλοιο
spaceship_group = pygame.sprite.Group()                     # Δημιουργεί group στο οποίο θα προσθέσουμε το διαστημόπλοιο
spaceship = spaceship(spaceship_rect.x,spaceship_rect.y,'spaceship.gif') #Φορτώνει τη κλάση του διαστημοπλοίου σε sprite
spaceship_group.add(spaceship)                              # Βάζει το sprite διαστημόπλοιο μέσα στο group

'''

      ΚΕΝΤΡΙΚΗ LOOPA:

'''

run = True                    # όσο είναι True μένει ανοιχτό το παράθυρο του παιχνιδιού
while run:
    clock.tick(60)            # αλλάζει 60 frames ανά δευτερόλεπτο
    '''
                window DRAWING:
    '''
    # Εκτελεί τη συνάρτηση που δημιουργεί το παράθυρο του παιχνιδιού:
    draw_window(ground, ground_rect, background, background_rect, wn, width, spaceship_group)
    ''' 
    
    Ελέγχει αν έχει χάσει ο παίκτης ή όχι για να δει αν χρειάζεται να σταματήσει το παιχνίδι: 
    
    '''
    if spaceship.game_over() == True:
        STOP_GAME = True
        mixer.music.stop()     # Σταματάει τη μουσική, αν σταματήσει το παιχνίδι.
        '''
         Η μεταβλητή death_sound είναι για να μην επαναλαμβάνεται συνέχεια το death_sound_effect
        '''
        if death_sound == True:
            death_sound_effect.play(0)
            death_sound = False
    ''' 
    
    Σταματάει το παιχνίδι σε περίπτωση που γίνει το STOP_GAME True: 
    
    '''
    if STOP_GAME == False:
        spaceship_group.update()
        '''
        
           Κινούμενο έδαφος και κινούμενο background:
           
           Δηλαδή έχουμε 2 ίδια εδάφοι τα οποία τα εμφανίζουμε το ένα δίπλα στο άλλο και κινούνται και τα δύο ταυτόχρονα
           δίνοντας την ψευδαίσθηση ότι κουνιέται ο παίκτης. Μόλις το ένα από τα δύο πάρει το χ του το μέγεθος του 
           πλάτους του παραθύρου σε αρνητική τιμή, τότε το χ του αποκτά την τιμή μηδέν. Aυτό, επαναλαμβάνεται 
           μέχρι να τελειώσει το παιχνίδι και το ίδιο ισχύει και για το background.
        '''

    # ΕΔΑΦΟΣ (ground):
        ground_rect.x -= 4
        if ground_rect.x == -width:
            ground_rect.x = 0
    # BACKGROUND:
        background_rect.x -= 2
        if background_rect.x == -width:
            background_rect.x = 0

    ''' 
    
    Μόλις ο Χρήστης κάνει "click" εκεί που κλείνει το παράθυρο τότε θέτει το "run" σε False και σταματάει η LOOPA: 
    
    '''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    # Αν ο χρήστης κάνει click και το STOP_GAME είναι False τότε το διαστημόπλοιο θα χοροπηδήσει:
        if event.type == pygame.MOUSEBUTTONDOWN and STOP_GAME == False:
            jump_sound_effect.play(0)

pygame.quit()                 # κλείνει το παράθυρο