from __future__ import print_function
from __future__ import absolute_import
from __future__ import division

import compas_rhino
from compas_ui.ui import UI
from compas_igs2.rhino.forms import AttributesForm


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

    # Turn on edge labels
    form_settings = {k: form.settings.get(k) for k in form.settings.keys()}
    force_settings = {k: force.settings.get(k) for k in force.settings.keys()}

    form.settings["show.edgelabels"] = True
    force.settings["show.edgelabels"] = True
    form.settings["show.constraints"] = False
    force.settings["show.constraints"] = False
    form.settings["show.forcepipes"] = False
    ui.scene.update()

    AttributesForm.from_sceneNode(form, dual=force)

    # Revert to original setting
    for key, value in form_settings.items():
        form.settings[key] = value
    for key, value in force_settings.items():
        force.settings[key] = value

    ui.scene.update()


if __name__ == "__main__":
    RunCommand(True)
