# This module contains the data model for the new
# motif set selection dialog.
# Author: Cyprian Corwin

# This is a utility class that will be used as a struct to hold motif
# set information.
class MotifSet:
    # longDescription and shortDescription must be strings
    # motifs must be a Python set
    def __init__(self, shortDescription, longDescription, motifs):
        self.longDescription = longDescription
        self.shortDescription = shortDescription
        self.motifs = motifs
