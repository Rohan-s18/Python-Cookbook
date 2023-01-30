"""
Author: Rohan Singh
12/29/2022
This Python Module contains source code for basic arithmertic operations on images like adding, blending and logical operations.
"""

#  Imports
import numpy as np
import cv2 as cv


#  Function to add two images (unweighted)
def add_images(img1, img2):
    img = cv.add(img1,img2)

    #Displaying the image
    cv.imshow('Summed Image',img)
    cv.waitKey(0)
    cv.destroyAllWindows() 



#  Function to Blend 2 images, weighted addition
def blend_images(img1, img2, w1, w2, w3):

    #Using the inputted weights to blend the images
    img = cv.addWeighted(img1,w1,img2,w2,w3)

    #Displaying the image
    cv.imshow('Blended Image',img)
    cv.waitKey(0)
    cv.destroyAllWindows() 



#  Function to demonstrate bitwise operations on 2 images
def bitwise_operations(img1, img2):

    #Creating an roi
    rows,cols,channels = img2.shape
    roi = img1[0:rows, 0:cols]

    #Creating a mask
    img2gray = cv.cvtColor(img2,cv.COLOR_BGR2GRAY)
    ret, mask = cv.threshold(img2gray, 10, 255, cv.THRESH_BINARY)

    #Creating the inverse mask using the 'NOT' Operation
    mask_inv = cv.bitwise_not(mask)

    #Blacking out the roi
    img1_bg = cv.bitwise_and(roi,roi,mask = mask_inv)
    #Taking out only the common region
    img2_fg = cv.bitwise_and(img2,img2,mask = mask)

    #Modifying the main image
    dst = cv.add(img1_bg,img2_fg)
    img1[0:rows, 0:cols ] = dst

    #Showing the image
    cv.imshow('res',img1)
    cv.waitKey(0)
    cv.destroyAllWindows()  


#  Main function
def main():

    #Change these filepaths to wherever the images are stored
    fp_1 = ""
    fp_2 = ""

    #Reading the images
    img_1 = cv.imread(fp_1)
    img_2 = cv.imread(fp_2)

    #Adding the 2 images
    add_images(img_1, img_2)

    #Blending the 2 images
    blend_images(img_1, img_2, 0.3,0.7,0.0)

    #Using the bitwise operations on the two images
    bitwise_operations(img_1, img_2)


    print("Hello World!")

    




if __name__ == "__main__":
    main()
