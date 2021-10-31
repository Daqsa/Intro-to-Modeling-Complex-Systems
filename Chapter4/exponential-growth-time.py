# 4.3 Simulating Discrete-Time Models with One Variable
# x_t = ax_{t-1} (4.12)

from pylab import *

a = 1.1 

def initialize():
    global x, result, t, timeSteps
    x = 1
    result = [x]
    t = 0
    timeSteps = [t]

def observe():
    global x, result, t, timeSteps
    result.append(x)
    timeSteps.append(t)


def update():
    global x, result, t
    x = a * x
    t += 0.1

if __name__ == "__main__":
    global result, t, timeSteps
    initialize()
    while t < 3:
        update()
        observe()
    plot(timeSteps, result)
    show()
