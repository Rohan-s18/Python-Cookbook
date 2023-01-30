"""
Author: Rohan Singh
12/27/22
This python moduel contains source code for creating a trackbar color palette
"""

#Imports
import numpy as np
import cv2 as cv

#Event callback function
def nothing(x):
    pass

#Function to create an rgb color palette
def color_palette():

    #Creating an all balck image    
    img = np.zeros((300,512,3), np.uint8)
    
    cv.namedWindow('palette')

    #Creating trackbars for color change
    cv.createTrackbar('R','image',0,255,nothing)
    cv.createTrackbar('G','image',0,255,nothing)
    cv.createTrackbar('B','image',0,255,nothing)

    #Creating a switch for ON/OFF functionality
    switch = '0 : OFF \n1 : ON'
    cv.createTrackbar(switch, 'image',0,1,nothing)

    while(True):
        cv.imshow('image',img)
        k = cv.waitKey(1) & 0xFF
        if k == 27:
            break
        #Getting the current positions of four trackbars
        r = cv.getTrackbarPos('R','image')
        g = cv.getTrackbarPos('G','image')
        b = cv.getTrackbarPos('B','image')
        s = cv.getTrackbarPos(switch,'image')

        #If the switch is off
        if s == 0:
            img[:] = 0
        else:
            #Setting the curent image to the rgb values if the switch is on
            img[:] = [b,g,r]

    cv.destroyAllWindows()


#Main method
def main():

    #print("Hello World!")

    color_palette()

if __name__ == "__main__":
    main()


