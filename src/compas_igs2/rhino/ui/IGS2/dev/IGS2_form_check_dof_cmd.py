from __future__ import print_function
from __future__ import absolute_import
from __future__ import division

import compas_rhino
from compas_ui.ui import UI


__commandname__ = "IGS2_form_check_dof"


@UI.error()
def RunCommand(is_interactive):
    ui = UI()

    # Get the FormDiagram from the scene
    objects = ui.scene.get("FormDiagram")
    if not objects:
        compas_rhino.display_message("There is no FormDiagram in the scene.")
        return
    form = objects[0]

    # Create a proxy for compas_ags.ags.graphstatics.form_count_dof
    form_count_dof = ui.proxy.function("compas_ags.ags.graphstatics.form_count_dof")

    # Cout the DOF.
    dof = form_count_dof(form.diagram)
    k = dof[0]
    inds = len(list(form.diagram.edges_where(is_ind=True)))

    # Compile a message according to the result.
    if k == inds:
        message = "Success: You have identified the correct number of externally applied loads."
    elif k > inds:
        message = "Warning: You have not yet identified all external loads. (%s required and %s selected)" % (k, inds)
    else:
        message = "Warning: You have identified too many external forces as loads. (%s required and %s selected)" % (
            k,
            inds,
        )

    # Display the message.
    compas_rhino.display_message(message)


if __name__ == "__main__":
    RunCommand(True)
