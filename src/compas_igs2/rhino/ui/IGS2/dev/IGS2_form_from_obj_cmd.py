from __future__ import print_function
from __future__ import absolute_import
from __future__ import division

import os
import compas_rhino

from compas_ui.ui import UI
from compas_ui.rhino.forms import FileForm

from compas_ags.diagrams import FormGraph
from compas_ags.diagrams import FormDiagram
from compas.datastructures import Mesh


__commandname__ = "IGS2_form_from_obj"


@UI.error()
def RunCommand(is_interactive):

    ui = UI()

    if "IGS2_form_from_obj.dirname" not in ui.registry:
        path = FileForm.open(ui.dirname or os.path.expanduser("~"))
        if not path:
            return
    else:
        dirname = ui.registry["IGS2_form_from_obj.dirname"]
        path = FileForm.open(dirname or os.path.expanduser("~"))
        if not path:
            return

    dirname = os.path.dirname(path)
    basename = os.path.basename(path)
    _, ext = os.path.splitext(path)

    ui.registry["IGS2_form_from_obj.dirname"] = dirname

    if ext == ".obj":
        mesh = Mesh.from_obj(path)
    elif ext == ".off":
        mesh = Mesh.from_off(path)
    elif ext == ".ply":
        mesh = Mesh.from_ply(path)
    elif ext == ".json":
        mesh = Mesh.from_json(path)
    else:
        raise NotImplementedError

    mesh.name = basename

    graph = FormGraph.from_obj()

    if not graph.is_planar_embedding():
        compas_rhino.display_message("The graph is not planar. Therefore, a form diagram cannot be created.")
        return

    form = FormDiagram.from_graph(graph)

    ui.scene.add(form, name="Form")
    ui.scene.update()
    ui.record()


if __name__ == "__main__":
    RunCommand(True)
