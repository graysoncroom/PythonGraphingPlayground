#!/bin/python
import matplotlib.pyplot as plt

population_ages = [22, 55, 62, 45, 34, 77, 4, 8, 14, 80, 65, 54, 43, 48, 24, 18, 13, 67]

min_age = 0
max_age = 140
age_step_by = 20

bins = [x for x in range(0, 141, 20)]

plt.hist(population_ages, bins, histtype='bar', rwidth=0.8)

plt.xlabel('x')
plt.ylabel('y')

plt.show()
