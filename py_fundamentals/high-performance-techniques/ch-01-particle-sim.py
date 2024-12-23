from matplotlib import pyplot as plt
from matplotlib import animation
from random import uniform
import timeit


class Particle:
    """Stores the particle positions, x and y, and their angular velocity"""

    __slots__ = ('x', 'y', 'ang_vel')

    def __init__(self, x, y, ang_vel):
        self.x = x
        self.y = y
        self.ang_vel = ang_vel


class ParticleSimulator:

    def __init__(self, particles):
        self.particles = particles

    def evolve(self, dt):
        timestep = 0.00001
        nsteps = int(dt/timestep)

        for i in range(nsteps):
            for p in self.particles:
                # 1. calculate the direction
                norm = (p.x**2 + p.y**2)**0.5
                v_x = (-p.y)/norm
                v_y = p.x/norm
                # 2. calculate the displacement
                d_x = timestep * p.ang_vel * v_x
                d_y = timestep * p.ang_vel * v_y

                p.x += d_x
                p.y += d_y
                # 3. repeat for all the time steps


def visualize(simulator: ParticleSimulator):
    # plt.matplotlib.use('Qt5Agg')  # Or 'TkAgg' 
    plt.matplotlib.use('TkAgg') 

    X = [p.x for p in simulator.particles]
    Y = [p.y for p in simulator.particles]

    fig = plt.figure()
    ax = plt.subplot(111, aspect='equal')
    # Set up the axes and use the plot function to display the particles. plot takes a list of x and y coordinates.
    line, = ax.plot(X, Y, 'ro')

    # Axis limits
    plt.xlim(-1, 1)
    plt.ylim(-1, 1)

    # Write an initialization function, init, and a function, animate, that updates the 
    # x and y coordinates using the line.set_data method.

    # It will be run when the animation starts
    def init():
        
        line.set_data([], [])
        return line,

    def animate(i):
        # We let the particle evolve for 0.1 time units
        simulator.evolve(0.01)
        X = [p.x for p in simulator.particles]
        Y = [p.y for p in simulator.particles]

        line.set_data(X, Y)
        return line,

    # Create a FuncAnimation instance by passing the init and animate functions
    # plus the interval parameters, which specify the update interval, and blit,
    # which improves the update rate of the image.

    # Call the animate function each 10 ms
    anim = animation.FuncAnimation(fig,
                                   animate,
                                   init_func=init,
                                   blit=True,
                                   interval=10, cache_frame_data=False)
    plt.show()


def test_visualize():
    particles = [Particle(0.3, 0.5, +1),
                 Particle(0.0, -0.5, -1),
                 Particle(-0.1, -0.4, +3)]

    simulator = ParticleSimulator(particles)
    visualize(simulator)


def test_evolve():
    particles = [Particle(0.3,  0.5, +1),
                 Particle(0.0, -0.5, -1),
                 Particle(-0.1, -0.4, +3)]

    simulator = ParticleSimulator(particles)

    simulator.evolve(0.1)

    p0, p1, p2 = particles

    def fequal(a, b):
        return abs(a - b) < 1e-5

    assert fequal(p0.x, 0.2102698450356825)
    assert fequal(p0.y, 0.5438635787296997)

    assert fequal(p1.x, -0.0993347660567358)
    assert fequal(p1.y, -0.4900342888538049)

    assert fequal(p2.x,  0.1913585038252641)
    assert fequal(p2.y, -0.3652272210744360)


def benchmark():
    particles = [Particle(uniform(-1.0, 1.0),
                          uniform(-1.0, 1.0),
                          uniform(-1.0, 1.0))
                 for i in range(100)]

    simulator = ParticleSimulator(particles)
    simulator.evolve(0.1)


def timing():
    result = timeit.timeit('benchmark()',
                           setup='from __main__ import benchmark',
                           number=10)
    # Result is the time it takes to run the whole loop
    print(result)

    result = timeit.repeat('benchmark()',
                           setup='from __main__ import benchmark',
                           number=10,
                           repeat=3)
    # Result is a list of times
    print(result)


def benchmark_memory():
    particles = [Particle(uniform(-1.0, 1.0),
                          uniform(-1.0, 1.0),
                          uniform(-1.0, 1.0))
                 for i in range(100000)]

    simulator = ParticleSimulator(particles)
    simulator.evolve(0.001)


if __name__ == '__main__':
    benchmark()
