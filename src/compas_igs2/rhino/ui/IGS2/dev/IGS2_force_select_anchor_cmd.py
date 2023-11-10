from __future__ import print_function
from __future__ import absolute_import
from __future__ import division

import compas_rhino
from compas_ui.ui import UI

# from compas.geometry import Point


__commandname__ = "IGS2_force_select_anchor"


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

    # Ask for a vertex to anchor
    vertex = force.select_vertex("Select the anchor vertex.")
    if vertex is None:
        return

    # Anchor to the selected vertex location
    vertex_xyz = force.artist.vertex_xyz
    anchor_xyz = vertex_xyz[vertex]  # sets the location as the anchor xyz position rotated or not
    # loc0 = force.location_0deg
    # loc90 = force.location_90deg

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

    force.location = anchor_xyz
    force.anchor = vertex

    # Update the scene and record
    ui.scene.update()
    ui.record()


if __name__ == "__main__":
    RunCommand(True)
