import pygame

# Δηλώνει τη συνάρτηση που δημιουργεί το ΠΑΡΑΘΥΡΟ του παιχνιδιού:
def draw_window(ground,ground_rect,background,background_rect,wn,width,spaceship_group):
    wn.blit(background, (background_rect.x, background_rect.y))         # Εμφανίζει το background στην οθόνη
    wn.blit(background, (background_rect.x+width, background_rect.y))   # Εμφανίζει το ίδιο background ακριβώς απο δίπλα
    wn.blit(ground, (ground_rect.x, ground_rect.y))                     # Εμφανίζει το έδαφος στην οθόνη
    wn.blit(ground, (ground_rect.x + width, ground_rect.y))             # Εμφανίζει το ίδιο έδαφος ακριβώς απο δίπλα
    spaceship_group.draw(wn)                                            # Εμφανίζει το διαστημόπλοιο στην οθόνη.
    pygame.display.update()                                             # Κάνει update την οθόνη.
