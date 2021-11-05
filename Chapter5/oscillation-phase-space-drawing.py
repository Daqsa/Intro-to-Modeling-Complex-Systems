from pylab import *

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

""" 
Visualize all phase spaces for a given range of initial values
"""
if __name__ == "__main__":
    coeffs = [0.5, 1, -0.5, 1]
    timeSpan = 30
    xlabel("Time")
    ylabel("State Variable")
    # Phase space!
    title("Phase Space")
        
    for x0 in range(-4, 4):
        for y0 in range(-4, 4):
            x0 /= 2
            y0 /= 2
            myModel = OscillationModel(coeffs, x0, y0)
            while myModel.t < timeSpan:
                myModel.update()
                myModel.observe()
            plot(myModel.xresult, myModel.yresult)
    show()
