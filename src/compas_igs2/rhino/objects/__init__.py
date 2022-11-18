from __future__ import print_function
from __future__ import absolute_import
from __future__ import division

from compas.plugins import plugin

from compas_ags.diagrams import Diagram
from compas_ags.diagrams import FormDiagram
from compas_ags.diagrams import ForceDiagram

from compas_ui.rhino.objects import RhinoObject

from .diagramobject import RhinoDiagramObject
from .formobject import RhinoFormObject
from .forceobject import RhinoForceObject


@plugin(category="ui", requires=["Rhino"])
def register_objects():
    RhinoObject.register(Diagram, RhinoDiagramObject, context="Rhino")
    RhinoObject.register(FormDiagram, RhinoFormObject, context="Rhino")
    RhinoObject.register(ForceDiagram, RhinoForceObject, context="Rhino")
    print("IGS Rhino Objects registered.")


__all__ = [
    "RhinoDiagramObject",
    "RhinoForceObject",
    "RhinoFormObject",
]
