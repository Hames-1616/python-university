import matplotlib.pyplot as plot
import seaborn as sn

sn.distplot([0,1,2,3,4,5],hist=False)


sn.histplot([0,1,2,3,4,5])
sn.kdeplot([0,1,2,3,4,5])
plot.show()

