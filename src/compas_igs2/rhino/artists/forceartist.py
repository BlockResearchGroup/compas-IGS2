from __future__ import print_function
from __future__ import absolute_import
from __future__ import division

from compas_igs2.artists import ForceArtist
from compas_igs2.rhino.artists import RhinoDiagramArtist


class RhinoForceArtist(ForceArtist, RhinoDiagramArtist):
    """
    Rhino artist for AGS force diagrams.
    """
