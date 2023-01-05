import matplotlib.pyplot as plt
import numpy as np

t = np.linspace(-np.pi,np.pi)
#x = [i*(np.pi/180)for i in t]
plt.plot(t,np.sin(t),marker="+")
plt.plot(t,np.cos(t),marker="^")

plt.show()