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

    guids = compas_rhino.select_lines(message="Select Form Diagram Lines")
    if not guids:
        return

    compas_rhino.rs.HideObjects(guids)

    lines = compas_rhino.get_line_coordinates(guids)
    graph = FormGraph.from_lines(lines)

    if not graph.is_planar_embedding():
        compas_rhino.display_message("The graph is not planar. Therefore, a form diagram cannot be created.")
        return

    form = FormDiagram.from_graph(graph)

    ui.scene.add(form, name="Form")
    ui.scene.update()
    ui.record()


if __name__ == "__main__":
    RunCommand(True)
