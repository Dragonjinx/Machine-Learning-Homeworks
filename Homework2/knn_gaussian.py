import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cbook as cbook

x, y = np.random.multivariate_normal([1,1],[[1,0],[0,1]], 30).T
a, b = np.random.multivariate_normal([-1,-1],[[1,0],[0,1]], 30).T
c, d = np.random.multivariate_normal([2,0],[[1,0],[0,1]], 30).T

plt.plot(x,y, 'o')
plt.plot(a,b, 'o')
plt.plot(c,d, 'o')

plt.show()