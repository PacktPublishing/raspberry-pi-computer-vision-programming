import matplotlib.pyplot as plt
import numpy as np
import mahotas
photo = mahotas.demos.load('luispedro', as_grey=True)
photo = photo.astype(np.uint8)
T_rc = mahotas.rc(photo)
plt.imshow(photo > T_rc, cmap='gray')
plt.axis('off')
plt.show()
