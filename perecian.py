""" Perecian

Usage:
    perecian.py menu
    perecian.py default
    perecian.py -h|--help
    perecian.py -v|--version

Options:
    menu  Opens the main menu
    default  Runs perecian with the default settings of a sie 10 baord, starting a position 6,6
    -h --help  Shows this screen
    -v --version  Shows the version number
    
"""

#------------------------------------------------------------------
#   Libraries
#------------------------------------------------------------------

import tour
import squares
import lists
from docopt import docopt
import csv
import pyfiglet
from PyInquirer import style_from_dict, Token, prompt, Validator, ValidationError


# Although the random module is used, random is seeded using the 
# starting coordinates of the knight
import random

#------------------------------------------------------------------
#   Functions
#------------------------------------------------------------------

def main(size, startx, starty, path, name):
    """
    Executes the Main Function

    Arguments:
    size : A number greater than 6, and equal to or less than 10
    startx : Starting position x coordinate between 1 and size
    starty : Starting position y coordinate between 1 and size

    """

    # Returns a knight's tour
    board, coords = tour.make(size, startx, starty)

    # Exit if something goes wrong
    if board == 1:
        return 1
    
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
        prompts = lists.make(coords, mols_list, size, path)
        
        # Saves the prompts to a text file named after the user's input
        filename = name + '.txt'
        f = open(filename, 'w+')

        f.write("=" * 50 + "\n")
        f.write("Knight's Tour" + "\n")
        f.write("=" * 50 +'\n\n')  

        f.write("  ")
        for num in range(size):
            f.write(str(num + 1) + ("   "))
        f.write("\n")    

        for row in range(len(board)):
            f.write(str(row + 1) + " " +str(board[row]) + "\n")
        f.write("\n")

        f.write("=" * 50 + "\n")
        f.write("Mutually Orthogonal Latin Squares (MOLS)" + "\n")
        f.write("=" * 50 +'\n\n')

        # TODO: Adjust the cutoff point on this slice to make it more dynamic to the csv list
        for mols in range(len(mols_list[0:21])):
            f.write("\n")
            f.write(str(mols + 1) + '\n')
            for row in mols_list[mols]:
                f.write(str(row) + "\n")
            f.write('\n')    

        for row in prompts:
            f.write("=" * 50 + "\n")
            f.write("Chapter" + str(row) + " | Knight Coodinates: " + str(coords[int(row - 1)]) + "\n") 
            f.write("=" * 50 +'\n\n')  
            for item in range(len(prompts[row])):
                for key, value in prompts[row][item].items():
                    f.write(str(item + 1) + " [] " "{}: {}".format(key, value) + "\n")
            f.write("\n")
                 

        f.close()        

    print("The prompts file was created and saved successfully as " + filename)            
    return 0

#------------------------------------------------------------------
#   PyInquirer Interface
#------------------------------------------------------------------

style = style_from_dict({
    Token.QuestionMark: '#673ab7 bold',
    Token.Selected: '#cc5454',  # default
    Token.Instruction: '',  # default
    Token.Answer: '#f44336 bold',
    Token.Question: '',
})

menu = [
    {
        'type':'list',
        'name': 'options',
        'message': 'Perecian Main Menu',
        'choices': [
                'New Custom Tour',
                'Quickstart Guide',
                'About Perecian',
                'Exit' 
        ]
    }
] 

class SizeValidator(Validator):
    def validate(self, document):
        try:
            num = int(document.text)
            if num > 10 or num < 5 or num == 6:
                raise ValidationError(
                message='Please enter a number between 5 and 10 that is not 6',
                cursor_position=len(document.text))
        except ValueError:
            raise ValidationError(
                message='Please enter a number',
                cursor_position=len(document.text))

class PosValidator(Validator):
    def validate(self, document):
        try:
            num = int(document.text)
            if num > int(answers['size']) or num < 1:
                raise ValidationError(
            message='Please Enter A number between 1 and the board size',
            cursor_position = len(document.text))

        except ValueError:
            raise ValidationError(
                message='Please enter a number',
                cursor_position=len(document.text)) 

settings = [
    
    {
        'type':'input',
        'name':'size',
        'message':'Chess Board Size (5-10 | 6 is not allowed): ',
        'default': '10',
        'validate': SizeValidator
    },
    {
        'type': 'input',
        'name': 'startx',
        'message': 'Knight Starting Position X: ',
        'default': '6',
        'validate': PosValidator
    },
    {
        'type': 'input',
        'name': 'starty',
        'message': 'Knight Starting Position Y: ',
        'default': '6',
        'validate': PosValidator
    },
    {
        'type': 'input',
        'name': 'file_path',
        'message': 'File path to the a csv file (default is lists/default.csv): ',
        'default': 'lists/default.csv'
    },
    {
        'type':'input',
        'name':'file_name',
        'message':'Output File Name: ',
        'default':'Perecian Prompts Output'
    },
    {
        'type': 'confirm',
        'name': 'exe',
        'message': 'Proceed using these settings?: ',
        'default': False
    }
]

#------------------------------------------------------------------
#   Main Execution
#------------------------------------------------------------------

