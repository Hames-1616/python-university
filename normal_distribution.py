from numpy import random
import seaborn as sn
import matplotlib.pyplot as plot
n = random.normal(size=(2,3))
print(n)
# 3x3  mean=2  std=3

s = random.normal(loc=2,scale=3,size=(3,3))
print(s)

sn.distplot(s,hist=False)
plot.show()