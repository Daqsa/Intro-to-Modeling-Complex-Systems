from pylab import *

"""
Implement logistic growth 
"""
class LogisticModel(object):
    """
    a, K : parameters
    x : initial state variable
    result : time series of state variable
    timeSteps : list of time
    """
    def __init__(self, a, K, x0):
        self.a = a
        self.K = K
        self.x = x0
        self.result = [self.x]
        self.t = 0
        self.timeSteps = [self.t]
    
    # store state variables in list
    def observe(self):
        self.result.append(self.x)
        self.timeSteps.append(self.t)
    
    # update state variable according to difference equation
    def update(self):
        coefficient = ((1-self.a) / self.K) * self.x + self.a
        self.x = coefficient * self.x
        self.t += 1


if __name__ == "__main__":
    a = 1.5
    K = 100 
    x0 = 5
    myModel = LogisticModel(a, K, x0)
    timeSpan = 30
    while myModel.t < timeSpan:
        myModel.update()
        myModel.observe()
    xlabel("Time")
    ylabel("x")
    plot(myModel.timeSteps, myModel.result)
    show()
