from __future__ import print_function
from __future__ import absolute_import
from __future__ import division

from compas_rhino.artists import MeshArtist as RhinoMeshArtist
from compas_igs2.artists import DiagramArtist


class RhinoDiagramArtist(DiagramArtist, RhinoMeshArtist):
    """
    Rhino Artist for AGS diagrams.
    """
