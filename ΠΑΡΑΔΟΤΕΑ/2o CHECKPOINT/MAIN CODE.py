'''

       ΒΙΒΛΙΟΘΗΚΕΣ:

'''
import random              # Για τη δημιουργία τυχαίων αριθμών
import os                  # Για να βρίσκει το path των φακέλων από το λογισμικό
import pygame              # Για τη δημιουργία του παιχνιδιού.
from pygame import mixer   # Για τη χρήση μουσικής και ηχητικών εφέ

''' Κάνει import, από τη βιβλιοθήκη που έχουμε δημιουργήσει CLASSES2, τις εξής κλάσεις:  '''
from CLASSES2 import spaceship  # 1.το διαστημόπλοιο
from CLASSES2 import pipe       # 2.τα εμπόδια
from CLASSES2 import restpipe   # 3.το υπόλοιπο εμπόδιο δηλαδή για να φαίνεται ότι το εμπόδιο είναι πάνω στο έδαφος.
from CLASSES2 import Alien      # 4.τους εξωγήινους
from CLASSES2 import rocket     # 5.τους πυραύλους
from CLASSES2 import PowerUp    # 6.τα power_ups

''' Κάνει import, από τη βιβλιοθήκη που έχουμε δημιουργήσει functions2, τη συνάρτηση που: '''
from functions2 import draw_window       # 1.δημιουργεί το κύριο παράθυρο του παιχνιδιού
from functions2 import draw_seconds      # 2.εμφανίζει το κείμενο με τα δευτερόλεπτα που απομένουν από τα power_ups
from functions2 import draw_press_SPACE  # 3.εμφανίζει το κείμενο εξηγεί στο χρήστη πως να χρησιμοποιήσει τα power_ups
from functions2 import draw_power_ups    # 4.εμφανίζει το κείμενο που λέει πόσα power_ups απομένουν



'''

       ΑΡΧΙΚΟΠΟΙΗΣΗ ΜΕΤΑΒΛΗΤΩΝ:

'''

pygame.init()   # Αρχικοποίηση του pygame

'''   

       ΔΗΛΩΣΗ ΑΡΧΙΚΩΝ ΜΕΤΑΒΛΗΤΩΝ: 

'''


clock = pygame.time.Clock()    # Δημιουργεί ένα αντικείμενο ρολογιού που μετρά την ώρα.
# FONT:
font_score = pygame.font.Font('freesansbold.ttf', 82)     # Δηλώνουμε τι είδους font θα χρησιμοποιήσουμε για το score
font_power_up = pygame.font.Font('freesansbold.ttf', 32)  # Δηλώνουμε τι είδους font θα χρησιμοποιήσουμε για το power_up
# Window:
width, height = 1000, 603                                # Πλάτος και ύψος του παραθύρου.
wn = pygame.display.set_mode((width, height))            # Δημιουργία του παραθύρου.
pygame.display.set_caption("Flappy Spaceship")           # Τίτλος παραθύρου Flappy bird.

# GAME_ENDING:
STOP_GAME = False                            # Σταματάει το παιχνίδι αν γίνει True.
GAME_OVER = False                            # Αν γίνει True σημαίνει οτι έχασε ο παίκτης

# POWER_UP:
power_up = False                            # Το power up είναι ανενεργό
power_up_used = False                       # Δεν έχει χρησιμοποιηθεί power up
SPACE_pressed = False                       # Δηλώνει ότι δεν πατήθηκε το κουμπί SPACE
power_up_text_disappear = False             # Εμφανίζεται το κείμενο με τον μετρητή των power ups
seconds_text_disappear = True               # Δεν εμφανίζεται το κείμενο με τα seconds
power_up_group = pygame.sprite.Group()      # Δημιουργεί group στο οποίο θα προσθέσουμε τα power ups
power_ups = 1                               # Αρχικό νούμερο των power ups
seconds = 0                                 # Αρχικοποίηση δευτερολέπτων που κρατάει το κάθε power up

# ΠΥΡΑΥΛΟΣ:
charge = False                              # Απαγορεύει να επιτεθεί ο πύραυλος στο διαστημόπλοιο
spawn = True                                # Επιτρέπει το να εμφανιστεί πύραυλος στην οθόνη
rocket_group = pygame.sprite.Group()        # Δημιουργεί group στο οποίο θα προσθέσουμε τους πυραύλους

