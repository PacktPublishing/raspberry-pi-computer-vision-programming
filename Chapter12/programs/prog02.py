import matplotlib.pyplot as plt
import mahotas
photo= mahotas.imread('/home/pi/book/dataset/4.1.01.tiff')
plt.imshow(photo, cmap='gray')
plt.axis('off')
plt.show()
