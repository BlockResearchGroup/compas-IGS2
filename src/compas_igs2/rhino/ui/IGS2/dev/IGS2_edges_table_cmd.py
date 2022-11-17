from __future__ import print_function
from __future__ import absolute_import
from __future__ import division

import compas_rhino
from compas_ui.ui import UI


__commandname__ = "IGS2_edges_table"


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

    # # Turn on edge labels
    # form_settings = form.settings.copy()
    # force_settings = force.settings.copy()
    # form.settings["show.edgelabels"] = True
    # force.settings["show.edgelabels"] = True
    # form.settings["show.constraints"] = False
    # force.settings["show.constraints"] = False
    # force.settings["show.forcepipes"] = False
    # scene.update()

    # AttributesForm.from_sceneNode(form, dual=force)

    # # Revert to original setting
    # form.settings = form_settings
    # force.settings = force_settings

    # Update the scene and record
    ui.scene.update()
    ui.record()


if __name__ == "__main__":
    RunCommand(True)
