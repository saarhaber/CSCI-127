#name Saar Haber
#date 22 February 2018
# #This program loads an image, displays it, and then creates, displays,
#    and saves a new image that has only the green channel displayed.

#Import the packages for images and arrays:
import matplotlib.pyplot as plt  
import numpy as np


img = plt.imread('csBridge.png')   #Read in image from csBridge.png
plt.imshow(img)		           #Load image into pyplot
plt.show()                         #Show the image (waits until closed to continue)

img2 = img.copy()        #make a copy of our image          
img2[:,:,0] = 0          #Set the red channel to 0
img2[:,:,2] = 0          #Set the blue channel to 0 

plt.imshow(img2)         #Load our new image into pyplot
plt.show()               #Show the image (waits until closed to continue)

plt.imsave('reds.png', img2)  #Save the image we created to the file: reds.png
