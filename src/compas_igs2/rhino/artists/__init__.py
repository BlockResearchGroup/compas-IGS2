from __future__ import print_function
from __future__ import absolute_import
from __future__ import division

from compas.plugins import plugin

from compas.artists import Artist

from compas_ags.diagrams import FormDiagram
from compas_ags.diagrams import ForceDiagram

from .diagramartist import RhinoDiagramArtist  # noqa: F401
from .forceartist import RhinoForceArtist
from .formartist import RhinoFormArtist


@plugin(category="factories", requires=["Rhino"])
def register_artists():
    Artist.register(FormDiagram, RhinoFormArtist, context="Rhino")
    Artist.register(ForceDiagram, RhinoForceArtist, context="Rhino")

    print("IGS Rhino Artists registered.")
