from __future__ import print_function
from __future__ import absolute_import
from __future__ import division

import compas_rhino
from compas_ui.ui import UI


__commandname__ = "IGS2_form_constraint_vertex_inspect"


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

    # Store the current form viz settings
    form_settings = {k: form.settings.get(k) for k in form.settings.keys()}

    # Store the current force viz settings
    force_settings = {k: force.settings.get(k) for k in force.settings.keys()}

    # Adjust form viz settings
    form.settings["show.edges"] = True
    form.settings["show.forcelabels"] = False
    form.settings["show.edgelabels"] = False
    form.settings["show.forcepipes"] = False
    form.settings["show.constraints"] = True

    # Adjust force viz settings
    force.settings["show.edges"] = True
    force.settings["show.forcelabels"] = False
    force.settings["show.edgelabels"] = False
    force.settings["show.constraints"] = True

    # Vertex index maps
    form_vertex_index = form.diagram.vertex_index()
    force_vertex_index = force.diagram.vertex_index()

    # Start an interactive loop
    while True:
        # Apply the viz settings
        ui.scene.update()

        # Note: This should be replaced by `compas_rhino.select_point`
        guid = compas_rhino.rs.GetObject(
            message="Select a vertex in the form or in the force diagram to check constraints",
            preselect=True,
            select=True,
            filter=compas_rhino.rs.filter.point,
        )

        # Check that the selection is valid.
        # Break out the loop otherwise.
        if not guid:
            break
        elif guid not in form.guid_vertex and guid not in force.guid_vertex:
            compas_rhino.display_message("Vertex does not belog to form or force diagram.")
            break

        # Get the vertex of the form diagram corresponding to the point
        # and its line constraint.
        if guid in form.guid_vertex:
            key_form = form.guid_vertex[guid]
            constraint = form.diagram.vertex_attribute(key_form, "line_constraint")
            index = form_vertex_index[key_form]

        # Get the vertex of the force diagram corresponding to the point
        # and its line constraint.
        if guid in force.guid_vertex:
            key_force = force.guid_vertex[guid]
            constraint = force.diagram.vertex_attribute(key_force, "line_constraint")
            index = force_vertex_index[key_force]

        # If there is a constraint,
        # redefine it as a line.
        if constraint:
            sp = constraint.start
            ep = constraint.end
            constraint = [sp, ep]

        # Inform the user.
        compas_rhino.display_message("Vertex Index: {0}\nLine constraint: {1}".format(index, constraint))

        # Ask the user if the loop should continue
        # Note: I would replace this by a simple escape
        answer = compas_rhino.rs.GetString("Continue selecting vertices?", "No", ["Yes", "No"])
        if not answer:
            break
        if answer == "No":
            break

    # Restore form viz settings
    for key, value in form_settings.items():
        form.settings[key] = value

    # Restore force viz settings
    for key, value in force_settings.items():
        force.settings[key] = value

    # Update the scene and record
    ui.scene.update()
    ui.record()


if __name__ == "__main__":
    RunCommand(True)
