from pylab import *
import numpy as np
import math

"""
omega = theta'
omega' = -g/L * sin (theta)

"""
g = 9.8
L = 9.8

thetavalues, omegavalues = meshgrid(np.arange(-5, 5, 0.01), np.arange(-5, 5, 0.01))

f = lambda x: -g/L * math.sin(x)
f2 = np.vectorize(f)

thetadot = omegavalues
omegadot = f2(thetavalues) 

streamplot(thetavalues, omegavalues, thetadot, omegadot)
show()
