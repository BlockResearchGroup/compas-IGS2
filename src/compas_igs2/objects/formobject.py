from __future__ import print_function
from __future__ import absolute_import
from __future__ import division

from compas.colors import Color
from compas_igs2.objects import DiagramObject


class FormObject(DiagramObject):
    """Base object for representing a form diagram in the scene."""

    SETTINGS = {
        "layer": "formdiagram",
        "show.vertices": True,
        "show.edges": True,
        "show.vertexlabels": False,
        "show.edgelabels": False,
        "show.forcecolors": True,
        "show.forcelabels": True,
        "show.forcepipes": False,
        "show.constraints": True,
        "color.vertices": Color.black(),
        "color.vertexlabels": Color.white(),
        "color.vertices:is_fixed": Color.red(),
        "color.vertices:line_constraint": Color.white(),
        "color.edges": Color.black(),
        "color.edges:is_ind": Color.cyan(),
        "color.edges:is_external": Color.green(),
        "color.edges:is_reaction": Color.green(),
        "color.edges:is_load": Color.green(),
        "color.edges:target_force": Color.white(),
        "color.edges:target_vector": Color.white(),
        "color.faces": Color.grey().lightened(50),
        "color.compression": Color.blue(),
        "color.tension": Color.red(),
        "scale.forces": None,
        "tol.edges": 0.01,
        "tol.forces": 0.01,
    }

    def __init__(self, diagram, *args, **kwargs):
        super(FormObject, self).__init__(diagram, *args, **kwargs)
        self.settings.update(FormObject.SETTINGS)
        settings = kwargs.get("settings") or {}
        if settings:
            self.settings.update(settings)
