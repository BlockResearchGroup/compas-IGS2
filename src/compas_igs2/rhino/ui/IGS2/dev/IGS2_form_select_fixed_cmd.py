from __future__ import print_function
from __future__ import absolute_import
from __future__ import division

import compas_rhino
from compas_ui.ui import UI


__commandname__ = "IGS2_form_select_fixed"


@UI.error()
def RunCommand(is_interactive):
    ui = UI()

    # Get the FormDiagram from the scene
    objects = ui.scene.get("FormDiagram")
    if not objects:
        compas_rhino.display_message("There is no FormDiagram in the scene.")
        return
    form = objects[0]

    # Unfix all vertices
    form.diagram.vertices_attribute("is_fixed", False)

    # Update the scene
    ui.scene.update()

    # Select the fixed vertices
    vertices = form.select_vertices("Fix selected vertices (unfix all others)")
    if not vertices:
        return

    # Update the form diagram
    form.diagram.vertices_attribute("is_fixed", True, keys=vertices)

    # Update the scene and record
    ui.scene.update()
    ui.record()


if __name__ == "__main__":
    RunCommand(True)
