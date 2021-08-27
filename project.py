#===============================================================================
#  File        : project.py
#  Project     : Perecian
#  Description : A class for managing perecian projects
#===============================================================================

#===============================================================================
#  Class Definition
#===============================================================================

class Project(object):
    """A class that defines a project object"""
    def __init__(self, args):
        self.name = args['<project_name>']
        self.order = args['<order>']
        
        
        self.tour = None
        self.mols = None
        self.list = None
    
    def export(self, mode):
        """Exports the project according to the mode argument
        
        Keyword arguments:
        mode -- flag from the command line that indicates how the user wishes to export this project
        """
        exit

    def set_tour(self, tour):
        self.tour = tour
    
    def set_export_path(self, path):
        self.export_path = path
    
    def set_import_path(self, path):
        self.import_path = path

    