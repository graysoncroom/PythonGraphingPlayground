#!/bin/python
import matplotlib.pyplot as plt

x = [x for x in range(1, 9)]
y = [5, 2, 4, 2, 1, 4, 5, 2]

plt.scatter(x, y, label='skitscat', color='k', marker='x', s=100)

plt.xlabel('x')
plt.ylabel('y')

plt.legend()
plt.show()
