from __future__ import print_function
from __future__ import absolute_import
from __future__ import division

import os
import compas_rhino

from compas_ui.ui import UI
from compas_ui.rhino.forms import FileForm

from compas_ags.diagrams import FormGraph
from compas_ags.diagrams import FormDiagram


__commandname__ = "IGS2_form_from_obj"


@UI.error()
def RunCommand(is_interactive):
    ui = UI()

    # Get a starting directory for selecting files.
    if "IGS2_form_from_obj.dirname" in ui.registry:
        dirname = ui.registry["IGS2_form_from_obj.dirname"]
    else:
        dirname = ui.dirname

    # Ask the user to select an OBJ file.
    path = FileForm.open(dirname or os.path.expanduser("~"))
    if not path:
        return

    # Process the provided path.
    dirname = os.path.dirname(path)
    # basename = os.path.basename(path)
    _, ext = os.path.splitext(path)

    # Store the directory name for later.
    ui.registry["IGS2_form_from_obj.dirname"] = dirname

    # Notify the user if the input is not valid.
    if ext != ".obj":
        compas_rhino.display_message("")

    # Make a graph from the OBJ data.
    graph = FormGraph.from_obj(path)

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
