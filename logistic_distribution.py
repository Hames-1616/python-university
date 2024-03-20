'''parameters 
    loc - mean
    scale - std dev
    size - shape of array
    draw a 2x3 sample from a logistic distribution with mean = 2 and scale = 3
    '''
from numpy import random
import matplotlib.pyplot as plot
import seaborn as sn 

l = random.logistic(loc=2,scale=3,size=(2,3))
sn.distplot(l,hist=False)
plot.show()