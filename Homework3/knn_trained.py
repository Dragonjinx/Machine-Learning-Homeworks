#!/usr/bin/python3.7
import matplotlib.pyplot as plt

training = [(1, 3), (5, 7), (4, 9), (6, 9)]
with_iterator = zip(*training)


plt.scatter(*with_iterator)

plt.show()
