import numpy as np
import matplotlib.pyplot as plt
import math

def f(x):
    return x**2

mu = 0
sigma = 1.15
N = 51
epsilons = np.random.normal(mu, sigma, N)
x = []
y = []
y0 = []
gap = 8/(N-1) #gap between each of N elements in range[-4,4]
for i in range(N):
    x.append(gap*i - 4)
    y.append(f(x[i]) + epsilons[i])
    y0.append(f(x[i]))

def transp(matr):
    wi = len(matr)
    he = len(matr[0])
    mat = []
    for i in range(he):
        mat.append([])
        for j in range(wi):
            mat[i].append([])
            mat[i][j] = matr[j][i]
    return mat

def quadraticPolynomial(x, y):
    a = [[x[0]*x[0], x[0], 1]]
    b = [[y[0]]]
    for i in range(1,len(x)):
        a.append([x[i]*x[i], x[i], 1])
        b.append([y[i]])
    a1 = transp(a)
    t = np.matmul(a1, a)
    t = np.linalg.inv(t)
    t = np.matmul(t, a1)
    t = np.matmul(t, b)
    return t

c = quadraticPolynomial(x, y)
print("fit function is ", c[0], "*x^2 + ", c[1], "*x + ", c[2])
def fu(x, c):
    return c[0]*x*x + c[1]*x + c[2]

g = np.random.rand(100)
g = g*8 - 4

plt.plot(x,y0, color = 'y', label = "Initial function")
plt.plot(x,y, 'o', color = 'g', label = "Datapoints")
plt.plot(x, fu(x, c), color = 'r', label = "Predicted fit function")
plt.plot(g, fu(g, c), '.', color = 'b', label = "Evaluation points")
plt.legend()
plt.show()