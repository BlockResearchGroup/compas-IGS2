from compas.plugins import plugin


@plugin(category="install", tryfirst=True)
def after_rhino_install(installed_packages):
    if "compas_ui" not in installed_packages:
        return []
    if "compas_cloud" not in installed_packages:
        return []
    if "compas_igs2" not in installed_packages:
        return []

    version = get_version_from_args()
    install(version)

    return [("compas_igs2", "Installed IGS2 UI", True)]


@plugin(category="install", tryfirst=True)
def installable_rhino_packages():
    return ["compas_igs2"]


if __name__ == "__main__":

    print("This installation procedure is deprecated.")
    print("Use `python -m compas_rhino.install` instead.")
