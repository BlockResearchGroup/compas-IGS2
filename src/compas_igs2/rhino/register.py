import os
import json
from compas.plugins import plugin

# from compas_ui.ui import UI


HERE = os.path.dirname(__file__)


@plugin(category="ui")
def register(ui):

    plugin_name = "IGS2"
    plugin_path = os.path.join(HERE, "ui", plugin_name)
    if not os.path.isdir(plugin_path):
        raise Exception("Cannot find the plugin: {}".format(plugin_path))

    plugin_path = os.path.abspath(plugin_path)
    plugin_dev = os.path.join(plugin_path, "dev")
    plugin_config = os.path.join(plugin_dev, "config.json")

    with open(plugin_config, "r") as f:
        config = json.load(f)
        settings = config["settings"]
        ui.registry["IGS2"] = settings
