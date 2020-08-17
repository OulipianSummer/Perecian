# Perecian
Perecian is an open source CLI program for writers. 

Based off of Georges Perec's masterpeice, Life: A User's Manual, Pereican solves both knight's tours, and mutually orthogonal latin squares to create a unique list of constrained writing prompts for novels, short stories, poems, and much more.

Perecain produces a .txt file of a unique combination of 42 prompts accross 100 chapters. More optional prompts and a customizeable UX will be added in a later update.

Perecian IS NOT a random number generator. The list of prompts is created using a two mathematical constructs: a knight's tour, and 21 mutually orthogonal latin squares.

## Quick Start
Perecian requires Docopt, so ensure to run pip install docopt before running.

Perecian has a default run mode that will produce a prompts list for a 10 x 10 chess board starting at space 6,6. 
To run Perecian using the default settings, simply navigate to the Perecain folder using your CLI application of choice, and run python main.py default


## More updates Comming
Perecain is stil in development, but future releases are expexcted to contain:
    + A CLI user interface for customizing your inputs (including the move order of the knight)
    + A wiki featuring documentation on the use of this program, and an explanation of what is happening under the hood
    + A set of optional lists for genres, short storeis, or other types of writing projects