import matplotlib.pyplot as plot
import numpy as np

x = np.array([80,30,40,20])
y = np.array([30,90,50,10])
font1 = {'family':'JetBrains Mono','color':'black','size':20}
plot.title("result",loc='left',fontdict=font1)
plot.plot(x,y)
# plot.show()
plot.grid(lineStyle,linewidth) #axis = x or y
plot.show()