from __future__ import print_function
from __future__ import absolute_import
from __future__ import division

import compas_rhino
from compas_ui.ui import UI


__commandname__ = "IGS2_form_deviation_threshold"


@UI.error()
def RunCommand(is_interactive):
    ui = UI()

    # Ask the user for the maximum deviation value.
    max_dev = compas_rhino.rs.GetReal(
        message="Assign threshold for maximum angle deviation",
        number=ui.registry["IGS2"]["max_deviation"],
    )
    if not max_dev:
        return

    # Store in the settings
    ui.registry["IGS2"]["max_deviation"] = max_dev

    # Update the scene and record
    # ui.scene.update()
    ui.record()


if __name__ == "__main__":
    RunCommand(True)
