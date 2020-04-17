import numpy as np
import matplotlib.pyplot as plt

a = np.array([1, 2, 1, 3, 4, 1, 2, 3, 4, 4, 2, 3, 4])

hist, bins = np.histogram(a) 

print(hist)
print(bins)

plt.hist(a)
plt.show()
