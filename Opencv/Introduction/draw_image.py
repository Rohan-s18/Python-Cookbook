"""
Author: Rohan Singh
12/27/22
This python module contains source code for drawing an image and shapes using opencv
"""

#Imports
import numpy as np
import cv2 as cv


#Function to draw a line
def draw_line(img):
    #This call will draw a line
    cv.line(
        img,                #image
        (0,0),              #Starting point
        (511,511),          #Ending point
        (255,255,255),      #Color (this case it is white)
        10                  #Line width
    )

    cv.imshow("Your Line",img)


#Function to draw a rectangle 
def draw_rectangle(img):
    cv.rectangle(
    img,                    #image
    (384,0),                #top-left corner
    (510,128),              #bottom-right corner
    (0,255,0),              #rgb color
    3                       #Width
    )

    cv.imshow("Your Rectangle", img)


#Function to draw a circle
def draw_circle(img):
    cv.circle(
    img,                    #image
    (447,63),               #Center
    63,                     #Radius
    (0,0,255),              #Color
    -1
    )

    cv.imshow("Your Circle",img)


#Function to add text to an image
def add_text(img):
    #Setting the font
    font = cv.FONT_HERSHEY_SIMPLEX
    cv.putText(img,
    'Hello World',
    (10,500), 
    font, 
    4,(255,255,255),2,cv.LINE_AA)

    cv.imshow("Your Text", img)

#Main method
def main():

    print("Hello World!")

    #This will create a black image of 512x512 pixels (all set to 0)
    my_img = np.zeros((512,512,3),np.uint8)


    draw_line(my_img)

    


if __name__ == "__main__":
    main()

