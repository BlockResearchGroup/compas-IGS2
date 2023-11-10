from __future__ import print_function
from __future__ import absolute_import
from __future__ import division

import Rhino
import compas_rhino
from compas_ui.ui import UI
from compas.geometry import Line


__commandname__ = "IGS2_force_constraint_vertex"


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

    # Define dynamic draw callback
    def OnDynamicDraw(sender, e):
        end = e.CurrentPoint
        e.Display.DrawDottedLine(start, end, color)

    # Start interactive loop
    while True:
        # Ask for a vertex to constrain
        # and break out of loop if non provided
        vertex = force.select_vertex("Select the vertex to constraint in the force diagram")
        if not vertex:
            break

        # Ask for a start point
        # and break out of loop if non provided
        start = compas_rhino.rs.GetPoint("Start of line constraint")
        if not start:
            break

        # Ask for an end point
        # and use the dynamic draw to viz the line
        color = Rhino.ApplicationSettings.AppearanceSettings.FeedbackColor
        gp = Rhino.Input.Custom.GetPoint()
        gp.DynamicDraw += OnDynamicDraw
        gp.SetCommandPrompt("End of line constraint")
        gp.Get()
        if gp.CommandResult() != Rhino.Commands.Result.Success:
            return
        end = list(gp.Point())

        # Convert to a line and store on the vertex
        line = Line(start, end)
        force.diagram.vertex_attribute(vertex, "line_constraint", line)

        # Update the scene
        ui.scene.update()

        # Ask to continue
        answer = compas_rhino.rs.GetString(
            "Continue selecting vertices?",
            "No",
            ["Yes", "No"],
        )
        if not answer:
            break
        if answer == "No":
            break

    # Update the scene and record
    ui.scene.update()
    ui.record()


if __name__ == "__main__":
    RunCommand(True)
