""" Perecian

Usage:
    perecian.py
    perecian.py default
    perecian.py -h|--help
    perecian.py -v|--version

Options:
    default  Runs perecian with the default settings of a sie 10 baord, starting a position 6,6, using defalt.csv
    -h --help  Shows this screen
    -v --version  Shows the version number
    
"""

#------------------------------------------------------------------
#   Libraries
#------------------------------------------------------------------

import tour
import squares
import lists
from textwrap import wrap, fill
from docopt import docopt
from csv import reader
from pyfiglet import figlet_format
from os.path import isfile
from PyInquirer import style_from_dict, Token, prompt, Validator, ValidationError, Separator


# Although the random module is used, random is seeded using the 
# starting coordinates of the knight
import random

#------------------------------------------------------------------
#   Functions
#------------------------------------------------------------------

def main(size, startx, starty, headers, path, name):
    """
    Executes the Main Function

    Arguments:
    size : A number greater than 6, and equal to or less than 10
    startx : Starting position x coordinate between 1 and size
    starty : Starting position y coordinate between 1 and size

    """
    
    # HACK: I don't love this solution for getting at the number of rows in the csv, but it does work
    with open(path, newline="") as fopen:
        csvreader = reader(fopen, delimiter=",")
        
        # Skips the headers
        next(csvreader)

        csv_len = 0
        for row in csvreader:
            csv_len += 1

    if csv_len % 2 != 0:
        print("Error: The csv you have chosen must have an even number of prompts")
        print("Solution: Consider adding another row to the chosen csv file.")
        return 1

    # Returns a knight's tour
    board, coords = tour.make(size, startx, starty)

    # Exit if something goes wrong
    if board == 1:
        return 1
    
    # Returns a list of len(size) mutually orthogonal latin squares
    mols_list = squares.make(size, csv_len)

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
        
        sections = headers

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

        for mols in range(len(mols_list[0:csv_len])):
            f.write("\n")
            f.write(str(mols + 1) + '\n')
            for row in mols_list[mols]:
                f.write(str(row) + "\n")
            f.write('\n')    

        for row in prompts:
            f.write("=" * 50 + "\n")
            f.write(sections + " " + str(row) + " | Knight Coodinates: " + str(coords[int(row - 1)]) + "\n") 
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
    Token.Separator: '#cc5454',
    Token.QuestionMark: '#673ab7 bold',
    Token.Selected: '#cc5454',  # default
    Token.Instruction: '',  # default
    Token.Answer: '#f44336 bold',
    Token.Question: '',
    Token.Pointer: '#673ab7 bold'
})

