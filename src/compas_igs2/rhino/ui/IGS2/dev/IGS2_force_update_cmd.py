from __future__ import print_function
from __future__ import absolute_import
from __future__ import division

import compas_rhino
from compas_ui.ui import UI


__commandname__ = "IGS2_force_select_fixed"


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

    # Create a proxy for compas_ags.ags.graphstatics.form_update_q_from_qind
    form_update_q_from_qind = ui.proxy.function("compas_ags.ags.graphstatics.form_update_q_from_qind")

    formdiagram = form_update_q_from_qind(form.diagram)
    form.diagram.data = formdiagram.data

    # Create a proxy for compas_ags.ags.graphstatics.force_update_from_form
    force_update_from_form = ui.proxy.function("compas_ags.ags.graphstatics.force_update_from_form")

    forcediagram = force_update_from_form(force.diagram, form.diagram)
    force.diagram.data = forcediagram.data

    # Update the scene and record
    ui.scene.update()
    ui.record()


if __name__ == "__main__":
    RunCommand(True)
