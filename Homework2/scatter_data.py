import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cbook as cbook

def takeSecond(elem):
    return elem[1]

def takeFirst(elem):
    return elem[0]

a = [0,0.3,0.75,1,2]
b = [0,1,2,3,4]
dict = {0:0, 1:0.3, 2:0.75, 3:1, 4:2}

k = input("Please enter k for knn algorithm:\n")
x = 4*(np.random.rand(100))
for i in range(100):
    c = [(b[0], abs(a[0] - x[i])),(b[1], abs(a[1] - x[i])),(b[2], abs(a[2] - x[i])),(b[3], abs(a[3] - x[i])),(b[4], abs(a[4] - x[i]))]
    c.sort(key=takeSecond)
    d = c[:k]
    average = 0
    for j in range(k):
        average += dict[takeFirst(d[j])]
    average /= k
    y[i] = average

#x,y = 4*(np.random.rand(2,100))

plt.plot(x,y, 'o')
plt.plot(b,a, 'o')

plt.show()