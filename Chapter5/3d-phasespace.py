from pylab import *
from mpl_toolkits.mplot3d import Axes3D

class ThreeDimModel(object):
    """
    x, y : initial state variable
    result : time series of state variable
    timeSteps : list of time
    """
    def __init__(self, x0, y0, z0):
        self.x = x0
        self.y = y0
        self.z = z0
        self.xresult = [self.x]
        self.yresult = [self.y]
        self.zresult = [self.z]
        self.t = 0
        self.timeSteps = [self.t]
    
    # store state variables in list
    def observe(self):
        self.xresult.append(self.x)
        self.yresult.append(self.y)
        self.zresult.append(self.z)
        self.timeSteps.append(self.t)

    # update state variable according to difference equation
    def update(self):
        nextx = 0.5 * self.x + self.y
        nexty = -0.5 * self.x + self.y
        nextz = -self.x - self.y + self.z
        self.x, self.y, self.z = nextx, nexty, nextz
        self.t += 1

""" 
Visualize all phase spaces for a given range of initial values
"""
if __name__ == "__main__":
    timeSpan = 30
    # Phase space!
    ax = gca(projection='3d') 
    for x0 in range(-2, 2):
        for y0 in range(-2, 2):
            for z0 in range(-2, 2):
                myModel = ThreeDimModel(x0, y0, z0)
                while myModel.t < timeSpan:
                    myModel.update()
                    myModel.observe()
                ax.plot(myModel.xresult, myModel.yresult, myModel.zresult, 'b')
    show()
