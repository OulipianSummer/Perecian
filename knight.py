#===============================================================================
#  File        : knight.py
#  Project     : Knight's Tour
#  Description : Knight class for knight's tour Python implementation.
#  Company     : Cal Poly Pomona
#  Engineer    : Byron Phung
#===============================================================================

#===============================================================================
#  Class Definition
#===============================================================================

class Knight(object):
    """A class that defines a Knight object to carry out a Knight's Tour."""
    def __init__(self, x, y):
        self.x = x - 1
        self.y = y - 1

    def move(self, x, y):
        """Move the Knight object to a new position.

        Keyword arguments:
        x -- x position of Knight object
        y -- y position of Knight object
        """
        self.x = x
        self.y = y
