from __future__ import print_function
from __future__ import absolute_import
from __future__ import division

import compas_rhino
from compas_ui.ui import UI


__commandname__ = "IGS2_form_move_nodes"


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
    form_show_edgelabels = form.settings["show.edgelabels"]
    form_show_forcelabels = form.settings["show.forcelabels"]

    # Store the current force viz settings
    force_show_edgelabels = force.settings["show.edgelabels"]

    # Adjust form viz settings
    form.settings["show.edgelabels"] = True
    form.settings["show.forcelabels"] = False

    # Adjust force viz settings
    force.settings["show.edgelabels"] = True

    # Update the scene with the current viz settings
    ui.scene.update()

    # Start an interactive loop
    while True:
        # Select form vertices and break out if none are selected
        vertices = form.select_vertices("Select vertices (Press ESC to exit)")
        if not vertices:
            break

        # If form vertices were moved
        # update equilibrium if auto update is on
        if form.move_vertices(vertices):
            if ui.registry["IGS2"]["autoupdate"]:
                form_update_q_from_qind = ui.proxy.function("compas_ags.ags.graphstatics.form_update_q_from_qind")
                formdiagram = form_update_q_from_qind(form.diagram)
                form.diagram.data = formdiagram.data

                force_update_from_form = ui.proxy.function("compas_ags.ags.graphstatics.force_update_from_form")
                forcediagram = force_update_from_form(force.diagram, form.diagram)
                force.diagram.data = forcediagram.data

            ui.scene.update()

    # Restore the old viz settings
    form.settings["show.edgelabels"] = form_show_edgelabels
    form.settings["show.forcelabels"] = form_show_forcelabels
    force.settings["show.edgelabels"] = force_show_edgelabels

    # Update the scene and record the changes
    ui.scene.update()
    ui.record()


if __name__ == "__main__":
    RunCommand(True)
