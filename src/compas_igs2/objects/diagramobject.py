from __future__ import print_function
from __future__ import absolute_import
from __future__ import division

from compas_ui.objects import MeshObject


class DiagramObject(MeshObject):
    """Base object for representing a form or force diagram in a scene."""

    def __init__(self, *args, **kwargs):
        super(DiagramObject, self).__init__(*args, **kwargs)

    @property
    def diagram(self):
        """The diagram associated with the object."""
        return self.mesh

    @diagram.setter
    def diagram(self, diagram):
        self.mesh = diagram
