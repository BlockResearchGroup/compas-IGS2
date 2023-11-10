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

    # Update viz settings
    form_settings = {k: form.settings.get(k) for k in form.settings.keys()}
    force_settings = {k: force.settings.get(k) for k in force.settings.keys()}
    form.settings["show.edges"] = True
    form.settings["show.forcelabels"] = False
    form.settings["show.edgelabels"] = False
    form.settings["show.forcepipes"] = False
    force.settings["show.edges"] = True
    force.settings["show.forcelabels"] = False
    force.settings["show.edgelabels"] = False
    force.settings["show.constraints"] = False

    # Create edge index map
    edge_index = form.diagram.edge_index()

    # Start interactive loop
    while True:
        ui.scene.update()

        # Ask to select an edge and break out of the loop if nothing is selected
        guid = compas_rhino.rs.GetObject(
            message="Select an edge in Form or Force Diagrams",
            preselect=True,
            select=True,
            filter=compas_rhino.rs.filter.curve,
        )
        if not guid:
            break

        # Break out of the loop if the selected object is not an edge
        if guid not in form.guid_edge and guid not in force.guid_edge:
            compas_rhino.display_message("Edge does not belog to form or force diagram.")
            break

        # Find the edge in the form diagram
        if guid in form.guid_edge:
            edge_form = form.guid_edge[guid]
            index = edge_index[edge_form]
            edge_force = list(force.diagram.ordered_edges(form.diagram))[index]

        # Find the edge in the force diagram
        if guid in force.guid_edge:
            edge_force = force.guid_edge[guid]
            edge_form = force.diagram.dual_edge(edge_force)
            index = edge_index[edge_form]

        # Force and length
        F = form.diagram.edge_attribute(edge_form, "f")
        L = abs(F * force.scale)

        # Tension or compression?
        tol = form.settings["tol.forces"]
        state = ""
        if not form.diagram.edge_attribute(edge_form, "is_external"):
            if F > +tol:
                state = "in tension"
            elif F < -tol:
                state = "in compression"

        # Mark form edge as selected
        edge_guid = {form.guid_edge[guid]: guid for guid in form.guid_edge}
        edge_guid.update({(v, u): edge_guid[(u, v)] for u, v in edge_guid})
        compas_rhino.find_object(edge_guid[edge_form]).Select(True)

        # Mark force edge as selected
        edge_guid = {force.guid_edge[guid]: guid for guid in force.guid_edge}
        edge_guid.update({(v, u): edge_guid[(u, v)] for u, v in edge_guid})
        if abs(F) > tol:
            compas_rhino.find_object(edge_guid[edge_force]).Select(True)

        # Highlight edges
        form.draw_highlight_edge(edge_form)
        force.draw_highlight_edge(edge_force)

        # Inform the user
        compas_rhino.display_message(
            "Edge Index: {0}\nForce Diagram Edge Length: {1:.3g}\nForce Drawing Scale: {2:.3g}\nForce Magnitude: {3:.3g}kN {4}".format(
                index,
                L,
                force.scale,
                abs(F),
                state,
            )
        )

        # Ask to continue
        answer = compas_rhino.rs.GetString("Continue selecting edges?", "No", ["Yes", "No"])
        if not answer:
            break
        if answer == "No":
            break

    # Revert to original setting
    for key, value in form_settings.items():
        form.settings[key] = value
    for key, value in force_settings.items():
        force.settings[key] = value

    # Update the scene and record
    ui.scene.update()
    ui.record()


if __name__ == "__main__":
    RunCommand(True)
