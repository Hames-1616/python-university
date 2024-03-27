import matplotlib.pyplot as plot
import numpy as np

x = np.random.randint(100,size=(100))
y = np.random.randint(100,size=(100))
colors = np.random.randint(100,size=(100))
dsize = np.random.randint(100,size=(100))
plot.scatter(x,y,c=colors,cmap='viridis',s=dsize,alpha=0.5)
plot.colorbar()
plot.show()