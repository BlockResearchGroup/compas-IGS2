from __future__ import print_function
from __future__ import absolute_import
from __future__ import division

import compas_rhino

from compas_ui.ui import UI

from compas_ags.diagrams import FormGraph
from compas_ags.diagrams import FormDiagram


__commandname__ = "IGS2_form_from_lines"


@UI.error()
def RunCommand(is_interactive):

    ui = UI()

    # Select lines in the Rhino model view.
    guids = compas_rhino.select_lines(message="Select Form Diagram Lines")
    if not guids:
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

    for obj in ui.scene.objects:
        name = obj.name
        if name.startswith("FormDiagram"):
            if name == "FormDiagram":
                index = 1
            else:
                index = int(name.split(".")[-1]) + 1
            obj.name = "FormDiagram.{}".format(index)

    for obj in ui.scene.objects:
        name = obj.name
        if name.startswith("ForceDiagram"):
            if name == "ForceDiagram":
                index = 1
            else:
                index = int(name.split(".")[-1]) + 1
            obj.name = "ForceDiagram.{}".format(index)

    # Add the form diagram to the scene.
    ui.scene.add(form, name="FormDiagram")
    ui.scene.update()
    ui.record()


if __name__ == "__main__":
    RunCommand(True)
