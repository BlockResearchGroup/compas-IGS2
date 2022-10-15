from __future__ import print_function
from __future__ import absolute_import
from __future__ import division

from compas_igs2.artist import DiagramArtist


class RhinoDiagramArtist(DiagramArtist):
    """Artist for force diagrams in AGS.

    Parameters
    ----------
    form: compas_ags.diagrams.FormDiagram
        The form diagram to draw.

    """

    def __init__(self, force, layer=None):
        super(RhinoDiagramArtist, self).__init__(*args, **kwargs)
