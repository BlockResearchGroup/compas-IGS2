from __future__ import print_function
from __future__ import absolute_import
from __future__ import division

import compas_rhino
from compas_ui.ui import UI


__commandname__ = "IGS2_toggle_bidirectional"


@UI.error()
def RunCommand(is_interactive):
    ui = UI()

    answer = compas_rhino.rs.GetString("Autoupdate of Form/Force Diagram", "Cancel", ["On", "Off", "Cancel"])

    answer = compas_rhino.rs.GetString(
        "Bi-directional function at Form/Force Diagrams", "Cancel", ["On", "Off", "Cancel"]
    )

    if answer == "On":
        ui.registry["IGS2"]["bi-directional"] = True
        compas_rhino.display_message("Bi-directional Form/Force: [On]")

    if answer == "Off":
        ui.registry["IGS2"]["bi-directional"] = False
        compas_rhino.display_message("Bi-directional Form/Force: [Off]")


if __name__ == "__main__":
    RunCommand(True)
