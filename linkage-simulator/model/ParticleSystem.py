
from typing import Sequence, List

from matplotlib.artist import Artist
from matplotlib.axes import Axes

# Adotped from: https://www.cs.cmu.edu/~baraff/sigcourse/
class Particle:
  def __init__(self, m=1, x=(0, 0), v=(0, 0), f=(0, 0)):
    self.m = m # mass
    self.x = x # position
    self.v = v # velocity
    self.f = f # force-accumulator
class ParticleSystem:
  def __init__(self, particles: List[Particle]):
    self.particles = particles # list of particles
    self.t = 0                 # simulation clock

    # self.state_tmp = [0] * 6 * len(self.particles)

  def draw(self, ax: Axes, cached: Sequence[Artist]) -> Sequence[Artist]:

    locs = [p.x for p in self.particles]

    if cached:
        cached[0].set_offsets(locs)
        return cached

    x, y = zip(*locs)
    nodes_plt = ax.scatter(x, y)

    return nodes_plt,