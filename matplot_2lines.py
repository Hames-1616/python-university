import matplotlib.pyplot as plot
import numpy as np

# x = np.array([0,50]) # for x axis
# y = np.array([0,200]) # for y axis



x1 = np.array([1,2,6,8])
y1 = np.array([3,8,1,10])
x2 = np.array([5,7,8,9])
y2 = np.array([10,15,20,25])

plot.plot(x1,y1,x2,y2)
plot.xlabel("x-axis")
plot.ylabel("y-axis")
plot.title("2 lines",loc="center")
plot.show()