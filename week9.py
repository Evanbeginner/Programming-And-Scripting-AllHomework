import numpy as np 
import matplotlib.pyplot as plt 
l = np.arange(0.0,250,0.5)
#print(l)
#a = l**2
#print(a)
#plt.plot(l,a)
#plt.show()
a = l**2

x = np.linspace(1.0,100,500)
#print(x)
plt.plot(l,x, 'g.',label="Bello")
plt.show()
plt.title("Hello")
plt.plot(l,a,"r.")
plt.show()
