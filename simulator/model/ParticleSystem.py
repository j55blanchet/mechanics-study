
from typing import Sequence, List

from matplotlib.artist import Artist
from matplotlib.axes import Axes

import numpy as np

# Adopted from: https://www.cs.cmu.edu/~baraff/sigcourse/
class Particle:
  def __init__(self, m=1, x=(0, 0), v=(0, 0), f=(0, 0)):
    self.m = m # mass
    self.x = x # position
    self.v = v # velocity

  def state_vector(self) -> np.array:
    return np.array([
      self.x[0],
      self.x[1],
      self.v[0],
      self.v[1]
    ])

class ParticleSystem:
  def __init__(self, particles: List[Particle], dimension=2):

    self.dimension = 2
    self.n = len(particles)

    # Flatmap of [x, y, z, vx, vy, vz] for each particle
    self.phase = np.array([
      x for p in particles for x in p.state_vector()
    ])

    self.masses = np.array([
      p.m for p in particles
    ])
    
    # Force accumulator
    self.forces = np.zeros(self.n * self.dimension)
    self.t = 0

    self.force_objects = []

  ################
  ## Simulation ##
  ################

  def euler_step(self, dt: float):
    phase_deriv = np.array([x for i in range(self.n) for x in self.particle_phase_deriv(i)])
    phase_deriv *= dt
    self.phase += phase_deriv
    self.t += dt
    

  ############
  ## FORCES ##
  ############

  def clear_forces(self):
    self.forces = np.zeros(self.n * self.dimension)

  def compute_forces(self):
    pass

  ######################
  ## HELPER FUNCTIONS ##
  ######################

  def state_i(self, particle_i: int) -> int:
    """Get the starting index of the state vector for the given particle

    Args:
        particle_i (int): Index of the particle to get the state index for

    Returns:
        int: Starting index of the particle's state vector (the particle's x position)
    """
    return particle_i * 2 * self.dimension

  def particle_x(self, particle_i: int) -> np.array:
    """Get the position vector of the given particle
    Args:
        particle_i (int): Particle to get the position vector for
    Returns:
        np.array: The position vector
    """
    i = self.state_i(particle_i)
    return self.phase[i: i+self.dimension]

  def particle_v(self, particle_i: int) -> np.array:
    """Get the velocity vector of the given particle
    Args:
        particle_i (int): Particle to get the velocity vector of
    Returns:
        np.array: The velocity vector
    """
    i = self.state_i(particle_i)
    return self.phase[i+self.dimension, i+2*self.dimension]

  def particle_a(self, particle_i: int) -> np.array:
    """Compute the instantenous acceleration of the particle

    Args:
        particle_i (int): Particle to calculate the acceleration for

    Returns:
        np.array: The calculated acceleration vector
    """
    i = particle_i * self.dimension
    f = self.forces[i: i+self.dimension]
    return f / self.masses[i]

  def particle_phase_deriv(self, particle_i: int) -> np.array:
    return np.array((
      *self.system.particle_v(particle_i), # Deriv of position: velocity
      *self.system.particle_a(particle_i)  # Deriv of velocity: acceleration
    ))

  def draw(self, ax: Axes, cached: Sequence[Artist]) -> Sequence[Artist]:
    """Draw the particle system to a figure, reusing the cached artist if given
    Args:
        ax (Axes): Figure axis to draw the particle system on
        cached (Sequence[Artist]): Cached artists to use
    Returns:
        Sequence[Artist]: Artists that have been drawn
    """
    locs = [
      self.particle_x(i) for i in range(self.n)
    ]

    if cached:
        cached[0].set_offsets(locs)
        return cached

    x, y = zip(*locs)
    nodes_plt = ax.scatter(x, y)

    return nodes_plt,