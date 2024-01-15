import random
import time


# Global variable for game over
game_over = False
# Global variable for alphabet
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"



# Player global variables

# Variable for grid
grid_AI = [[]]
# Variable for grid size
grid_size_AI = 10
# Variable for number of ships to place
num_of_ships_AI = 5
# Variable for bullets left
bullets_left_AI = 101
# Variable for number of ships sunk
num_of_ships_sunk_AI = 0
# Variable for ship positions
ship_positions_AI = [[]]


# AI global variables

# Variable for grid
grid = [[]]
# Variable for grid size
grid_size = 10
# Variable for number of ships to place
num_of_ships = 5
# Variable for bullets left
bullets_left = 101
# Variable for number of ships sunk
num_of_ships_sunk = 0
# Variable for ship positions
ship_positions = [[]]


def validate_grid_and_place_ship(start_row, end_row, start_col, end_col):
    """Will check the row or column to see if it is safe to place a ship there"""
    global grid
    global ship_positions

    all_valid = True
    for r in range(start_row, end_row):
        for c in range(start_col, end_col):
            if grid[r][c] != ".":
                all_valid = False
                break
    if all_valid:
        ship_positions.append([start_row, end_row, start_col, end_col])
        for r in range(start_row, end_row):
            for c in range(start_col, end_col):
                grid[r][c] = "O"
    return all_valid


def try_to_place_ship_on_grid(row, col, direction, length):
    """Based on direction will call helper method to try and place a ship on the grid"""
    global grid_size

    start_row, end_row, start_col, end_col = row, row + 1, col, col + 1
    if direction == "left":
        if col - length < 0:
            return False
        start_col = col - length + 1

    elif direction == "right":
        if col + length >= grid_size:
            return False
        end_col = col + length

    elif direction == "up":
        if row - length < 0:
            return False
        start_row = row - length + 1

    elif direction == "down":
        if row + length >= grid_size:
            return False
        end_row = row + length

    return validate_grid_and_place_ship(start_row, end_row, start_col, end_col)


def create_grid():
    """Will create a 10x10 grid and randomly place down ships
       of different sizes in different directions"""
    global grid
    global grid_size
    global num_of_ships
    global ship_positions

    shipsize = 6
    random.seed(time.time())

    rows, cols = (grid_size, grid_size)

    grid = []
    for r in range(rows):
        row = []
        for c in range(cols):
            row.append(".")
        grid.append(row)

    num_of_ships_placed = 0

    ship_positions = []

    while num_of_ships_placed != num_of_ships:
        random_row = random.randint(0, rows - 1)
        random_col = random.randint(0, cols - 1)
        direction = random.choice(["left", "right", "up", "down"])
        ship_size = shipsize -1
        if try_to_place_ship_on_grid(random_row, random_col, direction, ship_size):
            num_of_ships_placed += 1
            shipsize = shipsize - 1
            if (shipsize < 3):
                shipsize = 4


def print_grid():
    """Will print the grid with rows A-J and columns 0-9"""
    global grid
    global alphabet

    debug_mode = True

    alphabet = alphabet[0: len(grid) + 1]

    for row in range(len(grid)):
        print(alphabet[row], end=") ")
        for col in range(len(grid[row])):
            if grid[row][col] == "O":
                if debug_mode:
                    print("O", end=" ")
                else:
                    print(".", end=" ")
            else:
                print(grid[row][col], end=" ")
        print("")

    print("  ", end=" ")
    for i in range(len(grid[0])):
        print(str(i), end=" ")
    print("")


