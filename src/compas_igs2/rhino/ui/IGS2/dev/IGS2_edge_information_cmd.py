from __future__ import print_function
from __future__ import absolute_import
from __future__ import division

import compas_rhino
from compas_ui.ui import UI


__commandname__ = "IGS2_edge_information"


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

    # scale = force.scale
    # form_settings = form.settings.copy()
    # force_settings = force.settings.copy()
    # form.settings['show.edges'] = True
    # form.settings['show.forcelabels'] = False
    # form.settings['show.edgelabels'] = False
    # form.settings['show.forcepipes'] = False
    # force.settings['show.edges'] = True
    # force.settings['show.forcelabels'] = False
    # force.settings['show.edgelabels'] = False
    # force.settings['show.constraints'] = False
    # scene.update()

    # curvefilter = compas_rhino.rs.filter.curve

    # edge_index = form.diagram.edge_index()

    # while True:
    #     guid = compas_rhino.rs.GetObject(message="Select an edge in Form or Force Diagrams", preselect=True, select=True, filter=curvefilter)

    #     if not guid:
    #         break
    #     elif guid not in form.guid_edge and guid not in force.guid_edge:
    #         compas_rhino.display_message("Edge does not belog to form or force diagram.")
    #         break

    #     if guid in form.guid_edge:
    #         edge_form = form.guid_edge[guid]
    #         index = edge_index[edge_form]
    #         edge_force = list(force.diagram.ordered_edges(form.diagram))[index]
    #     if guid in force.guid_edge:
    #         edge_force = force.guid_edge[guid]
    #         edge_form = force.diagram.dual_edge(edge_force)
    #         index = edge_index[edge_form]

    #     f = form.diagram.edge_attribute(edge_form, 'f')
    #     l = abs(f * scale) # noqa E741

    #     tol = form.settings['tol.forces']
    #     state = ''
    #     if not form.diagram.edge_attribute(edge_form, 'is_external'):
    #         if f > + tol:
    #             state = 'in tension'
    #         elif f < - tol:
    #             state = 'in compression'

    #     key2guid = {form.guid_edge[guid]: guid for guid in form.guid_edge}
    #     key2guid.update({(v, u): key2guid[(u, v)] for u, v in key2guid})
    #     find_object(key2guid[edge_form]).Select(True)
    #     key2guid = {force.guid_edge[guid]: guid for guid in force.guid_edge}
    #     key2guid.update({(v, u): key2guid[(u, v)] for u, v in key2guid})
    #     if abs(f) > tol:
    #         find_object(key2guid[edge_force]).Select(True)

    #     form.draw_highlight_edge(edge_form)
    #     force.draw_highlight_edge(edge_force)

    #     compas_rhino.display_message(
    #         "Edge Index: {0}\nForce Diagram Edge Length: {1:.3g}\nForce Drawing Scale: {2:.3g}\nForce Magnitude: {3:.3g}kN {4}".format(index, l, scale, abs(f), state))

    #     answer = compas_rhino.rs.GetString("Continue selecting edges?", "No", ["Yes", "No"])
    #     if not answer:
    #         break
    #     if answer == "No":
    #         break
    #     if answer == 'Yes':
    #         scene.update()

    # form.settings = form_settings
    # force.settings = force_settings

    # Update the scene and record
    ui.scene.update()
    ui.record()


if __name__ == "__main__":
    RunCommand(True)
