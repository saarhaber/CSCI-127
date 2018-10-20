# Name:  Saar Haber
# Date:  March 1st 2018
# coast


#Import the libraries for arrays and displaying images:
import numpy as np
import matplotlib.pyplot as plt


#Read in the data to an array, called elevations:
elevations = np.loadtxt('elevationsNYC.txt')

#Take the shape (dimensions) of the elevations
#  and add another dimension to hold the 3 color channels:
mapShape = elevations.shape + (3,)

#Create a blank image that's all zeros:
floodMap = np.zeros(mapShape)

for row in range(mapShape[0]):
    for col in range(mapShape[1]):
        if elevations[row,col] <= 0: 
            #Below sea level
           floodMap[row,col,2] = 0.5     #Set the blue channel to 50% 
           floodMap[row,col,0] = 0.0    #red 0
           floodMap[row,col,1] = 0.0    #green 0
        elif elevations[row,col] == 1:
           floodMap[row,col,0] = 0.75     #Set the channels to 75%
           floodMap[row,col,1] = 0.75
           floodMap[row,col,2] = 0.75
        else: 
            floodMap[row,col,0] = 0.5   #Set the channels to 50%
            floodMap[row,col,1] = 0.5
            floodMap[row,col,2] = 0.5
     
#Save the image:
plt.imsave('coast.png', floodMap)
