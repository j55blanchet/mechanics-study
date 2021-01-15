
from .Controller import *

from ..model import ParticleSystem


class ParticleSimController(Controller):
    
    def __init__(self, system: ParticleSystem):
        self.system = system

    def update(self):
        pass

    def draw(self, ax: matplotlib.axes.Axes, cached) -> List[matplotlib.artist.Artist]:
        return self.system.draw(ax, cached)