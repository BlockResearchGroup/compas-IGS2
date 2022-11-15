from __future__ import print_function
from __future__ import absolute_import
from __future__ import division

import compas_rhino

from compas_ui.ui import UI

from compas_ags.diagrams import FormDiagram
from compas_ags.diagrams import ForceDiagram


__commandname__ = "IGS2_force_from_form"


@UI.error()
def RunCommand(is_interactive):

    ui = UI()

    # Get the FormDiagram from the scene
    objects = ui.scene.get("FormDiagram")
    if not objects:
        compas_rhino.display_message("There is no FormDiagram in the scene.")
        return
    form = objects[0]

    # Identify the independent edges.
    edges = list(form.diagram.edges_where(is_ind=True))

    # Inform the user if there are no independent edges.
    if not len(edges):
        compas_rhino.display_message(
            """You have not yet assigned force values to the form diagram.
            Please assign forces first."""
        )
        return

    # Create a proxy for compas_ags.ags.graphstatics.form_count_dof
    form_count_dof = ui.proxy.function("compas_ags.ags.graphstatics.form_count_dof")

    # Run compas_ags.ags.graphstatics.form_update_q_from_qind in the cloud.
    dof = form_count_dof(form.diagram)

    # Let the user know if the execution failed.
    if not dof:
        compas_rhino.display_message("Cloud execution of 'compas_ags.ags.graphstatics.form_count_dof' failed.")
        return

    # Let the user know if the number of independent edges is not equal to the dof of the system.
    if dof[0] != len(edges):
        compas_rhino.display_message(
            """You have not assigned the correct number of force values.
            Please, check the degrees of freedom of the form diagram and update the assigned forces accordingly."""
        )
        return

    # Get the ForceDiagram from the scene
    # and remove it.
    for obj in ui.scene.get("ForceDiagram"):
        ui.scene.remove(obj)

    # Create a (new) ForceDiagram and add it.
    forcediagram = ForceDiagram.from_formdiagram(form.diagram)
    force = ui.scene.add(forcediagram, name="ForceDiagram")

    # formdiagram = proxy.form_update_q_from_qind(form.diagram)
    # form.diagram.data = formdiagram.data

    # forcediagram = proxy.force_update_from_form(force.diagram, form.diagram)
    # force.diagram.data = forcediagram.data

    # force.scale = compute_force_drawingscale(form, force)

    # # compute and store the ideal location for the diagram at 0 and 90 degrees
    # force.rotation = [0, 0, +math.pi/2]
    # location_90deg = compute_force_drawinglocation(form, force).copy()

    # force.rotation = [0, 0, 0]
    # location_0deg = compute_force_drawinglocation(form, force).copy()

    # force.settings['_location_0deg'] = location_0deg
    # force.settings['_location_90deg'] = location_90deg

    # form.settings['scale.forces'] = compute_form_forcescale(form)

    # Update the scene.
    ui.scene.update()
    ui.record()


if __name__ == "__main__":
    RunCommand(True)
