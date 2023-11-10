from __future__ import print_function
from __future__ import absolute_import
from __future__ import division

import Rhino
import compas_rhino
from compas_ui.ui import UI
from compas.geometry import Line


__commandname__ = "IGS2_form_constraint_vertex"


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

    # Define a dynamic draw function
    def OnDynamicDraw(sender, e):
        end = e.CurrentPoint
        e.Display.DrawDottedLine(start, end, color)

    # Select a vertex of the FormDiagram
    vertex = form.select_vertex("Select the vertex to constraint in the form diagram")
    if vertex is None:
        return

    # Define the start point of the line constraint
    start = compas_rhino.rs.GetPoint("Start of line constraint")
    if not start:
        return

    # Define the end point of the line constraint
    color = Rhino.ApplicationSettings.AppearanceSettings.FeedbackColor
    gp = Rhino.Input.Custom.GetPoint()
    gp.DynamicDraw += OnDynamicDraw
    gp.SetCommandPrompt("End of line constraint")
    gp.Get()
    if gp.CommandResult() != Rhino.Commands.Result.Success:
        return
    end = list(gp.Point())

    # Create a line object
    line = Line(start, end)

    # Add the line to the Form and ForceDiagram
    form.diagram.vertex_attribute(vertex, "line_constraint", line)
    force.diagram.constraints_from_dual()

    # Update the scene and record
    ui.scene.update()
    ui.record()


if __name__ == "__main__":
    RunCommand(True)
