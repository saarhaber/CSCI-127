#Saar Haber
#March 20th
#Program 35

#Import libraries.
import matplotlib.pyplot as plt
import numpy as np

#2 Ask user for an image name.
inF = input("Enter input file name: ")
outF = input ("Enter output file name: ")

#3 Read in image.
img = plt.imread(inF) #Read in image from inF

img2=img

#4 Figure out size of image.
height = img.shape[0] #Get height
width = img.shape[1] #Get width


#5 Make a new image that’s half the height and half the width.img2 =
img2=img[int(height/2):, :int(width/2)] #Crop to lower left corner

#6 Display the new image.
plt.imsave(outF, img2) #Load our new image into pyplot
