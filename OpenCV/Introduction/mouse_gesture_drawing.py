"""
Author: Rohan Singh
12/27/2022
This python module contains source code to draw different shapes onto opencv windows using mouse gestures
"""

#Imports
import numpy as np
import cv2 as cv

#Creating a 512x512 black canvas
img = np.zeros((512,512,3), np.uint8)

#This is a mouse callback function (similar to event handler in Java), this will draw a circle where the mouse was clicked
def draw_circle(event,x,y,flags,param):
    #If the event is one of the mouse-clicks
    if event == cv.EVENT_LBUTTONDBLCLK:
        #Calling opencv's drawcircle method
        cv.circle(img,(x,y),100,(255,0,0),-1)


#This method will display the image on the window
def mouse_gesture_circle():

    cv.namedWindow('image')

    #Setting the mouse callback to the draw circle function
    cv.setMouseCallback('image',draw_circle)

    while(True):
        #Displaying the image
        cv.imshow('image',img)
        if cv.waitKey(20) & 0xFF == 27:
            break

    #Destroy Buzzlightyear
    cv.destroyAllWindows()





#Main method
def main():

    #print("Hello World!")

    #Calling the method to create mouse gesture circles
    mouse_gesture_circle()


if __name__ == "__main__":
    main()





