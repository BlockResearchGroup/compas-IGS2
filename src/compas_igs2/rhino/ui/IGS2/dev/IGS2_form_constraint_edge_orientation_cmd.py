from __future__ import print_function
from __future__ import absolute_import
from __future__ import division

import compas_rhino
from compas_ui.ui import UI


__commandname__ = "IGS2_form_constraint_edge_orientation"


@UI.error()
def RunCommand(is_interactive):
    ui = UI()

    # Get the FormDiagram from the scene
    objects = ui.scene.get("FormDiagram")
    if not objects:
        compas_rhino.display_message("There is no FormDiagram in the scene.")
        return
    form = objects[0]

    # Get the ForceDiagram from the scene
    objects = ui.scene.get("ForceDiagram")
    if not objects:
        compas_rhino.display_message("There is no ForceDiagram in the scene.")
        return
    force = objects[0]

    edges = form.select_edges("Edges to constraint their current orientation.")
    if not edges:
        return

    for edge in edges:
        sp, ep = form.diagram.edge_coordinates(*edge)
        dx = ep[0] - sp[0]
        dy = ep[1] - sp[1]
        length = (dx**2 + dy**2) ** 0.5
        form.diagram.edge_attribute(edge, "target_vector", [dx / length, dy / length])

    force.diagram.constraints_from_dual()

    # Update the scene and record
    ui.scene.update()
    ui.record()


if __name__ == "__main__":
    RunCommand(True)
