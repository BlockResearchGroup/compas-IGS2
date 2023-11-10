from __future__ import print_function
from __future__ import absolute_import
from __future__ import division

import compas_rhino
from compas_ui.ui import UI


__commandname__ = "IGS2_form_compute_loadpath"


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

    # Create a proxy for compas_ags.ags.loadpath.compute_loadpath
    compute_loadpath = ui.proxy.function("compas_ags.ags.loadpath.compute_loadpath")

    # Compute the loadpath using the proxy.
    lp = compute_loadpath(form.diagram, force.diagram)

    # Display the result.
    compas_rhino.display_message("The total load-path of the structure is {} kNm.".format(round(lp, 2)))


if __name__ == "__main__":
    RunCommand(True)
