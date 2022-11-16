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

    # @property
    # def state(self):
    #     _edge_color = self._edge_color or {}
    #     return {
    #         "default_vertexcolor": self.default_vertexcolor,
    #         "default_edgecolor": self.default_edgecolor,
    #         "default_facecolor": self.default_facecolor,
    #         "vertex_color": self._vertex_color,
    #         "edge_color": {"{},{}".format(*edge): self._edge_color[edge] for edge in _edge_color},
    #         "face_color": self._face_color,
    #         "vertices": self.vertices,
    #         "edges": self.edges,
    #         "faces": self.faces,
    #     }

    # @state.setter
    # def state(self, state):
    #     self.default_vertexcolor = state["default_vertexcolor"]
    #     self.default_edgecolor = state["default_edgecolor"]
    #     self.default_facecolor = state["default_facecolor"]
    #     self._vertex_color = state["vertex_color"]
    #     self._edge_color = {(int(edge[0]), int(edge[1])): state["edge_color"][edge] for edge in state["edge_color"]}
    #     self._face_color = state["face_color"]
    #     self.vertices = state["vertices"]
    #     self.edges = state["edges"]
    #     self.faces = state["faces"]
