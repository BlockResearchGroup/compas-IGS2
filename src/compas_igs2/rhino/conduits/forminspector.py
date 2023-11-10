from __future__ import print_function
from __future__ import absolute_import
from __future__ import division

from System.Collections.Generic import List
from System.Drawing.Color import FromArgb
from Rhino.Geometry import Point3d
from Rhino.Geometry import Line

from compas_rhino.conduits import BaseConduit
from compas_ui.rhino.mouse import Mouse

from compas.geometry import length_vector
from compas.geometry import cross_vectors
from compas.geometry import subtract_vectors


class FormDiagramInspector(BaseConduit):
    def __init__(self, *args, **kwargs):
        super(FormDiagramInspector, self).__init__(*args, **kwargs)
        self.mouse = Mouse(self)

    @property
    def form_vertex_xyz(self):
        return self._form_vertex_xyz

    @form_vertex_xyz.setter
    def form_vertex_xyz(self, vertex_xyz):
        self._form_vertex_xyz = vertex_xyz

    @property
    def force_vertex_xyz(self):
        return self._force_vertex_xyz

    @force_vertex_xyz.setter
    def force_vertex_xyz(self, vertex_xyz):
        self._force_vertex_xyz = vertex_xyz

    def enable(self):
        self.mouse.Enabled = True
        self.Enabled = True

    def disable(self):
        self.mouse.Enabled = False
        self.Enabled = False


class FormDiagramVertexInspector(FormDiagramInspector):
    """
    Inspect diagram topology at the vertices.
    """

    def __init__(self, form, tol=0.1, **kwargs):
        super(FormDiagramVertexInspector, self).__init__(**kwargs)
        self._form_vertex_xyz = None
        self._force_vertex_xyz = None
        self.form = form
        self.tol = tol
        self.dotcolor = FromArgb(255, 255, 0)
        self.textcolor = FromArgb(0, 0, 0)
        self.linecolor = FromArgb(255, 255, 0)
        self.form_vertex_edges = self._compute_form_vertex_edges()
        self.force_face_edges = self._compute_force_face_edges()

    def _compute_form_vertex_edges(self):
        form_vertex_edges = {vertex: [] for vertex in self.form.vertices()}
        for edge in self.form.edges_where(_is_edge=True):
            u, v = edge
            form_vertex_edges[u].append(edge)
            form_vertex_edges[v].append(edge)
        return form_vertex_edges

    def _compute_force_face_edges(self):
        force_face_edges = {}
        for face in self.form.dual.faces():
            force_face_edges[face] = []
            for edge in self.form.dual.face_halfedges(face):
                u, v = edge
                if self.form.dual.has_edge(edge):
                    force_face_edges[face].append((u, v))
                else:
                    force_face_edges[face].append((v, u))
        return force_face_edges

    def DrawForeground(self, e):
        draw_dot = e.Display.DrawDot
        draw_arrows = e.Display.DrawArrows
        a = self.mouse.p1
        b = self.mouse.p2
        ab = subtract_vectors(b, a)
        L = length_vector(ab)
        if not L:
            return

        for index, vertex in enumerate(self.form_vertex_xyz):
            c = self.form_vertex_xyz[vertex]
            D = length_vector(cross_vectors(subtract_vectors(a, c), subtract_vectors(b, c)))

            if D / L < self.tol:
                point = Point3d(*c)
                draw_dot(point, str(index), self.dotcolor, self.textcolor)

                lines = List[Line](len(self.form_vertex_edges[vertex]))
                for u, v in self.form_vertex_edges[vertex]:
                    lines.Add(
                        Line(
                            Point3d(*self.form_vertex_xyz[u]),
                            Point3d(*self.form_vertex_xyz[v]),
                        )
                    )
                draw_arrows(lines, self.linecolor)

                lines = List[Line](len(self.force_face_edges[vertex]))
                for u, v in self.force_face_edges[vertex]:
                    lines.Add(
                        Line(
                            Point3d(*self.force_vertex_xyz[u]),
                            Point3d(*self.force_vertex_xyz[v]),
                        )
                    )
                draw_arrows(lines, self.linecolor)

                break
