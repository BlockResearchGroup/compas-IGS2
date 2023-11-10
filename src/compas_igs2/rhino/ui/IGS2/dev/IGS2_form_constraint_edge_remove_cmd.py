from __future__ import print_function
from __future__ import absolute_import
from __future__ import division

import compas_rhino
from compas_ui.ui import UI


__commandname__ = "IGS2_form_constraint_edge_remove"


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

    for vertex, attr in form.diagram.vertices(True):
        attr["line_constraint"] = None

    for vertex, attr in force.diagram.vertices(True):
        attr["line_constraint"] = None
        attr["is_fixed"] = False

    for edge, attr in form.diagram.edges(True):
        attr["target_vector"] = None
        attr["target_force"] = None

    for edge, attr in force.diagram.edges(True):
        attr["target_vector"] = None

    # Update the scene and record
    ui.scene.update()
    ui.record()


if __name__ == "__main__":
    RunCommand(True)
