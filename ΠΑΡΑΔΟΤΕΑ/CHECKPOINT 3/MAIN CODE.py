'''

       ΒΙΒΛΙΟΘΗΚΕΣ:

'''
import random              # Για τη δημιουργία τυχαίων αριθμών
import os                  # Για να βρίσκει το path των φακέλων από το λογισμικό
import pygame              # Για τη δημιουργία του παιχνιδιού.
from pygame import mixer   # Για τη χρήση μουσικής και ηχητικών εφέ
from CLASSES3 import spaceship  # 1.το διαστημόπλοιο
from CLASSES3 import pipe       # 2.τα εμπόδια
from CLASSES3 import restpipe   # 3.το υπόλοιπο εμπόδιο δηλαδή για να φαίνεται ότι το εμπόδιο είναι πάνω στο έδαφος.
from CLASSES3 import Alien      # 4.τους εξωγήινους
from CLASSES3 import rocket     # 5.τους πυραύλους
from CLASSES3 import PowerUp    # 6.τα power_ups
from CLASSES3 import play_button  # 7. το κουμπί που ξεκινάει το κύριο παιχνίδι
from CLASSES3 import retry_button  # 8. το κουμπί που ξαναξεκινάει το κύριο παιχνίδι σε περίπτωση που χάσει ο παίκτης
from CLASSES3 import animation_1   # 9.Το πρώτο animation του menu
from CLASSES3 import animation_2    # 10.Το δεύτερο animation του menu
from CLASSES3 import menu_button    # 11. το κουμπί του menu
from CLASSES3 import exit_button    # το κουμπί που κλείνει το παράθυρο
from CLASSES3 import title          # Ο τίτλος του παιχνιδιού
from CLASSES3 import skins_button   # το κουμπί που μεταφέρει το παίκτη στο menu με τα skins.
# Οι 5 επιλογές του παίκτη να επιλέξει skins:
from CLASSES3 import skin_1
from CLASSES3 import skin_2
from CLASSES3 import skin_3
from CLASSES3 import skin_4
from CLASSES3 import skin_5
# Η συγκεκριμένη συνάρτηση:
from functions3 import draw_window       # 1.δημιουργεί το κύριο παράθυρο του παιχνιδιού
from functions3 import draw_seconds      # 2.εμφανίζει το κείμενο με τα δευτερόλεπτα που απομένουν από τα power_ups
from functions3 import draw_press_SPACE  # 3.εμφανίζει το κείμενο εξηγεί στο χρήστη πως να χρησιμοποιήσει τα power_ups
from functions3 import draw_power_ups    # 4.εμφανίζει το κείμενο που λέει πόσα power_ups απομένουν
from functions3 import draw_menu         # 5.εμφανίζει το αρχικό menu
from functions3 import draw_skin_TEXT    # 6.εμφανίζει το κείμενο που ζητάει απο τον παίκτη να επιλέξει skin
from functions3 import draw_skin_menu    # 7.εμφανίζει το menu με τα skins.
'''

       ΑΡΧΙΚΟΠΟΙΗΣΗ ΜΕΤΑΒΛΗΤΩΝ:

'''

pygame.init()   # Αρχικοποίηση του pygame

'''   

       ΔΗΛΩΣΗ ΑΡΧΙΚΩΝ ΜΕΤΑΒΛΗΤΩΝ: 

'''


# FONTS:
font_score = pygame.font.Font('freesansbold.ttf', 82)     # Δηλώνουμε τι είδους font θα χρησιμοποιήσουμε για το score
font_high_score = pygame.font.Font('freesansbold.ttf', 22)  # Δηλώνουμε τι είδους font θα χρησιμοποιήσουμε για το highscore
font_power_up = pygame.font.Font('freesansbold.ttf', 32)  # Δηλώνουμε τι είδους font θα χρησιμοποιήσουμε για το power_up
font_skins = pygame.font.Font('freesansbold.ttf', 82)  # Δηλώνουμε τι είδους font θα χρησιμοποιήσουμε για τα skins
# Window:
width, height = 1000, 603                               # Πλάτος και ύψος του παραθύρου.
wn = pygame.display.set_mode((width, height))            # Δημιουργία του παραθύρου.
pygame.display.set_caption("Flappy Spaceship")           # Τίτλος παραθύρου Flappy bird.

