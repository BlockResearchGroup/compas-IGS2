from __future__ import print_function
from __future__ import absolute_import
from __future__ import division

from compas.plugins import plugin

from compas_rhino.artists import RhinoArtist

from compas_ags.diagrams import FormDiagram
from compas_ags.diagrams import ForceDiagram

from .forceartist import RhinoForceArtist
from .formartist import RhinoFormArtist


@plugin(category="factories", requires=["Rhino"])
def register_artists():

    RhinoArtist.register(FormDiagram, RhinoFormArtist, context="Rhino")
    RhinoArtist.register(ForceDiagram, RhinoForceArtist, context="Rhino")

    print("IGS Rhino Artists registered.")
