#!/usr/bin/python
import numpy
import math
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
from scipy.stats import norm

walkers = 1000000
time = 6.0
timeStep = .01
steps = int(round(time / timeStep))
particles = numpy.random.normal(-3, 1, walkers)
og = numpy.copy(particles)
for i in range(steps):
    particles[:] = particles[:] - particles[:] * timeStep + numpy.random.normal(0, math.sqrt(timeStep), walkers)

mu, sigma = norm.fit(particles)
print("mu = " + str(mu) + "\nsigma = " + str(sigma))

p1 = numpy.arange(min(particles), max(particles), 0.01)
plt.hist(og, 60, normed=1, facecolor='cyan', alpha=.6, label="Initial Distribution")
plt.hist(particles, 60, normed=1, facecolor='y', alpha=.6, label="Final Distribution")
plt.plot(p1, mlab.normpdf(p1, mu, sigma), 'purple', linewidth=2, label="Fit of Final")
plt.legend(loc=2)
plt.title("Stochastic Diffusion With Non-Constant Drift Velocity")
plt.xlabel("x")
plt.ylabel("Probability")
plt.figtext(0.75, 0.5, "$\mu = " + str(round(mu, 3)) + "$\n$\sigma = " + str(round(sigma, 3)) + "$", fontsize=12)

plt.show()
