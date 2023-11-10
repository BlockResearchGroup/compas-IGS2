"""
********************************************************************************
compas_igs2
********************************************************************************

.. currentmodule:: compas_igs2


.. toctree::
    :maxdepth: 1


"""

from __future__ import print_function

import os


__author__ = ["Tom Van Mele, Juney Lee, Li Chen"]
__copyright__ = ""
__license__ = "MIT License"
__email__ = "van.mele@arch.ethz.ch, juney.lee@som.com, li.chen@arch.ethz.ch"
__version__ = "0.2.1"


HERE = os.path.dirname(__file__)

HOME = os.path.abspath(os.path.join(HERE, "../../"))
DATA = os.path.abspath(os.path.join(HOME, "data"))
DOCS = os.path.abspath(os.path.join(HOME, "docs"))
TEMP = os.path.abspath(os.path.join(HOME, "temp"))


__all__ = ["HOME", "DATA", "DOCS", "TEMP"]

__all_plugins__ = [
    "compas_igs2.rhino.install",
    "compas_igs2.rhino.artists",
    "compas_igs2.rhino.objects",
    "compas_igs2.rhino.register",
]
