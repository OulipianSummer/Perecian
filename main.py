"""Perecian

Usage:
    perecian new
    perecian new <project_name> (-e | --export) <src_path> <to_path>
    perecian new <project_name> [(-e | --export)] <order> <start> <list_path> [<to_path>]
    perecian generate tour <order> <start>
    perecian generate mols <order>
    perecian generate list <order> <length>
    perecian (-h | --help)
    perecian (-v | --version)

Options: 
    -h --help       Show this screen
    -v --version    Show version
    -e --export     Export results to path

Examples:
    
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