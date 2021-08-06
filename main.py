"""Perecian

Usage:
    perecian new (<project_name> [-i] (-t <tour_string> | [-s] <order> <start>) [<source_path>] [(-e [<export_path>] | -p)])
    perecian generate tour [-i] [-s] <order> <start> [<source_path>] [(-e [<export_path>] | -p)]
    perecian generate mols <order> [<source_path>] [(-e [<export_path>] | -p)]
    perecian generate list <order> <length> [<source_path>] [(-e [<export_path>])]
    perecian --help
    perecian --version

Options: 
    -h --help       Show this screen
    -v --version    Show version
    -e --export     Export results as a file to path
    -i --image      Include a generated image of the knight's tour as a part of your export
    -p --print      Prints the result to console without formatting
    -s --shuffle    Randomly shuffles the order moves in a knight's tour
    -t --tour       Provide a knight's tour in algebraic chess notation
"""

from tour import tour_make
import sys
import docopt

def main(args):
    """ Executes the main function
    """
    
    print(args)
    #tour_make()


if __name__ == '__main__':
    arguments = docopt.docopt(__doc__, version='Perecian v2.0.0')
    main(arguments)