MENU_picture = pygame.transform.scale(pygame.image.load('images/MENU1.jpg'),(1000,603))  # Φορτώνει την εικόνα του menu.
# Δήλωση της κλάσης του κουμπιού που ξεκινάει το κύριο παιχνίδι.
play_button_group = pygame.sprite.Group()
Play_button = play_button(498, 350)
play_button_group.add(Play_button)
# Δήλωση της κλάσης του κουμπιού που επιστρέφει στο αρχικό menu
menu_button_group = pygame.sprite.Group()
Menu_button = menu_button(80, 30)
menu_button_group.add(Menu_button)
# Δήλωση της κλάσης του κουμπιού που κλείνει το παράθυρο.
exit_button_group = pygame.sprite.Group()
Exit_button = exit_button(70, 550)
exit_button_group.add(Exit_button)
# Δήλωση της κλάσης του τίτλου του παιχνιδιού
title_group = pygame.sprite.Group()
Title = title(498,150)
title_group.add(Title)
# Δήλωση της κλάσης του κουμπιού που ξανά-ξεκινάει το παιχνίδι
retry_button_group = pygame.sprite.Group()
Retry_button = retry_button(880, 560)
retry_button_group.add(Retry_button)
retry_button_clicked = False
current_sprite = 0  # Αν ο παίκτης δεν επιλέξει κάποιο skin τότε αυτόματα το διαστημόπλοιο παίρνει το πρώτο skin.
# Δήλωση της κλάσης του κουμπιού που πηγαίνει στο menu με τα skins
skins_button_group = pygame.sprite.Group()
Skins_button = skins_button(498,420)
skins_button_group.add(Skins_button)
# Δηλώνονται όλες οι κλάσεις με τις επιλογές των skins που δίνονται στον χρήστη:
skin_1_group = pygame.sprite.Group()
Skin_1 = skin_1(200,250)
skin_1_group.add(Skin_1)
skin_2_group = pygame.sprite.Group()
Skin_2 = skin_2(350,250)
skin_2_group.add(Skin_2)
skin_3_group = pygame.sprite.Group()
Skin_3 = skin_3(500,250)
skin_3_group.add(Skin_3)
skin_4_group = pygame.sprite.Group()
Skin_4 = skin_4(650,250)
skin_4_group.add(Skin_4)
skin_5_group = pygame.sprite.Group()
Skin_5 = skin_5(800,250)
skin_5_group.add(Skin_5)
'''                                HIGHSCORE:
 Κάθε φορά που εκτελείται το πρόγραμμα, διαβάζεται το αρχείο highscore.txt 
 και μετατρέπει τον αριθμό, που αρχικά είναι σε μορφή συμβολοσειράς, 
 σε μορφή ακεραίου και τον αποθηκεύει στη μεταβλητή highscore.
'''
with open('files/highscore.txt', 'r') as f:
    High_score = int(f.read())

