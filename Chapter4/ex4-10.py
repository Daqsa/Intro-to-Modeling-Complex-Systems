from pylab import *

"""
Implement a model where population growth ratio is highest at a 
certain optimal population size, but it goes down as the population 
deviates from the optimal size. 
"""
class QuadraticLogisticModel(object):
    """
    P, r : parameters
    x : initial state variable
    result : time series of state variable
    timeSteps : list of time
    """
    def __init__(self, P, r, a, x0):
        self.P = P
        self.r = r
        self.a = a
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
        coefficient = -a * (self.x-self.P) ** 2 + self.r
        self.x = coefficient * self.x
        self.t += 1


if __name__ == "__main__":
    P = 1
    r = 1.3
    a = 1e-20
    x0 = 0.7
    myModel = QuadraticLogisticModel(P, r, a, x0)
    timeSpan = 100
    while myModel.t < timeSpan:
        myModel.update()
        myModel.observe()
        print(myModel.x)
    xlabel("Time")
    ylabel("x")
    plot(myModel.timeSteps, myModel.result)
    show()
