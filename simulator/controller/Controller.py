from abc import ABC, abstractmethod, abstractproperty
from typing import List

import numpy as np
import matplotlib.artist
import matplotlib.axes

from ..model import *

class Controller(ABC):

    @abstractmethod
    def update(self):
        pass

    # @abstractmethod
    # def meets_target(self, linkage: Linkage, target: np.array) -> bool:
    #     pass

    def draw(self, ax: matplotlib.axes.Axes, cached) -> List[matplotlib.artist.Artist]:
        return []