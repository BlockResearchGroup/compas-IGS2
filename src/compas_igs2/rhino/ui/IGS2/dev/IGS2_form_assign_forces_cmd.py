from __future__ import print_function
from __future__ import absolute_import
from __future__ import division

import compas_rhino
from compas_ui.ui import UI


__commandname__ = "IGS2_form_assign_forces"


@UI.error()
def RunCommand(is_interactive):
    ui = UI()

    # Get the FormDiagram from the scene
    objects = ui.scene.get("FormDiagram")
    if not objects:
        compas_rhino.display_message("There is no FormDiagram in the scene.")
        return
    form = objects[0]

    # Identify the independent edges.
    edges = list(form.diagram.edges_where(is_ind=True))

    # Inform the user and abort if there are no independent edges.
    if not len(edges):
        compas_rhino.display_message(
            """Warning: None of the edges of the diagram are marked as 'independent'.
            Forces can only be assigned to independent edges. Please select the independent edges first."""
        )
        return

    # Store the current label settings
    show_edgelabels = form.settings["show.edgelabels"]
    show_forcelabels = form.settings["show.forcelabels"]

    # Turn on the edge and force labels
    form.settings["show.edgelabels"] = True
    form.settings["show.forcelabels"] = False
    ui.scene.update()

    # Make an edge_index map.
    edge_index = form.diagram.edge_index()

    # Update the force values of the independent edges using indices as identifiers.
    names = [edge_index[edge] for edge in edges]
    values = [str(form.diagram.edge_attribute(edge, "f")) for edge in edges]
    values = compas_rhino.update_named_values(names, values, message="Independent edges.", title="Update force values.")
    if values:
        for edge, value in zip(edges, values):
            try:
                F = float(value)
            except (ValueError, TypeError):
                pass
            else:
                L = form.diagram.edge_length(*edge)
                Q = F / L
                form.diagram.edge_attribute(edge, "f", F)
                form.diagram.edge_attribute(edge, "q", Q)

    # Reset the label settings
    form.settings["show.edgelabels"] = show_edgelabels
    form.settings["show.forcelabels"] = show_forcelabels

    # Update the scene and record
    ui.scene.update()
    ui.record()


if __name__ == "__main__":
    RunCommand(True)