'''

                ΚΕΝΤΡΙΚΗ LOOPA:
    Η κεντρική loopa εκτελείται συνεχώς μέχρι να κλείσει ο χρήστης το αρχικό παράθυρο. 
    Η συγκεκριμένη loopa περιέχει μια loopa που εμφανίζει το αρχικό menu, μια άλλη που εμφανίζει το menu με τα skins
    και μία ακόμα που εμφανίζει το κύριο παιχνίδι.  
'''
Game = True
menu = True
MAIN_LOOP = True
skins = True
while MAIN_LOOP:
    start = pygame.time.get_ticks()
    '''
    --------------------------------------------------------------------------------------------------------------------
                                                                MENU:
    
            Δήλωση του πρώτου animation:
        Επειδή στο πρώτο animation εμφανίζονται όλα τα διαφορετικά διαστημόπλοια το ένα μετά απο το άλλο,
        τότε προσθέτεται μόνο μία class στο group του animation 1, 
        που αποτελείτε από 5 διαφορετικά sprites αλλάζοντας το ένα μετά το άλλο.
    '''
    animation1_group = pygame.sprite.Group()
    spaceships_1 = animation_1(-20,100)
    animation1_group.add(spaceships_1)
    allow_animation_1 = True
    '''
            Δήλωση του δεύτερου animation:
        Επειδή στο δεύτερο animation εμφανίζονται όλα τα διαστημόπλοιο την ίδια στιγμή,   
        μία λίστα που περιέχει ως στοιχεία την ίδια κλάση 5 φορές αλλά με διαφορετικές παραμέτρους,
        προσθέτεται στο group του animation 2.
    '''
    animation2_group = pygame.sprite.Group()
    spaceships_2 = [
        animation_2(-20, 100,  70, 'images/Spaceship_1.gif'),
        animation_2(-20, 200, 170, 'images/Spaceship_2.gif'),
        animation_2(-20, 300, 270, 'images/Spaceship_3.gif'),
        animation_2(-20, 400, 370, 'images/Spaceship_4.gif'),
        animation_2(-20, 500, 470, 'images/Spaceship_5.gif')
    ]
    for list in range(5):
        animation2_group.add(spaceships_2[list])
    allow_animation_2 = False
    animation_count = 0         # O αριθμός το animations animations που έχουν τελειώσει αρχικοποιείται σε μηδέν
    #music
    menu_music = mixer.music.load(os.path.join('music', 'menu_music.mp3'))
    mixer.music.play(-1)  # Το -1 είναι για να παίζει τη μουσική επ' άπειρον.
    mixer.music.set_volume(0.5)
    while menu:
        # Εκτελεί τη συνάρτηση που δημιουργεί το παράθυρο που εμφανίζει το αρχικό menu:
        draw_menu(wn,High_score,font_high_score,MENU_picture,animation1_group,animation2_group,exit_button_group,title_group,skins_button_group,play_button_group)

        '''
        ----------------------------------------------------------------------------------------------------------------
                                                            ANIMATION:
            Το menu έχει δύο animations. Πιο συγκεκριμένα, μόλις τελειώσει το πρώτο τότε ξεκινάει το δεύτερο και μόλις 
            τελειώσει το δεύτερο ξανά ξεκινάει το πρώτο πάλι κλπ.
        ----------------------------------------------------------------------------------------------------------------
        '''
        '''
                ANIMATION 1:   
        '''

        if spaceships_2[0].check() == True :
            allow_animation_2 = False
            allow_animation_1 = True
            animation_count = spaceships_2[0].Animation_count()
        if allow_animation_1 == True:
            animation1_group.update(width,allow_animation_1,animation_count)

        '''
                ANIMATION 2:
        '''
        if spaceships_1.check() == True :
            allow_animation_2 = True
            allow_animation_1 = False
            animation_count = spaceships_1.Animation_count()
        if allow_animation_2 == True:
            animation2_group.update(width,allow_animation_2,animation_count)



        '''
        ----------------------------------------------------------------------------------------------------------------
        '''
        # Αν πατηθεί το κουμπί με τα skins τότε εμφανίζεται το menu με τα skins:
        if Skins_button.check_button_clicked()==True:
            Game = False
            menu = False
            skins = True
        # Αν πατηθεί το κουμπί play τότε ξεκινάει το παιχνίδι:
        if Play_button.check_button_clicked() == True:
            Game = True
            menu = False
            skins = False
        # Αν πατηθεί το κουμπί exit ή το "x" πάνω δεξιά, τότε κλείνει το παράθυρο:
        if Exit_button.check_button_clicked() == True:
            Game = False
            MAIN_LOOP = False
            menu = False
            skins = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Game = False
                MAIN_LOOP = False
                menu = False
                skins = False
    mixer.music.stop()  # Σταματάει τη μουσική του menu.
    '''
    --------------------------------------------------------------------------------------------------------------------
                                                        SKINS:
    
    '''
    # ΔΗΛΩΝΕΙ ΤΗ CLASS ΜΕ ΤΟ ΚΟΥΜΠΙ ΤΟΥ ΠΟΥ ΕΠΙΣΤΡΈΦΕΙ ΣΤΟ ΑΡΧΙΚΟ MENU
    menu_button_group.remove(Menu_button)
    Menu_button = menu_button(500, 500)
    menu_button_group.add(Menu_button)
    while skins:
        draw_skin_menu()                                  # Καλεί τη συνάρτηση που εμφανίζει το menu με τα skins.
        '''
                    Σε αυτό το menu δίνονται στον χρήστη 5 επιλογές για το τι skin θα επιλέξει για το διαστημόπλοιο
                    και ανάλογα ποιο skin θα επιλέξει, τότε θα ξεκινάει το κεντρικό παιχνίδι με αυτό.
        '''
        if Skin_1.check_button_clicked() == True:
            Game = True
            skins = False
            menu = False
            current_sprite = 0
        if Skin_2.check_button_clicked() == True:
            Game = True
            skins = False
            menu = False
            current_sprite = 2
        if Skin_3.check_button_clicked() == True:
            Game = True
            skins = False
            menu = False
            current_sprite = 4
        if Skin_4.check_button_clicked() == True:
            Game = True
            skins = False
            menu = False
            current_sprite = 6
        if Skin_5.check_button_clicked() == True:
            Game = True
            skins = False
            menu = False
            current_sprite = 8

        # Αν πατηθεί το κουμπί που λέει menu τότε επιστρέφει τον χρήστη στο αρχικό menu.
        if Menu_button.check_menu_button_clicked() == True:
            Game = False
            skins = False
            menu = True
        # Αν πατηθεί το 'x' πάνω δεξιά τότε κλείνει το παράθυρο.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Game = False
                MAIN_LOOP = False
                menu = False
                skins = False

    '''
    --------------------------------------------------------------------------------------------------------------------
                                                ΜΕΤΑΒΛΗΤΕΣ ΠΑΙΧΝΙΔΙΟΥ:
                                                
    '''
    # GAME_ENDING:
    STOP_GAME = False  # Σταματάει το παιχνίδι αν γίνει True.
    GAME_OVER = False  # Αν γίνει True σημαίνει οτι έχασε ο παίκτης

    #MUSIC AND SOUND EFFECTS:
    space_music = mixer.music.load(os.path.join('music', 'space_music.wav'))  # Φορτώνει τη μουσική του παιχνιδιού.
    jump_sound_effect = mixer.Sound(os.path.join('sounds', 'jump_sound.wav'))  # Φορτώνει τον ήχο "jump" του διαστημόπλοιου.
    death_sound_effect = mixer.Sound(os.path.join('sounds', 'death_sound.wav'))  # Φορτώνει τον ήχο που κάνει όταν χάνει.
    mixer.music.play(-1)                # Το -1 είναι για να παίζει τη μουσική επ' άπειρον.
    death_sound = True                  # Δεν ξανά-επαναλαμβάνεται ο ήχος που κάνει όταν χάνει ο χρήστης
    jump_sound_effect.set_volume(0.1)   # Ορίζει τον ένταση του ηχητικού εφέ 'jump'.
    death_sound_effect.set_volume(0.2)  # Ορίζει τον ένταση του ηχητικού εφέ 'jump'.
    #ΠΥΡΑΥΛΟΣ:
    charge = False                      # Απαγορεύει να επιτεθεί ο πύραυλος στο διαστημόπλοιο
    spawn = True                        # Επιτρέπει το να εμφανιστεί πύραυλος στην οθόνη
    #ΕΜΠΟΔΙΑ:
    pipe_frequency = 1500  # Συχνότητα εμποδίων σε milliseconds
    last_pipe = - pipe_frequency
    pipe_counter = 0  # Αρχικό νούμερο εμποδίων
    # ΔΙΑΣΤΗΜΟΠΛΟΙΟ:
    spaceship_group = pygame.sprite.Group()     # Δημιουργεί group στο οποίο θα προσθέσουμε το διαστημόπλοιο
    Spaceship = spaceship(100, 80)              # Φορτώνει την κλάση του διαστημοπλοίου σε sprite
    spaceship_group.add(Spaceship)              # Βάζει το sprite διαστημόπλοιο μέσα στο group
    Spaceship.change_sprite(0)                  # Το διαστημόπλοιο παίρνει την αρχική του εμφάνιση
    # BACKGROUND:
    background_image = pygame.image.load(os.path.join('images', 'SPACE.jpg'))  # Φορτώνει την εικόνα του background
    background = pygame.transform.scale(background_image, (width, height))   # Μετατρέπει το μέγεθος της εικόνας του background στο μέγεθος του παραθύρου:
    background_rect = pygame.Rect(0, 0, 0, 0)  # Οι αρχικές συντεταγμένες του background και το μέγεθος του ως Rectangle
    # ΕΔΑΦΟΣ:
    ground_image = pygame.image.load(os.path.join('images', 'ground.gif'))   # Φορτώνει την εικόνα του Εδάφους:
    ground = pygame.transform.scale(ground_image, (width, height + 33))  # Μετατρέπει το μέγεθος της εικόνας του Εδάφους στο μέγεθος του παραθύρου
    ground_rect = pygame.Rect(0, -30, 0, 0)     # Οι αρχικές συντεταγμένες του εδάφους και το μέγεθος του ως Rectangle.
    # POWER_UP:
    power_up = False                            # Το power up είναι ανενεργό
    power_up_used = False                       # Δεν έχει χρησιμοποιηθεί power up
    SPACE_pressed = False                       # Δηλώνει ότι δεν πατήθηκε το κουμπί SPACE
    power_up_text_disappear = False             # Εμφανίζεται το κείμενο με τον μετρητή των power ups
    seconds_text_disappear = True               # Δεν εμφανίζεται το κείμενο με τα seconds
    power_up_group = pygame.sprite.Group()      # Δημιουργεί group στο οποίο θα προσθέσουμε τα power ups
    power_ups = 1                               # Αρχικό νούμερο των power ups
    # ΠΥΡΑΥΛΟΣ:
    rocket_group = pygame.sprite.Group()        # Δημιουργεί group στο οποίο θα προσθέσουμε τους πυραύλους

    # ΕΜΠΟΔΙΑ:
    pipe_group = pygame.sprite.Group()          # Δημιουργεί group στο οποίο θα προσθέσουμε τα εμπόδια
    missing_pipe_group = pygame.sprite.Group()  # Δημιουργεί group στο οποίο θα προσθέσουμε για το υπόλοιπο των εμποδίων


    # ΕΞΩΓΗΙΝΟΙ
    alien_group = pygame.sprite.Group()     # Δημιουργεί group στο οποίο θα προσθέσουμε τους εξωγήινους
    power_up_seconds = 0                    # Αρχικοποίηση δευτερολέπτων που κρατάει το κάθε power up
    clock = pygame.time.Clock()             # Δημιουργεί ένα αντικείμενο ρολογιού που μετρά την ώρα.
    starting = pygame.time.get_ticks()
    # SCORE:
    score = 0                                       # Αρχικοποιεί τον μετρητή του score σε μηδέν.
    if retry_button_clicked == True:
        Game = True
        retry_button_clicked = False
    Spaceship.change_sprite(current_sprite)         # Το διαστημόπλοιο ξεκινάει με το skin που προ-επέλεξε ο παίκτης.
    # ΔΗΛΩΝΕΙ ΤΗ CLASS ΜΕ ΤΟ ΚΟΥΜΠΙ ΠΟΥ ΕΠΙΣΤΡΈΦΕΙ ΣΤΟ ΑΡΧΙΚΟ MENU
    menu_button_group.remove(Menu_button)
    Menu_button = menu_button(80, 30)
    menu_button_group.add(Menu_button)
    # όσο είναι True μπορεί να ξεκινήσει το παιχνίδι
    while Game:
        # Σε περίπτωση που το διαστημόπλοιο ακουμπήσει το έδαφος τότε χάνει ο παίκτης
        if spaceship_group.sprites()[0].rect.y >= 450:
            GAME_OVER = True
        clock.tick(60)            # αλλάζει 60 frames ανά δευτερόλεπτο
        '''
                    window DRAWING:
        '''

        # Εκτελεί τη συνάρτηση που δημιουργεί το παράθυρο του κύριου παιχνιδιού:
        draw_window(ground, ground_rect, background, background_rect, wn, score, power_ups, font_score, font_power_up, width, pipe_group, spaceship_group, power_up_group, missing_pipe_group, alien_group, rocket_group, power_up_text_disappear, power_up_seconds, seconds_text_disappear)

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
        if GAME_OVER == True:
            STOP_GAME = True
            ''' 
            Αν έχει χάσει ο παίκτης τότε εμφανίζεται ένα κουμπί στην οθόνη που τον ρωτάει αν θέλει να ξαναπροσπαθήσει.
            Αν το πατήσει τότε ξανά ξεκινάει το παιχνίδι από την αρχή.
            
            '''
            retry_button_group.draw(wn)
            if Retry_button.check_retry_button_clicked() == True:
                retry_button_clicked = True
                menu = False
                Game = False
                skins = False
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
                if pygame.sprite.spritecollideany(Spaceship, pipe_group):
                    GAME_OVER = True
                if pygame.sprite.spritecollideany(Spaceship, rocket_group):
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

            alien_group.update()                        # 1.Των εξωγήινων
            pipe_group.update()                         # 2.Των εμποδίων
            missing_pipe_group.update()                 # 3.Του υπολοίπου των εμποδίων
            power_up_group.update()                     # 4.Των power ups
            spaceship_group.update(GAME_OVER)           # 5.Του διαστημοπλοίου



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
            # Αν τα power ups έχουν τελειώσει τότε απαγορεύει στον παίκτη να τα ξαναχρησιμοποιήσει
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
                    power_up_seconds = (pygame.time.get_ticks() - start_ticks)
                    if power_up_seconds <= 4000 and power_up_seconds >= 0 or pygame.sprite.spritecollideany(Spaceship, pipe_group):
                        power_up = True                 # 1.δηλώνεται ότι το power up είναι ενεργό
                        Spaceship.change_sprite(current_sprite+1)      # 2.αλλάζει η εμφάνιση το διαστημόπλοιο
                        seconds_text_disappear = False  # 3.όσο το power_up είναι ενεργό, εμφανίζεται το κείμενο με τα seconds
                    else:  # ΑΛΛΙΩΣ αν τα ξεπεράσει ή το διαστημόπλοιο δεν ακουμπάει κάποιο εμπόδιο τότε:
                        power_up = False                # 1.δηλώνεται ότι το power up είναι ανενεργό
                        seconds_text_disappear = True   # 2.και όσο είναι ανενεργό εξαφανίζεται το κείμενο με τα seconds
                        Spaceship.change_sprite(current_sprite)     # 3.το διαστημόπλοιο παίρνει την αρχική του εμφάνιση
                        SPACE_pressed = False           # 4.δηλώνεται ότι το κουμπί SPACE σταματάει να είναι πατημένο
                        power_up_used = True            # 5.δηλώνεται ότι το τρέχον power έχει χρησιμοποιηθεί


        else:
            # Καλεί την εντολή fall από την κλάση spaceship όπου κάνει το διαστημόπλοιο να πέφτει
            Spaceship.fall()

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
            if pygame.sprite.spritecollideany(Spaceship, power_up_group):
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
            if pygame.sprite.spritecollideany(Spaceship, alien_group):
                if add_score == True:
                    score += 5
                    add_score = False
                # Κάθε εξωγήινος που ακουμπά το διαστημόπλοιο αφαιρείται από το group των εξωγήινων
                alien_group.sprites()[0].kill()
            else:
                add_score = True
            '''
            Όταν η τεμνημένη του διαστημοπλοίου και η τεμνημένη του πρώτου εμποδίου είναι ίσες, 
            δηλαδή αν το διαστημόπλοιο περάσει ανάμεσα από το συγκεκριμένο εμπόδιο τότε προσθέτετε 1 πόντος στο score.
            '''
            if spaceship_group.sprites()[0].rect.x == pipe_group.sprites()[0].rect.x:
                score += 1
        # Μετά από 4 δευτερόλεπτα εξαφανίζεται το κείμενο που εξηγεί στον παίκτη πως να χρησιμοποιήσει τα power ups του.
        secs = (pygame.time.get_ticks() - starting)
        if secs >= 4000:
            power_up_text_disappear = True
        '''
         Αν το τρέχον score του παίκτη ξεπεράσει το προηγούμενο highscore τότε εκείνο γίνεται το νέο highscore
         και το γράφει στο αρχείο highscore.txt
        '''
        if High_score < score:
            High_score = score
            with open('files/highscore.txt','w') as f:
                f.write(str(High_score))
        '''
            Αν ο χρήστης πατήσει το κουμπί menu τότε επιστρέφει στο αρχικό menu.
        '''
        menu_button_group.draw(wn)
        if Menu_button.check_menu_button_clicked() == True:
            Game = False
            skins = False
            menu = True

        '''
        
            Μόλις ο Χρήστης κάνει "click" εκεί που κλείνει το παράθυρο τότε θέτει το "run" σε False και σταματάει η LOOPA: 
        
        '''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Game = False
                MAIN_LOOP = False
                menu = False
                skins = False
        # Αν ο χρήστης κάνει click και το STOP_GAME είναι False τότε το διαστημόπλοιο θα χοροπηδήσει:
            if event.type == pygame.MOUSEBUTTONDOWN and STOP_GAME == False:
                jump_sound_effect.play(0)

        pygame.display.update()         # Κάνει update την οθόνη.
    pipe_group.remove()                 # αφαιρεί από το group με τα εμπόδια όλα τα εμπόδια
    mixer.music.stop()                  # Σταματάει τη μουσική, αν σταματήσει το παιχνίδι.
    """
    --------------------------------------------------------------------------------------------------------------------
    """
pygame.quit()                 # κλείνει το παράθυρο