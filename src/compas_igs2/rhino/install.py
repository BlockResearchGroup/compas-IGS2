import os
import sys
import json
from shutil import copyfile
from subprocess import call

import compas
from compas.plugins import plugin
import compas_rhino
from compas_rhino.install import install as install_packages
from compas_rhino.install import _filter_installable_packages
from compas_rhino.install_plugin import install_plugin
from compas_ui.rhino.install import check_folders
from compas_ui.rhino.install import install as install_ui


HERE = os.path.dirname(__file__)


@plugin(category="install", tryfirst=True)
def installable_rhino_packages():
    return ["compas_igs2"]


def install(plugin_name, plugin_path, rhino_version):
    if not os.path.isdir(plugin_path):
        raise Exception("Cannot find the plugin: {}".format(plugin_path))

    plugin_path = os.path.abspath(plugin_path)
    plugin_dev = os.path.join(plugin_path, "dev")
    plugin_config = os.path.join(plugin_dev, "config.json")

    with open(plugin_config, "r") as f:
        config = json.load(f)

    packages = []
    packages = _filter_installable_packages(rhino_version, packages)

    if "packages" in config:
        for name in config["packages"]:
            if name not in packages:
                packages.append(name)

    install_packages(version=rhino_version, packages=packages)
    install_plugin(plugin_path)

    if compas.WINDOWS:
        plugin_ruipy = os.path.join(plugin_dev, "rui.py")
        plugin_rui = "{}.rui".format(plugin_name)
        python_plugins_path = compas_rhino._get_rhino_pythonplugins_path(rhino_version)

        call(sys.executable + " " + plugin_ruipy, shell=True)
        copyfile(
            os.path.join(plugin_dev, plugin_rui),
            os.path.join(python_plugins_path, "..", "..", "UI", plugin_rui),
        )


def main(plugin_name, rhino_version):
    print("=" * 20, "Checking Folders", "=" * 20)
    if not check_folders(plugin_name, rhino_version):
        return

    plugin_path = os.path.join(HERE, "ui", plugin_name)

    print("=" * 20, "Running COMPAS UI Installation", "=" * 20)
    install_ui(rhino_version)

    print("=" * 20, "Running COMPAS IGS2 Installation", "=" * 20)
    install(plugin_name, plugin_path, rhino_version)

    print("=" * 20, "Installation Completed", "=" * 20)


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="COMPAS IGS2 installer command line utility.")
    parser.add_argument(
        "-v",
        "--version",
        choices=compas_rhino.SUPPORTED_VERSIONS,
        default=compas_rhino.DEFAULT_VERSION,
        help="The version of Rhino to install the packages in.",
    )
    args = parser.parse_args()

    main("IGS2", args.version)
