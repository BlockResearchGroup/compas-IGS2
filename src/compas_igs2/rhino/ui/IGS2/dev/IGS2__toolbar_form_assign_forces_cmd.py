from __future__ import print_function
from __future__ import absolute_import
from __future__ import division

import IGS2_form_select_ind_cmd
import IGS2_form_assign_forces_cmd


__commandname__ = "IGS2__toolbar_form_assign_forces"


def RunCommand(is_interactive):
    IGS2_form_select_ind_cmd.RunCommand(True)
    IGS2_form_assign_forces_cmd.RunCommand(True)


if __name__ == "__main__":
    RunCommand(True)
