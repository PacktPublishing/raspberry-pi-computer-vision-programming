import matplotlib.pyplot as plt
import mahotas

photo = mahotas.demos.load('luispedro')
photo = mahotas.colors.rgb2sepia(photo)
plt.imshow(photo)
plt.axis('off')
plt.show()
