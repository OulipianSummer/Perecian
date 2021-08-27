#===============================================================================
#  File        : tour.py
#  Project     : Perecian
#  Description : A class for managing Perecian tours
#===============================================================================

#===============================================================================
#  Class Definition
#===============================================================================

from knight import Knight
from board import Board
import random

class Tour(object):
    """A class that defines and manages a knight's tour
    
    Properties:
    
    settings -- a dictionary containing settings used to create a knight's tour.
        shuffle -- a boolean used to shuffle the order of the moves before starting the tour
        format -- a string that describes how to output the completed tour
        mode -- a string that defines the type of tour that will be constructed
    
    order -- an integer that describes the size of the knight's tour
    max_moves -- an integer that describes the maximum number of moves in a given chess board
    start -- a string representing the starting position of the knight in either numeric (2,5) or algebraic chess notation (b5)
    knight -- an instance of the Knight class, instantiated with the starting position
    board -- an instance of the Board class, instantiated with the order
    """
    def __init__(self, args):

        # Initialize a dictionary of settings
        settings = dict(
            shuffle = False,
            format = 'print',
            mode = 'warnsdorff',
        )

        # Parse shuffle setting
        if args['--shuffle']:
            settings['shuffle'] = True

        # Parse and initialize export format
        if args['--export']:
            settings['format'] = 'file'
        if args['--json']:
            settings['format'] = 'json'
        
        # Initialize properties
        self.order = int(args['<order>'])
        self.max_moves = self.order**2
        self.settings = settings
        self.moves = [[-2,1],[-1,2],[1,2],[2,1],[2,-1],[1,-2],[-1,-2],[-2,-1]]

        # Shuffle the moves, if requested
        if self.settings['shuffle']:
            self.moves = self.__shuffle_moves()
        
        # Parse and initialize start position
        start = args['<start>']
        coords = start.split(',')
        if len(coords) == 2:
            x = (self.order + 1) - int(coords[0])
            y = int(coords[1])
            self.start = dict(x=x,y=y)
        else:
            alpha = (self.order + 1) - int(ord(start[0]) - 96)
            numeric = int(start[1:])
            self.start = dict(x=alpha,y=numeric)

        # Instantiate knight and board classes
        self.knight = Knight(self.start['x'], self.start['y'])
        self.board = Board(self.order)

    def __shuffle_moves(self):
        copy = self.moves.copy()
        random.shuffle(copy)
        return copy

    def create_tour(self):
        if self.settings['mode'] == 'warnsdorff':
           self.__make_warnsdorff()

    def __make_warnsdorff(self):
        """Creates a knight's tour using the Warnsdorff heuristic

        """
        max_moves = self.max_moves

        # Create a Knight object to move around the board.
        knight = self.knight

        # Instantiate a board and set the initial Knight position with move 1.
        board = self.board
        board.place_knight(1, knight.x, knight.y)

        # Test special cases for all the moves.
        for current_move in range(2, max_moves + 1):
            num_possibilities, next_x, next_y = self.__get_num_possibilities(knight, board)
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
                exits = self.__find_min_exits(board, num_possibilities, next_x, next_y)
                min_exits_idx = self.__get_idx_smallest_num_exits(num_possibilities, exits)

            # Move the knight and mark its position on the board.     
            knight.move(next_x[min_exits_idx], next_y[min_exits_idx])
            board.place_knight(current_move, knight.x, knight.y)


    def __get_num_possibilities(self, knight, board):
        """Test each of the eight squares one knight's move away from (I,J) and
        form a list of the possibilities for the next square (next_i(l), next_j(l)).

        Keyword arguments:
        knight -- Knight object
        board  -- Board object
        """
        board_size = self.order

        num_possibilities = 0
        next_x = [0] * board_size
        next_y = [0] * board_size

        # Test each of the 8 possible moves.
        for i in range(0, 8):
            # Check the next move without storing it.
            temp_x = knight.x + self.moves[i][0]
            temp_y = knight.y + self.moves[i][1]

            if (temp_x >= 0 and temp_x < board_size
                and temp_y >= 0 and temp_y < board_size
                and board.is_empty(temp_x, temp_y)):
                next_x[num_possibilities] = temp_x
                next_y[num_possibilities] = temp_y
                num_possibilities = num_possibilities + 1

        # Return the number of possibilities and list of next X & Y positions.
        return num_possibilities, next_x, next_y

    def __find_min_exits(self, board, num_possibilities, next_x, next_y):
        """Find the next squares with the minimum number of .

        Keyword arguments:
        num_possibilities -- Number of possibilities
        """
        board_size = self.order
        # Store the number of exits for each move.
        exits = [0] * board_size

        # Check all the exits for each possible moves.    
        for i in range(0, num_possibilities):
            num_exits = 0

            # Check the exits of the move after each next move.
            for j in range(0, 8):
                check_x = next_x[i] + self.moves[j][0]
                check_y = next_y[i] + self.moves[j][1]

                # If the exit of the move after the next move is valid, then
                # increment the number of possible exits.
                if (check_x >= 0 and check_x < board_size
                    and check_y >= 0 and check_y < board_size
                    and board.is_empty(check_x, check_y)):
                    num_exits = num_exits + 1

            # Store the number of exits in the current index.
            exits[i] = num_exits

        # Return the number of exits for each move.
        return exits

    def __get_idx_smallest_num_exits(self, num_possibilities, exits):
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