import numpy as np
import matplotlib.pyplot as plt
x, y = [[0, 1, 2, 3], [20, 0, 0, 0]]

def f(a):
    return 5*a*a -21*a + 19

t = np.arange(-0.5, 3.5, 0.1)


plt.plot(x,y, 'o', color = 'r', label = "Datapoints")
plt.plot(t, f(t), color = 'r', label = "Predicted fit function")
plt.legend()
plt.show()