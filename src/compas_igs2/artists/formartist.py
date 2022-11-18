from __future__ import print_function
from __future__ import absolute_import
from __future__ import division

from abc import abstractmethod
from compas.colors import Color
from compas_igs2.artists import DiagramArtist


class FormArtist(DiagramArtist):
    """
    Base artist for AGS form diagrams.

    Attributes
    ----------
    color_compression : 3-tuple
        Default color for compression.
    color_tension : 3-tuple
        Default color for tension.
    scale_forces : float
        Scale factor for the force pipes.
    tol_forces : float
        Tolerance for force magnitudes.

    """

    def __init__(self, *args, **kwargs):
        super(FormArtist, self).__init__(*args, **kwargs)
        self.color_compression = Color.blue()
        self.color_tension = Color.red()
        self.default_edgecolor = Color.black()
        self.scale_forces = 0.01
        self.tol_forces = 0.001

    @abstractmethod
    def draw_forcepipes(self):
        raise NotImplementedError
