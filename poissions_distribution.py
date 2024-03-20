'''
parameters 
    lam - rate of know no of occurences
    size - array
    Generate 1x10 random distribution for occurence of 3

'''

from numpy import random
import matplotlib.pyplot as plot
import seaborn as sn

s = random.poisson(lam=3,size=(10))
sn.distplot(s,hist=False)
plot.show()

