import pygame

# Initialize Pygame
pygame.init()

# Set the window size
window_size = (900, 900)

# Create the window
screen = pygame.display.set_mode(window_size)

# Set the window title
pygame.display.set_caption('Tic Tac Toe')

# Set the background color
bg_color = pygame.Color('grey12')

# Initialize the game board
board = [[None, None, None],
         [None, None, None],
         [None, None, None]]

# Initialize the current player (X starts)
current_player = 'X'

# Set the colors for each player
colors = {'X': pygame.Color('darkorchid1'),
          'O': pygame.Color('darkorange1')}

# Set the font and font size for the game
font = pygame.font.Font(None, 100)

# Set the width and height of each game cell
cell_width = cell_height = 200

# Set the margin between each cell
margin = 50

# Set the dimensions of the game board
board_width = cell_width * 3 + margin * 2
board_height = cell_height * 3 + margin * 2

# Set the dimensions of the game board rectangle
board_rect = pygame.Rect((0, 0), (board_width, board_height))

# Set the dimensions of each cell rectangle
cell_rects = []
for i in range(3):
    for j in range(3):
        rect = pygame.Rect((margin + j * (cell_width + margin),
                            margin + i * (cell_height + margin)),
                           (cell_width, cell_height))
        cell_rects.append(rect)

# Set the winning combinations
winning_combinations = [
    [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
    [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
    [0, 4, 8], [2, 4, 6]  # diagonals
]

# Run the game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Check which cell was clicked
            x, y = event.pos
            for i, rect in enumerate(cell_rects):
                if rect.collidepoint(x, y):
                    # Update the game board if the cell is empty
                    if board[i // 3][i % 3] is None:
                        board[i // 3][i % 3] = current_player
                        # Switch to the other player
                        current_player = 'O' if current_player == 'X' else 'X'

    # Draw the background
    screen.fill(bg_color)

    # Draw the game board
    pygame.draw.rect(screen, pygame.Color('white'), board_rect)

    for i, rect in enumerate(cell_rects):
        # Draw the cell
        pygame.draw.rect(screen, pygame.Color('grey'), rect)

        # Draw the player symbol
        symbol = board[i // 3][i % 3]
        if symbol is not None:
            text = font.render(symbol, True, colors[symbol])
            text_rect = text.get_rect(center=rect.center)
            screen.blit(text, text_rect)

    # Check if there is a winner
    for combination in winning_combinations:
        cells = [board[i // 3][i % 3] for i in combination]
        if all(cell == 'X' for cell in cells):
            print('X wins!')
            running = False
        elif all(cell == 'O' for cell in cells):
            print('O wins!')
            running = False

    # Update the display
    pygame.display.flip()
pygame.quit()
