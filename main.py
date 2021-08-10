"""Perecian

Usage:
    perecian new [( <project_name> <order> [(-t <start>)] [<source_path>] [-e [-i] [<export_path>] | -j] )]
    perecian generate tour ([-s] <order> <start> | [<source_path>]) [-e [-i] [<export_path>] | -j]
    perecian generate image (-t <tour_string> | [-s] <order> <start>) [(-e [<export_path>] )]
    perecian generate mols <order> <number> [(-e [<export_path>] | -j)]
    perecian generate list <order> <length> [(-e [<export_path>])]
    perecian ( -h | --help )
    perecian ( -v | --version )

Options: 
    -h --help       Show this screen
    -v --version    Show version
    -e --export     Export results as a file to path
    -i --image      Include a generated image of the knight's tour as a part of your export
    -s --shuffle    Randomly shuffles the order moves in a knight's tour
    -t --tour       Provide information for generating a knight's tour
    -j --json       Export results as JSON
"""

from tour import tour_make_warnsdorff
from project import Project
import re
import sys
import docopt


def main(args):
    """ Executes the main function
    """

    # Begin a new project
    if args['new'] and args['<project_name>']:
        
        name = args['<project_name>']
        order = args['<order>']

        if len(name) >= 150:
            raise SystemExit('The provided project name, "{}", is greater than 150 characters. Please shorten it to continue'.format(name))
        if not order.isnumeric():
            raise SystemExit('The provided order, "{}", is not a number. Please enter a numeric value to continue'.format(order))

        project = Project(name, order)

        if args['-t'] and args['--tour']:
            start = args['<start>']
            if len(start) > 5:
                raise SystemExit('The provided tour start, "{}", is greater than 5 characters. Please shorten it to continue'.format(start))
            
            search = re.findall(r'(\d{1,2},\d{1,2})|([a-z]{1}\d{1,2})')
            print(search)

    # Open the inquierer
    else:
        print('inquirer')



if __name__ == '__main__':
    arguments = docopt.docopt(__doc__, version='Perecian v2.0.0')
    main(arguments)