# 4.3 Simulating Discrete-Time Models with One Variable
# x_t = ax_{t-1} + b, x_0 = 1 (4.12)

from pylab import *


"""
when x is declared outside a function and you say x = x + 1 in a 
function body, Python defaults to assume x as a local variable and 
spits out error that local variable is referenced before assignment. 
To solve the local variable problem, use a class. 
I don't want to use global variables. 

Implement a exponential difference equation 
x_t = a * x_{t-1} + b
"""
class ExponentialModel(object):
    """
    a, b : parameters
    x : initial state variable
    result : time series of state variable
    timeSteps : list of time
    """
    def __init__(self, a, b, x0):
        self.a = a
        self.b = b
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
        self.x = self.a * self.x + self.b
        self.t += 1


if __name__ == "__main__":
    a = 1.1
    b = -0.05
    x0 = 1
    myModel = ExponentialModel(a, b, x0)
    timeSpan = 30
    while myModel.t < timeSpan:
        myModel.update()
        myModel.observe()
    xlabel("Time")
    ylabel("x")
    plot(myModel.timeSteps, myModel.result)
    show()
