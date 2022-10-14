from __future__ import print_function
from __future__ import absolute_import
from __future__ import division

from compas.plugins import plugin

from compas_ags.diagrams import FormDiagram  # noqa: F401
from compas_ags.diagrams import ForceDiagram  # noqa: F401

from compas_ui.rhino.objects import RhinoObject

from .diagramobject import RhinoDiagramObject  # noqa: F401
from .formobject import RhinoFormObject  # noqa: F401
from .forceobject import RhinoForceObject  # noqa: F401


@plugin(category="ui", requires=["Rhino"])
def register_objects():

    RhinoObject.register(FormDiagram, RhinoFormObject, context="Rhino")
    RhinoObject.register(ForceDiagram, RhinoForceObject, context="Rhino")

    print("IGS Rhino Objects registered.")


__all__ = [
    "DiagramObject",
    "RhinoForceObject",
    "RhinoFormObject"
]
