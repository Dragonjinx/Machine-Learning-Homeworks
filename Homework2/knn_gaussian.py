import numpy as np
import matplotlib.pyplot as plt
import matplotlib.lines as mlines
import matplotlib.cbook as cbook
import math

x, y = np.random.multivariate_normal([1,1],[[1,0],[0,1]], 30).T
a, b = np.random.multivariate_normal([-1,-1],[[1,0],[0,1]], 30).T
c, d = np.random.multivariate_normal([2,0],[[1,0],[0,1]], 30).T
dots = [[x,y,1],[a,b,2],[c,d,3]]

plt.plot(x,y, 'o', color = 'r', label = "Class A training")
plt.plot(a,b, 'o', color = 'b', label = "Class B training")
plt.plot(c,d, 'o', color = 'g', label = "Class C training")

v,w = 8*(np.random.rand(2,100)) - 4

k = input("Please enter k for knn algorithm:\n")
k = int(k)

for i in range(100):
    m = []
    for j in range(30):
        m.append(((v[i] - x[j])**2)+(w[i] - y[j])**2)
        m.append(((v[i] - a[j])**2)+(w[i] - b[j])**2)
        m.append(((v[i] - c[j])**2)+(w[i] - d[j])**2)
    g = np.argsort(m)
    g = g[:k]
    g = np.remainder(g,3)
    (un, counts) = np.unique(g, return_counts=True)
    s = un[np.argmax(counts)]
    if s == 0:
        f = 'r'
    if s == 1:
        f = 'b'
    if s == 2:
        f = 'g'
    plt.plot(v[i],w[i], 'x', color = f)
plt.plot([],[], 'x', color = 'r', label="Class A classified data")
plt.plot([],[], 'x', color = 'b', label="Class B classified data")
plt.plot([],[], 'x', color = 'g', label="Class C classified data")

plt.legend()

plt.show()