import cv2
j=0
for filename in dir(cv2):
    if filename.startswith('COLOR_'):
        print(filename)
        j = j + 1
print('There are ' + str(j) +
      ' Colorspace Conversion flags in OpenCV '
      + cv2.__version__ + '.')
