from pylab import *

"""
Implement continuous Lotka-Volterra equations 
Numerical integration using Euler method
"""
class LotkaVolterraModel(object):
    """
    a, b, c, d : parameters
    dt : step
    x, y : state variable
    result : time series of state variable
    timeSteps : list of time
    """
    def __init__(self, x0, y0, a, b, c, d, dt=0.01):
        self.x = x0
        self.y = y0
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.dt = dt
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
        self.x += (self.a*self.x - self.b*self.x*self.y) * self.dt
        self.y += (-self.c*self.y + self.d*self.x*self.y) * self.dt
        self.t += self.dt


if __name__ == "__main__":
    x0 = 0.1
    y0 = 0.1
    a = 1
    b = 1
    c = 1
    d = 1
    dt = 0.2
    myModel = LotkaVolterraModel(x0, y0, a, b, c, d, dt=dt)
    timeSpan = 50
    while myModel.t < timeSpan:
        myModel.update()
        myModel.observe()

    # visualize using a phase space
    xlabel("x")
    ylabel("y")
    plot(myModel.xresult, myModel.yresult, "b-")
    show()
