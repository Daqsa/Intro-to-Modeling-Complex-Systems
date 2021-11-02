# 4.4 Simulating Discrete-Time Models with Multiple Variables 

from pylab import *


"""
when x is declared outside a function and you say x = x + 1 in a 
function body, Python defaults to assume x as a local variable and 
spits out error that local variable is referenced before assignment. 
To solve the local variable problem, use a class. 
I don't want to use global variables. 

Implement an oscillation
x_t = a11 * x_{t-1} + a12 * y_{t-1}
y_t = a21 * x_{t-1} + a22 * y_{t-1}
"""
class OscillationModel(object):
    """
    coeffs = [a11, a12, a21, a22] : parameters
    x, y : initial state variable
    result : time series of state variable
    timeSteps : list of time
    """
    def __init__(self, coeffs, x0, y0):
        self.coeffs = coeffs
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
        nextx = coeffs[0] * self.x + coeffs[1] * self.y 
        nexty = coeffs[2] * self.x + coeffs[3] * self.y
        self.x, self.y = nextx, nexty
        self.t += 1


if __name__ == "__main__":
    coeffs = [0.5, 1, -0.5, 1]
    x0 = 1
    y0 = 1
    myModel = OscillationModel(coeffs, x0, y0)
    timeSpan = 30
    while myModel.t < timeSpan:
        myModel.update()
        myModel.observe()
    xlabel("Time")
    ylabel("State Variable")
    # plot(myModel.timeSteps, myModel.xresult, 'b-')
    # plot(myModel.timeSteps, myModel.yresult, 'g--')
    # Phase space!
    title("Phase Space")
    plot(myModel.xresult, myModel.yresult)
    show()
