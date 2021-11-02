from pylab import *

"""
Implement predator-prey model (Lotka-Volterra model) 
"""
class PredatorPreyModel(object):
    """
    Prey parameters
        r : growth rate 
        K : carrying capacity
        b : death rate from being eaten by predators
    Predator parameters
        d : death rate 
        c : growth rate from eating prey
    x : initial state variable
    result : time series of state variable
    timeSteps : list of time
    """
    def __init__(self, r, K, b, d, c, x0, y0):
        self.r = r
        self.K = K
        self.b = b
        self.d = d
        self.c = c
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
        preyGrowthRate = self.r * (1-self.x/self.K)
        preyDeathRate = -(1-1/(self.b*self.y+1))
        preyRate = 1 + preyGrowthRate + preyDeathRate
        nextx = preyRate * self.x
    
        predatorDeathRate = -self.d
        predatorGrowthRate = self.c * self.x
        predatorRate = 1 + predatorDeathRate + predatorGrowthRate
        nexty = predatorRate * self.y

        self.x, self.y = nextx, nexty
        self.t += 1


if __name__ == "__main__":
    r = 1 
    K = 5
    b = 1
    d = 1
    c = 1 
    x0 = 1
    y0 = 5
    myModel = PredatorPreyModel(r, K, b, d, c, x0, y0)
    timeSpan = 200
    while myModel.t < timeSpan:
        myModel.update()
        myModel.observe()
    xlabel("Time")
    ylabel("Population")
    # plot(myModel.timeSteps, myModel.xresult, 'b-')
    # plot(myModel.timeSteps, myModel.yresult, 'g--')
    title("Phase Space")
    plot(myModel.xresult, myModel.yresult)

    show()
