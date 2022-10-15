from __future__ import print_function
from __future__ import absolute_import
from __future__ import division

from compas_igs2.objects import DiagramObject


class ForceObject(DiagramObject):
    """Base object for representing a force diagram in a scene."""
    SETTINGS = {
        'layer': "forcediagram",

        'show.vertices': True,
        'show.edges': True,
        'show.vertexlabels': False,
        'show.edgelabels': False,
        'show.forcelabels': False,
        'show.forcecolors': True,
        'show.constraints': True,

        'color.vertices': (0, 0, 0),
        'color.vertexlabels': (255, 255, 255),
        'color.vertices:is_fixed': (255, 0, 0),
        'color.vertices:line_constraint': (255, 255, 255),
        'color.edges': (0, 0, 0),
        'color.edges:is_ind': (0, 255, 255),
        'color.edges:is_external': (0, 255, 0),
        'color.edges:is_reaction': (0, 0, 0),
        'color.edges:is_load': (0, 255, 0),
        'color.edges:target_force': (255, 255, 255),
        'color.edges:target_vector': (255, 255, 255),
        'color.faces': (210, 210, 210),
        'color.compression': (0, 0, 255),
        'color.tension': (255, 0, 0),

        'rotate.90deg': False,

        'tol.forces': 1e-3,
    }

    def __init__(self, diagram, *args, **kwargs):
        super(ForceObject, self).__init__(diagram, *args, **kwargs)
        self.settings.update(ForceObject.SETTINGS)
        settings = kwargs.get('settings') or {}
        if settings:
            self.settings.update(settings)

