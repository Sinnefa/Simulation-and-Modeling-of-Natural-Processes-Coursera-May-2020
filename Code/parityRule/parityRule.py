# -*- coding: utf-8 -*-
# Copyright (C) 2016 Universite de Geneve, Switzerland
# E-mail contact: sebastien.leclaire@etu.unige.ch
#
# The Parity Rule
#

from numpy import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
import copy
import imageio

# Definition of functions
def readImage(string): # This function only work for monochrome BMP.
    image =  imageio.imread(string,"BMP");
    image[image == 255] = 1
    image = image.astype(int)
    return image # Note that the image output is a numPy array of type "int".

# Main Program

# Program input, i.e. the name of the image "imageName" and the maximum number of iteration "maxIter"
imageName = 'image3.bmp'
maxIter   = 32

# Read the image and store it in the array "image"
image = readImage(imageName) # Note that "image" is a numPy array of type "int".
# Its element are obtained as image[i,j]
# Also, in the array "image" a white pixel correspond to an entry of 1 and a black pixel to an entry of 0.

# Get the shape of the image , i.e. the number of pixels horizontally and vertically.
# Note that the function shape return a type "tuple" (vertical_size,horizontal_size)
imageSize = shape(image);

# Print to screen the initial image.
print('Initial image:')
plt.clf()
plt.imshow(image, cmap=cm.gray)
plt.show()
plt.pause(0.1)

# Main loop
for it in range(1,maxIter+1):

    imageCopy = copy.copy(image);

    # You need to write here the core of the parity rule algorithm.
    # Altough not mandatory, you might need to use the array "imageCopy" and the tuple "imageSize".
    #
    # Code that you need to write...
    x = imageSize[0]
    y = imageSize[1]
    for i in range (0,x):
        for j in range(0,y):
            sopra = 0
            sotto = 0
            destra = 0
            sinistra = 0
            if i==0:
                 sopra = imageCopy[x-1,j]
            else:
                 sopra = imageCopy[i-1,j]
            if i==x-1:
                 sotto = imageCopy[0,j]
            else:
                 sotto = imageCopy[i+1,j]
            if j==0:
                 sinistra = imageCopy[i,y-1]
            else:
                 sinistra = imageCopy[i,j-1]
            if j==y-1:
                 destra = imageCopy[i,0]
            else:
                 destra = imageCopy[i,j+1]
            sum = sopra + sotto + sinistra + destra
            if sum % 2 == 0:
                 image[i,j]=0
            else:
                 image[i,j]=1
    # Code that you need to write...

    # Print to screen the image after each iteration.
    #print('Image after',it,'iterations:')
    #plt.clf()
    #plt.imshow(image, cmap=cm.gray)
    #plt.show()
    #plt.pause(0.1)

# Print to screen the number of white pixels in the final image
print(image)
print("The number of white pixels after",it,"iterations is: ", np.sum(image))
