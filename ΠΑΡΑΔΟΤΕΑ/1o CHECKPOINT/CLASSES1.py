import pygame
import os

class spaceship(pygame.sprite.Sprite):
    def __init__(self,x,y,name):
        pygame.sprite.Sprite.__init__(self)
        # Ρυθμίζει το μέγεθος της εικόνας του διαστημοπλοίου
        self.image = pygame.transform.scale(pygame.image.load(os.path.join('images',name)), (64, 56))
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]         # Η αρχική θέση του διαστημοπλοίου
        self.acceleration = 0.3           # Η αρχική τιμή της επιτάχυνσης.
        self.velocity = 0                 # Η αρχική τιμή της ταχύτητας.
        self.clicked = False              # δηλώνει ότι ο χρήστης δεν έχει πατήσει click εξαρχής
        self.GAMEOVER = False             # δηλώνει ότι δεν έχει χάσει ο παίκτης ακόμα
        self.STOP_GAME = False            # δηλώνει ότι δεν έχει τελειώσει το παιχνίδι ακόμα
    def update(self):
        if self.STOP_GAME == False:
            # gravity
            self.rect.y += self.velocity        # Το y του το διαστημοπλοίου αυξάνεται ανάλογα με την ταχύτητα του
            self.velocity += self.acceleration  # Η ταχύτητά του αυξάνεται ανάλογα με την επιτάχυνση του
            if self.velocity > 10:              # Εμποδίζει την ταχύτητα του να γίνει μεγαλύτερη απο 10
                self.velocity = 10
            # jump #Το διαστημόπλοιο αντιδράει μόνο όταν πατάει συνεχώς click ο χρήστης και όχι όσο το κρατάει πατημένο:
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                self.velocity = -4
            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False
            # Δεν αφήνει το διαστημόπλοιο να ξεπεράσει τα όρια του παραθύρου :
            if self.rect.y <= 0:
                self.rect.y = 0
            # CHECK FOR GAME OVER:
            if self.rect.y >= 450:              # Aν το διαστημόπλοιο αγγίξει το έδαφος τελειώνει το παιχνίδι
                self.GAMEOVER = True
            if self.GAMEOVER == True:           # Αν χάσει ο χρήστης τότε σταματάει το παιχνίδι
                self.STOP_GAME = True

    # Συνάρτηση που επιστρέφει True στο κεντρικό παιχνίδι αν έχει χάσει ο παίκτης:

    def game_over(self):
        if self.GAMEOVER == True:
            return True