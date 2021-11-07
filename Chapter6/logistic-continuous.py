from pylab import *

"""
Implement continuous logistic growth
Numerical integration using Euler method
"""
class LogisticModel(object):
    """
    r : rate
    K : population capacity
    dt : step
    x : initial state variable
    result : time series of state variable
    timeSteps : list of time
    """
    def __init__(self, x0, r, K, dt=0.01):
        self.x = x0
        self.r = r
        self.K = K
        self.dt = dt
        self.result = [self.x]
        self.t = 0
        self.timeSteps = [self.t]
    
    # store state variables in list
    def observe(self):
        self.result.append(self.x)
        self.timeSteps.append(self.t)
    
    # update state variable according to difference equation
    def update(self):
        coefficient = 1 + self.r * (1 - self.x/self.K) * self.dt
        self.x = coefficient * self.x
        self.t += self.dt


if __name__ == "__main__":
    x0 = 0.1
    r = 0.2
    K = 1
    dt = 0.01
    myModel = LogisticModel(x0, r, K, dt=dt)
    widerModel = LogisticModel(x0, r, K, dt=2*dt)
    timeSpan = 50
    while myModel.t < timeSpan:
        myModel.update()
        myModel.observe()
        widerModel.update()
        widerModel.observe()
    xlabel("Time")
    ylabel("x")
    plot(myModel.timeSteps, myModel.result, "b-")
    plot(myModel.timeSteps, myModel.result, "r--")
    show()
