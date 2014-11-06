import numpy
import math
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
from scipy.stats import norm

walkers = 100000
time = 10
timeStep = .01
steps = int(round(time / timeStep))
particles = numpy.random.normal(-3, 1, walkers)
og = numpy.copy(particles)
for i in range(steps):
    particles[:] = particles[:] - particles[:] * timeStep + numpy.random.normal(0, math.sqrt(timeStep), walkers)

mu, sigma = norm.fit(particles)
print("mu = " + str(mu) + "\nsigma = " + str(sigma))

p1 = numpy.arange(min(particles), max(particles), 0.01)
plt.plot(p1, mlab.normpdf(p1, mu, sigma), 'r-', linewidth=3)
plt.hist(og, 100, normed=1, facecolor='cyan', alpha=.6)
plt.hist(particles, 100, normed=1, facecolor='purple', alpha=.6)
plt.show()
