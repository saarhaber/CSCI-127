#name Saar Haber
#date 15 February 2018
#program green picture

import matplotlib.pyplot as plt
import numpy as np

n=input("enter a name of an image png file")
h=input("enter the name of an output file")

img=plt.imread(n)
plt.imshow(img)

img2=img.copy()

img2[:,:,2]=0
img2[:,:,0]=0

plt.imshow(img2)

plt.imsave(h,img2)
