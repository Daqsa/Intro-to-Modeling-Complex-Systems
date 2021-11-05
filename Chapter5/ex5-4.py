from pylab import *

class OscillationModel(object):
    """
    x, y : initial state variable
    result : time series of state variable
    timeSteps : list of time
    """
    def __init__(self, a, b, x0, y0):
        self.a = a
        self.b = b
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
        nextx = self.x + self.a * (self.x - self.x * self.y) 
        nexty = self.y + self.b * (self.y - self.x * self.y) 
        if nextx > 0:
            self.x = nextx
        if nexty > 0:
            self.y = nexty
        self.t += 1

""" 
Visualize all phase spaces for a given range of initial values
"""
if __name__ == "__main__":
    a = 0.1
    b = 0.1
    timeSpan = 30
    xlabel("x")
    ylabel("y")
    # Phase space!
    title("Phase Space")
    xlim(0, 1)
    ylim(0, 1)
    for x0 in range(10):
        for y0 in range(10):
            x0 /= 10
            y0 /= 10
            myModel = OscillationModel(a, b, x0, y0)
            while myModel.t < timeSpan:
                myModel.update()
                myModel.observe()
            plot(myModel.xresult, myModel.yresult)
    """
    x0 = 0.25
    y0 = 0.2
    myModel = OscillationModel(a, b, x0, y0)
    while myModel.t < timeSpan:
        myModel.update()
        myModel.observe()
    plot(myModel.xresult, myModel.yresult)
    """
    show()
