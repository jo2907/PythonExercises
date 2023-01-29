import numpy as np 
import matplotlib.pyplot as plt

t = np.array(np.linspace(0,5,num=500))
y = (t**2)*np.exp(-2*t)
plt.plot(t,y,'r-', linewidth=4)

# add labels
plt.xlabel("x values")
plt.ylabel("y")

plt.show()
