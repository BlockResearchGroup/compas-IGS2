from __future__ import print_function
from __future__ import absolute_import
from __future__ import division

import compas_rhino
from compas_ui.ui import UI


__commandname__ = "IGS2_form_update_from_qind"


@UI.error()
def RunCommand(is_interactive):
    ui = UI()

    # Get the FormDiagram from the scene
    objects = ui.scene.get("FormDiagram")
    if not objects:
        compas_rhino.display_message("There is no FormDiagram in the scene.")
        return
    form = objects[0]

    # Create a proxy for compas_ags.ags.graphstatics.form_update_q_from_qind
    form_update_q_from_qind = ui.proxy.function("compas_ags.ags.graphstatics.form_update_q_from_qind")

    # Run compas_ags.ags.graphstatics.form_update_q_from_qind in the cloud.
    formdiagram = form_update_q_from_qind(form.diagram)

    # Update the form diagram data.
    form.diagram.data = formdiagram.data

    # Update the scene.
    ui.scene.update()
    ui.record()


if __name__ == "__main__":
    RunCommand(True)
