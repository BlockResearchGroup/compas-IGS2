from __future__ import print_function
from __future__ import absolute_import
from __future__ import division

import compas_rhino
from compas_ui.ui import UI
from compas_igs2.utilities import check_equilibrium
from compas_igs2.utilities import compute_angle_deviations


__commandname__ = "IGS2_form_check_deviation"


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

    # Get the maximum deviation from the settings.
    threshold = ui.registry["IGS2"]["max_deviation"]

    # Compute the angle deviations.
    compute_angle_deviations(form.diagram, force.diagram, tol_force=threshold)

    # Check if angle deviations are below the threshold
    # and that constraints are not violated.
    check = check_equilibrium(form.diagram, force.diagram, tol_angle=threshold, tol_force=threshold)
    max_dev = max(form.diagram.edges_attribute("a"))

    if check:
        compas_rhino.display_message(
            "Diagrams are parallel!\nMax. angle deviation: {0:.2g} deg\nThreshold assumed: {1:.2g} deg.".format(
                max_dev, threshold
            )
        )
    else:
        compas_rhino.display_message(
            "Diagrams are not parallel!\nMax. angle deviation: {0:.2g} deg\nThreshold assumed: {1:.2g} deg.".format(
                max_dev, threshold
            )
        )


if __name__ == "__main__":
    RunCommand(True)
