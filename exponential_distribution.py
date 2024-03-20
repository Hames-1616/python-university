'''
Parameters
    scale = inverse of rate - default(1)
    size - array - that u will get in return

    draw exp dist with 2.0 as scale and 2x3 size
'''
from numpy import random
import matplotlib.pyplot as plot
import seaborn as sn

e = random.exponential(scale=2,size=(2,3))
print(e)
sn.distplot(e,hist=False)
plot.show()