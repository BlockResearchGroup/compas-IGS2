from __future__ import print_function
from __future__ import absolute_import
from __future__ import division

import compas_rhino
from compas_ui.ui import UI

import IGS2_force_inspector_on_cmd
import IGS2_force_inspector_off_cmd


__commandname__ = "IGS2_force_inspector_control"


@UI.error()
def RunCommand(is_interactive):
    ui = UI()

    # Get the FormDiagram from the scene
    objects = ui.scene.get("FormDiagram")
    if not objects:
        compas_rhino.display_message("There is no FormDiagram in the scene.")
        return
    # form = objects[0]

    # Get the ForceDiagram from the scene
    objects = ui.scene.get("ForceDiagram")
    if not objects:
        compas_rhino.display_message("There is no ForceDiagram in the scene.")
        return
    # force = objects[0]

    # Ask to turn the inspector on or off
    answer = compas_rhino.rs.GetString(
        "Force Dual Inspector",
        "Cancel",
        ["On", "Off", "Cancel"],
    )
    if answer == "On":
        IGS2_force_inspector_on_cmd.RunCommand(True)
    if answer == "Off":
        IGS2_force_inspector_off_cmd.RunCommand(True)


if __name__ == "__main__":
    RunCommand(True)
