import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cbook as cbook

x,y = np.random.rand(2,100)

ax = plt.subplot()
ax.scatter(x,y)

plt.show()