from __future__ import print_function
from __future__ import absolute_import
from __future__ import division

import compas_rhino

from math import fabs
from compas_igs2.artists import FormArtist
from compas_igs2.rhino.artists import RhinoDiagramArtist


class RhinoFormArtist(FormArtist, RhinoDiagramArtist):
    """
    Rhino Artist for AGS form diagrams.
    """

    def draw_edges(self, edges=None, color=None):
        """
        Draw a selection of edges.

        This method overwrites the base method of the parent mesh artist
        to include arrows on the edges.

        Parameters
        ----------
        edges : list, optional
            A selection of edges to draw.
            The default is ``None``, in which case all edges are drawn.
        color : tuple or dict of tuple, optional
            The color specififcation for the edges.
            The default color is black, ``(0, 0, 0)``.

        Returns
        -------
        list
            The GUIDs of the created Rhino objects.

        """
        leaves = set(self.diagram.leaves())
        edges = edges or list(self.diagram.edges())
        vertex_xyz = self.vertex_xyz
        self.edge_color = color
        lines = []
        for edge in edges:
            arrow = None
            if self.diagram.edge_attribute(edge, "is_external"):
                f = self.diagram.edge_attribute(edge, "f")
                if f > 0:
                    arrow = "start" if edge[0] in leaves else "end"
                elif f < 0:
                    arrow = "start" if edge[1] in leaves else "end"
            lines.append(
                {
                    "start": vertex_xyz[edge[0]],
                    "end": vertex_xyz[edge[1]],
                    "color": self.edge_color.get(edge, self.default_edgecolor).rgb255,
                    "name": "{}.edge.{}-{}".format(self.diagram.name, *edge),
                    "arrow": arrow,
                }
            )
        return compas_rhino.draw_lines(
            lines,
            layer=self.layer,
            clear=False,
            redraw=False,
        )

    def draw_forcepipes(
        self,
        color_compression=None,
        color_tension=None,
        scale=None,
        tol=None,
    ):
        """
        Draw the forces in the internal edges as pipes with color and thickness matching the force value.

        Parameters
        ----------
        color_compression
        color_tension
        scale
        tol

        Returns
        -------
        list
            The GUIDs of the created Rhino objects.

        """
        color_compression = color_compression or self.color_compression
        color_tension = color_tension or self.color_tension
        scale = scale or self.scale_forces
        tol = tol or self.tol_forces
        vertex_xyz = self.vertex_xyz
        edges = []
        pipes = []
        for edge in self.diagram.edges_where({"is_external": False}):
            force = self.diagram.edge_attribute(edge, "f")
            if not force:
                continue
            radius = fabs(scale * force)
            if radius < tol:
                continue
            edges.append(edge)
            color = color_tension if force > 0 else color_compression
            pipes.append(
                {
                    "points": [vertex_xyz[edge[0]], vertex_xyz[edge[1]]],
                    "color": color.rgb255,
                    "radius": radius,
                    "name": "{}.force.{}-{}".format(self.diagram.name, *edge),
                }
            )
        return compas_rhino.draw_pipes(
            pipes,
            layer=self.layer,
            clear=False,
            redraw=False,
        )
