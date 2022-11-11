from __future__ import print_function
from __future__ import absolute_import
from __future__ import division

import compas_rhino

from compas_igs2.objects import FormObject
from compas_igs2.rhino.objects import RhinoDiagramObject


class RhinoFormObject(FormObject, RhinoDiagramObject):
    def __init__(self, *args, **kwargs):
        super(RhinoFormObject, self).__init__(*args, **kwargs)
        self._guid_force = {}

    @property
    def guids(self):
        guids = super(FormObject, self).guids
        guids += list(self.guid_force.keys())
        return guids

    @property
    def guid_force(self):
        return self._guid_force

    @guid_force.setter
    def guid_force(self, items):
        self._guid_force = dict(items)

    def clear(self):
        super(FormObject, self).clear()
        compas_rhino.delete_objects(self.guids, purge=True)
        self._guid_force = {}

    # ==========================================================================
    # Draw
    # ==========================================================================

    def draw(self):
        """
        Draw the form diagram.

        The visible components, display properties and visual style of the form diagram
        drawn by this method can be fully customised using the configuration items
        in the settings dict: ``FormArtist.settings``.

        The method will clear the scene of any objects it has previously drawn
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

        def vertex_is_constrained(key, attr):
            return True if attr["line_constraint"] else False

        def edge_is_constrained(key, attr):
            return True if attr["target_vector"] else False

        self.artist.vertex_xyz = self.vertex_xyz

        # vertices
        if self.settings["show.vertices"]:
            vertices = list(self.diagram.vertices())
            constrained = self.diagram.vertices_where_predicate(vertex_is_constrained)
            fixed = self.diagram.vertices_where(is_fixed=True)

            color = self.settings["color.vertices"]
            color_constrained = self.settings["color.vertices:line_constraint"]
            color_fixed = self.settings["color.vertices:is_fixed"]

            vertex_color = {vertex: color for vertex in vertices}
            if self.settings["show.constraints"]:
                vertex_color.update({vertex: color_constrained for vertex in constrained})
            vertex_color.update({vertex: color_fixed for vertex in fixed})

            guids = self.artist.draw_vertices(color=vertex_color)
            self.guid_vertex = zip(guids, vertices)

        # edges
        if self.settings["show.edges"]:
            edges = list(self.diagram.edges())
            external = self.diagram.edges_where(is_external=True)
            loads = self.diagram.edges_where(is_load=True)
            reactions = self.diagram.edges_where(is_reaction=True)
            indetermined = self.diagram.edges_where(is_ind=True)
            constrained = self.diagram.edges_where_predicate(edge_is_constrained)

            color = self.settings["color.edges"]
            color_external = self.settings["color.edges:is_external"]
            color_load = self.settings["color.edges:is_load"]
            color_reaction = self.settings["color.edges:is_reaction"]
            color_ind = self.settings["color.edges:is_ind"]
            color_constrained = self.settings["color.edges:target_vector"]

            edge_color = {edge: color for edge in edges}
            edge_color.update({edge: color_external for edge in external})
            edge_color.update({edge: color_load for edge in loads})
            edge_color.update({edge: color_reaction for edge in reactions})
            edge_color.update({edge: color_ind for edge in indetermined})

            # force colors
            if self.settings["show.forcecolors"]:
                tol = self.settings["tol.forces"]
                for edge in self.diagram.edges_where(is_external=False):
                    if self.diagram.edge_attribute(edge, "f") > +tol:
                        edge_color[edge] = self.settings["color.tension"]
                    elif self.diagram.edge_attribute(edge, "f") < -tol:
                        edge_color[edge] = self.settings["color.compression"]

            # edge target orientation constraints
            if self.settings["show.constraints"]:
                edge_color.update({edge: color_constrained for edge in constrained})

            guids = self.artist.draw_edges(color=edge_color)
            self.guid_edge = zip(guids, edges)

    def draw_highlight_edge(self, edge):
        f = self.diagram.edge_attribute(edge, "f")
        text = {edge: "{:.3g}kN".format(abs(f))}
        color = {}
        color[edge] = self.settings["color.edges"]

        if self.diagram.edge_attribute(edge, "is_external"):
            color[edge] = self.settings["color.edges:is_external"]
        if self.diagram.edge_attribute(edge, "is_load"):
            color[edge] = self.settings["color.edges:is_load"]
        if self.diagram.edge_attribute(edge, "is_reaction"):
            color[edge] = self.settings["color.edges:is_reaction"]
        if self.diagram.edge_attribute(edge, "is_ind"):
            color[edge] = self.settings["color.edges:is_ind"]

        tol = self.settings["tol.forces"]
        for edge in self.diagram.edges_where({"is_external": False}):
            if f > +tol:
                color[edge] = self.settings["color.tension"]
            elif f < -tol:
                color[edge] = self.settings["color.compression"]

        guid_edgelabel = self.artist.draw_edgelabels(text=text, color=color)
        self.guid_edgelabel = zip(guid_edgelabel, edge)