# ΕΜΠΟΔΙΑ:
pipe_group = pygame.sprite.Group()          # Δημιουργεί group στο οποίο θα προσθέσουμε τα εμπόδια
missing_pipe_group = pygame.sprite.Group()  # Δημιουργεί group στο οποίο θα προσθέσουμε για το υπόλοιπο των εμποδίων
pipe_frequency = 1500                       # Συχνότητα εμποδίων σε milliseconds
last_pipe = - pipe_frequency
pipe_counter = 0                            # Αρχικό νούμερο εμποδίων

# ΕΞΩΓΗΙΝΟΙ
alien_group = pygame.sprite.Group()         # Δημιουργεί group στο οποίο θα προσθέσουμε τους εξωγήινους

# ΔΙΑΣΤΗΜΟΠΛΟΙΟ:
spaceship_group = pygame.sprite.Group()                     # Δημιουργεί group στο οποίο θα προσθέσουμε το διαστημόπλοιο
spaceship = spaceship(100,80)                               # Φορτώνει την κλάση του διαστημοπλοίου σε sprite
spaceship_group.add(spaceship)                              # Βάζει το sprite διαστημόπλοιο μέσα στο group

#SCORE:
score = 0                       # Αρχικό score
'''

    MUSIC AND SOUND EFFECTS:

'''
space_music = mixer.music.load(os.path.join('music', 'space_music.wav'))    # Φορτώνει τη μουσική του παιχνιδιού.
mixer.music.play(-1)                                                 # Το -1 είναι για να παίζει τη μουσική επ' άπειρον.
jump_sound_effect = mixer.Sound(os.path.join('sounds', 'jump_sound.wav'))  # Φορτώνει τον ήχο "jump" του διαστημόπλοιου.
death_sound_effect = mixer.Sound(os.path.join('sounds', 'death_sound.wav'))    # Φορτώνει τον ήχο που κάνει όταν χάνει.
jump_sound_effect.set_volume(0.1)                                        # Ορίζει τον ένταση του ηχητικού εφέ 'jump'.
death_sound_effect.set_volume(0.2)                                        # Ορίζει τον ένταση του ηχητικού εφέ 'jump'.
death_sound = True                                     # Δεν ξανά-επαναλαμβάνεται ο ήχος που κάνει όταν χάνει ο χρήστης
'''      

        BACKGROUND:       

'''
# Φορτώνει την εικόνα του background:
background_image = pygame.image.load(os.path.join('images', 'SPACE.jpg'))

# Μετατρέπει το μέγεθος της εικόνας του background στο μέγεθος του παραθύρου:
background = pygame.transform.scale(background_image, (width, height))

# Οι αρχικές συντεταγμένες του background και το μέγεθος του ως Rectangle:
background_rect = pygame.Rect(0, 0, 0, 0)

# Φορτώνει την εικόνα του Εδάφους:
ground_image = pygame.image.load(os.path.join('images', 'ground.gif'))

# Μετατρέπει το μέγεθος της εικόνας του Εδάφους στο μέγεθος του παραθύρου:
ground = pygame.transform.scale(ground_image, (width, height+33))

