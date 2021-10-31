# 4.3 Simulating Discrete-Time Models with One Variable
# x_t = ax_{t-1} (4.12)

from pylab import *

a = 1.1 

def initialize():
    global x, result
    x = 1
    result = [x]

def observe():
    global x, result
    result.append(x)

def update():
    global x, result
    x = a * x

if __name__ == "__main__":
    global result
    initialize()
    for t in range(30):
        update()
        observe()
    plot(result)
    show()
