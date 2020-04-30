import csv
import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt
from scipy.linalg import solve_triangular

def normalize(inp):
    ln = len(inp)
    lenn = len(inp[0])
    for i in range(lenn):
        mx = inp[0][i]
        mn = inp[0][i]
        for j in range(ln):
            if(inp[j][i] > mx):
                mx = inp[j][i]
            if(inp[j][i] < mn):
                mn = inp[j][i]
        delt = mx - mn
        for j in range(ln):
            inp[j][i] = (inp[j][i] - mn)/delt
    return inp

def k(x, x1):
    ln = len(x)
    ans = 0
    for i in range(ln):
        ans += ((x[i]-x1[i])**2)
    return math.exp(-ans)

def datasplit(table):
    ln = len(table)
    lenn = len(table[0])
    inp = []
    out = []
    for i in range(ln):
        inp.append([])
        for j in range(lenn-1):
            inp[i].append(table[i][j])
        out.append(table[i][lenn-1])
    return inp, out

def Cholesky(A, b):
    L = np.linalg.cholesky(A)
    L1 = L.T.conj()
    y = solve_triangular(L, b, lower=True)
    x = solve_triangular(L1, y, lower=False)
    return x

def AplusLambdaI(lmbd, A):
    ln = len(A)
    for i in range(ln):
        A[i][i] += lmbd
    return A

def kernelRidge(inp, out, x, lmbd):
    ln = len(inp)
    #print(ln)
    A = []
    for i in range(ln):
        A.append([])
        for j in range(ln):
            A[i].append([])
            A[i][j] = k(inp[i], inp[j])
            #print(k(inp[i], inp[j]))
    #lmbd = 0.001
    A1 = AplusLambdaI(lmbd, A)
    #print(A)
    alpha = Cholesky(A1, out)
    Y = []
    for i in range(len(x)):
        Y.append([])
        Y[i] = 0
        for j in range(len(alpha)):
            # print(len(inp))
            # print(len(alpha))
            # print(len(x))
            Y[i] += alpha[j]*k(x[i], inp[j])
    return Y

def l2loss(yexpect, yreal):
    return ((yexpect - yreal)**2)

def k_folds_cross(data, labels, kernelRidge, K, lmbd):
    ln = len(data)
    split = np.random.permutation(ln)
    folds_index = []
    for i in range(K):
        folds_index.append(split[int(ln*i/K):int(ln*(i+1)/K)])
    error = 0
    for i in range(K):
        validation_data = []
        validation_label = []
        training_data = []
        training_label = []
        for j in range(len(folds_index[i])):
            validation_data.append(data[folds_index[i][j]])
            validation_label.append(labels[folds_index[i][j]])
        for l in range(0,i):
            for j in range(len(folds_index[l])):
                training_data.append(data[folds_index[l][j]])
                training_label.append(labels[folds_index[l][j]])
        for l in range(i+1,K):
            for j in range(len(folds_index[l])):
                training_data.append(data[folds_index[l][j]])
                training_label.append(labels[folds_index[l][j]])
        #print(validation_data)
        #print(validation_label)
        #print(training_data)
        #print(training_label)
        predicted_labels = kernelRidge(training_data, training_label, validation_data, lmbd)
        errorx = 0
        for i in range(len(validation_label)):
            errorx = errorx + l2loss(predicted_labels[i], validation_label[i])
        errorx *= (1/len(validation_data))
        error += errorx
    error *= (1/K)
    return error

table = np.array(pd.read_csv('winequality-red.csv', ';'))
inp, out = datasplit(table)
inp = normalize(inp)

ld = [100, 1, 0.1, 0.001, 0.00001]
print("Each plot generates long (~15 sec) because of many datapoints")
print("Please, be patient, calculations take time, 0/5 plot generated")
N = [8, 16, 32, 64, 128, 256, 512, 1024]
y = []
for j in range(len(N)):
    split = np.random.permutation(len(inp))
    training = split[:N[j]]
    data = []
    label = []
    for i in training:
        data.append(inp[i])
        label.append(out[i])
    #print(data)
    #print(label)
    y.append(k_folds_cross(data, label, kernelRidge, 3, 100))
plot = plt.figure('lambda = 100')
plt.xscale('log')
plt.yscale('log')
plt.plot(N, y, color = 'r', label = "Error function")
plt.legend()

print("Please, be patient, calculations take time, 1/5 plot generated")
N = [8, 16, 32, 64, 128, 256, 512, 1024]
y = []
for j in range(len(N)):
    split = np.random.permutation(len(inp))
    training = split[:N[j]]
    data = []
    label = []
    for i in training:
        data.append(inp[i])
        label.append(out[i])
    #print(data)
    #print(label)
    y.append(k_folds_cross(data, label, kernelRidge, 3, 1))
plot = plt.figure('lambda = 1')
plt.xscale('log')
plt.yscale('log')
plt.plot(N, y, color = 'r', label = "Error function")
plt.legend()

print("Please, be patient, calculations take time, 2/5 plot generated")
N = [8, 16, 32, 64, 128, 256, 512, 1024]
y = []
for j in range(len(N)):
    split = np.random.permutation(len(inp))
    training = split[:N[j]]
    data = []
    label = []
    for i in training:
        data.append(inp[i])
        label.append(out[i])
    #print(data)
    #print(label)
    y.append(k_folds_cross(data, label, kernelRidge, 3, 0.1))
plot = plt.figure('lambda = 0.1')
plt.xscale('log')
plt.yscale('log')
plt.plot(N, y, color = 'r', label = "Error function")
plt.legend()

print("Please, be patient, calculations take time, 3/5 plot generated")
N = [8, 16, 32, 64, 128, 256, 512, 1024]
y = []
for j in range(len(N)):
    split = np.random.permutation(len(inp))
    training = split[:N[j]]
    data = []
    label = []
    for i in training:
        data.append(inp[i])
        label.append(out[i])
    #print(data)
    #print(label)
    y.append(k_folds_cross(data, label, kernelRidge, 3, 0.001))
plot = plt.figure('lambda = 0.001')
plt.xscale('log')
plt.yscale('log')
plt.plot(N, y, color = 'r', label = "Error function")
plt.legend()

print("Please, be patient, calculations take time, 4/5 plot generated")
N = [8, 16, 32, 64, 128, 256, 512, 1024]
y = []
for j in range(len(N)):
    split = np.random.permutation(len(inp))
    training = split[:N[j]]
    data = []
    label = []
    for i in training:
        data.append(inp[i])
        label.append(out[i])
    #print(data)
    #print(label)
    y.append(k_folds_cross(data, label, kernelRidge, 3, 0.00001))
plot = plt.figure('lambda = 0.00001')
plt.xscale('log')
plt.yscale('log')
plt.plot(N, y, color = 'r', label = "Error function")
plt.legend()
print("Thanks for your patience, 5/5 plot generated :)")
print("Also it can be seen that actually lambda = 0.1 is one of the best choices")
plt.show()