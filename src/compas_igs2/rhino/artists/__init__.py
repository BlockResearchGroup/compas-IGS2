from __future__ import print_function
from __future__ import absolute_import
from __future__ import division

from compas.plugins import plugin
from compas_rhino.artists import RhinoArtist

from compas_ags.diagrams import FormDiagram  # noqa: F401
from compas_ags.diagrams import ForceDiagram  # noqa: F401

from compas_rhino.artists import RhinoArtist

from .diagramartist import RhinoDiagramArtist
from .forceartist import RhinoForceArtist
from .formartist import RhinoFormArtist


@plugin(category="factories", requires=["Rhino"])
def register_artists():

    RhinoArtist.register(ForceDiagram, RhinoForceArtist, context="Rhino")
    RhinoArtist.register(FormConstraint, RhinoFormArtist, context="Rhino")

    print("IGS Rhino Artists registered.")


__all__ = [
    "RhinoDiagramArtist",
    "RhinoForceArtist",
    "RhinoFormArtist",
]
