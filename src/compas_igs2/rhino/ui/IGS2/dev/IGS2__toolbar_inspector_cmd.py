from __future__ import print_function
from __future__ import absolute_import
from __future__ import division

import compas_rhino

import IGS2_edges_table_cmd
import IGS2_edge_information_cmd
import IGS2_form_inspector_control_cmd
import IGS2_form_constraint_edge_inspect_cmd
import IGS2_form_constraint_vertex_inspect_cmd
import IGS2_constraint_table_cmd


__commandname__ = "IGS2__toolbar_inspector"


def RunCommand(is_interactive):
    options = [
        "EdgesTable",
        "EdgeInformation",
        "ForcePolygons",
        "EdgeConstraints",
        "VertexConstraints",
        "ConstraintsTable",
    ]
    option = compas_rhino.rs.GetString("Select Inspection Mode:", strings=options)

    if not option:
        return

    if option == "EdgesTable":
        IGS2_edges_table_cmd.RunCommand(True)

    elif option == "EdgeInformation":
        IGS2_edge_information_cmd.RunCommand(True)

    elif option == "ForcePolygons":
        IGS2_form_inspector_control_cmd.RunCommand(True)

    elif option == "EdgeConstraints":
        IGS2_form_constraint_edge_inspect_cmd.RunCommand(True)

    elif option == "VertexConstraints":
        IGS2_form_constraint_vertex_inspect_cmd.RunCommand(True)

    elif option == "ConstraintsTable":
        IGS2_constraint_table_cmd.RunCommand(True)


if __name__ == "__main__":
    RunCommand(True)
