from __future__ import print_function
from __future__ import absolute_import
from __future__ import division

import compas_rhino
from compas_ui.ui import UI

# from compas.geometry import Point


__commandname__ = "IGS2_force_scale"


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

    # Ask for a scaling mode
    options = ["Factor", "3Points"]
    option = compas_rhino.rs.GetString("Scale ForceDiagram:", strings=options)
    if not option:
        return

    # Scale by a factor
    if option == "Factor":
        scale_factor = compas_rhino.rs.GetReal("Scale factor", force.scale)
        force.scale = scale_factor

    # Scale interactively
    elif option == "3Points":
        # loc0 = force.location_0deg
        # loc90 = force.location_90deg

        # force.scale_from_3_points(message="Select the base node of the Force Diagram for the scaling operation.")

        # anchor_xyz = force.location.copy()

        # if force.settings["rotate.90deg"]:
        #     force.location_90deg = anchor_xyz
        #     anchor_vector = anchor_xyz - loc90
        #     anchor_rotated = Point(anchor_vector[1], -anchor_vector[0], 0.0)  # rotate 90
        #     force.location_0deg = loc0 + anchor_rotated
        # else:
        #     force.location_0deg = anchor_xyz
        #     anchor_vector = anchor_xyz - loc0
        #     anchor_rotated = Point(-anchor_vector[1], anchor_vector[0], 0.0)  # rotate -90
        #     force.location_90deg = loc90 + anchor_rotated

        compas_rhino.display_message("This scaling method is not available yet.")

    # Update the scene and record
    ui.scene.update()
    ui.record()


if __name__ == "__main__":
    RunCommand(True)
