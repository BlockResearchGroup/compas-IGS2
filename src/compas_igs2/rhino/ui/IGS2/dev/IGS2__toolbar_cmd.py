from __future__ import print_function
from __future__ import absolute_import
from __future__ import division

import os
from compas_ui.ui import UI
from compas_ui.rhino.forms import ToolbarForm


__commandname__ = "IGS2__toolbar"


HERE = os.path.dirname(__file__)


@UI.error()
def RunCommand(is_interactive):
    ui = UI()  # noqa: F841

    config = [
        {
            "command": "IGS2__toolbar_form",
            "icon": os.path.join(HERE, "assets", "IGS2_form.png"),
        },
        {"type": "separator"},
        {
            "command": "IGS2_form_select_fixed",
            "icon": os.path.join(HERE, "assets", "IGS2_form_select_fixed.png"),
        },
        {
            "command": "IGS2__toolbar_form_assign_forces",
            "icon": os.path.join(HERE, "assets", "IGS2_form_assign_forces.png"),
        },
        {
            "command": "IGS2_form_check_dof",
            "icon": os.path.join(HERE, "assets", "IGS2_form_check_dof.png"),
        },
        {"type": "separator"},
        {
            "command": "IGS2_force_from_form",
            "icon": os.path.join(HERE, "assets", "IGS2_force_from_form.png"),
        },
        {
            "command": "IGS2_form_move_nodes",
            "icon": os.path.join(HERE, "assets", "IGS2_form_move_nodes.png"),
        },
        {
            "command": "IGS2_force_update",
            "icon": os.path.join(HERE, "assets", "IGS2_force_update.png"),
        },
        {
            "command": "IGS2_force_move_nodes",
            "icon": os.path.join(HERE, "assets", "IGS2_force_move_nodes.png"),
        },
        {
            "command": "IGS2_form_update_from_force",
            "icon": os.path.join(HERE, "assets", "IGS2_form_update_from_force.png"),
        },
        {"type": "separator"},
        {
            "command": "IGS2_form_default_constraints",
            "icon": os.path.join(HERE, "assets", "IGS2_form_default_constraints.png"),
        },
        {
            "command": "IGS2__toolbar_form_constraints_vertex",
            "icon": os.path.join(HERE, "assets", "IGS2_form_constraints_vertex.png"),
        },
        {
            "command": "IGS2__toolbar_form_constraints_edge",
            "icon": os.path.join(HERE, "assets", "IGS2_form_constraints_edge.png"),
        },
        {
            "command": "IGS2_update_both",
            "icon": os.path.join(HERE, "assets", "IGS2_update_both.png"),
        },
        {"type": "separator"},
        {
            "command": "IGS2__toolbar_inspector",
            "icon": os.path.join(HERE, "assets", "IGS2_inspector.png"),
        },
        {
            "command": "IGS2_form_compute_loadpath",
            "icon": os.path.join(HERE, "assets", "IGS2_form_compute_loadpath.png"),
        },
        {
            "command": "IGS2_unified_diagram",
            "icon": os.path.join(HERE, "assets", "IGS2_unified_diagram.png"),
        },
    ]

    toolbar = ToolbarForm()
    toolbar.setup(config, HERE, title="IGS2")
    toolbar.Show()


if __name__ == "__main__":
    RunCommand(True)
