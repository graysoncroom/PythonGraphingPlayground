#!/bin/python
import matplotlib.pyplot as plt

days = [1, 2, 3, 4, 5]

sleeping = [7, 8, 6, 11, 7]
eating   = [1, 2, 1, 3, 4]
working  = [7, 8, 7, 2, 2]
playing  = [8, 5, 7, 8, 13]

plt.plot([], [], color='purple', label='sleeping', linewidth=5)
plt.plot([], [], color='cyan'  , label='eating'  , linewidth=5)
plt.plot([], [], color='red', label='working' , linewidth=5)
plt.plot([], [], color='black' , label='playing' , linewidth=5)

plt.stackplot(days, sleeping, eating, working, playing, colors=['purple','cyan','red','black'])

plt.title('Stack Plot')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()

plt.show()
