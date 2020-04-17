import matplotlib.pyplot as plt
import numpy as np

x = np.array([1, 2, 3, 4], dtype=np.uint8)

y = x**2 + 1

plt.plot(x, y)

plt.grid('on')

plt.show()
