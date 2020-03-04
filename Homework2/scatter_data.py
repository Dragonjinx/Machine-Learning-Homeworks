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
k = int(k)
x = 4*(np.random.rand(100))
y = [None] * 100
for i in range(100):
    c = [(b[0], abs(b[0] - x[i])),(b[1], abs(b[1] - x[i])),(b[2], abs(b[2] - x[i])),(b[3], abs(b[3] - x[i])),(b[4], abs(b[4] - x[i]))]
    c.sort(key=takeSecond)
    #d = c[:k]
    average = 0
    for j in range(k):
        print(takeFirst(c[j]), dict[takeFirst(c[j])])
        average += dict[takeFirst(c[j])]
    average /= k
    y[i] = average

#x,y = 4*(np.random.rand(2,100))

plt.plot(x,y, 'o')
plt.plot(b,a, 'o')

plt.show()