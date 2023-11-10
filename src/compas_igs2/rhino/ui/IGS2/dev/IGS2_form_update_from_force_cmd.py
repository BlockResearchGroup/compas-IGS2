from __future__ import print_function
from __future__ import absolute_import
from __future__ import division

import compas_rhino
from compas_ui.ui import UI
from compas_igs2.utilities import check_equilibrium
from compas_igs2.utilities import compute_angle_deviations


__commandname__ = "IGS2_form_update_from_force"


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

    # Update the form diagram from the force diagram
    form_update_from_force = ui.proxy.function("compas_ags.ags.graphstatics.form_update_from_force")
    formdiagram, forcediagram = form_update_from_force(form.diagram, force.diagram)
    form.diagram.data = formdiagram.data
    force.diagram.data = forcediagram.data

    # Check equilibrium and deviations
    threshold = ui.registry["IGS2"]["max_deviation"]
    compute_angle_deviations(form.diagram, force.diagram, tol_force=threshold)
    if not check_equilibrium(form.diagram, force.diagram, tol_angle=threshold, tol_force=threshold):
        compas_rhino.display_message(
            "Error: Invalid movement on force diagram nodes or insuficient constraints in the form diagram."
        )
        max_dev = max(form.diagram.edges_attribute("a"))
        compas_rhino.display_message(
            "Diagrams are not parallel!\nMax. angle deviation: {0:.2g} deg\nThreshold assumed: {1:.2g} deg.".format(
                max_dev,
                threshold,
            )
        )

    # Update the scene and record.
    ui.scene.update()
    ui.record()


if __name__ == "__main__":
    RunCommand(True)
