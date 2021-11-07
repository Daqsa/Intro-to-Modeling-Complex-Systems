from pylab import *

"""
Implement two species competing for the same resource in differential equations
--> shares the carrying capacity.
"""
class CompetingSpeciesModel(object):
    """
    rx, ry : growth rate for each species
    K = carrying capacity
    x, y : species population, state variable
    result : time series of state variable
    timeSteps : list of time
    """
    def __init__(self, rx, ry, K, x0, y0, dt=0.01):
        self.rx = rx
        self.ry = ry
        self.K = K
        self.x = x0
        self.y = y0
        self.xresult = [self.x]
        self.yresult = [self.y]
        self.t = 0
        self.dt = dt
        self.timeSteps = [self.t]
    
    # store state variables in list
    def observe(self):
        self.xresult.append(self.x)
        self.yresult.append(self.y)
        self.timeSteps.append(self.t)
    
    # update state variable according to difference equation
    def update(self):
        carryingCapacityFactor = 1-(self.x+self.y)/self.K
        xderivative = self.rx * carryingCapacityFactor
        yderivative = self.ry * carryingCapacityFactor
        self.x += self.x * xderivative * self.dt
        self.y += self.y * yderivative * self.dt
        self.t += self.dt


if __name__ == "__main__":
    rx = 1.4
    ry = 1.1
    K = 10
    x0 = 5
    y0 = 9
    dt = 0.01
    myModel = CompetingSpeciesModel(rx, ry, K, x0, y0, dt=dt)
    timeSpan = 30
    while myModel.t < timeSpan:
        myModel.update()
        myModel.observe()
    xlabel("Time")
    ylabel("Population")
    plot(myModel.timeSteps, myModel.xresult, 'b-')
    plot(myModel.timeSteps, myModel.yresult, 'g--')
    # title("Phase Space")
    # plot(myModel.xresult, myModel.yresult)
    show()
