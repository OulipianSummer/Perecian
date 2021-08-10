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
    def __init__(self, name, order):
        self.name = name
        self.order = order
        
        self.tour_settings = None
        
        self.tour = None
        self.mols = None
        self.list = None

    def set_tour_settings(self, tour_settings):
        """Set settings used for creating a knight's tour

        Keyword arguments:
        tour_settings -- a dictionary containing settings for starting a knight's tour
        """
        self.tour_settings = tour_settings
        exit
    
    def export(self, mode):
        """Exports the project according to the mode argument
        
        Keyword arguments:
        mode -- flag from the command line that indicates how the user wishes to export this project
        """
        # TODO
        exit