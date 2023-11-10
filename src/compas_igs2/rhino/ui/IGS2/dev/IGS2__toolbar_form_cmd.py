from __future__ import print_function
from __future__ import absolute_import
from __future__ import division

import compas_rhino

import IGS2_form_from_obj_cmd
import IGS2_form_from_lines_cmd
import IGS2_form_from_layer_cmd


__commandname__ = "IGS2__toolbar_form"


def RunCommand(is_interactive):
    options = ["FromObj", "FromLines", "FromLayer"]
    option = compas_rhino.rs.GetString("Create Form:", strings=options)

    if not option:
        return

    if option == "FromObj":
        IGS2_form_from_obj_cmd.RunCommand(True)

    elif option == "FromLines":
        IGS2_form_from_lines_cmd.RunCommand(True)

    elif option == "FromLayer":
        IGS2_form_from_layer_cmd.RunCommand(True)


if __name__ == "__main__":
    RunCommand(True)
