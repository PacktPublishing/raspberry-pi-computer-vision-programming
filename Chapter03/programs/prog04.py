import matplotlib.pyplot as plt
import numpy as np

x = np.array([[0, 1, 2, 3, 4],
              [5, 6, 7, 8, 9]], dtype = np.uint8 )

plt.imshow(x, cmap='Accent')

plt.axis('off')
plt.grid('off')

plt.show()
