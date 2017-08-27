#!/bin/python
import matplotlib.pyplot as plt

x = [1, 3, 5, 7, 9]
y = [6, 7, 8, 2, 4]

x2 = [2, 4, 6, 8, 10]
y2 = [9, 6, 2, 4, 2]

plt.bar(x, y, label='Bars1', color='orange')
plt.bar(x2, y2, label='Bars2', color='purple')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Graph Title')
plt.legend()
plt.show()
