from __future__ import print_function
from __future__ import absolute_import
from __future__ import division

import compas_rhino

import IGS2_form_constraint_edge_force_cmd
import IGS2_form_constraint_edge_orientation_cmd


__commandname__ = "IGS2__toolbar_form_constraints_edge"


def RunCommand(is_interactive):
    options = ["ForceMagnitude", "Orientation"]
    option = compas_rhino.rs.GetString("Constraint Edge:", strings=options)

    if not option:
        return

    if option == "ForceMagnitude":
        IGS2_form_constraint_edge_force_cmd.RunCommand(True)

    elif option == "Orientation":
        IGS2_form_constraint_edge_orientation_cmd.RunCommand(True)


if __name__ == "__main__":
    RunCommand(True)
