#===============================================================================
#  File        : board.py
#  Project     : Knight's Tour
#  Description : Board class for knight's tour Python implementation.
#  Company     : Cal Poly Pomona
#  Engineer    : Byron Phung
#===============================================================================

#===============================================================================
#  Class Definition
#===============================================================================

class Board(object):
    """A class that creates a virtual board to store Knight positions for a
    Knight's Tour.
    """ 
    def __init__(self, size):
        self.size = size
        self.board = [([0] * size) for row in range(size)]

    def is_empty(self, x, y):
        """Check if the specified (x,y) position is empty, i.e. is 0.

        Keyword arguments:
        x -- x position
        y -- y position
        """
        return self.board[x][y] == 0

    def place_knight(self, move_number, x, y):
        """Place the Knight move number in the specified position.

        Keyword arguments:
        move_number -- move number of knight object to store
        x           -- x position of knight
        y           -- y position of knight
        """
        self.board[x][y] = move_number

    def print_board(self):
        """Prints out the board with Knight move numbers.

        Keyword arguments:
        <None>
        """
        for i in range(self.size):
            for j in range(self.size):
                print(str(self.board[i][j]).rjust(2) + " ", end="")
            print()
