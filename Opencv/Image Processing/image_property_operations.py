"""
Author: Rohan Singh
12/29/2022
This Python module contains code for simple operations to access/modify image properties. 
"""

#  Imports
import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

#  This function will return the pixel on the given location of the given image
def get_pixel(img, x, y):
    px = img[x,y]
    print(px)
    return px

#  This function will modify the attributes of the given pixel
def modify_pixel(img, x, y, r, g, b):
    img[x,y] = np.array([b,g,r])

#  Modifying a particular attribute of a pixel to the val
def modify_attribute(img, x, y, attr, val):
    if(attr == 'b'):
        img.itemset((x,y,0),val)
    elif(attr == 'g'):
        img.itemset((x,y,1),val)
    elif(attr == 'r'):
        img.itemset((x,y,2),val)
    else:
        print("Invalid Attribute")

#  This function will print out the image properties
def print_image_properties(img):
    print("Dimensions: ",img.shape)
    print("Size: ",img.size)
    print("Image datatype: ",img.dtype)

#  This function will return a region of image (ROI)
def roi(img, x1, x2, y1, y2):
    roi = img[x1:x2, y1:y2]
    return roi

#  This function will paste a given roi in a different region
def paste_roi(img, roi, x1, x2, y1, y2):
    img[x1:x2, y1:y2] = roi

#  This function will modify the entire channel (b,g,r) of an image
def modify_channel(img, attr, val):
    b,g,r = cv.split(img)
    if(attr == 'b'):
        img[:,:,0] = val
    elif(attr == 'g'):
        img[:,:,1] = val
    elif(attr == 'b'):
        img[:,:,2] = val
    else:
        print("Invalid Attribute")
    img = cv.merge((b,g,r))
    return img

#  This function will modify the borders of an image
def modify_borders(img, wid):
    GREEN = [0,255,0]

    replicate = cv.copyMakeBorder(img,wid,wid,wid,wid,cv.BORDER_REPLICATE)
    reflect = cv.copyMakeBorder(img,wid,wid,wid,wid,cv.BORDER_REFLECT)
    reflect101 = cv.copyMakeBorder(img,wid,wid,wid,wid,cv.BORDER_REFLECT_101)
    wrap = cv.copyMakeBorder(img,wid,wid,wid,wid,cv.BORDER_WRAP)
    constant= cv.copyMakeBorder(img,wid,wid,wid,wid,cv.BORDER_CONSTANT,value=GREEN)
    plt.subplot(231),plt.imshow(img,'gray'),plt.title('ORIGINAL')
    plt.subplot(232),plt.imshow(replicate,'gray'),plt.title('REPLICATE')
    plt.subplot(233),plt.imshow(reflect,'gray'),plt.title('REFLECT')
    plt.subplot(234),plt.imshow(reflect101,'gray'),plt.title('REFLECT_101')
    plt.subplot(235),plt.imshow(wrap,'gray'),plt.title('WRAP')
    plt.subplot(236),plt.imshow(constant,'gray'),plt.title('CONSTANT')
    plt.show()

#  This is the main function of the module to demonstrate the working of these operations
def main():

    #Write the filepath of your image here
    filepath = ""
    img = cv.imread(filepath)

    print("\n")

    #Getting the pixel info
    get_pixel(img,100,100)


    
    #Modifying the B attribute
    modify_attribute(img,100,100,'b',255)

    print("\n")

    #Getting the image properties
    print_image_properties(img)

    print("\n")

    #Getting the region of image
    my_roi = roi(img,20,80,20,80)
    cv.imshow("Region",my_roi)

    #Modifying the 'G' channel to 10
    img = modify_channel(img,'g',10)
    cv.imshow("Lmao",img)

    #Changing the borders of the image
    modify_borders(img,100)


    print("Hello World!")


if __name__ == "__main__":
    main()
