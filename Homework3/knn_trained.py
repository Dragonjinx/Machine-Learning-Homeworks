import matplotlib.pyplot as plot
import numpy

training = [(1, 3), (5, 7), (4,9), (6,9)]
with_iterator = zip(*training)

figure, ax = plot.subplots()
ax.scatter(*with_iterator)

ax.show()