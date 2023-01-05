import matplotlib.pyplot as plt
import numpy as np
import math

#t = math.pi/6
for t in range (0,1080):
    U = t/180

    plt.plot(np.sin(U),np.cos(U),marker = "+")

    print(t)
plt.show()