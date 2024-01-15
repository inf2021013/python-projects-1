import pygame       # Για τη δημιουργία του παιχνιδιού

# Δηλώνει τη συνάρτηση που δημιουργεί το ΠΑΡΑΘΥΡΟ του παιχνιδιού:
def draw_window(ground, ground_rect, background, background_rect, wn, score,power_ups,font_score,font_power_up, width, pipe_group,spaceship_group,power_up_group,missing_pipe_group,alien_group,rocket_group,power_up_text_disappear,seconds,seconds_text_disappear):
    wn.blit(background, (background_rect.x, background_rect.y))         # Εμφανίζει το background στην οθόνη
    wn.blit(background, (background_rect.x+width, background_rect.y))   # Εμφανίζει το ίδιο background ακριβώς απο δίπλα
    alien_group.draw(wn)                                                # Εμφανίζει τους εξωγήινους στην οθόνη
    power_up_group.draw(wn)                                             # Εμφανίζει τα power ups στην οθόνη
    pipe_group.draw(wn)                                                 # Εμφανίζει τα εμπόδια στην οθόνη
    wn.blit(ground, (ground_rect.x, ground_rect.y))                     # Εμφανίζει το έδαφος στην οθόνη
    wn.blit(ground, (ground_rect.x + width, ground_rect.y))             # Εμφανίζει το ίδιο έδαφος ακριβώς απο δίπλα
    missing_pipe_group.draw(wn)                                         # Εμφανίζει το υπόλοιπο των εμποδίων στην οθόνη
    draw_score(score, wn, font_score)                                   # Εμφανίζει το score στην οθόνη
    draw_power_ups(power_ups,wn,font_power_up)                          # Εμφανίζει τον μετρητή των power ups στην οθόνη
    rocket_group.draw(wn)                                               # Εμφανίζει τους πυραύλους στην οθόνη.
    spaceship_group.draw(wn)                                            # Εμφανίζει το διαστημόπλοιο στην οθόνη.
    if seconds_text_disappear == False:                                 # Ελέγχει αν πρέπει να εμφανιστούν τα seconds
        draw_seconds(seconds, wn, font_power_up)
    if power_up_text_disappear == False:  # Ελέγχει αν πρέπει να εμφανιστεί αυτό που εξηγεί στο χρήστη πως να χρησιμοποιήσει τα power_ups του
        draw_press_SPACE(wn, font_power_up)
    pygame.display.update()    # Κάνει update την οθόνη.

# Εμφανίζει το score στην οθόνη σε χρώμα άσπρο:
def draw_score(score,wn,font):
    score_text = font.render(str(score), True, (255, 255, 255))
    wn.blit(score_text, (450, 30))

# Εμφανίζει το κείμενο με τα δευτερόλεπτα που απομένουν από τα power_ups σε χρώμα κόκκινο και άσπρο:
def draw_seconds(seconds,wn,font):
    seconds_text_a = font.render("seconds: ", True, (255, 0, 0))
    seconds_text_b = font.render(str(int(seconds / 1000)), True, (255, 255, 255))
    wn.blit(seconds_text_a, (20, 30))
    wn.blit(seconds_text_b, (170, 30))

# Εμφανίζει το κείμενο εξηγεί στο χρήστη πως να χρησιμοποιήσει τα power_ups του σε χρώμα άσπρο:
def draw_press_SPACE(wn,font):
    press_a = font.render("press \"SPACE\" to use your power ups",True,(255,255,255))
    wn.blit(press_a,(20,400))

# Εμφανίζει τον μετρητή των power ups στην οθόνη σε χρώμα ροζ και άσπρο:
def draw_power_ups(power_ups,wn,font):
    power_ups_text_a = font.render("POWER UPS: ", True, (255, 0, 255))
    power_ups_text_b = font.render(str(power_ups), True, (255, 255, 255))
    wn.blit(power_ups_text_a, (20, 550))
    wn.blit(power_ups_text_b, (230, 550))