menu = [
    {
        'type':'list',
        'name': 'options',
        'message': ' ==== Perecian Main Menu ==== ',
        'choices': [
                'New Custom Tour',
                'Instructions',
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

class FileValidator(Validator):
    def validate(self, document):
        if isfile(document.text) == False:
            raise ValidationError(
        message = 'Please enter a valid csv filepath',
        cursor_position = len(document.text))

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
        'name': 'headers',
        'message': 'Section Headers:',
        'default': 'Chapter',
    },
    {
        'type': 'input',
        'name': 'file_path',
        'message': 'File path to the a csv file (default is lists/default.csv): ',
        'default': 'lists/default.csv',
        'validate': FileValidator
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
        main(10, 6, 6, "Chapters", "lists/default.csv", "Perecian Prompts Output")
    else:
        menu = prompt(menu, style=style)
        
        if menu['options'] == "New Custom Tour":

            settings = prompt(settings, answers, style=style)
            
            if settings['exe'] == True:
                print("Generating Prompts")
                main(int(settings['size']),int(settings['startx']),int(settings['starty']), settings['headers'], settings['file_path'], settings['file_name'])

        elif menu['options'] == "Exit":
            print("Exiting Perecian")
            exit
        elif menu['options'] == 'Instructions':
            print()
            start ="""
========Getting Started========
To run Perecian using its default settings and lists, simply execute

python perecian.py default

in you favorite command line interface. Your text file will be saved to the Perecian folder as:

Perecian Prompts Output.txt

========Customization========

===Tours===
In order to change the default settings of Perecian, open the main menu by executing:

python perecian.py

and navigate to the New Custom Tour option from the main menu. From this page, you will be able to input your own preferred settings into the program.

>>>Note On Tour Sizes<<<
Although a knight's tour is possible on a 6 x 6 chess board, users are disallowed from creating them because it is mathematically impossible to solve a mutually orthogonal latin square of order 6.

>>>Note On Starting Positions<<<
Perecian cannot (yet) solve all knight's tours on all boards on all posible starting positions. For example, a tour made with board size 5 x 5 at starting position 1,2 is not solveable, and will result in a traceback error. These errors are more common on smaller boards.

===CSV Lists===
Users are encouraged to create their own prompts lists for Perecian in order to create their own unique writing projects. In order to do this, it is advised to open the lists folder and copy empty.csv. From there, users can input their own content into the new csv file.

>>>Note On Custom Lists<<<
Custom lists MUST contain an even number of rows (excluding the header row) in order for Perecian to read  them. Additionally, each row MUST contain the same number of prompts as the board size. For instance, if  a user selects a chess board size of 10 x 10, the csv file must have 10 prompts per row.

Besides the above limitations, a user can add as many row lists as they desire provided that their chosen hardware can solve half that number of MOLS and store them in memory. Alternatively, if a user selects a smaller chess board size (say, 7 x 7), Perecian will still run correctly with a prompts list containing 10 items each row, but the last 3 prompts from each list be lost since Perecian will only read the first 7 prompts.

========I Made A Text File... Now What?========
Now it's time to get started writing! The inspiration behind Perecian comes from a novel writen by Georges Perec called Life: A User's Manual. Perec initially came up with the idea of writing a novel that was written using a type of creative writing called constrained writing. Constrained writing, for the purposes of this program at least, is a style of writing in which the writer chooses to subject themselves to an arbitrary set of rules in order to challenge themselves and affect the style of writing they are able to produce. So, in many ways, this program is really just an aide or a springboard for creative writing.

With respect to the file produced by running this program, Perecian recreate the system Georges Perec used to write Life: A User's Manual all the way down to even using a csv containing many of the same original prompts Perec devised for use in his novel. There is plenty of articles talking about how Perec wrote this masterpeice of fiction, but I will simply defer to the Wikipedia article on this novel for further reading.

There are, however, some key exceptions between this program's output and Perec's original constraint system.

To begin with, Life: A User's Manual is a story about the residents of a fictional apartment building in Paris. Perec tells the story one chapter at a time by moving from room to room in the building. The order in which the story is written was selected by means of overlaying the knight's tour path onto an architectural cross-section of the fictional building. Perecian cannot, currently, take as input any kind of map or building, or the like. If a user wants to recreate this part of the constraint system, they will simply need to do it by hand.

Additionally, it should be noted that, although scholars do know a lot about how Perec wrote Life: A User's Manual, it is widely acknowledged that there were some additional constraint systems that Perec never told anybody about. With that in mind, users are encouraged to customize their writing prompts beyond what even this program is capable of doing.

Besides that, the sky is the limit! Feel free to use this program to create any kind of writing constraint system that you can immagine.
            """
            wraplist = wrap(text=start, replace_whitespace=False, drop_whitespace=False, width = 90)
            for row in wraplist:
                print(row)  

        elif menu['options'] == 'About Perecian':
            print()
            title = figlet_format("Perecian", font="roman", width=90)
            print(title)
            print("Beta 1.0")
            
            about ="""Perecian is an open souce CLI tool for writers written in Python.
                    
Based off of the constraints Georges Perec useed to create his masterpeice, Life: A User's Manual, Pereican uses both knight's tours, and mutually orthogonal latin squares to create a unique list of constrained writing prompts for novels, short stories, poems, and much more.
"""
            how = """Perecian produces a list of writing promtps by first solving two classic mathematical puzzles: a knight's tour, and a colleciton of mutually orthogonal latin squares (MOLS). By using the solutions to these two puzzles, it will generate a list of writing prompts by programatically pulling from a specially formatted csv file stored in the lists folder. 
The text file Perecian produces will first list the solutions to these puzzles, and then each individual chapter. By default, Perecian will solve a knight's tour on a 10 x 10 chess board, and 21 MOLS of order 10. However, it is possible to customize Perecian to solve both larger and smaller chess board sizes and MOLS. Additionally, the user is able to create a custom prompts list csv to enable Perecian to output prompts for different types of writing assignments.
                """
            aboutfill = fill(text=about, width = 90)
            howfill = fill(text=how)
            print(aboutfill)
            print()
            print("====How It Works====")
            print()
            print(howfill)
            
            