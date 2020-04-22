# all graphs generate at once but in separate windows
# Programming problem 1
import numpy as np
import matplotlib.pyplot as plt

x, y = np.random.multivariate_normal([1,1],[[1,0],[0,1]], 30).T
a, b = np.random.multivariate_normal([-1,-1],[[1,0],[0,1]], 30).T
c, d = np.random.multivariate_normal([2,0],[[1,0],[0,1]], 30).T
v = np.concatenate((x,a,c), axis = 0)
w = np.concatenate((y,b,d), axis = 0)
dat = []
for i in range(len(v)):
    dat.append([v[i],w[i]])

def kkluster(data, k):
    ln = len(data)
    c = np.random.randint(1,k+1,ln) #initial guess of clusters
    t = False
    cprev = []
    for i in range(ln):
        cprev.append(0)
    while(t == False):
        for i in range(ln):
            cprev[i] = c[i]
        centroids = []
        counters = []
        for i in range(k):
            centroids.append([0,0])
            counters.append(0)
        for i in range(ln):
            centroids[c[i]-1] = np.add(centroids[c[i]-1],data[i])
            counters[c[i]-1] += 1
        for i in range(k):
            if(counters[i] != 0):
                centroids[i] = np.divide(centroids[i],counters[i])
        for i in range(ln):
            d = []
            for j in range(k):
                d.append((data[i][0] - centroids[j][0])**2 + (data[i][1] - centroids[j][1])**2)
            c[i] = np.argmin(d) + 1
        if(all(cprev == c)):
            t = True
    return c, centroids

m3, n3 = kkluster(dat, 3)
m1, n1 = kkluster(dat, 1)
m2, n2 = kkluster(dat, 2)
m5, n5 = kkluster(dat, 5)

plot1 = plt.figure('Initial classification')
plt.plot(x,y, 'o', color = 'r', label = "Class A initial")
plt.plot(a,b, 'o', color = 'b', label = "Class B initial")
plt.plot(c,d, 'o', color = 'g', label = "Class C initial")
plt.plot(1,1, '*', color = 'r', label = "Mean of Class A")
plt.plot(-1,-1, '*', color = 'b', label = "Mean of Class B")
plt.plot(2,0, '*', color = 'g', label = "Mean of Class C")
plt.legend()

plot2 = plt.figure('Clastering into 3 clasters')
for i in range(len(v)):
    if(m3[i] == 1):
        plt.plot(v[i],w[i], 'o', color = 'r')
    if(m3[i] == 2):
        plt.plot(v[i],w[i], 'o', color = 'b')
    if(m3[i] == 3):
        plt.plot(v[i],w[i], 'o', color = 'g')
plt.plot([], [], 'o', color = 'r', label = 'Claster A')
plt.plot([], [], 'o', color = 'b', label = 'Claster B')
plt.plot([], [], 'o', color = 'g', label = 'Claster C')
plt.plot(n3[0][0],n3[0][1], '*', color = 'r', label = "Center of Claster A")
plt.plot(n3[1][0],n3[1][1], '*', color = 'b', label = "Center of Claster B")
plt.plot(n3[2][0],n3[2][1], '*', color = 'g', label = "Center of Claster C")
plt.legend()

plot3 = plt.figure('Clastering into 1 claster')
for i in range(len(v)):
    if(m1[i] == 1):
        plt.plot(v[i],w[i], 'o', color = 'r')
plt.plot([], [], 'o', color = 'r', label = 'Claster A')
plt.plot(n1[0][0],n1[0][1], '*', color = 'r', label = "Center of Claster A")
plt.legend()

plot4 = plt.figure('Clastering into 2 clasters')
for i in range(len(v)):
    if(m2[i] == 1):
        plt.plot(v[i],w[i], 'o', color = 'r')
    if(m2[i] == 2):
        plt.plot(v[i],w[i], 'o', color = 'b')
plt.plot([], [], 'o', color = 'r', label = 'Claster A')
plt.plot([], [], 'o', color = 'b', label = 'Claster B')
plt.plot(n2[0][0],n2[0][1], '*', color = 'r', label = "Center of Claster A")
plt.plot(n2[1][0],n2[1][1], '*', color = 'b', label = "Center of Claster B")
plt.legend()

plot5 = plt.figure('Clastering into 5 clasters')
for i in range(len(v)):
    if(m5[i] == 1):
        plt.plot(v[i],w[i], 'o', color = 'r')
    if(m5[i] == 2):
        plt.plot(v[i],w[i], 'o', color = 'b')
    if(m5[i] == 3):
        plt.plot(v[i],w[i], 'o', color = 'g')
    if(m5[i] == 4):
        plt.plot(v[i],w[i], 'o', color = 'c')
    if(m5[i] == 5):
        plt.plot(v[i],w[i], 'o', color = 'y')
plt.plot([], [], 'o', color = 'r', label = 'Claster A')
plt.plot([], [], 'o', color = 'b', label = 'Claster B')
plt.plot([], [], 'o', color = 'g', label = 'Claster C')
plt.plot([], [], 'o', color = 'c', label = 'Claster D')
plt.plot([], [], 'o', color = 'y', label = 'Claster E')
plt.plot(n5[0][0],n5[0][1], '*', color = 'r', label = "Center of Claster A")
plt.plot(n5[1][0],n5[1][1], '*', color = 'b', label = "Center of Claster B")
plt.plot(n5[2][0],n5[2][1], '*', color = 'g', label = "Center of Claster C")
plt.plot(n5[3][0],n5[3][1], '*', color = 'c', label = "Center of Claster D")
plt.plot(n5[4][0],n5[4][1], '*', color = 'y', label = "Center of Claster E")
plt.legend()

plt.show()