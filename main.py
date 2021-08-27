"""Perecian

Usage:
    perecian new [( <project_name> <order> [(-t [-s] <start>)] [<source_path>] [-e [-i] [<export_path>] | -j] )]
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

from tour import Tour
from project import Project
from validate import validate_project_name, validate_start, validate_order, validate_path
import sys
import docopt



def main(args):
    """ Executes the main function
    """

    # Begin a new project
    if args['new'] and args['<project_name>']:
        
        name = args['<project_name>']
        order = args['<order>']
        
        validate_project_name(name)
        validate_order(order)

        project = Project(args)

        if args['--tour'] or args['<start>']:
            start = args['<start>']
            validate_start(start)
            tour = Tour(args)
            project.set_tour(tour)
        
        if args['<source_path>']:
            import_path = args['<source_path>']
            validate_path(import_path)
            project.set_import_path(import_path) 

         # Get tour
        project.tour.create_tour()
        
        # Get MOLS

        # Get list

        if args['--export']:
            export_path = args['<export_path>']
            validate_path(export_path)
            project.set_export_path(export_path)

        



    # Open the inquierer
    else:
        print('inquirer')



if __name__ == '__main__':
    arguments = docopt.docopt(__doc__, version='Perecian v2.0.0')
    main(arguments)
