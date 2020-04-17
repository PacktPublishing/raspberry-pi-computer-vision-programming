import matplotlib.pyplot as plt
import numpy as np

x = np.random.rand(3, 3, 3)

plt.imshow(x)

plt.axis('off')
plt.grid('off')

plt.show()
