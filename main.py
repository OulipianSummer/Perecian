#!/usr/bin/env python

from tour import make_tour
import sys

def main():
    """ Executes the main function

    filepath settings?

    Options
    -f or --full <-- default
        if given a dir path, exports formatted to file
        otherwise, prints to console        

    -F or --fullcustom
        takes two filepaths seperated by a >
        custom > output
        same behavior as base form
        if custom is empty, search in basedir
        if output is empty, place in basedir

    -t or --tour
        -w or --warnsdorff
        -s or --shuffle
    
    -T or --tourcustom
        takes string or filepath

    -m or --mols
        takes a filepath to a mols file

    -M or --molscustom
        takes string or filepath

    -l or --list
        takes a filepath

    -L or --listcustom
        takes filepath

    -h or --help
    -v or --version
    """
    
    try:
        arg = sys.argv[1]
    except IndexError:
        raise SystemExit(f"Usage: {sys.argv[0]} <options> <arguments>")

    

    make_tour()


main()