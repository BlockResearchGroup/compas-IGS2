from __future__ import print_function
from __future__ import absolute_import
from __future__ import division

from compas_ui.artists import MeshArtist


class DiagramArtist(MeshArtist):
    """Base artist for diagrams in AGS.

    Attributes
    ----------
    diagram : :class:`compas_ags.diagrams.Diagram`
        The diagram associated with the artist.

    """

    @property
    def diagram(self):
        """The diagram assigned to the artist."""
        return self.mesh

    @diagram.setter
    def diagram(self, diagram):
        self.mesh = diagram
