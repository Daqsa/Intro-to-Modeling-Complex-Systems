from pylab import *

"""
Implement the rise and fall of the popularity of a pop song
"""
class PopSongPopularityModel(object):
    """
    P : popularity, state variable (units: hundreds of people)
    a : attractivity, the ratio of people who find the song attractive
    tr : trend time, the amount of time it takes for a person to feel the song is no longer attractive
    result : time series of state variable
    timeSteps : list of time
    """
    def __init__(self, P0, a, tr, dt=0.01):
        self.P = P0
        self.a = a
        self.tr = tr
        self.result = [self.P]
        self.t = 0
        self.dt = dt
        self.timeSteps = [self.t]
    
    # store state variables in list
    def observe(self):
        self.result.append(self.P)
        self.timeSteps.append(self.t)
    
    # update state variable according to differential equation
    def update(self):
        # people still find it attractive 
        if self.t < self.tr:
            self.P += self.a * self.P * self.dt
        # the trend is over and people find it no longer attractive
        else:
            self.P += -self.a * self.P * self.dt

        self.t += self.dt


if __name__ == "__main__":
    P0 = 1 
    a = 0.5
    tr = 15
    dt = 0.01
    myModel = PopSongPopularityModel(P0, a, tr, dt=dt)
    timeSpan = 30
    while myModel.t < timeSpan:
        myModel.update()
        myModel.observe()
    xlabel("Time")
    ylabel("Popularity")
    plot(myModel.timeSteps, myModel.result, 'b-')
    # title("Phase Space")
    # plot(myModel.xresult, myModel.yresult)
    show()
