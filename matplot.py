'''
matplolib
pyplot 

draw a line
(0,0) to (50,200)

0 = x and 50 = x and 0 = y and 200 = y

draw a line
(1,3) to (2,8) then (6,1) finally (8,10)
'''

import matplotlib.pyplot as plot
import numpy as np

# x = np.array([0,50]) # for x axis
# y = np.array([0,200]) # for y axis



x = np.array([1,2,6,8])
y = np.array([3,8,1,10])
plot.plot(x,y,marker = 'o' , ms = 100,mec='r',mfc='black',ls="dotted",color="red") # * x X p + D #__ - .
# plot.plot(x,y,'o:r')
plot.show()

# fmt string format