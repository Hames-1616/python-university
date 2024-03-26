'''
subplot
params -> rows,columns,figure index
'''

import matplotlib.pyplot as plot
import numpy as np


x = np.array([0,1,2,3])
y = np.array([3,8,9,10])

plot.subplot(1,2,1)
plot.plot(x,y)
plot.title("result 1")
# plot 2
s = np.array([0,1,2,3])
t = np.array([7,8,9,10])
plot.subplot(1,2,2)
plot.plot(s,t)
plot.title("result 2")
plot.suptitle("subplotting")
plot.show()