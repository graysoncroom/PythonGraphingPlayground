#!/bin/python
import matplotlib.pyplot as plt

sleeping = [7, 8, 6, 11, 7]
eating   = [1, 2, 1, 3, 4]
working  = [7, 8, 7, 2, 2]
playing  = [8, 5, 7, 8, 13]

slices = [7, 2, 2, 13]
activities = ['sleeping','eating','working','playing']
cols = ['c', 'm', 'r', 'k']

_, _, autotexts = plt.pie(slices,
        labels=activities,
        colors=cols,
        startangle=90,
        explode=(0, 0.1, 0, 0),
        autopct='%1.1f%%')

for autotext in autotexts:
    autotext.set_color('white')

plt.title('Pie Chart')

plt.show()
