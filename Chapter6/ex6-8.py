from pylab import *

"""
Implement the chemical reaction
S + E --> 2E
"""
class ChemicalReactionModel(object):
    """
    r : rate of reaction (the above reaction happens r times per unit time)
    S, E : quantity of chemical species in moles
    result : time series of state variable
    timeSteps : list of time
    """
    def __init__(self, S, E, r, dt=0.01):
        self.S = S
        self.E = E
        self.r = r
        self.sresult = [self.S]
        self.eresult = [self.E]
        self.t = 0
        self.dt = dt
        self.timeSteps = [self.t]
    
    # store state variables in list
    def observe(self):
        self.sresult.append(self.S)
        self.eresult.append(self.E)
        self.timeSteps.append(self.t)
    
    # update state variable according to differential equation
    def update(self):
        # chemicals only react when there's a positive quantity of them
        if self.S <= 0 or self.E <= 0:
            self.t += self.dt
            return None

        sderivative = -self.r
        ederivative = self.r
        self.S += sderivative * self.dt
        self.E += ederivative * self.dt 
        self.t += self.dt


if __name__ == "__main__":
    S = 100
    E = 100
    r = 1
    dt = 0.01
    myModel = ChemicalReactionModel(S, E, r, dt=dt)
    timeSpan = 30
    while myModel.t < timeSpan:
        myModel.update()
        myModel.observe()
    xlabel("Time")
    ylabel("Quantity(mol)")
    plot(myModel.timeSteps, myModel.sresult, 'b-')
    plot(myModel.timeSteps, myModel.eresult, 'g--')
    # title("Phase Space")
    # plot(myModel.xresult, myModel.yresult)
    show()
