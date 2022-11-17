from __future__ import print_function
from __future__ import absolute_import
from __future__ import division

# from math import pi
from compas_igs2.objects import ForceObject
from compas_igs2.rhino.objects import RhinoDiagramObject
from compas_igs2.rhino.conduits import ForceDiagramVertexInspector


class RhinoForceObject(ForceObject, RhinoDiagramObject):
    """"""

    def __init__(self, *args, **kwargs):
        super(RhinoForceObject, self).__init__(*args, **kwargs)

    @property
    def inspector(self):
        if not self._inspector:
            self._inspector = ForceDiagramVertexInspector(self.diagram)
        return self._inspector

    def inspector_on(self, form):
        self.inspector.form_vertex_xyz = form.artist.vertex_xyz
        self.inspector.force_vertex_xyz = self.artist.vertex_xyz
        self.inspector.enable()

    def inspector_off(self):
        self.inspector.disable()

    # ==========================================================================
    # Draw
    # ==========================================================================

    def draw(self):
        """Draw the diagram.

        The visible components, display properties and visual style of the diagram
        can be fully customised using the configuration items in the settings dict.

        The method will clear the drawing layer and any objects it has drawn in a previous call,
        and keep track of any newly created objects using their GUID.

        Parameters
        ----------
        None

        Returns
        -------
        None

        """
        self.clear()
        if not self.visible:
            return

        # if self.settings["rotate.90deg"]:
        #     self.rotation = [0, 0, pi / 2]
        #     self.location = self.location_90deg
        # else:
        #     self.rotation = [0, 0, 0]
        #     self.location = self.location_0deg

        self.artist.vertex_xyz = self.vertex_xyz

        # vertices
        if self.settings["show.vertices"]:
            vertices = list(self.diagram.vertices())
            vertex_color = {}

            for vertex in vertices:
                vertex_color[vertex] = self.settings["color.vertices"]

                if self.settings["show.constraints"]:
                    if self.diagram.vertex_attribute(vertex, "line_constraint"):
                        vertex_color[vertex] = self.settings["color.vertices:line_constraint"]

                if self.diagram.vertex_attribute(vertex, "is_fixed"):
                    vertex_color[vertex] = self.settings["color.vertices:is_fixed"]

            guids = self.artist.draw_vertices(color=vertex_color)
            self.guids += guids
            self.guid_vertex = zip(guids, vertices)

            # vertex labels
            if self.settings["show.vertexlabels"]:
                vertex_text = {vertex: index for index, vertex in enumerate(vertices)}
                guids = self.artist.draw_vertexlabels(text=vertex_text)
                self.guids += guids

        # edges

        def is_constrained(key, attr):
            return True if attr["target_vector"] else False

        if self.settings["show.edges"]:
            tol = self.settings["tol.forces"]

            edges = []
            for edge in self.diagram.edges():
                if self.diagram.edge_length(*edge) > tol:
                    edges.append(edge)

            edge_color = {}

            for edge in edges:
                edge_color[edge] = self.settings["color.edges"]
            for edge in self.diagram.edges_where_dual({"is_external": True}):
                edge_color[edge] = self.settings["color.edges:is_external"]
            for edge in self.diagram.edges_where_dual({"is_load": True}):
                edge_color[edge] = self.settings["color.edges:is_load"]
            for edge in self.diagram.edges_where_dual({"is_reaction": True}):
                edge_color[edge] = self.settings["color.edges:is_reaction"]
            for edge in self.diagram.edges_where_dual({"is_ind": True}):
                edge_color[edge] = self.settings["color.edges:is_ind"]

            # force colors
            if self.settings["show.forcecolors"]:
                tol = self.settings["tol.forces"]
                for edge in self.diagram.edges_where_dual({"is_external": False}):
                    if self.diagram.dual_edge_force(edge) > +tol:
                        edge_color[edge] = self.settings["color.tension"]
                    elif self.diagram.dual_edge_force(edge) < -tol:
                        edge_color[edge] = self.settings["color.compression"]

            if self.settings["show.constraints"]:
                for edge in self.diagram.edges_where_predicate(is_constrained):
                    edge_color[edge] = self.settings["color.edges:target_vector"]

            guids = self.artist.draw_edges(edges=edges, color=edge_color)
            self.guids += guids
            self.guid_edge = zip(guids, edges)

            self.guid_edgelabel = []

            # edge labels
            if self.settings["show.edgelabels"]:
                edge_index = self.diagram.edge_index(self.diagram.dual)
                edge_index.update({(v, u): i for (u, v), i in edge_index.items()})
                edge_text = {edge: edge_index[edge] for edge in edges}

                guids = self.artist.draw_edgelabels(text=edge_text)
                self.guids += guids

            # edge constraints
            elif self.settings["show.constraints"]:
                edge_text = {}
                edges_target_force = []
                for edge in edges:
                    target_force = self.diagram.dual_edge_targetforce(edge)
                    if target_force:
                        edge_text[edge] = "{:.3g}kN".format(abs(target_force))
                        edges_target_force.append(edge)

                if edges_target_force:
                    guids = self.artist.draw_edgelabels(text=edge_text)
                    self.guids += guids

            # force labels
            elif self.settings["show.forcelabels"]:
                edge_text = {}
                for edge in edges:
                    f = self.diagram.dual_edge_force(edge)
                    edge_text[edge] = "{:.4g}kN".format(abs(f))

                guids = self.artist.draw_edgelabels(text=edge_text)
                self.guids += guids

    def draw_highlight_edge(self, edge):
        if not self.diagram.has_edge(edge):
            edge = edge[1], edge[0]

        f = self.diagram.dual_edge_force(edge)

        edge_text = {edge: "{:.3g}kN".format(abs(f))}
        edge_color = {}
        edge_color[edge] = self.settings["color.edges"]

        if edge in self.diagram.edges_where_dual({"is_external": True}):
            edge_color[edge] = self.settings["color.edges:is_external"]
        if edge in self.diagram.edges_where_dual({"is_load": True}):
            edge_color[edge] = self.settings["color.edges:is_load"]
        if edge in self.diagram.edges_where_dual({"is_reaction": True}):
            edge_color[edge] = self.settings["color.edges:is_reaction"]
        if edge in self.diagram.edges_where_dual({"is_ind": True}):
            edge_color[edge] = self.settings["color.edges:is_ind"]

        tol = self.settings["tol.forces"]
        if edge in self.diagram.edges_where_dual({"is_external": False}):
            if f > +tol:
                edge_color[edge] = self.settings["color.tension"]
            elif f < -tol:
                edge_color[edge] = self.settings["color.compression"]

        guids = self.artist.draw_edgelabels(text=edge_text)
        self.guids += guids
