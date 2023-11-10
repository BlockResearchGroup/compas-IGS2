from __future__ import print_function
from __future__ import absolute_import
from __future__ import division

import webbrowser
from compas_ui.ui import UI


__commandname__ = "IGS2_docs"


@UI.error()
def RunCommand(is_interactive):
    ui = UI()  # noqa: F841

    webbrowser.open("https://blockresearchgroup.github.io/compas_ags/")


if __name__ == "__main__":
    RunCommand(True)
