import numpy as np
import matplotlib.pyplot as plt
"""a=np.array([2,5])
b=np.array([6,7])
mean_a=np.mean(a)"""

"""a=np.array([0,np.pi/2,np.pi])
b=np.sin(a)
print(a)"""

a=np.linspace(0,2*np.pi,100)
b=np.sin(a)
plt.plot(a,b)
plt.show()
