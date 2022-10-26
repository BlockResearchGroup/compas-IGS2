import os

from compas_ags.diagrams import FormGraph
from compas_ags.diagrams import FormDiagram
from compas_ags.diagrams import ForceDiagram

from compas.artists import Artist
from compas_cloud import Proxy

p = Proxy()

form_update_q_from_qind = p.function(
    "compas_ags.ags.graphstatics.form_update_q_from_qind"
)
force_update_from_form = p.function(
    "compas_ags.ags.graphstatics.force_update_from_form"
)

# ------------------------------------------------------------------------------
# 1. get lines of a plane triangle frame in equilibrium, its applied loads and reaction forces
#    make form and force diagrams
# ------------------------------------------------------------------------------

graph = FormGraph.from_obj(
    os.path.join(os.path.dirname(__file__), "../data/gs_form_force.obj")
)

form = FormDiagram.from_graph(graph)
force = ForceDiagram.from_formdiagram(form)

# ------------------------------------------------------------------------------
# 2. set applied load
# ------------------------------------------------------------------------------

# choose an independent edge and set the magnitude of the applied load
# the system is statically determinate, thus choosing one edge is enough
form.edge_force(0, -30.0)

# update force densities of form and force diagrams
form = form_update_q_from_qind(form)
force = force_update_from_form(force, form)

# ------------------------------------------------------------------------------
# 3. display force and form diagrams
# ------------------------------------------------------------------------------

artist = Artist(form, layer="AGS::FormDiagram")
artist.clear_layer()
artist.draw_vertices()
artist.draw_edges()
artist.draw_vertexlabels()
artist.draw_edgelabels()

artist = Artist(force, layer="AGS::ForceDiagram")
artist.clear_layer()
artist.draw_vertices()
artist.draw_edges()
artist.draw_vertexlabels()
artist.draw_edgelabels()
