from __future__ import print_function
from __future__ import absolute_import
from __future__ import division

import compas_rhino
from compas_ui.ui import UI


__commandname__ = "IGS2_form_select_ind"


@UI.error()
def RunCommand(is_interactive):
    ui = UI()

    # Get the FormDiagram from the scene
    objects = ui.scene.get("FormDiagram")
    if not objects:
        compas_rhino.display_message("There is no FormDiagram in the scene.")
        return
    form = objects[0]

    # Select all independent edges.
    edges = form.select_edges("Select ALL independent edges.")

    # Update the form diagram accordingly.
    if edges:
        form.diagram.edges_attribute("is_ind", False)
        form.diagram.edges_attribute("is_ind", True, keys=edges)

        ui.scene.update()
        ui.record()


if __name__ == "__main__":
    RunCommand(True)
