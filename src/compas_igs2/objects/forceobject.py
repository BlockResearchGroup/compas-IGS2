from __future__ import print_function
from __future__ import absolute_import
from __future__ import division

from compas.colors import Color
from compas_igs2.objects import DiagramObject


class ForceObject(DiagramObject):
    """Base object for representing a force diagram in a scene."""

    SETTINGS = {
        "layer": "forcediagram",
        "show.vertices": True,
        "show.edges": True,
        "show.vertexlabels": False,
        "show.edgelabels": False,
        "show.forcelabels": False,
        "show.forcecolors": True,
        "show.constraints": True,
        "color.vertices": Color.black(),
        "color.vertexlabels": Color.white(),
        "color.vertices:is_fixed": Color.red(),
        "color.vertices:line_constraint": Color.white(),
        "color.edges": Color.black(),
        "color.edges:is_ind": Color.cyan(),
        "color.edges:is_external": Color.green(),
        "color.edges:is_reaction": Color.black(),
        "color.edges:is_load": Color.green(),
        "color.edges:target_force": Color.white(),
        "color.edges:target_vector": Color.white(),
        "color.faces": Color.grey().lightened(50),
        "color.compression": Color.blue(),
        "color.tension": Color.red(),
        "rotate.90deg": False,
        "tol.forces": 1e-3,
    }

    def __init__(self, diagram, *args, **kwargs):
        super(ForceObject, self).__init__(diagram, *args, **kwargs)
        self.settings.update(ForceObject.SETTINGS)
        settings = kwargs.get("settings") or {}
        if settings:
            self.settings.update(settings)
