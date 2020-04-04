import numpy as np 
import matplotlib.pyplot as plt 
a = np.arange(0,4,0.5)
b = a**2
c = a**3
plt.plot(a,b,'g.')
plt.plot(a,c,'r.')
plt.show()