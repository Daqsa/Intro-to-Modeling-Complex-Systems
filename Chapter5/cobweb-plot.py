from pylab import *


class CobwebPlot(object):
    def __init__(self, updateFunction, x0):
        self.updateFunction = updateFunction
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
        self.x = self.updateFunction(self.x) 
        self.t += 1

def f(x):
    return 1.1 * x

def logistic(x):
    r = 2.5
    K = 1
    return x + r*x*(1-x/K)

if __name__ == "__main__":
    x0 = 0.1
    function = logistic
    myModel = CobwebPlot(function, x0)
    timeSpan = 30
    figure(figsize=(8, 8), dpi=80)
    while myModel.t < timeSpan:
        myModel.update()
        myModel.observe()

    # draw diagonal line
    xmin, xmax = 0, 3.5/2.5
    plot([xmin, xmax], [xmin, xmax], 'k')

    # drawing curve (sampling 100 points)
    rng = [xmin + (xmax-xmin)/100 * i for i in range(100)]
    plot(rng, list(map(function, rng)), 'k')

    # drawing trajectory
    horizontal = [myModel.result[0]]
    vertical = [myModel.result[0]]
    for x in myModel.result[1:]:
        # add point (x_{t-1}, x_t)
        horizontal.append(vertical[-1])
        vertical.append(x)
        # add point (x_t, x_t)
        horizontal.append(x)
        vertical.append(x)
    plot(horizontal, vertical, 'b')

    show()