if __name__ == '__main__':
    arguments = docopt(__doc__, version='Beta 1.0')
    if arguments["default"] == True:
        main(10, 6, 6, "lists/default.csv", "Perecian Prompts Output")
    elif arguments["menu"] == True:
        menu = prompt(menu, style=style)
        
        if menu['options'] == "New Custom Tour":
           
            answers = {'ignore':'me'}

            settings = prompt(settings, answers, style=style)
            
            if settings['exe'] == True:
                size = int(settings['size'])
                startx = int(settings['startx'])
                starty = int(settings['starty'])
                path = settings['file_path']
                name = settings['file_name']
                print("Generating Prompts")
                main(size,startx,starty, path, name)

        elif menu['options'] == "Exit":
            print("Exiting Perecian")
            exit
        elif menu['options'] == 'Quickstart Guide':
            print()
            title = pyfiglet.figlet_format("Quick Start", font='roman', width = 150)
            print(title)

            start ="""
=== Default Settings ===

    Perecian can be run using only its default settings. To do this, navigate to the Perecain folder and run:

    python main.py default

    Using this command, Perecian will export prompts based on a 10 x 10 chess board starting at position 6 6, using the default
    moveset of, [[-2,1],[-1,2],[1,2],[2,1],[2,-1],[1,-2],[-1,-2],[-2,-1]] and using default.csv as its list source.


=== How Does Perecian Work? ===

    An in-depth explantion can be found under "About Perecain" from the main menu options


== Custom Tours ==

    To make your own custom tours with different board sizes, starting positions, list sources, and move orders,
    navigate to the Perecain folder and run:

    python main.py

    Then select the "New Custom Tour" option from main menu options
            """

            print(start)    

        elif menu['options'] == 'About Perecian':
            print()
            title = pyfiglet.figlet_format("Perecian", font="roman", width=90)
            print(title)
            print("Beta 1.0")
            
            about ="""
    Perecian is an open souce CLI tool for writers written in Python.
                    
    Based off of the constraints Georges Perec useed to create his masterpeice, 
    Life: A User's Manual, Pereican uses both knight's tours, and mutually 
    orthogonal latin squares to create a unique list of constrained writing 
    prompts for novels, short stories, poems, and much more.

== How It Works ==

    By default, Perecian creates prompts by first solving a knight's tour on 
    a 10 x 10 chess board. A knight's tour is a classic logic puzzle involving
    moving a single knight chess piece in such a way that it visits or "tours"
    every space on a chess board exactly once. To put this puzzle in perspective, 
    a standard 8 x 8 chessboard contains over 19 quadrillion possible knight's
    tours!

    In order to make this puzzle easier to solve, Perecian utilizes a simple
    rule called Warnsdorff's Rule, first described by H. C. von Warnsdorff
    in 1823. The rule states that a tour can be solved on any chess board
    (larger than 4 x 4), from any starting position granted that the puzzle
    solver always moves the knight to the square with the fewest possible
    following moves. Using this heuristic, Perecian is able to solve a
    knight's tour in less than a second on most computers.
    
    Next, Perecian uses the move coordinates of the knight's tour to reference
    21 mutually orthogonal latin squares (MOLS) of order 10 (also created by 
    Perecain at run time). A MOLS (someitmes refered to as a latin bi-square 
    or a graeco-latin square) is another mathematical puzzle created from combining 
    two latin squares, which are spiritually similar to a Sudoku square. Each row in 
    an order 10 latin square contains the numbers 1 - 10, and each column also contains
    the numbers 1 - 10. A MOLS is created by overlaying two latin squares
    such that each number pairing across the grid is unique.

    Using the coordinates from each step in the knight's tour, Perecian references
    that same square in each of the 21 MOLS. For example, if the knight starts at
    row 6, column 6, Perecain will look at the number pairings in row 6, column 6
    of each of the MOLS. Using the unique number parings located at that specific cell
    in each MOLS table, Perecian makes an aditional reference to a list of prompts
    stored in lists/default.csv. Using each of those unique number pairings stored
    in the 21 MOLS, Perecian constructs a unique list of 42 prompts for each move
    the knight makes in its tour.

    At the end of this dizzying list of steps, chess moves, and cross references, 
    Perecian produces 100 unique lists of 42 prompts. For the writer, each list
    is constructed as a checklist of items, colors, materials, movitves, feelings,
    ideas, books, paintings, quotes, and much more. These lists, like in Life:
    A User's Manual are considerd to be a sort of inventory of what each chapter of a
    potential novel will contain. 
                    
== For Writers ==

    Using these lists, a writer is able to construct an entire novel's worth of
    constrained writing prompts. Perecian can also be customized to export
    tours both larger and smaller than those created by a 10 x 10 chess board.
    Writers are encouraged to add or remove constraints as they see
    fit (since Perec himself did so, either strictly or loosely adhereing to constraints
    as the need arose or inspiration struck), but the aim of Perecian is to challenge
    writers to test their skills by trying to adhere to the constraints as much as possible
    to train and challenge themselves to produce works entirely unlike what they are used to
    creating.


    Writers are encouraged to be as creative as possible when writing using the prompts created
    by Perecian. Georges Perec himself used similar constratints and took them a step further by
    overlaying the knight's tour chess board onto a floorplan of a fictional Parisian apartment
    building wherein each chapter represented stories of the residents of that building told
    in the order of the knight's tour.
                    
    Additionally, Perecain's lists could also be used as prompts for poetry,
    short stories, letters, and much more. 

== Further Customization ==

    Perecain's default prompt's list (found in lists/default.csv) can be customized for different
    themes, genres, settings, and more. In order to make your own, it is best to simply make a copy of
    lists/empty.csv and fill in all of the empty cells with your own content.
                """
            print(about)
            
            