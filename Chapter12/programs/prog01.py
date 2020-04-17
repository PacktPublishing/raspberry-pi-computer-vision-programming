import matplotlib.pyplot as plt
import mahotas
#photo = mahotas.demos.load('luispedro')
#plt.imshow(photo)
photo = mahotas.demos.load('luispedro', as_grey=True)
plt.imshow(photo, cmap='gray')
plt.axis('off')
plt.show()
