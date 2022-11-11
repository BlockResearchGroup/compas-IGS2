from __future__ import print_function
from __future__ import absolute_import
from __future__ import division

from compas_ui.objects import MeshObject


class DiagramObject(MeshObject):
    """
    Base object for representing AGS diagrams in a scene.
    """

    @property
    def diagram(self):
        return self.mesh

    @diagram.setter
    def diagram(self, diagram):
        self.mesh = diagram