def accept_valid_bullet_placement():
    """Will get valid row and column to place bullet shot"""
    global alphabet
    global grid_AI

    is_valid_placement = False
    row = -1
    col = -1
    while is_valid_placement is False:
        placement = input("Enter row (A-J) and column (0-9) such as A3: ")
        placement = placement.upper()
        if len(placement) <= 0 or len(placement) > 2:
            print("Error: Please enter only one row and column such as A3")
            continue
        row = placement[0]
        col = placement[1]
        if not row.isalpha() or not col.isnumeric():
            print("Error: Please enter letter (A-J) for row and (0-9) for column")
            continue
        row = alphabet.find(row)
        if not (-1 < row < grid_size_AI):
            print("Error: Please enter letter (A-J) for row and (0-9) for column")
            continue
        col = int(col)
        if not (-1 < col < grid_size_AI):
            print("Error: Please enter letter (A-J) for row and (0-9) for column")
            continue
        if grid_AI[row][col] == "#" or grid_AI[row][col] == "X":
            print("You have already shot a bullet here, pick somewhere else")
            continue
        if grid_AI[row][col] == "." or grid_AI[row][col] == "O":
            is_valid_placement = True

    return row, col


def check_for_ship_sunk(row, col):
    """If all parts of a shit have been shot it is sunk and we later increment ships sunk"""
    global ship_positions_AI
    global grid_AI

    for position in ship_positions_AI:
        start_row = position[0]
        end_row = position[1]
        start_col = position[2]
        end_col = position[3]
        if start_row <= row <= end_row and start_col <= col <= end_col:
            # Ship found, now check if its all sunk
            for r in range(start_row, end_row):
                for c in range(start_col, end_col):
                    if grid_AI[r][c] != "X":
                        return False
    return True


def shoot_bullet():
    """Updates grid and ships based on where the bullet was shot"""
    global grid_AI
    global num_of_ships_sunk_AI
    global bullets_left

    row, col = accept_valid_bullet_placement()
    print("")
    print("----------------------------")

    if grid_AI[row][col] == ".":
        print("You missed, no ship was shot")
        grid_AI[row][col] = "#"
    elif grid_AI[row][col] == "O":
        print("You hit!", end=" ")
        grid_AI[row][col] = "X"
        if check_for_ship_sunk(row, col):
            print("A ship was completely sunk!")
            num_of_ships_sunk_AI += 1
        else:
            print("A ship was shot")

    bullets_left -= 1






def validate_grid_and_place_ship_AI(start_row_AI, end_row_AI, start_col_AI, end_col_AI):
    """Will check the row or column to see if it is safe to place a ship there"""
    global grid_AI
    global ship_positions_AI

    all_valid_AI = True
    for r_AI in range(start_row_AI, end_row_AI):
        for c_AI in range(start_col_AI, end_col_AI):
            if grid_AI[r_AI][c_AI] != ".":
                all_valid_AI = False
                break
    if all_valid_AI:
        ship_positions_AI.append([start_row_AI, end_row_AI, start_col_AI, end_col_AI])
        for r_AI in range(start_row_AI, end_row_AI):
            for c_AI in range(start_col_AI, end_col_AI):
                grid_AI[r_AI][c_AI] = "O"
    return all_valid_AI


def try_to_place_ship_on_grid_AI(row, col, direction, length):
    """Based on direction will call helper method to try and place a ship on the grid"""
    global grid_size_AI

    start_row, end_row, start_col, end_col = row, row + 1, col, col + 1
    if direction == "left":
        if col - length < 0:
            return False
        start_col = col - length + 1

    elif direction == "right":
        if col + length >= grid_size_AI:
            return False
        end_col = col + length

    elif direction == "up":
        if row - length < 0:
            return False
        start_row = row - length + 1

    elif direction == "down":
        if row + length >= grid_size_AI:
            return False
        end_row = row + length

    return validate_grid_and_place_ship_AI(start_row, end_row, start_col, end_col)


