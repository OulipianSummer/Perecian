#------------------------------------------------------------------
#   Globals
#------------------------------------------------------------------

MOVES = [[-2,1],[-1,2],[1,2],[2,1],[2,-1],[1,-2],[-1,-2],[-2,-1]]

#------------------------------------------------------------------
#   Functions
#------------------------------------------------------------------

def make(size, startx, starty):
    """
    Usage:
    make() is the main function of tour.py. 
    It produces a knights tour from any given start position using the Warnsdorf huerstic.

    Arguments:
    size : A number greater than 6, and equal to or less than 10
    startx : Starting position x coordinate between 1 and size
    starty : Starting position y coordinate between 1 and size

    """
    
    # Establishes the board size
    board_size = size or 10
    max_moves = board_size * board_size

    # Start Positions
    x = startx or 6
    y = starty or 6

    # Assigns a virtual knight to the start position provided by x and y
    kx = x - 1
    ky = y - 1

    # Creates a virtual chess board as a list of lists (for easy board[x][y] indexing)
    board = []
    for i in range(size):
        board.append([0] * size)

    # Places knight on the chessboard
    board[kx][ky] = 1
    
    # Creates a list of the fist xy coords of the knight, and then appends them to a list to be used for recording subsequent move coords
    first_coords = [x,y]
    coords = []
    coords.append(first_coords) 

    for move in range(2, max_moves + 1):
        possible_moves = 0
        next_x = [0] * size
        next_y = [0] * size

        for i in range(0, 8):
            check_x = kx + MOVES[i][0]
            temp_y = ky + MOVES[i][1]

            if (check_x >= 0 and check_x < size
                and temp_y >=0 and temp_y < size
                and board[check_x][temp_y] == 0):
                next_x[possible_moves] = check_x
                next_y[possible_moves] = temp_y
                possible_moves += 1
        smallest_move = 0

        if possible_moves == 0:
            print("Something went wrong around" + str(kx + 1) + "," + str(ky+1) + " at move " + str(move))
            print()
            break

        elif possible_moves > 1:
            exits = [0] * size

            for i in range(0, possible_moves):
                num_exits = 0

                for j in range(0, 8):
                    check_x = next_x[i] + MOVES[j][0]
                    check_y = next_y[i] + MOVES[j][1]

                    if (check_x >= 0 and check_x < size
                        and check_y >= 0 and check_y < size
                        and board[check_x][check_y] == 0):
                        num_exits += 1
                
                exits[i] = num_exits
             
            smallest_move = 0
            
            current_num_exit = exits[0]

            for i in range(1, possible_moves):
                if current_num_exit > exits[i]:
                    current_num_exit = exits[i]
                    smallest_move = i

        kx = next_x[smallest_move]
        ky = next_y[smallest_move]
        
        # Appends the chosen move coordinates to the coords list (adding 1 to make it easier to read the list.csv files)
        current_coords = [kx + 1,ky + 1]
        coords.append(current_coords)

        board[kx][ky] = move  

    return board, coords
