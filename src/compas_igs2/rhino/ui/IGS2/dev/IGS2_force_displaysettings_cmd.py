from __future__ import print_function
from __future__ import absolute_import
from __future__ import division

import compas_rhino
from compas_ui.ui import UI


__commandname__ = "IGS2_force_displaysettings"


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
    force = objects[0]

    # Define the options
    options = ["VertexLabels", "EdgeLabels", "ForceLabels", "CompressionTension", "Constraints"]

    # Start an interactivce loop
    while True:
        option = compas_rhino.rs.GetString("FormDiagram Display", strings=options)
        if not option:
            break

        if option == "VertexLabels":
            if force.settings["show.vertexlabels"] is True:
                force.settings["show.vertexlabels"] = False
            else:
                force.settings["show.vertexlabels"] = True

        elif option == "EdgeLabels":
            if force.settings["show.edgelabels"] is True:
                force.settings["show.edgelabels"] = False
            else:
                force.settings["show.edgelabels"] = True
                force.settings["show.forcelabels"] = False

        elif option == "ForceLabels":
            if force.settings["show.forcelabels"] is True:
                force.settings["show.forcelabels"] = False
            else:
                force.settings["show.forcelabels"] = True
                force.settings["show.edgelabels"] = False

        elif option == "CompressionTension":
            if force.settings["show.forcecolors"] is True:
                force.settings["show.forcecolors"] = False
            else:
                force.settings["show.forcecolors"] = True

        elif option == "Constraints":
            if force.settings["show.constraints"] is True:
                force.settings["show.constraints"] = False
            else:
                force.settings["show.constraints"] = True

        ui.scene.update()

    # Update the scene and record
    ui.scene.update()
    ui.record()


if __name__ == "__main__":
    RunCommand(True)
