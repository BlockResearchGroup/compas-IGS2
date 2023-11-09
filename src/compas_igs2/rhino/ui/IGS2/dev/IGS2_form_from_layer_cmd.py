from __future__ import print_function
from __future__ import absolute_import
from __future__ import division

import compas_rhino

from compas_ui.ui import UI

from compas_ags.diagrams import FormGraph
from compas_ags.diagrams import FormDiagram


__commandname__ = "IGS2_form_from_layer"


@UI.error()
def RunCommand(is_interactive):
    ui = UI()

    # Ask the user to specify a layer.
    layer = compas_rhino.rs.GetString("Type the name of the layer containing the input lines for the FormDiagram.")
    if not layer:
        return

    # Get the lines on the layer.
    guids = compas_rhino.get_lines(layer=layer)
    if not guids:
        compas_rhino.display_message("The layer does not contain input lines.")
        return

    # Hide the selected lines.
    compas_rhino.rs.HideObjects(guids)

    # Get the pairs of points defining the lines.
    lines = compas_rhino.get_line_coordinates(guids)

    # Convert the point pairs to a graph.
    graph = FormGraph.from_lines(lines)

    # Inform the user if the input is not valid.
    if not graph.is_planar_embedding():
        compas_rhino.display_message("The graph is not planar. Therefore, a form diagram cannot be created.")
        return

    # Conver the graph to a form diagram.
    form = FormDiagram.from_graph(graph)

    # Inform the user that the seen is about to be cleared.
    # Ask the user to confirm.
    ui.scene.clear()

    # Add the form diagram to the scene.
    ui.scene.add(form, name="FormDiagram")
    ui.scene.update()
    ui.record()


if __name__ == "__main__":
    RunCommand(True)
