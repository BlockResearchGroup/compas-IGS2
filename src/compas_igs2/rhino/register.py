import os
from compas.plugins import plugin

from compas_ui.values import Settings
from compas_ui.values import BoolValue
from compas_ui.values import IntValue
from compas_ui.values import FloatValue

HERE = os.path.dirname(__file__)

SETTINGS = Settings(
    {
        "autoupdate": BoolValue(False),
        "bi-directional": BoolValue(False),
        "max_deviation": FloatValue(0.1),
    }
)


@plugin(category="ui")
def register(ui):

    plugin_name = "IGS2"
    plugin_path = os.path.join(HERE, "ui", plugin_name)
    if not os.path.isdir(plugin_path):
        raise Exception("Cannot find the plugin: {}".format(plugin_path))

    ui.registry["IGS2"] = SETTINGS
