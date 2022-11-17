from __future__ import print_function
from __future__ import absolute_import
from __future__ import division

import compas_rhino
from compas_ui.ui import UI


__commandname__ = "IGS2_force_move_nodes"


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

    # fixed = list(form.diagram.vertices_where({'is_fixed': True}))
    # if len(fixed) < 2:
    #     answer = compas_rhino.rs.GetString("You only have {0} fixed vertices in the Form Diagram. Continue?".format(len(form.diagram.fixed())), "No", ["Yes", "No"])
    #     if not answer:
    #         return
    #     if answer == "No":
    #         return

    # proxy.package = 'compas_ags.ags.graphstatics'

    # form.settings['show.edgelabels'] = True
    # form.settings['show.forcelabels'] = False
    # force.settings['show.edgelabels'] = True

    # scene.update()

    # while True:
    #     vertices = force.select_vertices("Select vertices (Press ESC to exit)")
    #     if not vertices:
    #         break

    #     if force.move_vertices(vertices):
    #         scene.update()

    # if scene.settings['IGS']['autoupdate']:
    #     formdiagram, forcediagram = proxy.form_update_from_force(form.diagram, force.diagram)
    #     form.diagram.data = formdiagram.data
    #     force.diagram.data = forcediagram.data

    #     threshold = scene.settings['IGS']['max_deviation']
    #     compute_angle_deviations(form.diagram, force.diagram, tol_force=threshold)
    #     if not check_equilibrium(form.diagram, force.diagram, tol_angle=threshold, tol_force=threshold):
    #         compas_rhino.display_message('Error: Invalid movement on force diagram nodes or insuficient constraints in the form diagram.')
    #         max_dev = max(form.diagram.edges_attribute('a'))
    #         compas_rhino.display_message('Diagrams are not parallel!\nMax. angle deviation: {0:.2g} deg\nThreshold assumed: {1:.2g} deg.'.format(max_dev, threshold))

    # form.settings['show.edgelabels'] = False
    # form.settings['show.forcelabels'] = True
    # force.settings['show.edgelabels'] = False

    # Update the scene and record
    ui.scene.update()
    ui.record()


if __name__ == "__main__":
    RunCommand(True)
