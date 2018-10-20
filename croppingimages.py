import matplotlib.pyplot as plt
import numpy as np

inImg=input('enter input image: ')
img=plt.imread(inImg)
plt.imshow(img)
plt.show() 

outImg=input('enter out image: ')
t=int(input('enter top:'))
b=int(input('enter bottom:'))
l=int(input('enter left:'))
r=int(input('enter right:'))

img2=img[t:b,l:r]

plt.imshow(img2)
plt.show()

plt.imsave(outImg, img2)
