import pygame
import random
import math
import time
import sys


pygame.init()
class DrawInformation: #ορισμός χρωμάτων
    BLACK = 0, 0, 0
    WHITE = 255, 255, 255
    GREEN = 0, 255, 0
    RED = 255, 0, 0
    BACKGROUND_COLOR = WHITE
    GRADIENTS = [
        (128, 128, 128),
        (160, 160, 160),
        (192, 192, 192)
    ]
    FONT = pygame.font.SysFont('comicsans', 30) #ορισμός γραμματοσειράς
    LARGE_FONT = pygame.font.SysFont('comicsans', 40)
    SIDE_PAD = 100 #ανω και πλαγια γεμίσματα
    TOP_PAD = 150

    def __init__(self, width, height, lst):  # ορισμός κλάσης
        self.width = width
        self.height = height
        self.window = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Απεικόνειση αλγορίθμων ταξινόμησης")
        self.set_list(lst)

    def set_list(self, lst):  # μέθοδος ορισμού μεγέθους λίστας
        self.lst = lst
        self.min_val = min(lst)
        self.max_val = max(lst)
        self.block_width = round((self.width - self.SIDE_PAD) / len(lst))
        self.block_height = math.floor((self.height - self.TOP_PAD) /(self.max_val - self.min_val))
        self.start_x = self.SIDE_PAD // 2
def draw(draw_info, algo_name, ascending): #εμφάνιση γραμμάτων οδηγιών
    draw_info.window.fill(draw_info.BACKGROUND_COLOR)
    title = draw_info.LARGE_FONT.render(f"{algo_name} - {'Άυξουσα' if ascending else 'Φθίνουσα'}", 1,draw_info.GREEN)
    draw_info.window.blit(title, (draw_info.width / 2 - title.get_width() /2, 5))
    controls = draw_info.FONT.render("R - Δημιουργία νέου πίνακα | SPACE -Έναρξη ταξινόμησης | A - Άυξουσα | D - Φθίνουσα", 1,draw_info.BLACK)
    draw_info.window.blit(controls, (draw_info.width / 2 -controls.get_width() / 2, 45))
    sorting = draw_info.FONT.render("I - Ταξινόμηση με εισαγωγή | B -Ταξινόμηση φυσαλίδας", 1, draw_info.BLACK)
    draw_info.window.blit(sorting, (draw_info.width / 2 - sorting.get_width()/ 2, 75))
    draw_list(draw_info)
    pygame.display.update()
def draw_list(draw_info, color_positions={}, clear_bg=False): #μέθοδος εμφάνισης της λίστας στην οθόνη
    lst = draw_info.lst
    if clear_bg:
        clear_rect = (draw_info.SIDE_PAD // 2, draw_info.TOP_PAD,draw_info.width - draw_info.SIDE_PAD, draw_info.height- draw_info.TOP_PAD)
        pygame.draw.rect(draw_info.window, draw_info.BACKGROUND_COLOR,clear_rect)
    for i, val in enumerate(lst):
         x = draw_info.start_x + i * draw_info.block_width
         y = draw_info.height - (val - draw_info.min_val) *draw_info.block_height
         color = draw_info.GRADIENTS[i % 3]
         if i in color_positions:
            color = color_positions[i]
            pygame.draw.rect(draw_info.window, color, (x, y,draw_info.block_width, draw_info.height))
    if clear_bg:
        pygame.display.update()
def generate_starting_list(n, min_val, max_val): #μέθοδος δημιουργίας λίστας
    lst = []
    for _ in range(n):
        val = random.randint(min_val, max_val)
        lst.append(val)
    return lst
def main():
    run = True
    clock = pygame.time.Clock()
    n = 50  # αριθμός στοιχείων της λίστας
    min_val = 0
    max_val = 100
    lst = generate_starting_list(n, min_val, max_val)  # κάλεσμα μεθόδου δημιουργίας λίστας
    draw_info = DrawInformation(1230, 820, lst)
    sorting = False
    ascending = True
    sorting_algo_name = "Ταξινόμηση φυσαλίδας"
    sorting_algorithm_generator = None
    while run:
        clock.tick(60)
        if sorting:
            try:
                next(sorting_algorithm_generator)
            except StopIteration:
                sorting = False
        else:
            draw(draw_info, sorting_algo_name, ascending)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type != pygame.KEYDOWN:
                continue
            if event.key == pygame.K_r:
                lst = generate_starting_list(n, min_val, max_val)
                draw_info.set_list(lst)
                sorting = False
            elif event.key == pygame.K_SPACE and sorting == False:
                sorting = True
            elif event.key == pygame.K_a and not sorting:
                ascending = True
            elif event.key == pygame.K_d and not sorting:
                ascending = False
            elif event.key == pygame.K_i and not sorting:
                sorting_algo_name = "Ταξινόμηση με εισαγωγή"
            elif event.key == pygame.K_b and not sorting:
                sorting_algo_name = "Ταξινόμηση φυσαλίδας"
            elif event.key == pygame.K_s and not sorting:
                sorting_algo_name = "Ταξινόμηση με επιλογής"
           pygame.quit()
if __name__ == "__main__":
 main()