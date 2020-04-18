import numpy as np 
import matplotlib.pyplot as plt 
# importing numpy as np and mathplotlib as plt
a = np.arange(0,4,0.5)
#using arrange to range a from 0 to 4 in 0.5 increments
b = a**2
#setting b as a to the power of 2
c = a**3
#setting c as a to the power of 3
plt.plot(a,b,'g.')
# plotting a on x axis and b on y axis in green
plt.plot(a,c,'r.')
# plotting a on x axis and x on y axis in red
plt.show()
# using show method to show plot 