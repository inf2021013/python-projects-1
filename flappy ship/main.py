from classes import *
clock = pygame.time.Clock()
# DEFINE VARIABLES:
WIDTH, HEIGHT = 736, 547
wn = pygame.display.set_mode((WIDTH, HEIGHT))
run = True
ship_scale = 1
pipe_frequency = 1500  # Συχνότητα εμποδίων σε milliseconds
last_pipe = - pipe_frequency
pipe_counter = 0  # Αρχικό νούμερο εμποδίων
pipe_group = pygame.sprite.Group()  # Δημιουργεί group στο οποίο θα προσθέσουμε τα εμπόδια
ship_group =pygame.sprite.Group()
ship = Ship(100,200)
ship_group.add(ship)
game_over = False
background_image = pygame.image.load('images/background_1.jpg')
background = pygame.transform.scale(background_image, (WIDTH, HEIGHT))
background_rect = pygame.Rect(0, 0, 0, 0)
ground_image = pygame.image.load('images/sea.png')
ground = pygame.transform.scale(ground_image, (WIDTH+8, 104))
ground_rect = pygame.Rect(0, 450, 0, 0)
drown =False
def draw_ground():
    wn.blit(
        # Εμφανίζει το ίδιο background ακριβώς απο δίπλα.
        ground, (ground_rect.x + WIDTH, ground_rect.y)
    )
    wn.blit(
        # Εμφανίζει το background στην οθόνη.
        ground, (ground_rect.x, ground_rect.y)
    )

# FUNCTIONS:
def draw_window():
    wn.fill((0, 0, 0))
    wn.blit(
        # Εμφανίζει το background στην οθόνη.
        background, (background_rect.x, background_rect.y)
    )
    wn.blit(
        # Εμφανίζει το ίδιο background ακριβώς απο δίπλα.
        background, (background_rect.x + WIDTH, background_rect.y)
    )

    pipe_group.draw(wn)  # Εμφανίζει τα εμπόδια στην οθόνη.
    ship_group.draw(wn)
    draw_ground()
    pygame.display.update()





while run:
    if ship_group.sprites()[0].rect.y >=400:
        game_over=True
        ship.drown()
        drown = True
    clock.tick(60)

    # ENDS THE GAME
    if game_over == False:
        ship_group.update(game_over)
        background_rect.x -= 2
        if background_rect.x == -WIDTH:
            background_rect.x = 0
        ground_rect.x -= 4
        if ground_rect.x == -WIDTH:
            ground_rect.x = 0

        # Pipe Generator:
        time_now = pygame.time.get_ticks()  # Μετράει την τρέχον χρονική στιγμή σε milliseconds
        if time_now - last_pipe > pipe_frequency:
            pipe_height = random.randint(-100, 100)  # Δημιουργεί ένα τυχαίο ακέραιο αριθμό για το ύψος των εμποδίων
            btm_pipe = Pipe(WIDTH, int(HEIGHT/ 2) + pipe_height - 70, -1)  # Κάτω μέρος του εμποδίου με τυχαίο ύψος.
            tp_pipe = Pipe(WIDTH, int(HEIGHT / 2) + pipe_height - 50, 1)  # Πάνω μέρος του εμποδίου με τυχαίο ύψος.
            pipe_group.add(btm_pipe)  # Βάζει το κάτω μέρος του εμποδίου στο group με τα εμπόδια
            pipe_group.add(tp_pipe)  # Βάζει το πάνω μέρος του εμποδίου στο group με τα εμπόδια
            last_pipe = time_now  # Δηλώνει τη χρονική στιγμή που εμφανίστηκε το τελευταίο εμπόδιο.
            pipe_counter += 1  # Μετράει πόσα εμπόδια έχουν δημιουργηθεί
        pipe_group.update(4)
    elif not drown:
        ship.fall()
    draw_window()
    if len(pipe_group) > 0:
        if pygame.sprite.collide_mask(ship, pipe_group.sprites()[0]):
            game_over = True
        if pygame.sprite.collide_mask(ship, pipe_group.sprites()[1]):
            game_over = True

    # QUIT GAME:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run= False



