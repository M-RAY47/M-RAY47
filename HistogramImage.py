import matplotlib.pyplot as plt
import skimage.io
import skimage.color
import numpy as np

im = skimage.io.imread("F:\\New folder\\photos of\\Gear11.jpg", as_gray=False)
#im = skimage.io.imread("C:\\Users\\amray\\PycharmProjects\\pythonProject\\dog.jpg", as_gray=False)
im_HSV = skimage.color.rgb2hsv(im)
Hue = im_HSV[:, :, 0]
hist = np.histogram(Hue, bins=360)

plt.bar(np.arange(360), hist[0], align="center", width=0.1)

skimage.io.imshow(im_HSV)
plt.show()

