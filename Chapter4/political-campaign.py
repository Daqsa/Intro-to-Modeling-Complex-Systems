from pylab import *

"""
implement dynamics of three political ideologies
implement political campaigns to sway supporters

bug found : proportions can be negative when included political campaign
"""


class CampaignIdeologiesModel(object):
    """
    c, l, n : proportions of conservative, liberal, and neutral
        0 <= c + l + n <= 1, each proportions are between 0 and 1, inclusive
    r : constant for rate
        r > 0
    p : constant for campaign sway rate
    result : time series of state variable
    timeSteps : list of time
    """
    def __init__(self, r, p, c0, n0, l0):
        self.r = r
        self.p = p
        self.c = c0
        self.n = n0
        self.l = l0
        self.cresult = [self.c]
        self.nresult = [self.n]
        self.lresult = [self.l]
        self.t = 0
        self.timeSteps = [self.t]
    
    # store state variables in list
    def observe(self):
        self.cresult.append(self.c)
        self.nresult.append(self.n)
        self.lresult.append(self.l)
        self.timeSteps.append(self.t)
    
    # update state variable according to difference equation
    def update(self):
        consvRate = 1
        libRate = 1
        neutRate = 1

        # find which side is popular, neutral or conservative, then adjust rate
        deltaRate = self.r * (self.n - self.c)
        neutRate += deltaRate
        consvRate -= deltaRate
        
        # find which side is popular, liberal or neutral, then adjust rate
        deltaRate = self.r * (self.l - self.n)
        libRate += deltaRate
        neutRate -= deltaRate

        # find which side is popular, conservative or liberal, then adjust rate
        deltaRate = self.r * (self.c - self.l)
        consvRate += deltaRate
        libRate -= deltaRate
        
        # compute the intensity of the parties' campaign
        deltaRate = self.p * (1 / self.c)
        consvRate += deltaRate
        libRate -= deltaRate

        deltaRate = self.p * (1 / self.l)
        libRate += deltaRate
        consvRate -= deltaRate


        # update actual proportions
        self.c *= consvRate
        self.l *= libRate
        self.n *= neutRate
        self.t += 1

        # normalize proportions so that they sum up to 1
        normalizingFactor = 1 / (self.c + self.n + self.l)
        self.c *= normalizingFactor
        self.n *= normalizingFactor 
        self.l *= normalizingFactor

if __name__ == "__main__":
    r = 0.1
    p = 0.1
    c0 = 0.5
    n0 = 0.2
    l0 = 0.3
    myModel = CampaignIdeologiesModel(r, p, c0, n0, l0)
    timeSpan = 50
    while myModel.t < timeSpan:
        myModel.update()
        myModel.observe()
    xlabel("Time")
    ylabel("Proportion")
    plot(myModel.timeSteps, myModel.cresult, 'r-')
    plot(myModel.timeSteps, myModel.nresult, '+')
    plot(myModel.timeSteps, myModel.lresult, 'b--')
    
    # title("Phase Space")
    # plot(myModel.xresult, myModel.yresult)
    show()
