from __future__ import print_function
from __future__ import absolute_import
from __future__ import division

from compas.colors import Color
from compas_ui.values import Settings
from compas_ui.values import StrValue
from compas_ui.values import BoolValue
from compas_ui.values import ColorValue
from compas_ui.values import FloatValue
from compas_igs2.objects import DiagramObject


class FormObject(DiagramObject):
    """Base object for representing a form diagram in the scene."""

    SETTINGS = Settings(
        {
            "layer": StrValue("formdiagram"),
            "show.vertices": BoolValue(True),
            "show.edges": BoolValue(True),
            "show.vertexlabels": BoolValue(False),
            "show.edgelabels": BoolValue(False),
            "show.forcecolors": BoolValue(True),
            "show.forcelabels": BoolValue(True),
            "show.forcepipes": BoolValue(False),
            "show.constraints": BoolValue(True),
            "color.vertices": ColorValue(Color.black()),
            "color.vertexlabels": ColorValue(Color.white()),
            "color.vertices:is_fixed": ColorValue(Color.red()),
            "color.vertices:line_constraint": ColorValue(Color.white()),
            "color.edges": ColorValue(Color.black()),
            "color.edges:is_ind": ColorValue(Color.cyan()),
            "color.edges:is_external": ColorValue(Color.green()),
            "color.edges:is_reaction": ColorValue(Color.green()),
            "color.edges:is_load": ColorValue(Color.green()),
            "color.edges:target_force": ColorValue(Color.white()),
            "color.edges:target_vector": ColorValue(Color.white()),
            "color.faces": ColorValue(Color.grey().lightened(50)),
            "color.compression": ColorValue(Color.blue()),
            "color.tension": ColorValue(Color.red()),
            "scale.forces": FloatValue(1.0),
            "tol.edges": FloatValue(0.01),
            "tol.forces": FloatValue(0.01),
        }
    )
