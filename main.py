""" Perecian

Usage:
    perecian.py
    perecian.py default
    perecian.py -h | --help
    pereican.py -v | --version



Options:
    <default> | Runs perecian with the default settings of a sie 10 baord, starting a position 6,6

    About:

    ooooooooo.                                           o8o                        
    `888   `Y88.                                         `"'                        
    888   .d88'  .ooooo.  oooo d8b  .ooooo.   .ooooo.  oooo   .oooo.   ooo. .oo.   
    888ooo88P'  d88' `88b `888""8P d88' `88b d88' `"Y8 `888  `P  )88b  `888P"Y88b  
    888         888ooo888  888     888ooo888 888        888   .oP"888   888   888  
    888         888    .o  888     888    .o 888   .o8  888  d8(  888   888   888  
    o888o        `Y8bod8P' d888b    `Y8bod8P' `Y8bod8P' o888o `Y888""8o o888o o888o  
        
    {v 1.0}                                                                                                                                                  
        
    Perecian is an open source CLI program for writers.
        
    Based off of Georges Perec's masterpeice, Life: A User's Manual,
    Pereican solves both knight's tours, and mutually orthogonal latin squares
    to create a unique list of constrained writing prompts for novels, short stories, poems,
    and much more.

"""

#------------------------------------------------------------------
#   Libraries
#------------------------------------------------------------------

import tour
import squares
import lists
from sys import argv
from docopt import docopt
import csv

# Although the random module is used, random is seeded using the 
# starting coordinates of the knight
import random

#------------------------------------------------------------------
#   Functions
#------------------------------------------------------------------

def main(size, startx, starty):
    """
    Executes the Main Function

    Arguments:
    size : A number greater than 6, and equal to or less than 10
    startx : Starting position x coordinate between 1 and size
    starty : Starting position y coordinate between 1 and size

    """

    # Returns a knight's tour
    board, coords = tour.make(size, startx, starty)
    
    # Returns a list of len(size) mutually orthogonal latin squares
    mols_list = squares.make(size)

    # Tests mols_list to ensure nothing went wrong during calculation.
    if mols_list == 1:
        print("Error: Not enough Mutually Orthogonal Latin Squares (MOLS) were produced by squares.py")
        return 1
    
    # Shuffles the mols list according to the starting coordinates
    # An unshuffled mols list would result in different tours using the same prompts csv to return the exact same chapter prompts in an arbitrary order
    # As stated above, although random is used, it is seeded and produces more predictable results.
    else:
        # Produces a seed for random using the starting position of the knight
        seed = int(str(startx) + str(starty))
        random.seed(seed)
        
        # Shuffles the list according to the seed set above
        random.shuffle(mols_list)
        
        # Creates a list of prompts for each capter
        prompts = lists.make(coords, mols_list, size)

        
        f = open("Perecian.txt", 'w+')

        for row in prompts:
            f.write("\n" + "Chapter" + str(row) + "\n" + "\n") 
            for item in range(len(prompts[row])):
                f.write(str(item + 1) + " [] " + str(prompts[row][item]) + "\n")

        f.close()        
                
    return 0

#------------------------------------------------------------------
#   Main Execution
#------------------------------------------------------------------

if __name__ == '__main__':
    arguments = docopt(__doc__, version='v1.0')
    if "default" in arguments:
        main(10, 6, 6)
    else:
        print(arguments)    