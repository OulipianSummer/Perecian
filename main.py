#===============================================================================
#  File        : main.py
#  Project     : Knight's Tour
#  Description : Python implementation to solve a knight's tour using
#                Warnsdorff's Rule.
#  Company     : Cal Poly Pomona
#  Engineer    : Byron Phung
#===============================================================================

#===============================================================================
#  Libraries
#===============================================================================

from knight import Knight
from board import Board

#===============================================================================
#  Constants
#===============================================================================

# Define the board size and use it to determine the maximum moves.
BOARD_SIZE = 8
MAX_MOVES = BOARD_SIZE**2

# Define the possible combinations of Knight moves.
MOVE_X = [-2, -1, 1, 2, 2, 1, -1, -2]
MOVE_Y = [1, 2, 2, 1, -1, -2, -2, -1]

#===============================================================================
#  Functions
#===============================================================================

def main():
    """Executes the main application.

    Keyword arguments:
    <None>
    """
    # Instantiate the x & y position variables.
    x = 9
    y = 9

    # Take x & y initial inputs. Loop while invalid.
    while (x < 1 or x > BOARD_SIZE) or (y < 1 or y > BOARD_SIZE):
        x, y = input("Enter x & y (1-" + str(BOARD_SIZE)
                     + ") separated by a space (e.g. 4 4): ").split()
        x, y = [int(x), int(y)]

        if x < 1 or x > BOARD_SIZE:
            print("ERROR:: x must be 1-" + str(BOARD_SIZE))

        if y < 1 or y > BOARD_SIZE:
            print("ERROR:: y must be 1-" + str(BOARD_SIZE))

    print()

    # Create a Knight object to move around the board.
    knight = Knight(x, y)

    # Instantiate a board and set the initial Knight position with move 1.
    board = Board(BOARD_SIZE)
    board.place_knight(1, knight.x, knight.y)

    # Test special cases for all the moves.
    for current_move in range(2, MAX_MOVES + 1):
        num_possibilities, next_x, next_y = get_num_possibilities(knight, board)
        min_exits_idx = 0

        # If there are no possibilities left, then end the tour prematurely.
        if num_possibilities == 0:
            print("The knight's tour ended prematurely at (" + str(knight.x + 1)
                  + "," + str(knight.y + 1) + ") during move #"
                  + str(current_move - 1) + ".")
            print()
            break
        
        # If there is more than 1 possibility, then find the next squares with the
        # minimum number of exits.
        elif num_possibilities > 1:
            exits = find_min_exits(board, num_possibilities, next_x, next_y)
            min_exits_idx = get_idx_smallest_num_exits(num_possibilities, exits)

        # Move the knight and mark its position on the board.     
        knight.move(next_x[min_exits_idx], next_y[min_exits_idx])
        board.place_knight(current_move, knight.x, knight.y)

    # Print out the board.
    board.print_board()

def get_num_possibilities(knight, board):
    """Test each of the eight squares one knight's move away from (I,J) and
    form a list of the possibilities for the next square (next_i(l), next_j(l)).

    Keyword arguments:
    knight -- Knight object
    board  -- Board object
    """
    num_possibilities = 0
    next_x = [0] * BOARD_SIZE
    next_y = [0] * BOARD_SIZE

    # Test each of the 8 possible moves.
    for i in range(0, 8):
        # Check the next move without storing it.
        temp_x = knight.x + MOVE_X[i]
        temp_y = knight.y + MOVE_Y[i]

        if (temp_x >= 0 and temp_x < BOARD_SIZE
            and temp_y >= 0 and temp_y < BOARD_SIZE
            and board.is_empty(temp_x, temp_y)):
            next_x[num_possibilities] = temp_x
            next_y[num_possibilities] = temp_y
            num_possibilities = num_possibilities + 1

    # Return the number of possibilities and list of next X & Y positions.
    return num_possibilities, next_x, next_y

def find_min_exits(board, num_possibilities, next_x, next_y):
    """Find the next squares with the minimum number of .

    Keyword arguments:
    num_possibilities -- Number of possibilities
    """
    # Store the number of exits for each move.
    exits = [0] * BOARD_SIZE

    # Check all the exits for each possible moves.    
    for i in range(0, num_possibilities):
        num_exits = 0

        # Check the exits of the move after each next move.
        for j in range(0, 8):
            check_x = next_x[i] + MOVE_X[j]
            check_y = next_y[i] + MOVE_Y[j]

            # If the exit of the move after the next move is valid, then
            # increment the number of possible exits.
            if (check_x >= 0 and check_x < BOARD_SIZE
                and check_y >= 0 and check_y < BOARD_SIZE
                and board.is_empty(check_x, check_y)):
                num_exits = num_exits + 1

        # Store the number of exits in the current index.
        exits[i] = num_exits

    # Return the number of exits for each move.
    return exits

def get_idx_smallest_num_exits(num_possibilities, exits):
    """Get the smallest number of exits to ultimately decide the knight's next
    move based on Warnsdorff's Rule.

    Keyword arguments:
    num_possibilities -- Number of possibilities
    exits             -- Number of exits for each move
    """
    min_exits_idx = 0
    current_num_exit = exits[0]

    # Get the index that contains the smallest number of exits.
    for i in range(1, num_possibilities):
        if current_num_exit > exits[i]:
            current_num_exit = exits[i]
            min_exits_idx = i

    # Return the index for which there is the smallest number of exits.
    return min_exits_idx

#===============================================================================
#  Main Execution
#===============================================================================

main()
