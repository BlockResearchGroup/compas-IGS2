from __future__ import print_function
from __future__ import absolute_import
from __future__ import division

import compas_rhino

import IGS2_form_constraint_vertex_cmd
import IGS2_force_constraint_vertex_cmd


__commandname__ = "IGS2__toolbar_form_constraints_vertex"


def RunCommand(is_interactive):
    options = ["FormDiagram", "ForceDiagram"]
    option = compas_rhino.rs.GetString("Constraint Vertex in the:", strings=options)

    if not option:
        return

    if option == "FormDiagram":
        IGS2_form_constraint_vertex_cmd.RunCommand(True)

    elif option == "ForceDiagram":
        IGS2_force_constraint_vertex_cmd.RunCommand(True)


if __name__ == "__main__":
    RunCommand(True)
