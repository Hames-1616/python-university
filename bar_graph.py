import matplotlib.pyplot as plot
import numpy as np

x = np.array([
    "python",
    "c",
    "c++"
])

y = np.array([
    70,30,45
])

plot.bar(x,y,width=0.1,color = "red")

#horzontal bar
# plot.barh(x,y) no width only height
plot.show()