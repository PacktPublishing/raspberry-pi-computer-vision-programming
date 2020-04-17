import matplotlib.pyplot as plt
import numpy as np

x = np.array([1, 2, 3, 4], dtype=np.uint8)

y = x**2 + 1

plt.plot(x, y)

y = x + 1
plt.plot(x, y)
plt.title('Graph')
plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')

plt.grid('on')

plt.savefig('test1.png', dpi=300, bbox_inches='tight')

plt.show()

