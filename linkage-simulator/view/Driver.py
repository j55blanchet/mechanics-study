from matplotlib.lines import Line2D
from typing import Tuple

from ..model import *
from ..controller import *

class Driver:
    def __init__(self, controller: Controller) -> None:
        self.controller = controller
        self.artists_controller = None
        self.pframe = 0

    def get_plot_size(self) -> Tuple[float, float, float, float]:
        return (-5, 5, -5, 5)

    def update(self, frame: float):
        dframe = frame - self.pframe
        self.controller.update()
        self.pframe = frame
        print(f"Frame: {frame}")
        
    def plot(self, ax) -> Tuple[Line2D]:
       
        self.artists_controller = self.controller.draw(ax, self.artists_controller)
        return self.artists_controller

    def button_clicked(self, x, y):
        print(f"Button Click: {x}, {y}")
        # self.target_provider.button_clicked(x, y)

    