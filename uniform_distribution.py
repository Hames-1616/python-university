'''
when distribution contains equal values
parameters 
    a - lowerbound
    b - upper bound
    size - array

'''

from numpy import random
import matplotlib.pyplot as plot
import seaborn as sn

s = random.uniform(size=(2,3))
sn.distplot(s,hist=False)
plot.show()

