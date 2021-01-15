
import random
import math

import numpy as np

from .controller import *
from .model import *
from .view import *

fps = 30
full_circle_time = 4

def test_pendulum():

    tri_system = ParticleSystem([
        Particle(x=(-1, 0)),
        Particle(x=(1, 0)),
        Particle(x=(0, 1.5))                             
    ])

    ctlr = ParticleSimController(tri_system)
    driver = Driver(ctlr)

    frames = np.linspace(0, 1, fps * full_circle_time)
    return driver, frames, True


# test = test_nullspace_projection
# test = testcase_2bar_ik
test = test_pendulum
print(test.__name__)
# test = testcase_constraint_dynamicnetwork
driver, frames, save_res = test()
anim = PlotAnimator(driver, frames=frames)
anim.run(fps=fps, show=True, save=False, filename=test.__name__, repeat=True)