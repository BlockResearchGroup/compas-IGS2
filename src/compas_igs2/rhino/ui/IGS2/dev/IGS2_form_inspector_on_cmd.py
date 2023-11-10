from __future__ import print_function
from __future__ import absolute_import
from __future__ import division

import compas_rhino
from compas_ui.ui import UI


__commandname__ = "IGS2_form_inspector_on"


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
    if objects:
        force = objects[0]
    else:
        force = None

    # Turn the form inspector on.
    if force:
        form.inspector_on(force)
        compas_rhino.display_message("Form inspector: [ON]")


if __name__ == "__main__":
    RunCommand(True)