# Οι αρχικές συντεταγμένες του εδάφους και το μέγεθος του ως Rectangle.
ground_rect = pygame.Rect(0, -30, 0, 0)

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
    draw_window(ground, ground_rect, background, background_rect, wn, score, power_ups, font_score, font_power_up, width, pipe_group, spaceship_group, power_up_group, missing_pipe_group, alien_group, rocket_group, power_up_text_disappear, seconds, seconds_text_disappear)

    '''

                       ΔΗΜΙΟΥΡΓΙΑ ΠΟΛΛΑΠΛΩΝ ΕΜΠΟΔΙΩΝ:

    '''

    time_now = pygame.time.get_ticks()            # Μετράει την τρέχον χρονική στιγμή σε milliseconds
    ''' 
    
        Όταν το αποτέλεσμα της αφαίρεσης της τρέχον χρονικής στιγμή,
        με το πότε εμφανίστηκε το προηγούμενο εμπόδιο, 
        είναι μεγαλύτερο απο τη συχνότητα εμφάνισης των εμποδίων τότε εμφανίζεται ένα νέο εμπόδιο.
        
    '''
    if time_now - last_pipe > pipe_frequency:
        pipe_height = random.randint(-100, 100)  # Δημιουργεί ένα τυχαίο ακέραιο αριθμό για το ύψος των εμποδίων
        btm_pipe = pipe(width, int(height / 2) + pipe_height - 70, -1)  # Κάτω μέρος του εμποδίου με τυχαίο ύψος.
        tp_pipe = pipe(width, int(height / 2) + pipe_height - 50, 1)    # Πάνω μέρος του εμποδίου με τυχαίο ύψος.
        pipe_group.add(btm_pipe)                   # Βάζει το κάτω μέρος του εμποδίου στο group με τα εμπόδια
        pipe_group.add(tp_pipe)                    # Βάζει το πάνω μέρος του εμποδίου στο group με τα εμπόδια
        missing_pipe = restpipe(width-1, 485)      # Είναι για να φαίνεται ότι το εμπόδιο ακουμπάει το έδαφος.
        missing_pipe_group.add(missing_pipe)       # Το βάζει σε ειδικό group από sprites.
        last_pipe = time_now                       # Δηλώνει τη χρονική στιγμή που εμφανίστηκε το τελευταίο εμπόδιο.
        pipe_counter += 1                          # Μετράει πόσα εμπόδια έχουν δημιουργηθεί
        '''
        
            ΣΥΧΝΟΤΗΤΑ ΕΜΦΑΝΙΣΗΣ ΚΑΘΕ ΕΞΩΓΗΙΝΟΥ:
        
            Αρχικά σε αυτό κομμάτι αυτό του κώδικά μας, έχουμε δημιουργήσει ένα μετρητή,
            που μετρά πόσα εμπόδια έχουν εμφανιστεί, μετά θα παράγουμε συνεχώς έναν τυχαίο αριθμό 
            σε βρόχο 20 επαναλήψεων. Ο τυχαίος αριθμός αυτός θα παίρνει τιμές 
            από τη μεταβλητή num1 μέχρι τη μεταβλητή num2, όπου θα ξεκινάνε με τιμές 1 και 10 αντίστοιχα και 
            στο τέλος κάθε επανάληψης του βρόχου θα αυξάνονται κατά 10 και οι δύο. 
            Τέλος, σε κάθε επανάληψη του βρόχου θα ελέγχει αν ο τυχαίος αριθμός που παρήγαγε είναι ίσος
            με τον μετρητή εμποδίων, αν ο έλεγχος αυτός βγει αληθής τότε εμφανίζεται ένας εξωγήινος.
            
        '''
        num1 = 1                    # Αρχικοποίησης 1ης μεταβλητής ή αλλιώς num1 σε 1
        num2 = 10                   # Αρχικοποίησης 2ης μεταβλητής ή αλλιώς num2 σε 10
        for i in range(20):         # Βρόχος 20 επαναλήψεων
            if pipe_counter == random.randint(num1, num2):    # Έλεγχος μεταξύ μετρητή εμποδίων και τυχαίου αριθμού.
                '''
                 Το ύψος στο οποίο θα εμφανίζεται κάθε εξωγήινος θα έχει μια τυχαία τιμή απο 50 εώς 300.
                 Ο κάθε εξωγήινος θα πρέπει να εμφανίζεται δίπλα σε κάθε εμπόδιο και όχι πάνω σε αυτό. 
                 Το πόσο δίπλα θα εμφανίζεται, θα είναι μία τυχαία τιμή από 190 μέχρι 300.
                 Τέλος όλοι οι εξωγήινοι βρίσκονται σε ένα group απο sprites.
                '''
                alien_y = random.randint(50, 300)
                alien_x = random.randint(190, 300)
                alien = Alien(width + alien_x, alien_y)
                alien_group.add(alien)
            num1 = num1 + 10    # Αύξηση 1ης μεταβλητής num1 κατά 10
            num2 = num2 + 10    # Αύξηση 2ης μεταβλητής num2 κατά 10
        '''
    
            ΣΥΧΝΟΤΗΤΑ ΕΜΦΑΝΙΣΗΣ ΚΑΘΕ POWER UP:

            Αρχικά, θα παράγουμε συνεχώς έναν τυχαίο αριθμό σε βρόχο 20 επαναλήψεων. 
            Ο τυχαίος αριθμός αυτός θα παίρνει τιμές από τη μεταβλητή num1 μέχρι τη μεταβλητή num2, 
            όπου θα ξεκινάνε με τιμές 1 και 20 αντίστοιχα, 
            και στο τέλος κάθε επανάληψης του βρόχου θα αυξάνονται κατά 20 και οι δύο. 
            Τέλος, σε κάθε επανάληψη του βρόχου θα ελέγχει αν ο τυχαίος αριθμός που παρήγαγε είναι ίσος
            με τον μετρητή εμποδίων, αν ο έλεγχος αυτός βγει αληθής τότε εμφανίζεται ένα power_up.
    
        '''
        num3 = 1  # Αρχικοποίησης 1ης μεταβλητής ή αλλιώς num1 σε 1
        num4 = 20  # Αρχικοποίησης 2ης μεταβλητής ή αλλιώς num2 σε 40
        for i in range(20):  # Βρόχος 20 επαναλήψεων
            if pipe_counter == random.randint(num3, num4):  # Έλεγχος μεταξύ μετρητή εμποδίων και τυχαίου αριθμού.
                '''
                 Το ύψος στο οποίο θα εμφανίζεται κάθε power_up θα έχει μια τυχαία τιμή απο 50 εώς 300.
                 To κάθε power_up θα πρέπει να εμφανίζεται δίπλα σε κάθε εμπόδιο και όχι πάνω σε αυτό. 
                 Το πόσο δίπλα θα εμφανίζεται, θα είναι μία τυχαία τιμή από 190 μέχρι 300.
                 Τέλος όλα τα power_ups βρίσκονται σε ένα group απο sprites.
                '''
                power_up_y = random.randint(50, 300)
                power_up_x = random.randint(190, 300)
                POWER_UP = PowerUp(width + power_up_x, power_up_y)
                power_up_group.add(POWER_UP)
            num3 = num3 + 20  # Αύξηση 1ης μεταβλητής num1 κατά 40
            num4 = num4 + 20  # Αύξηση 2ης μεταβλητής num2 κατά 40


    ''' 
    
    Ελέγχει αν έχει χάσει ο παίκτης ή όχι για να δει αν χρειάζεται να σταματήσει το παιχνίδι: 
    
    '''
    if spaceship.game_over() == True or GAME_OVER == True:
        STOP_GAME = True
        mixer.music.stop()     # Σταματάει τη μουσική, αν σταματήσει το παιχνίδι.
        '''
         Η μεταβλητή death_sound είναι για να μην επαναλαμβάνεται συνέχεια το death_sound_effect
        '''
        if death_sound == True:
            death_sound_effect.play(0)
            death_sound = False

    ''' 
    
    Σταματάει το παιχνίδι σε περίπτωση που γίνει το STOP_GAME True 
    και το διαστημόπλοιο αρχίζει και πέφτει μέχρι να βρει έδαφος: 
    
    '''
    if STOP_GAME == False:


        # Αν το διαστημόπλοιο ακουμπήσει κάποιο εμπόδιο ή κάποιον πύραυλο, ο χρήστης χάνει:
        if power_up == False:
            if pygame.sprite.spritecollideany(spaceship, pipe_group):
                GAME_OVER = True
            if pygame.sprite.spritecollideany(spaceship, rocket_group):
                GAME_OVER = True
        '''
        
           Κινούμενο έδαφος και κινούμενο background:
           
           Δηλαδή έχουμε 2 ίδια εδάφοι τα οποία τα εμφανίζουμε το ένα δίπλα στο άλλο και κινούνται και τα δύο ταυτόχρονα
           δίνοντας την ψευδαίσθηση ότι κουνιέται ο παίκτης. Μόλις το ένα από τα δύο πάρει το χ του το μέγεθος του 
           πλάτους του παραθύρου σε αρνητική τιμή, τότε το χ του αποκτά την τιμή μηδέν. Αυτό, επαναλαμβάνεται 
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
        ΚΑΛΕΙ ΤΗ ΣΥΝΑΡΤΗΣΗ UPDATE  ΑΠΟ ΤΙΣ ΚΛΑΣΕΙΣ:
        '''

        alien_group.update()            # 1.Των εξωγήινων
        pipe_group.update()             # 2.Των εμποδίων
        missing_pipe_group.update()     # 3.Του υπολοίπου των εμποδίων
        power_up_group.update()         # 4.Των power ups
        spaceship_group.update()        # 5.Του διαστημοπλοίου

        '''
                        ΠΥΡΑΥΛΟΣ:
            Καταρχάς, το ύψος στο οποίο θα εμφανίζεται κάθε πύραυλος θα έχει μια τυχαία τιμή από 50 εώς 400
            και η αρχική του θέση θα είναι από τα δεξιά αλλά εκτός της οθόνης. Έπειτα, όσο το score 
            έχει τιμές 10,20,30,40 δηλαδή διαιρείται ακριβώς με το 10 τότε αν η μεταβλητή spawn, 
            είναι αληθής, εμφανίζεται πύραυλος στην οθόνη και η spawn παίρνει κατευθείαν την τιμή False
            για να μην εμφανίζεται ταυτόχρονα πάνω από ένας πύραυλος, στην οθόνη. Μετά, δίνει στη μεταβλητή
            charge την τιμή True, η οποία ελέγχει το πότε να κινηθεί ο πύραυλος από δεξιά προς τα αριστερά μέσω της 
            συνάρτησης update της κλάσης rocket. 
            Με λίγα λόγια αν ο μετρητής του σκορ έχει τιμή που τελειώνει σε 9 (π.χ 9,19,29 κλπ) τότε και ΜΟΝΟ τότε
            εμφανίζεται ΈΝΑΣ μόνο πύραυλος στη οθόνη. Τέλος, αν το πύραυλος ακουμπήσει το διαστημόπλοιο, 
            ο χρήστης χάνει.  
            
        '''

        rocket_height = random.randint(50, 400)  # Η τιμή του ύψους του πυραύλου με τυχαίο ακέραιο από το 50 εώς το 400.
        Rocket = rocket(width, rocket_height)    # Οι αρχικές συντεταγμένες του πυραύλου.
        if (score + 1) % 10 == 0:                # Γίνεται True μόνο αν το score έχει τιμές 10,20,30,40,50 κλπ.
            if spawn == True:                    # Ελέγχει αν μπορεί να εμφανίσει πύραυλο στην οθόνη
                rocket_group.add(Rocket)         # Αν μπορεί τότε εμφανίζει τον πύραυλο στην οθόνη
                spawn = False           # Απαγορεύει στον πύραυλο από το να ξαναεμφανιστεί μέχρι το spawn να γίνει True
            charge = True               # Επιτρέπει στον πύραυλο να επιτεθεί στον διαστημόπλοιο
        if charge == True:              # Ελέγχει αν επιτρέπετε να επιτεθεί ο πύραυλος στο διαστημόπλοιο
            rocket_group.update()       # Καλεί τη συνάρτηση update από την κλάση rocket
            ''' 
            Αν ο μετρητής του σκορ έχει τιμή που τελειώνει σε 9 (π.χ 9,19,29 κλπ), 
            επιτρέπει το να εμφανιστεί πύραυλος στην οθόνη.                           
            '''
            if score % 10 == 0:
                spawn = True
        '''
        
                POWER UP
                
        '''
        if power_ups > 0:
            power_up_used = False

        keys = pygame.key.get_pressed()    # Μεταβλητή που ελέγχει αν έχει πατηθεί κάποιο κουμπί από το πληκτρολόγιο.
        if power_up_used == False:         # Όσο δεν έχει χρησιμοποιηθεί το τρέχον power up
            if SPACE_pressed == False:           # Όσο το κουμπί SPACE δεν έχει πατηθεί ακόμα τότε:
                if keys[pygame.K_SPACE]:
                    start_ticks = pygame.time.get_ticks()   # 1.ξεκινάει ο μετρητής του χρόνου για το power up
                    SPACE_pressed = True             # 2.δηλώνει ότι πατήθηκε για να μη γίνεται τίποτα όσο μένει πατημένο.
                    power_ups -= 1                   # 3.δηλώνει οτι ένα power up χρησιμοποιήθηκε
                    power_up_text_disappear = True   # 4.εξαφανίζεται το κείμενο που εξηγεί πως να χρησιμοποιηθεί το power up
            else:   # ΑΛΛΙΩΣ
                ''' 
                Όσο ο μετρητής του χρόνου δεν ξεπερνά τα 4 δευτερόλεπτα ή αλλιώς τα 4000 milliseconds 
                ή όσο το διαστημόπλοιο ακουμπάει κάποιο εμπόδιο κατά την διάρκεια που λειτουργεί το power up τότε:
                '''
                seconds = (pygame.time.get_ticks() - start_ticks)
                if seconds <= 4000 and seconds >= 0 or pygame.sprite.spritecollideany(spaceship, pipe_group):
                    power_up = True                 # 1.δηλώνεται ότι το power up είναι ενεργό
                    spaceship.change_sprite(1)      # 2.αλλάζει η εμφάνιση το διαστημόπλοιο
                    seconds_text_disappear = False  # 3.όσο το power_up είναι ενεργό, εμφανίζεται το κείμενο με τα seconds
                else:  # ΑΛΛΙΩΣ αν τα ξεπεράσει ή το διαστημόπλοιο δεν ακουμπάει κάποιο εμπόδιο
                    power_up = False                # 1.δηλώνεται ότι το power up είναι ανενεργό
                    seconds_text_disappear = True   # 2.και όσο είναι ανενεργό εξαφανίζεται το κείμενο με τα seconds
                    spaceship.change_sprite(0)      # 3.το διαστημόπλοιο παίρνει την αρχική του εμφάνιση
                    SPACE_pressed = False           # 4.δηλώνεται ότι το κουμπί SPACE σταματάει να είναι πατημένο
                    power_up_used = True            # 5.δηλώνεται ότι το τρέχον power έχει χρησιμοποιηθεί


    else:
        # Καλεί την εντολή fall από την κλάση spaceship όπου κάνει το διαστημόπλοιο να πέφτει
        spaceship.fall()

    '''
            Μετρητής του SCORE και μετρητής των power_ups:
        Όσο ο μετρητής των εμποδίων που έχουν δημιουργηθεί είναι πάνω από μηδέν 
        τότε αν το διαστημόπλοιο ακουμπήσει έναν οποιοδήποτε power_up, 
        ελέγχει αν έχει ήδη αυξήσει τον μετρητή των power_ups κατά 1
        ή αν το διαστημόπλοιο ακουμπήσει έναν οποιοδήποτε εξωγήινο, 
        ελέγχει αν έχει ήδη αυξήσει τον μετρητή του score κατά 5.
        Αυτό το κάναμε για να μην παίρνει άπειρους πόντους όσο ακουμπάει κάποιον εξωγήινο ή
        να μην παίρνει άπειρα power_ups όσο ακουμπάει κάποιο power_up.
        Επίσης αν το διαστημόπλοιο περάσει ανάμεσα από ένα εμπόδιο τότε προσθέτετε 1 πόντος στο score.
         
    '''

    if pipe_counter > 0:      # Ελέγχει αν ο μετρητής των εμποδίων είναι πάνω απο μηδέν
        '''
            Μετρητής των power_ups:
        '''
        # Για κάθε ξεχωριστό power_up που ακουμπά το διαστημόπλοιο προσθέτεται μόνο 1 power_up.
        if pygame.sprite.spritecollideany(spaceship, power_up_group):
            if add_power_up == True:
                power_ups += 1
                add_power_up = False
            # Κάθε power_up που ακουμπά το διαστημόπλοιο αφαιρείται από το group των power_ups
            power_up_group.sprites()[0].kill()
        else:
            add_power_up = True
        '''
            Μετρητής του SCORE:
        '''
        # Για κάθε ξεχωριστό εξωγήινο που ακουμπά το διαστημόπλοιο προσθέτονται μόνο 5 πόντοι στο score τη φορά
        if pygame.sprite.spritecollideany(spaceship, alien_group):
            if add_score == True:
                score += 5
                add_score = False
            # Κάθε εξωγήινος που ακουμπά το διαστημόπλοιο αφαιρείται από το group των εξωγήινων
            alien_group.sprites()[0].kill()
        else:
            add_score = True
        '''
        Όταν το x του διαστημοπλοίου και το x του πρώτου εμποδίου είναι ίσα, 
        δηλαδή αν το διαστημόπλοιο περάσει ανάμεσα από το συγκεκριμένο εμπόδιο τότε προσθέτετε 1 πόντος στο score.
        '''
        if spaceship_group.sprites()[0].rect.x == pipe_group.sprites()[0].rect.x:
            score += 1
    # Μετά από 4 δευτερόλεπτα εξαφανίζεται το κείμενο που εξηγεί στον παίκτη πως να χρησιμοποιήσει τα power ups του.
    if pygame.time.get_ticks() >= 4000:
        power_up_text_disappear = True

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