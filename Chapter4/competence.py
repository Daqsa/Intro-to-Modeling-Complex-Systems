from pylab import *

"""
Implement two species competing for the same resource
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
    def __init__(self, rx, ry, K, x0, y0):
        self.rx = rx
        self.ry = ry
        self.K = K
        self.x = x0
        self.y = y0
        self.xresult = [self.x]
        self.yresult = [self.y]
        self.t = 0
        self.timeSteps = [self.t]
    
    # store state variables in list
    def observe(self):
        self.xresult.append(self.x)
        self.yresult.append(self.y)
        self.timeSteps.append(self.t)
    
    # update state variable according to difference equation
    def update(self):
        carryingCapacityFactor = 1-(self.x+self.y)/self.K
        xgrowthRate = 1 + self.rx * carryingCapacityFactor
        ygrowthRate = 1 + self.ry * carryingCapacityFactor
        self.x = xgrowthRate * self.x
        self.y = ygrowthRate * self.y
        self.t += 1


if __name__ == "__main__":
    rx = 1.4
    ry = 1.1
    K = 10
    x0 = 5
    y0 = 9
    myModel = CompetingSpeciesModel(rx, ry, K, x0, y0)
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
