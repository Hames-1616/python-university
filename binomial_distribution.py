# binomial distribution
'''parameters -> n = no of trials
    p = probability
    size = 
    given 20 trials for coin toss generate 10 points 
'''
from numpy import random
import seaborn
import matplotlib.pyplot as plot
s = random.binomial(n=20,p=0.5,size=10)
print(s)

seaborn.distplot(s,hist=True)
plot.show()
