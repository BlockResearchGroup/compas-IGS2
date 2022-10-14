from __future__ import print_function
from __future__ import absolute_import
from __future__ import division

from abc import abstractmethod

from compas_igs2.artists import DiagramArtist


class FormArtist(DiagramArtist):

    def __init__(self, *args, **kwargs):
        super(FormArtist, self).__init__(*args, **kwargs)
