#!/bin/python
import matplotlib.pyplot as plt
import numpy as np

x, y = np.loadtxt('example.txt', delimiter=',', unpack=True)

plt.plot(x, y, label='Loaded from file')

plt.title('Line Graph\nLoaded from file')
plt.show()
