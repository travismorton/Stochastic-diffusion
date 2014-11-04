import numpy, math, random
walkers, time, timeStep = 1000, 100, .1
steps = int(round(time / timeStep))
particles, eta = numpy.random.normal(-3, 1, walkers), numpy.random.normal(0, math.sqrt(timeStep), 1000000)
for i in range(steps):
    for j in range(walkers):
        particles[j] = particles[j] - particles[j] * timeStep + random.choice(eta)


