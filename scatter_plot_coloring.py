import matplotlib.pyplot as plot
import numpy as np

x = np.array([1,2,3,4])
y = np.array([10,20,30,40])
# Colors = np.array(["red","blue","green","black"])
# plot.scatter(x,y,color = Colors)


s = np.array([40,50,60,70])
plot.scatter(x,y,c=s,cmap='viridis')
plot.colorbar()
plot.show()