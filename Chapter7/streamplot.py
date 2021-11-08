from pylab import *
import numpy as np

xvalues, yvalues = meshgrid(np.arange(0, 3, 0.1), np.arange(0, 3, 0.1))

xdot = xvalues - xvalues * yvalues
ydot = -yvalues + xvalues * yvalues

streamplot(xvalues, yvalues, xdot, ydot)
show()
