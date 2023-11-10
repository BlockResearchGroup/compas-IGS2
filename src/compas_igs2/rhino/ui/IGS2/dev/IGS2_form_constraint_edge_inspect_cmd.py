from __future__ import print_function
from __future__ import absolute_import
from __future__ import division

import compas_rhino
from compas_ui.ui import UI


__commandname__ = "IGS2_form_constraint_edge_inspect"


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

    # Create an edge index map
    edge_index = form.diagram.edge_index()

    # Start an interaction loop
    while True:
        # Update the scene
        ui.scene.update()

        # Get an edge of the form diagram
        # and the corresponding edge of the force diagram.
        edge_form = form.select_edge("Select an edge of the Form Diagram to inspect constraints.")
        index = edge_index[edge_form]
        edge_force = list(force.diagram.ordered_edges(form.diagram))[index]

        # Find the corresponding target force (magnitude) and target vector.
        target_force = form.diagram.edge_attribute(edge_form, "target_force")
        target_vector = form.diagram.edge_attribute(edge_form, "target_vector")

        # Find the current edge force value.
        f = form.diagram.edge_attribute(edge_form, "f")

        # Set the tolerance
        tol = form.settings["tol.forces"]

        # Determine the state of the selected edge
        state = ""
        if not form.diagram.edge_attribute(edge_form, "is_external"):
            if f > +tol:
                state = "in tension"
            elif f < -tol:
                state = "in compression"

        # Define a non-directional form edge to guid map
        edge_guid = {form.guid_edge[guid]: guid for guid in form.guid_edge}
        edge_guid.update({(v, u): edge_guid[(u, v)] for u, v in edge_guid})

        # Mark the obj representing the form edge as selected.
        guid = edge_guid[edge_form]
        obj = compas_rhino.find_object(guid)
        obj.Select(True)

        # Define a non-directional force edge to guid map
        edge_guid = {force.guid_edge[guid]: guid for guid in force.guid_edge}
        edge_guid.update({(v, u): edge_guid[(u, v)] for u, v in edge_guid})

        # Mark the obj representing the force edge as selected
        # if the force mangnitude is above the threshold
        if abs(f) > tol:
            guid = edge_guid[edge_force]
            obj = compas_rhino.find_object(guid)
            obj.Select(True)

        # Notify the user
        compas_rhino.display_message(
            "Edge Index: {0}\nTarget Force assigned (kN): {1}\nTarget Vector Assigned: {2}\nCurrent Force Magnitude: {3:.3g}kN {4}".format(
                index, target_force, target_vector, abs(f), state
            )
        )

        # Ask if the user wnats to continue inspecting
        answer = compas_rhino.rs.GetString("Continue selecting edges?", "No", ["Yes", "No"])
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
