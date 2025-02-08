import cv2 as cv
import numpy as np

blankImg = np.zeros(( 500, 500, 3), dtype ='uint8')

blankImg[:] = 0,0,0

# Write text:
cv.putText(blankImg, 'Hello everyone!', (100,50) , cv.FONT_HERSHEY_TRIPLEX, 1.0 , (15, 72, 77) ,2)
cv.imshow('text img' , blankImg)


image = cv.imread('PythonProjects/Horse logo.jpg') # to read the image
cv.imshow('My horsey', image) # to display the image, the first peramiter is the name of the widow(can be anything u want), 2nd peramiter is the path of the file/image.

shadeImg = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
cv.imshow('greyish' , shadeImg )

if ():
    print("key: ")

cv. waitKey(0)