def create_grid_AI():
    """Will create a 10x10 grid and randomly place down ships
       of different sizes in different directions"""
    global grid_AI
    global grid_size_AI
    global num_of_ships_AI
    global ship_positions_AI
    global alphabet

    shipsize_AI = 6
    rows, cols = (grid_size_AI, grid_size_AI)

    grid_AI = []
    for r_AI in range(rows):
        row = []
        for c_AI in range(cols):
            row.append(".")
        grid_AI.append(row)

    num_of_ships_placed_AI = 0

    ship_positions_AI = []

    while num_of_ships_placed_AI != num_of_ships_AI:
        random_row_AI = random.randint(0, rows - 1)
        random_col_AI = random.randint(0, cols - 1)
        direction_AI = random.choice(["left", "right", "up", "down"])
        ship_size_AI = shipsize_AI - 1

        if try_to_place_ship_on_grid_AI(random_row_AI, random_col_AI, direction_AI, ship_size_AI):
            num_of_ships_placed_AI += 1
            shipsize_AI = shipsize_AI - 1
            if (shipsize_AI < 3):
                shipsize_AI = 4


def print_grid_AI():
    """Will print the grid with rows A-J and columns 0-9"""
    global grid_AI
    global alphabet

    debug_mode = True

    alphabet = alphabet[0: len(grid_AI) + 1]

    for row in range(len(grid_AI)):
        print(alphabet[row], end=") ")
        for col in range(len(grid_AI[row])):
            if grid_AI[row][col] == "O":
                if debug_mode:
                    print("O", end=" ")
                else:
                    print(".", end=" ")
            else:
                print(grid_AI[row][col], end=" ")
        print("")

    print("  ", end=" ")
    for i in range(len(grid_AI[0])):
        print(str(i), end=" ")
    print("")


def shoot_bullet_AI():
    global grid
    global num_of_ships_sunk
    global bullets_left_AI

    row, col = accept_valid_bullet_placement_AI()

    if grid[row][col] == ".":
        grid[row][col] = "#"
    elif grid[row][col] == "O":
        grid[row][col] = "X"
        if check_for_ship_sunk_AI(row, col):
            num_of_ships_sunk += 1

    bullets_left_AI -= 1


def accept_valid_bullet_placement_AI():
    global grid

    is_valid_placement = False

    while is_valid_placement is False:
        row = random.randint(0, 9)
        col = random.randint(0, 9)
        if grid[row][col] == "#" or grid[row][col] == "X":
            continue
        if grid[row][col] == "." or grid[row][col] == "O":
            is_valid_placement = True

    return row, col


def check_for_ship_sunk_AI(row, col):
    """If all parts of a shit have been shot it is sunk and we later increment ships sunk"""
    global ship_positions
    global grid

    for position in ship_positions:
        start_row = position[0]
        end_row = position[1]
        start_col = position[2]
        end_col = position[3]
        if start_row <= row <= end_row and start_col <= col <= end_col:
            # Ship found, now check if its all sunk
            for r in range(start_row, end_row):
                for c in range(start_col, end_col):
                    if grid[r][c] != "X":
                        return False
    return True


def check_for_game_over():
    """If all ships have been sunk or we run out of bullets its game over"""
    global num_of_ships_sunk_AI
    global num_of_ships_AI
    global num_of_ships
    global num_of_ships_sunk
    global game_over

    if num_of_ships_AI == num_of_ships_sunk_AI:
        print("you won")
        game_over = True
    elif num_of_ships == num_of_ships_sunk:
        print("Sorry, you lost")
        game_over = True


def main():
    """Main entry point of application that runs the game loop"""
    global game_over

    print("-----Welcome to Battleships-----")
    print("You have to take down 5 ships, may the battle begin!")

    create_grid_AI()
    create_grid()
    while game_over is False:

        print_grid_AI()
        print("---------------------------")
        print_grid()
        print("Number of ships to destroy: " + str(num_of_ships_AI - num_of_ships_sunk_AI))
        print("Number of ships remaining: " + str(num_of_ships - num_of_ships_sunk))
        shoot_bullet()

        shoot_bullet_AI()
        print("----------------------------")
        print("")
        check_for_game_over()


if __name__ == '__main__':
    """Will only be called when program is run from terminal or an IDE like PyCharms"""
    main()