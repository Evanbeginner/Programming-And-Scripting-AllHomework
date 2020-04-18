import matplotlib.pyplot as plt 
import numpy as np 
a = [95.00,89.15,100.00,85.00,97.15]
b = [91.15,87.97,85.17,98.15,99.57]
y = [2014,2015,2016,2017,2018]


plt.plot(y,a)
plt.plot(y,b)
plt.xlabel('Year')
plt.ylabel('Stock Price')
plt.axis([2013,2019,30.00,150.00])
plt.show()


fig_1 = plt.figure(1,figsize=(6.4,4.8))

chart_1 = fig_1.add_subplot(121)
chart_2 =fig_1.add_subplot(122)
chart_1.plot(y,a)
chart_2.plot(y,b)
plt.show()
