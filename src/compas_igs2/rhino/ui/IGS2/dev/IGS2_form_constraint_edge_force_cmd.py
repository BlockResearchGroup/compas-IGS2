from __future__ import print_function
from __future__ import absolute_import
from __future__ import division

import compas_rhino
from compas_ui.ui import UI


__commandname__ = "IGS2_form_constraint_edge_force"


@UI.error()
def RunCommand(is_interactive):
    ui = UI()

    # Get the FormDiagram from the scene
    objects = ui.scene.get("FormDiagram")
    if not objects:
        compas_rhino.display_message("There is no FormDiagram in the scene.")
        return
    form = objects[0]

    edges = form.select_edges("Edges to assign target force")
    if not edges:
        return

    forcemag = compas_rhino.rs.GetReal("Value of the target force (KN)", 1.0)
    if not forcemag or forcemag == 0.0:
        return

    for edge in edges:
        form.diagram.edge_attribute(edge, "target_force", abs(forcemag))

    # Update the scene and record
    ui.scene.update()
    ui.record()


if __name__ == "__main__":
    RunCommand(True)
