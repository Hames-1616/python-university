import matplotlib.pyplot as plot
import numpy as np

x = np.array([10,35,30,45])
label = np.array(["A","B","C","D"])
color = np.array(["red","orange","black","yellow"])
y=np.array([0,2,0,0])
plot.pie(x,labels=label,explode=y,shadow=True,startangle=90,colors=color)
plot.legend()
plot.show()